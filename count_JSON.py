import urllib
import json

total = 0

url_choice = raw_input("Which file do you want to open?\n 1 = comments_42.html\n 2 = comments_238863.html\n")
if url_choice == "1":
    url = "http://python-data.dr-chuck.net/comments_42.json"
elif url_choice == "2":
    url = "http://python-data.dr-chuck.net/comments_238863.json"
else:
    print "Illegal choise."
    quit()

json_data = urllib.urlopen(url).read()
json_dict = json.loads(json_data)
comments = json_dict["comments"]

for item in comments:
    total += item["count"]

print "Sum of counts = ", total
