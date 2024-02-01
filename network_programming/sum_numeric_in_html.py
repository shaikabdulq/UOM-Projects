# Parses HTML using BeautifulSoup Module from a URL to extract and
# get sum of numeric values contained in 'span' tags.

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1745708.html'
html = urlopen(url).read()

soup = BeautifulSoup(html,'html.parser')

tags = soup('span')

sum = 0
count = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
    count = count + 1

print("Count ",count)
print("Sum",sum)
