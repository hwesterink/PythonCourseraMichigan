import urllib
import xml.etree.ElementTree as ET

total = 0

url_choice = raw_input("Which file do you want to open?\n 1 = comments_42.html\n 2 = comments_238862.html\n")
if url_choice == "1":
    url = "http://python-data.dr-chuck.net/comments_42.xml"
elif url_choice == "2":
    url = "http://python-data.dr-chuck.net/comments_238859.xml"
else:
    print "Illegal choise."
    quit()

xml_data = urllib.urlopen(url).read()
tree = ET.fromstring(xml_data)
counts = tree.findall('.//count')

for count in counts:
    total += int(count.text)

print "Sum of counts = ", total
