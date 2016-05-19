import json
import sqlite3

# Connect to or create database as needed
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Drop the old tables with the names Users, Member and Course if they exist
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course
''')

# Create the tables Users, Member and Course again
# in the database "rosterdb.sqlite"
cur.executescript('''
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Open the file to be processed
# Use the file name roster_data.json as default for the file name
fname = raw_input("File name defaults to roster_data.json\nEnter file name: ")
if len(fname) == 0:
    fname = "roster_data.json"
try:
    fhandle = open(fname)
except:
    print "File", fname, "does not exist"
    quit()

# Read the XML file and create a list of entries
str_data = open(fname).read()
json_data = json.loads(str_data)
# Process each entry to fill the database trackdb.sqlite
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print name, title

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''', 
        ( user_id, course_id, role ) )

# Commit all changes to the database
conn.commit()

# Print out the result of the query from the assignment
result = cur.execute('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
                     User JOIN Member JOIN Course 
                     ON User.id = Member.user_id AND Member.course_id = Course.id
                     ORDER BY X''')
output = result.fetchone()[0]
print
print "Result:"
print output


# Close file and database connections
fhandle.close()
cur.close()
