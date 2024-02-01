# Takes input for Pokemon Name and Make API call to PokeAPI for Pokemon Data
## No API Key Needed

import urllib.request, urllib.parse, urllib.error
import json

poke_url = 'http://pokeapi.co/api/v2/pokemon/'
poke = input('Enter a pokemon: ')
url = poke_url + poke.lower()
print(url)
request = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
open = urllib.request.urlopen(request)
data = open.read().decode()

js = json.loads(data)
#print(json.dumps(js, indent=4))
print('Name:            ',js['name'])
print('ID:              ',js['id'])
print('Height:          ',js['height'])
print('Weight:          ',js['weight'])
print('Move-1:          ',js['moves'][0]['move']['name'])
print('Move-2:          ',js['moves'][1]['move']['name'])
try: print('Move-2:          ',js['moves'][2]['move']['name'])
except: print('Move-3:           None')
print('Type-1:          ',js['types'][0]['type']['name'])
try:print('Type-2:          ',js['types'][1]['type']['name'])
except:print('Type-2:           None')
print('HP:              ',js['stats'][0]['base_stat'])
print('Attack:          ',js['stats'][1]['base_stat'])
print('Defence:         ',js['stats'][2]['base_stat'])
print('Special Attack:  ',js['stats'][3]['base_stat'])
print('Special Defense: ',js['stats'][4]['base_stat'])
print('Speed:           ',js['stats'][5]['base_stat'])