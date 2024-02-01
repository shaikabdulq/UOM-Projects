# Parses HTML from a url using  BeautifulSoup and prints the contents and
# href of 'a' tags (aka Links in Anchor Tags). Also displays count of 
# 'a' tags found. 

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter URL: ")
if len(url)<1:
    url = 'http://google.com'
html = urlopen(url).read()

soup = BeautifulSoup(html,'html.parser')
#print(soup)

tags = soup('a')
count=0
for tag in tags:
    count=count+1
    print(tag.contents[0],":",tag.get('href',None))
print("count: ",count)