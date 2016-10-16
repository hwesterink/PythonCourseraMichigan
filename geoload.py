import urllib
import sqlite3
import json
import time
import ssl

# If you are in China use this URL:
# serviceurl = "http://maps.google.cn/maps/api/geocode/json?"
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

# Connect to or create database as needed
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# Create a table in the database geodata.sqlite if it does not exist
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Open input file and initialize counter
fhandle = open("where.data")
count = 1

for line in fhandle:
    # Stop after 5 addresses have been retrieved
    if count > 200 : break

    # Check whether the address is already in the database, if so skip it
    address = line.strip()
    print ''
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (buffer(address), ))
    try:
        data = cur.fetchone()[0]
        print "Found in database ",address
        continue
    except:
        pass

    # Retrieve the address information from Google
    print 'Resolving', address
    url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})
    print 'Retrieving', url
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
    print 'Retrieved',len(data),'characters',data[:20].replace('\n',' ')
    count = count + 1

    # Check whether the data is OK
    try: 
        js = json.loads(str(data))
    except: 
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print '==== Failure To Retrieve ===='
        print data
        break

    # Store the data in the database
    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
    conn.commit() 

    # Wait 1 second before moving to the next line
    time.sleep(1)

# Close the database and the file
cur.close()
fhandle.close()
    
# Complete the program with the instructions for the next step
print "Run geodump.py to read the data from the database so you can visualize it on a map."
