from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import User

# blueprint for auth routes in our app
from .auth import auth as auth_blueprint

# blueprint for non-auth parts of app
from .main import main as main_blueprint

app = Flask(__name__)

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://sqladmin:iLAmO46czQdqINjdCCq4@sql-spamapp.database.windows.net/db-spamapp"

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

@app.route('/')
def hello_world():
    return 'Hello, World!'
