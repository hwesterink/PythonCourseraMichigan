import xml.etree.ElementTree as ET
import sqlite3

# Helper function to extract data from the XML-file
def lookup(d, key):
    """
    This function returns a string-value for a key from the block of XML in d.
        d =     The line of XML-line
        key =   The key to search for
    """
    
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

# Connect to or create database as needed
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Drop the old tables with the names Artist, Genre, Album and Track if they exist
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
''')

# Create the tables Artists, Genre, Album and Track again
# in the database "trackdb.sqlite"
cur.executescript('''
CREATE TABLE Artist (
    id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title      TEXT UNIQUE
);

CREATE TABLE Track (
    id        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title     TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len       INTEGER,
    rating    INTEGER,
    count     INTEGER
);
''')

# Open the file to be processed
# Use the file name Library.xml as default for the file name
fname = raw_input("File name defaults to Library.xml\nEnter file name: ")
if len(fname) == 0:
    fname = "Library.xml"
try:
    fhandle = open(fname)
except:
    print "File", fname, "does not exist"
    quit()

# Read the XML file and create a list of entries
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
# Process each entry to fill the database trackdb.sqlite
for entry in all:
    # Skip all input that has no track-id
    if ( lookup(entry, 'Track ID') is None ):
        continue
    # Find the data to transfer to the database
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    # Skip all input that has no track-name, no artist-name, no album-name or no genre
    if name is None or artist is None or album is None or genre is None: 
        continue
    print name, artist, album, genre, count, rating, length

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

# Commit all changes to the database
conn.commit()

# Close file and database connections
fhandle.close()
cur.close()
