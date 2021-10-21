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


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
c.execute('''CREATE TABLE IF NOT EXISTS roster (
    name TEXT       NOT NULL, 
    age INTEGER     NOT NULL,
    userid INTEGER  NOT NULL
)''')

with open('students.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        command = f"INSERT INTO roster VALUES (\"{row['name']}\", {row['age']}, {row['id']});"
        c.execute(command)

c.execute('''CREATE TABLE IF NOT EXISTS courses (
    code TEXT       NOT NULL, 
    mark INTEGER    NOT NULL,
    juniors INTEGER NOT NULL
)''')

with open('courses.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        command = f"INSERT INTO courses VALUES (\"{row['code']}\", {row['mark']}, {row['id']});"
        c.execute(command)

# ==========================================================

db.commit()  # save changes
db.close()  # close database
