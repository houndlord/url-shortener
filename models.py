#database model

from app import db

class Link(db.model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(62), index=True)
    shortlink = db.Column(db.String(6), index=True)
