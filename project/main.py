from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from .models import Mails
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/adminpanel')
def adminpanel():
    return render_template('adminpanel.html')


@main.route('/adminpanel', methods=['POST'])
def adminpanel_post():
    email = request.form.get('Email')
    subject = request.form.get('Subject')
    text = request.form.get('Text')
    date = request.form.get('Date')
    time = request.form.get('Time')

    # co bedzie zapisane do bazy danych
    db_record_new_session = Mails(email=email, subject=subject, text=text, date=date, time=time)

    # add the new user to the database
    db.session.add(db_record_new_session)  # przygotowanie obiektu ORM
    db.session.commit()  # commit do bazy
    return redirect(url_for('main.adminpanel'))
