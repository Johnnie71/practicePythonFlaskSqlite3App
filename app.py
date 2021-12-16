from sqlite3.dbapi2 import connect
from flask import Flask, render_template, url_for, redirect, request
import sqlite3

app = Flask(__name__)

def db_connection():
    connection = sqlite3.connect("sqlite3.db")
    return connection

@app.route("/")
def index():
    connect = db_connection()
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM books")

    books = [
        dict(id=row[0], title=row[1], author=row[2], language=row[3])
        for row in cursor.fetchall()
    ]
    print(books)
    return render_template("base.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
