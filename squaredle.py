from collections import defaultdict

import mysql.connector

def get_word_list():
	# Connect to the MySQL database
	conn = mysql.connector.connect(
		host='localhost',
		user='SomeUserName',
		password='glw39tbce4$1C4WUS*q6bb0EDqCDLY9JAe2I$NexQdjKQzYtis685@kS#20UB7C$SZM4*z712I6HDjdlH98ycv0nG6X&M@pgWXT*noBR71v&zuYBUeIAfZWG6FbKjx6P',
		database='wordlist'
	)
	cursor = conn.cursor()
	cursor.execute("SELECT word, squaredle FROM eng ORDER BY squaredle DESC")
	words = cursor.fetchall()
	cursor.close()
	conn.close()
	return words

def is_valid_word(word, grid, x, y, visited):
	if not word:
		return True
	if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or 
		visited[x][y] or grid[x][y] != word[0]):
		return False
	
	visited[x][y] = True
	word = word[1:]
	
	# Check all 8 possible directions
	directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	for dx, dy in directions:
		if is_valid_word(word, grid, x + dx, y + dy, visited):
			return True
	
	visited[x][y] = False
	return False

def find_words_in_grid(grid, words):
	valid_words = defaultdict(set)  # Change list to set
	for item in words:
		word = item[0]
		if len(word) < 4:
			continue
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
				if is_valid_word(word, grid, i, j, visited):
					valid_words[item[1]].add(word)  # Use add instead of append
					if(item[1] == 3):
						valid_words[2].add(word) 
					break
	return {key: list(value) for key, value in valid_words.items()}  # Convert sets back to lists

def main():
	grid = []
	with open('C:/Users/kevin/OneDrive/Desktop/Scripts/input.txt', 'r') as file:
		for line in file:
			grid.append(list(line.strip()))
	
	words = get_word_list()
	valid_words = find_words_in_grid(grid, words)
	prevLength = 0

	try:
		# Sort and print words for squaredle = 1
		print("Known Words: ("+str(len(valid_words[1]))+")")
		for word in sorted(list(valid_words[1]), key=lambda x: (len(x), x)):
			if prevLength == 0:
				prevLength = len(word)
			elif len(word) != prevLength:
				prevLength = len(word)
				print()
			print(f"\t{len(word)}\t{word}")
		print()
		print()
	except:
		print("Error with Known Words")

	try:
		prevLength = 0
		# Sort and print words for squaredle = 1
		print("Possible Words: ("+str(len(valid_words[0]))+")")
		for word in sorted(list(valid_words[0]), key=lambda x: (len(x), x)):
			if prevLength == 0:
				prevLength = len(word)
			elif len(word) != prevLength:
				prevLength = len(word)
				print()
			print(f"\t{len(word)}\t{word}")
		print()
		print()
	except:
		print("Error with Possible Words")

	try:
		prevLength = 0
		# Sort and print words for squaredle = 3
		print("Previous Bonus Words of the Day: ("+str(len(valid_words[3]))+")")
		for word in sorted(list(valid_words[3]), key=lambda x: (len(x), x)):
			if prevLength == 0:
				prevLength = len(word)
			elif len(word) != prevLength:
				prevLength = len(word)
				print()
			print(f"\t{len(word)}\t{word}")
		print()
		print()
	except:
		print("Error with Bonus Words of the Day")

	try:
		prevLetter = 'a'
		# Sort and print words for squaredle = 2
		print("Bonus Words: ("+str(len(valid_words[2]))+")")
		for word in sorted(valid_words[2]):
			if prevLetter != word[0]:
				prevLetter = word[0]
				print()
			print(f"\t{len(word)}\t{word}")
	except:
		print("Error with Bonus Words")
	
if __name__ == "__main__":
	main()