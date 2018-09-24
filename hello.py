from flask import Flask, flash, redirect, render_template, request
from flask import session, abort
import os

app = Flask(__name__)


@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Login Success"


@app.route("/login", methods=['POST'])
def do_login():
    if request.form['password'] == 'password' and request.form['username'] == 'user':
        session['logged_in'] = True
    else:
        flash('Wrong Password')
    return home()


# create a button that links to this url route
@app.route("/logout")
def do_logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()
