# Parses and prints information from a simple XML structure

import xml.etree.ElementTree as ET

xml = '''<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(xml)
print(tree.find('name').text)
print(tree.find('phone').text.strip())
print(tree.find('email').text)
print(tree.find('email').get("hide"))

