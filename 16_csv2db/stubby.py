#a Python script for interacting with an SQLite db:
import sqlite3 #enable SQLite operations
import csv

#open db if exists, otherwise create
db = sqlite3.connect("foo")

c = db.cursor() #facilitate db ops


c.execute("CREATE TABLE IF NOT EXISTS roster(name TEXT, age INTEGER, userid INTEGER)")

with open('students.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        command = f"INSERT INTO roster VALUES ({row['name']}, {row['age']}, {row['name']});"
        c.execute(command)

db.commit() #save changes
db.close()
