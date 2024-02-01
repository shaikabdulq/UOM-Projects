# Builds the request URL, Makes API request to Google Maps Geocoding 
# API and prints Location Name, Address, Latitudes and Longitudes 

## program is working but access is denied due to missing API key

import urllib.request, urllib.parse, urllib.error
import json

url = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = input('Enter a location:')
if len(address)<0:
    address = r'Ann Arbor, MI'
complete_url = url+urllib.parse.urlencode({'address':address})
print(complete_url)

byte_json = urllib.request.urlopen(complete_url)
raw_json = byte_json.read().decode()

try:
    data = json.loads(raw_json)
except:
    print('Error! Could not process json')
    quit()

print('Name: ', data['results'][0]['address_components'][0]['long_name'])
print('Address: ', data['results'][0]['formatted_address'])
print('Lat: ', data['results'][0]['geometry']['location']['lat'])
print('Lat: ', data['results'][0]['geometry']['location']['lng'])
