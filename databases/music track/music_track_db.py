# Creates a music track database (trackdb.sqlite) from an XML file (Library.xml). It defines three tables:
# Artist, Album, and Track, with relationships among them. The script uses XML parsing to extract music
# track information such as track name, artist, album, play count, rating, and length. This data is then 
# inserted into the respective tables

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

stuff = ET.parse(fname)
data = stuff.findall('dict/dict/dict')

# Finally working !!
def lookup(items,key_word):
    found = False
    for item in items:
        if found is True:
            return item.text
            found = False
        if item.tag == 'key' and item.text == key_word:
            found = True

c = 0
for items in data:

    name = lookup(items, 'Name')
    artist = lookup(items, 'Artist')
    album = lookup(items, 'Album')
    count = lookup(items, 'Play Count')
    rating = lookup(items, 'Rating')
    length = lookup(items, 'Total Time')

    if name is None or artist is None or album is None:
       continue

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, len, rating, count) VALUES ( ?, ?, ?, ?, ? )''',
    ( name, album_id, length, rating, count ) )

    if c == 20:
        conn.commit()
        c = 0
    c = c + 1
