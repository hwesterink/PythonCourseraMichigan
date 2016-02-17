# Initialize variables
counters = dict()
max_address = "No lines selected!"
max_count = 0

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

# Select the lines beginning with "From ", split them, and count how many
# times each e-mail address occurs in the file
for line in fhandle :
    if not line.startswith("From ") : continue
    line = line.rstrip()
    splitted_line = line.split()
    counters[splitted_line[1]] = counters.get(splitted_line[1], 0) + 1

# Close the file
fhandle.close()

# Select the e-mail address with the highest occurrence and print it
for key, count in counters.items() :
    if max_count < count :
        max_address = key
        max_count = count

# Print the result of the selection
if max_address == "No lines selected!" :
    print "===> Input error:", max_address
else :
    print max_address, max_count
