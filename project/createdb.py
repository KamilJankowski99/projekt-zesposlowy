from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask (__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://sqladmin:iLAmO46czQdqINjdCCq4@sql-spamapp.database.windows.net/db-spamapp"

db = SQLAlchemy(app)

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

with app.test_request_context():
     db.init_app(app)
     db.create_all()
     print("Test")