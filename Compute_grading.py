scr = raw_input("Enter a Score between 0.0 and 1.0:")
try:
    score = float(scr)
except:
    print ("Please enter a numeric Score")
    quit()
if score > 1.0 :
    print ("***** Error ==> Score bigger than 1")
    quit()
elif score >= 0.9:
    grading = "A"
elif score >= 0.8:
    grading = "B"
elif score >= 0.7:
    grading = "C"
elif score >= 0.6:
    grading = "D"
elif score >= 0.0:
    grading = "F"
else:
    print ("***** Error ==> Score is negative")
    quit()
print grading
