# initialize variables
largest = None
smallest = None
numbers = False

while True :
    # get next number
    inp = raw_input ("Enter a number: ")

    # handle end conditions
    if inp == "done" : break
    if len(inp) == 0 : break

    # convert the number or give a message on wrong input
    try:
        num = int(inp)
    except:
        print "Invalid input"
        continue

    # work the number entered
    if largest is None :
        largest = num
        smallest = num
        numbers = True
    else :
        if largest < num :
            largest = num
        if smallest > num :
            smallest = num

# print largest and smallest
if numbers :
    print "Maximum is", largest
    print "Minimum is", smallest
else :
    print "No numbers entered"
