import sqlite3

connection = sqlite3.connect("sqlite3.db")


sql_query = """ CREATE TABLE books (
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    language text NOT NULL
)
"""

connection.execute(sql_query)
print("table created!")