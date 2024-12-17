'''
PRACTICAL EXAMPLE
Creates a database called (members.db)
Create a table called (members) with the columns
    - ID (Integer)
    - Name (string)
    - Email (string)
    - Grade (string)
Insert members (rows/information) in the members table
'''
import sqlite3

# Connect to the SQLite database named 'members.db'
db = sqlite3.connect('members.db')
# Create a cursor object to interact with the database
cursor = db.cursor()

# Execute a SQL command to create a table named 'members' if it doesn't exist
# The table has four columns: id, name, email, and grade
cursor.execute('''
    CREATE TABLE IF NOT EXISTS members(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(50),    
        email VARCHAR(50),   
        grade VARCHAR(50),
        date_due DATE DEFAULT (DATE('now'))
    )''')

# member_id = 2
# name = "Dan"
# email = "dan@gmail.com"
# grade = "A"
# cursor.execute('''INSERT INTO members (id, name, email, grade) VALUES(?, ?, ?, ?)''', (member_id, name, email, grade))

members_list = [
    ["Dan", "dan@gmail.com", "A"],
    ["John", "john@gmail.com", "D"],
    ["Jane", "jane@gmail.com", "C"],
    ["Bob", "bob@gmail.com", "D"]
]
# cursor.execute('DELETE FROM members')

cursor.executemany('''INSERT OR IGNORE INTO members(name, email, grade) VALUES(?,?,?)''', members_list)


cursor.execute('''SELECT * FROM members''')
members = cursor.fetchall()

print(type(members))
for member in members:
    print(member)


# Commit the changes to the database
db.commit()
# Close the database connection
db.close() 




