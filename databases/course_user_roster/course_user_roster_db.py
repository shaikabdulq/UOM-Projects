# Creates an SQLite database rosterdb.sqlite with tables User, Course, and Member. Then reads data from a 
# JSON file (roster_data.json), containing user names and course titles, inserts this data into the database, 
# linking users with courses in the Member table.

import sqlite3
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,'name' TEXT UNIQUE);

CREATE TABLE Course ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
'title' TEXT UNIQUE);

CREATE TABLE Member ('user_id' INTEGER, 'course_id' INTEGER, 'role' INTEGER, 
PRIMARY KEY (user_id,course_id));
''')

# Json part
import json
file = open('roster_data.json')
fhand = file.read()
data = json.loads(fhand)

count=0
for row in data:
    #print(row)
    name = row[0]
    title = row[1]
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''',(name,))
    cur.execute('''SELECT id FROM User WHERE name=?''',(name,))
    user_id=(cur.fetchone()[0])

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''',(title,))
    cur.execute('''SELECT id FROM Course WHERE title=?''',(title,))
    course_id=(cur.fetchone()[0])

    # In the below code, IGNORE/REPLACE command give the same result but Charles informed us to use replace (idkw)
    cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id) VALUES (?,?)''',(user_id,course_id))

    count=count+1
    if count==10:
        conn.commit()
        count=0


cur.execute('''SELECT User.name, Course.title FROM User JOIN Course JOIN Member ON User.id=Member.user_id AND Course.id=Member.course_id ORDER BY User.name,Course.title''')
print(cur.fetchall())
conn.close()