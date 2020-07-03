from datetime import datetime
from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    lastname = db.Column(db.String(120), index=True)
    books = db.relationship("Intermediate", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author {self.name} {self.lastname}>"


class Intermediate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey('book.id'))
    id_author = db.Column(db.Integer, db.ForeignKey('author.id'))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    authors = db.relationship("Intermediate", backref="book", lazy="dynamic")

    def __str__(self):
        return f"<Book {self.title}>"


class Borrowed(db.Model):
    id = db.Cb9.idolumn(db.Integer, primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey('book.id'))
    date_borrowed = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_return = db.Column(db.Boolean, default=False)