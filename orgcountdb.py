import sqlite3

# Initialize counter to follow progress
counter = 0

# Connect to or create database as needed
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the old table with the name counts if it exists
cur.execute('''
DROP TABLE IF EXISTS Counts''')

# Create a new table Counts in the database "emaildb.sqlite"
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Open the file to be processed
# Use the file name mbox.txt as default for the file name
fname = raw_input("File name defaults to mbox.txt\nEnter file name: ")
if len(fname) == 0 :
    fname = "mbox.txt"
try :
    fhandle = open(fname)
except :
    print "File", fname, "does not exist"
    quit()

# Read the file and process the e-mail adresses found
fhandle = open(fname)
for line in fhandle:
    if not line.startswith('From: ') : continue
    counter += 1
    pieces = line.split()
    mail = pieces[1]
    org = mail[mail.index("@")+1:]
    if counter % 100 == 0:
        print "===>", counter, "e-mails processed"
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))

# Commit all changes to the database
conn.commit()

# Print the first 10 lines of the resulting table
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

# Close file and database connections
fhandle.close()
cur.close()
