# Use words.txt as the file name
fname = raw_input("Use words.txt as the file name\nEnter file name: ")
try :
    fhandle = open(fname)
except :
    print "File", fname, "does not exists"
    quit()
for line in fhandle :
    line = line.rstrip()
    line = line.upper()
    print line
fhandle.close()
