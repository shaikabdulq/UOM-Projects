# Creates two tables, People and Follows in the twfriends.sqlite database. The People table stores 
# Twitter user names and a flag indicating whether their friends have been retrieved. The Follows table
# records relationships between users, showing who follows whom. The script allows the user to enter a
# Twitter account name, fetches the friends list for that account, and updates the database accordingly.

import sqlite3
import json
import twurl
import urllib.request, urllib.parse, urllib.error
import ssl

twitter_url = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('twfriends.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS People
('id' INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
'name' TEXT UNIQUE, retrieved INTEGER)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Follows
('from_id' INTEGER, 'to_id' INTEGER, UNIQUE(from_id,to_id))''')

# Ignore SSL Certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acc = input('Enter a twitter account, or quit: ')
    if acc == 'quit': break
    if len(acc) < 1: 
        cur.execute('''SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1''')
        try:
            (id,acc) = cur.fetchone()
        except:
            print('No unretrieved twitter accounts found')

            
    else:
        cur.execute('''SELECT id FROM People WHERE name=? LIMIT 1''',(acc,))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name,retrieved) VALUES (?,0)''',(acc,))
            conn.commit()
            if cur.rowcount!=1:
                print('Error inserting account',acc)
            id = cur.lastrowid


    url = twurl.augment(twitter_url,{'screen_name':acc,'count':25})
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Error! Failed to retrieve', err)
        quit()
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining',headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print("Unable to parse")
        print(data)
        break

    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(data,indent=4))
        continue

    cur.execute('''UPDATE People SET retrieved=1 WHERE name=?''',(acc,))


    countold = 0
    countnew = 0
    for u in js['users']:
        friend = u['screen_name']
        cur.execute('''SELECT id FROM People WHERE name=?''',(friend,))
    try:
        friend_id = cur.fetchone()[0]
        countold=countold+1
    except:
        cur.execute('''INSERT OR IGNORE INTO People (name,retrieved) VALUES (?,0)''',(friend,))
        conn.commit()
        if cur.rowcount!=1:
            print('Error inserting',friend)
            continue
        friend_id = cur.lastrowid
        countnew=countnew+1


    cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id) VALLUES (?,?)''',(id, friend_id))
    print('New Accounts:',countnew,'Revisted',countold)
    conn.commit()


cur.close()
