# Creates an SQLite database trackdb2.sqlite with tables for Artist, Album, Track, and Genre. Then it reads 
# from an XML file (Library.xml) and extracts details such as track name, length, rating, play count, genre, 
# album, and artist. These details are then inserted into their respective tables. 

import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('trackdb2.sqlite')
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

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
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    genre_id INTEGER,
    album_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);
''')

def lookup(var,key_word):
    condition=False
    for itr in var:
        if condition == True:
            return itr.text
        condition = False
        if itr.text == key_word:
            condition = True



fhand = ET.parse('Library.xml')
#print(fhand)

file = fhand.findall('dict/dict/dict')
counter=0
for a in file:
    counter+=1


    track = lookup(a, 'Name')
    len = lookup(a,'Total Time')
    rating = lookup(a, 'Rating')
    count = lookup(a, 'Play Count')
    genre = lookup(a, 'Genre')
    album= lookup(a,'Album')
    artist = lookup(a, 'Artist')
    print(track, len, rating, count, genre, album, artist)

    if artist ==None or album==None or genre==None or track==None :
        continue
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''',(artist,) )
    cur.execute('''SELECT id from Artist where name=? ''',(artist,))
    artist_id=cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title,artist_id) Values (?,?) ''',(album,artist_id))
    cur.execute('''SELECT id from Album where title=?''', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''',(genre,))
    cur.execute('''SELECT id from Genre where name=?''',(genre,))
    genre_id= cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track (title,len,rating,count,genre_id,album_id) VALUES (?,?,?,?,?,?)''', (artist,len,rating,count,genre_id,album_id))
    if counter==20:
        counter=0
        conn.commit()

cur.execute('''SELECT Track.title,Track.len''')



