from flask import render_template

from config import app
from model import Book


@app.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)


if __name__ == '__main__':
    app.run()
