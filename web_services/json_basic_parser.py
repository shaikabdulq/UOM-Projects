# Parsing and printing with a basic JSON object

import json

content='''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

string_of_content = json.loads(content)
print(string_of_content['phone']['number'])
print(string_of_content['name'])
print(string_of_content['email']['hide'])