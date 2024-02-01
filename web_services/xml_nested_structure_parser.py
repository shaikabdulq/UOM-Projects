import xml.etree.ElementTree as ET

xml='''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(xml)
lst = tree.findall('users/user')
print("No. of users: ",len(lst))
print(lst)
for item in lst:
    print("ID: ",item.find('id').text)
    print("Name: ",item.find('name').text)
    print("Attr: ",item.get('x'))