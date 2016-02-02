hrs = raw_input("Enter Hours:")
hours = float(hrs)
rt = raw_input("Enter Rate per Hour:")
rate = float(rt)
if hours > 40 :
    pay = (40 * rate) + (hours - 40) * rate * 1.5
else:
    pay = hours * rate
print pay
