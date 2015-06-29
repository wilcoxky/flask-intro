from functools import wraps
from flask import render_template, Blueprint, \
    request, flash, redirect, url_for, session  # pragma: no cover

from project import db   # pragma: no cover
from project.models import BlogPosts   # pragma: no cover
# Helpers #

# def wrap function required to login

home_blueprint = Blueprint('home', __name__, template_folder='templates')

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('you must log in first!')
            return redirect(url_for('users.login'))
    return wrap


@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(BlogPosts).all()
    return render_template("index.html", posts=posts)


@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")
