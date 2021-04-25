from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Session_tracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.String(1000))

class Mails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    text = db.Column(db.String(1000))
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))