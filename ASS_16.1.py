"""
This file holds the solution to assignment 16.1 of the book
Python for Informatics by Charles Severance
"""

# Import modules needed in this program
import os
from os.path import join
import hashlib

######################################################################
#  Main program flow
######################################################################

# Initialize variables for this job
pict_dir = {}

# Initialize constants for this job
TYPE_DICT = type(pict_dir)

# Build a directory based on the sizes of the files
for (dirname, dirs, files) in os.walk("C://Temp/Foto's/"):
    for filename in files:
        if filename.endswith('.JPG'):
            thefile = os.path.join(dirname,filename)
            size = os.path.getsize(thefile)
            pict_dir[size] = pict_dir.get(size, [])
            pict_dir[size].append(thefile)

# Build dictionaries in the pict_dir dictionary with checksums of files with
# the same size
for key, value in pict_dir.items():
    if len(value) > 1:
        checksums = {}
        for thefile in value:
            fhandle = open(thefile, 'r')
            data = fhandle.read()
            fhandle.close()
            checksum = hashlib.md5(data).hexdigest()
            checksums[checksum] = checksums.get(checksum, [])
            checksums[checksum].append(thefile)
        pict_dir[key] = checksums

# Print out the results
for values in pict_dir.values():
    if type(values) == TYPE_DICT:
        for value in values.values():
            if len(value) > 1:
                print "The following files are equal:"
                for thefile in value:
                    print thefile
            print
        

            
