# Initialize variables
count = 0
total = 0

# Open the file to be processed
# Use the file name mbox-short.txt as the file name
fname = raw_input("Use mbox-short.txt as the file name\nEnter file name: ")
try :
    fhandle = open(fname)
except :
    print "File", fname, "does not exist"
    quit()

# Select the lines with the right input and process them 
for line in fhandle :
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    pos = line.find(":")
    strvalue = line[(pos + 1):9999]
    floatvalue = float(strvalue)
    count += 1
    total += floatvalue

# Compute and display the average SPAM-confidence
if count != 0 :
    average = total / count
    print "Average spam confidence:", average
else :
    print "There are no X-DSPAM-Confidence lines in the input file."
