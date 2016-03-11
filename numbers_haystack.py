# Import modules for this program
import re

# Initialize variables
numbers = []

# Open the file to be processed
# Use the file name regex_sum_42.txt as the default file name
fname = raw_input("File name defaults to regex_sum_42.txt\nEnter file name: ")
if len(fname) == 0 :
    fname = "regex_sum_42.txt"
try :
    fhandle = open(fname)
except :
    print "File", fname, "does not exist"
    quit()

# Extract the numbers from the lines, convert them into integers
# and build a list of integers 
for line in fhandle :
    nums = re.findall("[0-9]+", line)
    if len(nums) == 0 : continue
    for num in nums :
        numbers.append(int(num))
        
# Close the file
fhandle.close()

# Print the count and sum for the selected numbers
print "Numbers found", len(numbers)
print "with a sum of", sum(numbers)

# Do the same in a one-line unreadable version for regex_sum_238857
print sum([int(n) for n in re.findall('[0-9]+', open('regex_sum_238857.txt').read())])
