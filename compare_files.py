# Open, read and close the first file
fname = raw_input("Enter file name 1: ")
try :
    fhandle = open(fname)
except :
    print "File", fname, "does not exist"
    quit()
inp1 = fhandle.read()
fhandle.close()

# Open, read and close the second file
fname = raw_input("Enter file name 2: ")
try :
    fhandle = open(fname)
except :
    print "File", fname, "does not exist"
    quit()
inp2 = fhandle.read()
fhandle.close()

# Compare the files and print the result
if inp1 == inp2 :
    print "Both files are exactly the same."
else :
    print "The files are different."
