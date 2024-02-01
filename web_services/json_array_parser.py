# Parsing a JSON array, iterating through items and printing

import json

content='''[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

conv_content=json.loads(content)
for item in conv_content:
    print(item['id'])
    print(item['name'])
    print(item['x'])