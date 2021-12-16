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
    return render_template("base.html", books=books)

@app.route("/add", methods=["POST"])
def add():
    connect = db_connection()
    cursor = connect.cursor()

    title = request.form.get('title')
    author = request.form.get("author")
    language = request.form.get("language")
    sql = """INSERT INTO books(title, author, language) VALUES (?, ?, ?)"""

    cursor.execute(sql, (title, author, language))
    connect.commit()

    return redirect(url_for("index"))

@app.route("/book/<int:id>")
def book(id):
    print(id)
    connect = db_connection()
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM books WHERE id=?", (id,))

    book = [
        dict(id=row[0], title=row[1], author=row[2], language=row[3])
        for row in cursor.fetchall()
    ]

    return render_template('book.html', book=book)

if __name__ == "__main__":
    app.run(debug=True)
