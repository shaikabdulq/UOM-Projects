# Checks current weather using latitude and longitude with an API request
# to the OpenWeatherMap API.

## API key needed

import urllib.parse
import urllib.request, urllib.error
import json

# Program to check weather across the world using latitudes and longitudes
def weather():
    link='http://api.openweathermap.org/data/2.5/weather?'
    lat=input('Latitudes: ')
    lon=input('Longitudes: ')
    api_key = 'ENTER_API_KEY'
    url= link + urllib.parse.urlencode({'lat':lat,'lon':lon,'appid':api_key})
    # print(url)
    handle = urllib.request.urlopen(url)
    byte_data = handle.read().decode()
    headers = handle.getheaders()
    #print(headers)
    js = json.loads(byte_data)
    print(json.dumps(js, indent=4))
    print('City:', js['name'])
    print('Country:', js['sys']['country'])
    print('Weather:', js['weather'][0]['description'])
    print('Date_and_Time:', headers[1][1])

weather()
