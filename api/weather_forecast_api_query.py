# Checks weather forecast for next 4 days using latitude and longitude
# with an API request to the OpenWeatherMap API.

## API key needed

import urllib.parse, urllib.request, urllib.error
import json

def weather_forecast():
    link='http://api.openweathermap.org/data/2.5/forecast?'
    lat=input('Enter Latitudes:')
    lon=input('Enter Longitudes:')
    if len(lat)<0: lat=17.3850
    if len(lon)<0: lon=78.4867
    api_key = 'ENTER_API_KEY'
    url= link + urllib.parse.urlencode({'lat':lat,'lon':lon,'appid':api_key})
    print(url)
    handle = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    try:
        opened_handle = urllib.request.urlopen(handle)
        data = opened_handle.read().decode()
        # print(data)
    except urllib.error.HTTPError as e:
        print('Error',e.code)
        quit()
    js = json.loads(data)
    for i in js['list']:
        date_time = i['dt_txt']
        #Converting Temperature from Kelvin to Celsius
        temp = float(i['main']['temp'])-273.15
        humidity = i['main']['humidity']
        weather = i['weather'][0]['description']
        print(f'\nWeather Forecast for {date_time}...')
        print('Temperature:',round(temp,1))
        print('Humidity:',humidity)
        print('Weather:',weather)

weather_forecast()