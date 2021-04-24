from project import create_app
from project import db
from flask_login import UserMixin
from .models import User, Session_tracking, Mails

app = create_app()

with app.test_request_context():
     db.init_app(app)
     db.create_all()
     print("Baza aplikacji została założona")