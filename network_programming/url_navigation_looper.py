# Fetches HTML from URL and navigates through the links in a loop, 
# based on count and position. Displays current URL being retrieved.

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
url_count = 0
desired_count = input('Enter count: ')
desired_position = input('Enter position: ')
if len(url)<1:
    url = "http://py4e-data.dr-chuck.net/known_by_Connor.html"
print('Retrieving: ', url)
while url_count != int(desired_count):
    url_count = url_count + 1
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    tag_position = 0
    for tag in tags:
        tag_position = tag_position + 1
        if tag_position == int(desired_position):
            url = tag.get('href', None)
            print('Retrieving: ', url)