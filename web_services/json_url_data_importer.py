# Importing json from URL and retrieving data

import urllib.request, urllib.parse
import json

url =  'http://py4e-data.dr-chuck.net/comments_1745711.json'
print('Retrieving',url)
handle = urllib.request.urlopen(url)
code = handle.read().decode()
data = json.loads(code)
print('Retrieved',len(code),'characters')
#print(json.dumps(data,indent=4))
list = data['comments']
count=0
sum=0
for item in list:
    #print(item['name'],item['count'])
    count=count+1
    sum=sum+int(item['count'])
print('Count:',count)
print('Sum:',sum)