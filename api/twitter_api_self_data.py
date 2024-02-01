# Sends a request to the Twitter API's endpoint and parses the JSON data returned by the API,
# extracts the user's ID, name, and username from the response and prints them out.

import json
import urllib.request, urllib.parse, urllib.error
import ssl

url = 'https://api.twitter.com/2/users/me'


# Ignore SSL Certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

    
try:
    connection = urllib.request.urlopen(url, context=ctx)
except Exception as err:
    print('Error! Failed to retrieve', err)
    quit()


data = connection.read().decode()
headers = dict(connection.getheaders())


print('Remaining',headers['x-rate-limit-remaining'])

try:
    js = json.loads(data)
except:
    print("Unable to parse")
    print(data)
    quit()

id = js[0]['data']['id']
name = js[0]['data']['name']
username = js[0]['data']['username']

print('Id:',id,)
print('Name:',name,)
print('Id:',username,)

