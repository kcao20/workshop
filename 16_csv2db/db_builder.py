# Team The Best Laptop - Jonathan Wu [Loki] , Alif Abdullah [The Eagle in the Sand], Kevin Cao [Pipi] | Period 2
# SoftDev
# K16 - All About Database/Using sqlite3 and python together/As a group, we learned using sqlite3 and python together into: creating a db, reading a csv and then inserting data into a db table.
# 2021-10-20
# Time Spent: 90 minutes

import sqlite3  # enable control of an sqlite database
import csv  # facilitate CSV I/O

DB_FILE = "discobandit.db"  # creates a db file with the name discobandit

db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
c = db.cursor()  # facilitate db ops -- you will use cursor to trigger db events

# ==========================================================
# creates a table for the students.csv file with row 'name', 'age', 'id'
c.execute('''CREATE TABLE IF NOT EXISTS roster (
    name TEXT       NOT NULL,
    age INTEGER     NOT NULL,
    userid INTEGER  NOT NULL
)''')

# these statements here check if there is data in the db, if there isn't, then inverts values into the db
c.execute("SELECT * from roster")
studentData = c.fetchall()
if (studentData == []):
    # reads the csv file and then inserts the csv values into the respective rows
    with open('students.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            command = f"INSERT INTO roster VALUES (\"{row['name']}\", {row['age']}, {row['id']});"
            c.execute(command)

# creates a table for the courses.csv file with row 'code', 'mark', 'id'
c.execute('''CREATE TABLE IF NOT EXISTS courses (
    code TEXT       NOT NULL,
    mark INTEGER    NOT NULL,
    juniors INTEGER NOT NULL
)''')

# these statements here check if there is data in the db, if there isn't, then inverts values into the db
c.execute("SELECT * from courses")
courseData = c.fetchall()
if (courseData == []):
    # reads the csv file and then inserts the csv values into the respective rows
    with open('courses.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            command = f"INSERT INTO courses VALUES (\"{row['code']}\", {row['mark']}, {row['id']});"
            c.execute(command)
# ==========================================================

db.commit()  # save changes
db.close()  # close database
