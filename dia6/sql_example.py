import sqlite3


con = sqlite3.connect("sql_exemple.db")
con.execute("PRAGMA foreign_keys = ON;")

instructions = """\
CREATE TABLE  if not exists person(
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar NOT NULL,
    emial varchar UNIQUE NOT NULL,
    dept varchar NOT NULL,
    role varchar NOT NULL
);
---
CREATE TABLE  if not exists balance(
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer UNIQUE NOT NULL,
    value integer NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE  if not exists movement(
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer NOT NULL,
    value integer NOT NULL,
    date integer NOT NULL,
    actor integer NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE  if not exists user(
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer NOT NULL,
    password varchar NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
"""

for instruction in instructions.split('---'):
    con.execute(instruction)

con.close()

con = sqlite3.connect("sql_exemple.db")
con.execute("PRAGMA foreign_keys = ON;")

instruction = """\
SELECT id, name, emial, dept, role
FROM person
WHERE dept = 'Sales';
"""

cur = con.cursor()
result = cur.execute(instruction)
print(*result)
