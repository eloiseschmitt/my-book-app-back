from flask_sqlalchemy import SQLAlchemy

from config import app

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    read = db.Column(db.Boolean)


with app.app_context():
    db.create_all()
