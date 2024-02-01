# Python Database Programs

### Overview
This repository contains a collection of Python scripts designed for database management. These scripts are used for setting up and interacting with SQLite databases.

1. **email_counter_db.py:** This script is a Python program that interacts with an SQLite database. It creates a database emaildb.sqlite and a table Count with columns email and count. The script then processes a text file (by default mbox-short.txt or a user-specified file), extracts email addresses from lines starting with 'From:', and updates the database with the count of each email. After processing, it commits the changes and retrieves the top 10 email addresses by count, displaying them. This script demonstrates basic SQLite operations in Python, including creating tables, inserting/updating data, and querying.

2. **course_user_roster_db.py:** This script creates an SQLite database rosterdb.sqlite with tables User, Course, and Member. It then reads data from a JSON file (roster_data.json), that contains user names and course titles. The script inserts this data into the database, linking users with courses in the Member table. It demonstrates more complex database operations like table creation with primary keys, data insertion with foreign keys, and using JOIN to combine data from multiple tables. The final query fetches and displays the combined user and course data, showcasing a many-to-many relationship between users and courses.

3. **music_track_db.py:** This script deals with creating and populating a music track database (trackdb.sqlite) from an XML file (Library.xml). It defines three tables: Artist, Album, and Track, with relationships among them. The script uses XML parsing to extract music track information such as track name, artist, album, play count, rating, and length. This data is then inserted into the respective tables, demonstrating complex database operations, including handling of foreign keys and data normalization. The script shows efficient database design for managing music library data, ensuring that each entity (artist, album, track) is stored once and linked appropriately.

4. **extended_music_track_db.py:** is similar to database3.py but with an added complexity of handling genres. It creates an SQLite database trackdb2.sqlite with tables for Artist, Album, Track, and now Genre. The script reads from an XML file (Library.xml) and extracts details such as track name, length, rating, play count, genre, album, and artist. These details are then inserted into their respective tables. The addition of the Genre table shows an advanced level of database normalization and association, allowing for more detailed queries and data organization. The script also demonstrates robust XML parsing and efficient data insertion strategies.

### Requirements
To use these scripts, you'll need Python 3.11 installed on your system. Additionally, ensure you have the sqlite3 module (included in standard Python distributions) for database operations. 

### Usage
Run each script individually as per your requirements. Ensure you have the appropriate files and database setup

### Contributing
Contributions to enhance these scripts or add new functionalities are welcome. Please adhere to standard coding practices and provide documentation for any changes made.