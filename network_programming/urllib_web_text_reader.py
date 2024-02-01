# This script retrieves text from a specific URL using urllib and 
# prints each line of the text

import urllib.request
import urllib.parse
import urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())