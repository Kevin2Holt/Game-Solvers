import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
	host='localhost',
	user='SomeUserName',
	password='glw39tbce4$1C4WUS*q6bb0EDqCDLY9JAe2I$NexQdjKQzYtis685@kS#20UB7C$SZM4*z712I6HDjdlH98ycv0nG6X&M@pgWXT*noBR71v&zuYBUeIAfZWG6FbKjx6P',
	database='wordlist'
)

# Create a cursor object
cursor = conn.cursor()

print("Connected to the database")
count = 0

# Open and read the text file
with open('C:/Users/kevin/OneDrive/Desktop/Scripts/database.txt', 'r') as file:
	for line in file:
		if line.startswith(tuple('0123456789')):
			continue
		words = line.split()
		for word in words:
			# Insert each word into the MySQL database
			# cursor.execute("INSERT INTO eng (word, wordle) VALUES ('"+word+"', 1) ON DUPLICATE KEY UPDATE word = '"+word+"'")
			count += 1
			print(word)
			cursor.execute("UPDATE eng SET squaredle = 2 WHERE word = %s AND squaredle <> 3", (word,))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print(count, "words processed into the database")