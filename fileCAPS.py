# Use words.txt as the file name
fname = raw_input("File name defaults to words.txt\nEnter file name: ")
if len(fname) == 0 :
    fname = "words.txt"
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
