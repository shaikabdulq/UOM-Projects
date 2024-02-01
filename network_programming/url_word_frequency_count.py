# Reads a text file from a URL using urllib and displays the most
# frequently occurring word along with its frequency

import urllib.request
import urllib.parse
import urllib.error

file=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
dword={}

for line in file:
    line=line.decode().lower().strip()
    print(line)
    for word in line.split():
        dword[word]=dword.get(word,0)+1


print(f'\n"{(sorted(((v,k) for k,v in dword.items()),reverse=True))[0][1]}" is the most repeated word.')
print(f'It is repeated {(sorted(((v,k) for k,v in dword.items()),reverse=True))[0][0]} times')