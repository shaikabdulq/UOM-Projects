# Parses a complex JSON structure, typically resembling a response from a web API and print specific fields

import json

raw_json = '''{
    "status": "OK",
     "results": [
        {
            "geometry": {
                "location_type": "APPROXIMATE",
                 "location": {
                    "lat": 42.2808256,
                     "lng": -83.7430378
                }
            },
            "address_components": [
                {
                    "long_name": "Ann Arbor",
                     "types": [
                        "locality",
                         "political"
                    ],
                    "short_name": "Ann Arbor"
                }
             ],
             "formatted_address": "Ann Arbor, MI, USA",
             "types": [
                "locality",
                "political"
            ]
        }
    ]
}'''

try:
    data = json.loads(raw_json)
except:
    print('Error! Could not process json')
    quit()

print('Name: ', data['results'][0]['address_components'][0]['long_name'])
print('Address: ', data['results'][0]['formatted_address'])
print('Lat: ', data['results'][0]['geometry']['location']['lat'])
print('Lat: ', data['results'][0]['geometry']['location']['lng'])
