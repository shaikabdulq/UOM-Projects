# Program to use PY4E GeoCode API and retrieve data for addresses 
# and other details

## No API Key needed

import urllib.parse, urllib.request
import json

api = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    url = api + urllib.parse.urlencode({'address':address,'key':42})
    print('Retrieving',url)

    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    print('Retrieved',len(data),'characters')
    js = json.loads(data)
    #print(json.dumps(js,indent=4))
    print("Address:",js['results'][0]['formatted_address'])
    print('Place id',js['results'][0]['place_id'])
    print("Latitude:",js['results'][0]['geometry']['location']['lat'])
    print('Longitude:',js['results'][0]['geometry']['location']['lng'])
    print('Types:',tuple(js['results'][0]['types']))
