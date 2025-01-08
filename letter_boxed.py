from collections import deque
import json
import requests
from bs4 import BeautifulSoup

def fetch_game_data():
	url = 'https://www.nyt.com/puzzles/letter-boxed'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	
	# Find the script tag containing the game data
	script_tag = soup.find('script', string=lambda t: 'window.gameData' in t)
	if script_tag:
		# Extract the JavaScript variable
		script_content = script_tag.string
		start_index = script_content.find('window.gameData = ') + len('window.gameData = ')
		end_index = script_content.find('}', start_index) + 1
		game_data = script_content[start_index:end_index].strip()
		return game_data
	return None

def get_rules(game_data):
	game_data = json.loads(game_data)  # Load game data from the provided game_data
	sides = game_data['sides']  # Extract the sides from the game data
	return [set(side) for side in sides]  # Convert each side to a set and return as a list

def search_words(letters, rules, game_data):
	game_data = json.loads(game_data)  # Load game data from the provided game_data
	dictionary = game_data['dictionary']  # Extract the dictionary from the game data
	
	matching_words = []
	for word in dictionary:
		if set(word).issubset(set(letters)):  # Check if the word can be formed using the given letters
			matching_words.append(word)  # Add the word to the list of matching words
	
	return matching_words

def find_shortest_chains(words, rules):
	all_chars = set.union(*rules)  # Combine all characters from the rules sets
	word_dict = {word: set(word) for word in words}  # Create a dictionary of words and their character sets
	
	def bfs(start_word):
		queue = deque([(start_word, [start_word], word_dict[start_word])])  # Initialize the BFS queue
		visited = set()  # Keep track of visited words
		chains = []  # Store the chains of words
		
		while queue:
			current_word, path, used_chars = queue.popleft()  # Dequeue the next word and its path
			if used_chars == all_chars:  # Check if all characters are used
				chains.append(path)  # Add the path to the list of chains
			
			for next_word in words:
				if next_word not in visited and next_word[0] == current_word[-1]:  # Check if the next word can follow the current word
					new_used_chars = used_chars | word_dict[next_word]  # Update the set of used characters
					queue.append((next_word, path + [next_word], new_used_chars))  # Enqueue the next word and its updated path
					visited.add(next_word)  # Mark the next word as visited
		
		return chains

	all_chains = []
	for word in words:
		chains = bfs(word)  # Find chains starting from the current word
		all_chains.extend(chains)
	
	all_chains.sort(key=len)  # Sort the chains by length
	return all_chains[:10]  # Return the 10 shortest chains

def update_database_with_words(game_data):
	game_data = json.loads(game_data)  # Load game data from the provided game_data
	dictionary = game_data['dictionary']  # Extract the dictionary from the game data
	
	import mysql.connector  # Import the MySQL connector at the top of the file

	# Establish a database connection
	connection = mysql.connector.connect(
		host='localhost',  # Replace with your database host
		user='SomeUserName',  # Replace with your database user
		password='glw39tbce4$1C4WUS*q6bb0EDqCDLY9JAe2I$NexQdjKQzYtis685@kS#20UB7C$SZM4*z712I6HDjdlH98ycv0nG6X&M@pgWXT*noBR71v&zuYBUeIAfZWG6FbKjx6P',  # Replace with your database password
		database='wordList'  # Replace with your database name
	)
	cursor = connection.cursor()  # Create a cursor object

	for word in dictionary:
		# Example query to insert the word into a MySQL database
		query = "UPDATE eng SET letter_boxed = 1 WHERE word = %s"
		cursor.execute(query, (word,))
		# This is a placeholder for the actual database update logic.
		print(f"Updating database with word: {word}")  # Replace with actual database update code

	# Close the cursor and connection after the updates
	cursor.close()
	connection.commit()  # Commit the changes to the database
	connection.close()  # Close the database connection

def main():
	game_data = fetch_game_data()  # Fetch the game data
	if game_data is None:
		print("Failed to fetch game data.")
		return
	
	rules = get_rules(game_data)  # Get the rules using the fetched game data
	letters = ''.join(set.union(*rules))  # Combine all letters from the sets into a single string
	matching_words = search_words(letters, rules, game_data)  # Search for matching words using the fetched game data
	
	shortest_chains = find_shortest_chains(matching_words, rules)  # Find the shortest chains of words
	
	if shortest_chains:
		print("10 shortest chains of words that use all characters in the rules sets:")
		for chain in shortest_chains:
			print(f"{len(chain)}\t{' -> '.join(chain)}")
	else:
		print("No valid chain found.")
	update_database_with_words(game_data)  # Update the database with the words from the game data

if __name__ == "__main__":
	main()