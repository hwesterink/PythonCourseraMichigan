import urllib
import re
from BeautifulSoup import *

url_choice = raw_input("Which link do you want to start with?\n 1 = known_by_Fikret.html\n 2 = known_by_Abbi.html\n")
if url_choice == "1":
    url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
    repeats = 4
    position = 2
elif url_choice == "2":
    url = "http://python-data.dr-chuck.net/known_by_Abbi.html"
    repeats = 7
    position = 17
else:
    print "Illegal choise."
    quit()

for i in range(repeats):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    string = str(tags[position])
    url = re.findall('href="(.+)"', string)[0]

print tags[position].contents[0]
