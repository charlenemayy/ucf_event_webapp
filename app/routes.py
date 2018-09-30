from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm #, RegistrationForm
# from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Knightro'},
            'body': 'Go Knights!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index')) # gets url for function that maps to 'index'

    form = LoginForm()
    '''
    # login and validate user
    if form.validate_on_submit():
        # query user from the database
        # user = User.query.filter_by(username=form.username.data).first()
        # check for null
        # if user is None or not user.check_password(form.password.data):
        if form.password.data != "test":
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        '''
    return render_template('login.html', title='Sign In', form=form)
