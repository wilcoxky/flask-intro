from flask import Flask, render_template, url_for, redirect, request, \
 session, flash, g
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
# import sqlite3

app = Flask(__name__)
bcrypt = Bcrypt(app)


#config file
import os
app.config.from_object(os.environ['APP_SETTINGS'])


#Create Sqlachemy object
db = SQLAlchemy(app)

#import Models after you make the db object
from models import *

#def wrap function required to login
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('you must log in first!')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPosts).all()
    return render_template("index.html", posts = posts)


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

# route for handling the login page logic


@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
      error = 'Invalid Credentials. Please try again.'
    else:
      session['logged_in'] = True
      flash("You were just logged in")
      return redirect(url_for('home'))
  return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
  session.pop('logged_in', None)
  flash("You were just logged out")
  return redirect(url_for("welcome"))





if(__name__) == '__main__':
    app.run()
