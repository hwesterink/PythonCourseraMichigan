import urllib
from BeautifulSoup import *

count = 0
total = 0

url_choice = raw_input("Which file do you want to open?\n 1 = comments_42.html\n 2 = comments_238862.html\n")
if url_choice == "1":
    url = "http://python-data.dr-chuck.net/comments_42.html"
elif url_choice == "2":
    url = "http://python-data.dr-chuck.net/comments_238862.html"
else:
    print "Illegal choise."
    quit()

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

for tag in tags :
    count += 1
    total += int(tag.contents[0])
    print count, tag, tag.contents[0], total

print
print "Count:", count
print "Total:", total
