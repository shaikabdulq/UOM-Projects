# Imports XML from URL and retrieves data

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url =  'http://py4e-data.dr-chuck.net/comments_1745710.xml'
print("Retrieving",url)
uh = urllib.request.urlopen(url)

data = uh.read().decode()
#print(data)
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

list = tree.findall('comments/comment')
sum = 0
count=0
for item in list:
    #print(item.find('name').text, item.find('count').text)
    sum = sum + int(item.find('count').text)
    count=count+1
print('Count:',count)
print('Sum:',sum)