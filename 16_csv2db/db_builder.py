# Team The Best Laptop - Jonathan Wu [Loki] , Alif Abdullah [The Eagle in the Sand], Kevin Cao [Pipi] | Period 2
# SoftDev
# K16 - All About Database
# 2021-10-20

import sqlite3  # enable control of an sqlite database
import csv  # facilitate CSV I/O


DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
c = db.cursor()  # facilitate db ops -- you will use cursor to trigger db events

# ==========================================================


# creates a table for the students.csv file with row 'name', 'age', 'id'
c.execute('''CREATE TABLE IF NOT EXISTS roster (
    name TEXT       NOT NULL,
    age INTEGER     NOT NULL,
    userid INTEGER  NOT NULL    PRIMARY KEY
)''')

# reads the csv file and then inserts the csv values into the respective rows
with open('students.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        command = f"INSERT INTO roster VALUES (\"{row['name']}\", {row['age']}, {row['id']});"
# this try except block is to ensure that the user doesn't append the data multiple times to the database
        try:
            c.execute(command)
        except:
            continue
# creates a table for the courses.csv file with row 'code', 'mark', 'id'
c.execute('''CREATE TABLE IF NOT EXISTS courses (
    code TEXT       NOT NULL,
    mark INTEGER    NOT NULL,
    juniors INTEGER NOT NULL
)''')

# reads the csv file and then inserts the csv values into the respective rows
with open('courses.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        command = f"INSERT INTO courses VALUES (\"{row['code']}\", {row['mark']}, {row['id']});"
        c.execute(command)

# ==========================================================

db.commit()  # save changes
db.close()  # close database
