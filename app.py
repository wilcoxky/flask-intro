#########################
##### imports ###########
#########################

from flask import Flask, render_template, url_for, redirect, request, \
 session, flash, g
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

###################
##### config ######
###################
import os
app.config.from_object(os.environ['APP_SETTINGS'])

###################
#### Database #####
###################
db = SQLAlchemy(app)

#import Models after you make the db object
from models import *
from project.users.views import users_blueprint

app.register_blueprint(users_blueprint)

###################
#### Helpers  #####
###################

#def wrap function required to login
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('you must log in first!')
            return redirect(url_for('users.login'))
    return wrap


@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPosts).all()
    return render_template("index.html", posts = posts)


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")



if(__name__) == '__main__':
    app.run()
