import sqlite3
import json
import codecs

# Connect to existing database geodata.sqlite
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# Select the whole Locations table
cur.execute('SELECT * FROM Locations')

# Open a file to write the java-script input into
fhandle = codecs.open('where.js','w', "utf-8")

# Write the first line of the where.js file and initialize the counter
fhandle.write("myData = [\n")
count = 0

for row in cur :
    # Interpret the data of the next row
    data = str(row[1])
    try: 
        js = json.loads(str(data))
    except: 
        continue

    # Check if the row contains data that is OK, otherwise skip the row
    if not('status' in js and js['status'] == 'OK'): 
        continue

    # Skip the row if geometric information for the location is missing
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0:
        continue
    
    # Create a formatted description of the location
    where = js['results'][0]['formatted_address']
    where = where.replace("'","")
    try :
        # Add the location information to the java script input
        # Skip if there is something wrong with it
        print where, lat, lng
        count = count + 1
        if count > 1:
            fhandle.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhandle.write(output)
    except:
        continue

# Finalize the file
fhandle.write("\n];\n")

# Close the database and the file
cur.close()
fhandle.close()

# Print the result of the program and instructions for the next step
print count, "records written to where.js"
print "Open where.html to view the data in a browser"
