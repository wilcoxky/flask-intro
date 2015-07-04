from functools import wraps
from flask import render_template, Blueprint, \
    request, flash, redirect, url_for, session  # pragma: no cover
from flask.ext.login import login_required, current_user
from project import db   # pragma: no cover
from project.models import BlogPosts   # pragma: no cover
from form import MessageForm
# Helpers #

# def wrap function required to login

home_blueprint = Blueprint('home', __name__, template_folder='templates')

# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('you must log in first!')
#             return redirect(url_for('users.login'))
#     return wrap


@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        blog = BlogPosts(
            title=form.title.data,
            description=form.content.data,
            author_id=current_user.id
        )
        db.session.add(blog)
        db.session.commit()
        flash("New Post has been added", category='message')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPosts).all()
        return render_template("index.html", posts=posts, form=form)


@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")
