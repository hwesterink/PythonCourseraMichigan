# Initialize variables
My_list = list()

# Open the file to be processed
# Use the file name romeo.txt as the file name
fname = raw_input("File name defaults to romeo.txt\nEnter file name: ")
if len(fname) == 0 :
    fname = "romeo.txt"
try :
    fhandle = open(fname)
except :
    print "File", fname, "does not exist"
    quit()

# Select each line, split it into words and add unique words to the wordlist
for line in fhandle :
    line = line.rstrip()
    splitted_line = line.split()
    for word in splitted_line :
        if word in My_list : continue
        My_list.append(word)

# Close the file
fhandle.close()

# Sort list and print the result
My_list.sort()
print My_list
