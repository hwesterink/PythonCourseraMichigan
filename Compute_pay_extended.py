hrs = raw_input("Enter Hours:")
try:
    hours = float(hrs)
except:
    print ("***** Error ==> Please enter numeric input for hours")
    quit()
rt = raw_input("Enter Rate per Hour:")
try:
    rate = float(rt)
except:
    print ("***** Error ==> Please enter numeric input for rate")
    quit()
if hours < 0 or rate < 0 :
    print ("***** Error ==> Negative numbers for hours or rate not allowed")
    quit()
if hours > 40 :
    pay = (40 * rate) + (hours - 40) * rate * 1.5
else:
    pay = hours * rate
print "Amount to pay = ", pay
