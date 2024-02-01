# Creates a database emaildb.sqlite and a table Count with columns email and count. Then extracts emails from 
# a text file mbox-short.txt, and updates the database with the count of each email. After processing, it 
# retrieves the top 10 email addresses by count, displaying them.

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Count''')
cur.execute('''CREATE TABLE Count (email TEXT, count INTEGER)''')
file = input('Enter File Name: ')
if len(file)<1: fh = open('mbox-short.txt')
else: fh =open(file)
c = 0
for line in fh:
    if line.startswith('From:'):
        word=line.split()
        email = word[1]
        # Database codes
        cur.execute('''SELECT count from Count WHERE email = ?''',(email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Count (email, count) VALUES (?,1)''',(email,))
        else:
            cur.execute('''UPDATE Count SET count = count + 1 WHERE email = ? ''',(email,))
        c = c + 1
        if c == 10:
            conn.commit()
            c=0
    else: continue

# For reading in Python
cur.execute('''SELECT email, count FROM Count ORDER BY count DESC LIMIT 10''')
rows = cur.fetchall()
for row in rows:
    print(row[0],row[1])

cur.close()
