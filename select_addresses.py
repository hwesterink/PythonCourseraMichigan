# Initialize variables
count = 0

# Open the file to be processed
# Use the file name mbox-short.txt as the file name
fname = raw_input("File name defaults to mbox-short.txt\nEnter file name: ")
if len(fname) == 0 :
    fname = "mbox-short.txt"
try :
    fhandle = open(fname)
except :
    print "File", fname, "does not exist"
    quit()

# Select the lines beginning with "From ", split them, print the e-mail address
# and count the addresses printed 
for line in fhandle :
    if not line.startswith("From ") : continue
    line = line.rstrip()
    splitted_line = line.split()
    print splitted_line[1]
    count += 1

# Close the file
fhandle.close()

# Print the count for the selected lines
print "There were", count, "lines in the file with From as the first word"
