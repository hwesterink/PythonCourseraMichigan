import sqlite3

# Initialize the variable org
org = "Is er niet"

# Connect to the emaildb.sqlite database as needed
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Select the non-existing row and print the value asked for
cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
print cur.fetchone()
