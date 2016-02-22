# Initialize variables
counters = dict()
lines_selected = False

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

# Select the lines beginning with "From ", split them twice, and count how many
# e-mails are send per hour
for line in fhandle :
    if not line.startswith("From ") : continue
    lines_selected = True
    line = line.rstrip()
    splitted_line = line.split()
    time_string = splitted_line[5]
    splitted_string = time_string.split(":")
    counters[splitted_string[0]] = counters.get(splitted_string[0], 0) + 1

# Close the file
fhandle.close()

# If lines are selected move the resulting counters into a list and sort

# Print the result of the selection
if not lines_selected :
    print "===> Input error: There are no 'From ' lines in the file."
else :
    count_list = counters.items()
    count_list.sort()
    for hour, count in count_list :
        print hour, count
