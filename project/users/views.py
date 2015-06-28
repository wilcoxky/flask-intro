########################
##### imports ###########
#########################

from flask import render_template, url_for, redirect, request, \
 session, flash, Blueprint
from functools import wraps
from flask.ext.bcrypt import Bcrypt
from app import app
bcrypt = Bcrypt(app)


################
#### config ####
################
users_blueprint = Blueprint('users', __name__, template_folder='templates')


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

################
### Routes #####
################

@users_blueprint.route('/login', methods=['GET', 'POST'])
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


@users_blueprint.route('/logout')
@login_required
def logout():
  session.pop('logged_in', None)
  flash("You were just logged out")
  return redirect(url_for("welcome"))
