def computepay(h,r):
    if hours > 40 :
        p = (40 * r) + (h - 40) * r * 1.5
    else:
        p = h * r
    return p

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
pay = computepay(hours,rate)
print pay
