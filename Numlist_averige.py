# initialize counters
count = 0
total = 0

while True :
    # get next number
    inp = raw_input ("Enter a number: ")

    # handle end conditions
    if inp == "done" : break
    if len(inp) == 0 : break

    # convert the number or give a message on wrong input
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue

    # work the number entered
    count = count + 1
    total = total + num

# print the averige
if count > 0 :
    print total / count
else :
    print "No numbers entered"
