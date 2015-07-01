########################
##### imports ###########
#########################

from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, session   # pragma: no cover

from project import db   # pragma: no cover
from project.models import User, bcrypt   # pragma: no cover
from functools import wraps
from form import LoginForm

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
            return redirect(url_for('users.login'))
    return wrap

################
### Routes #####
################

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  form = LoginForm(request.form)
  if request.method == 'POST':
      if form.validate_on_submit():
          user = User.query.filter_by(name=request.form['username']).first()
          if user is not None and bcrypt.check_password_hash(
            user.password, request.form['password']):
              session['logged_in'] = True
              flash("You were just logged in")
              return redirect(url_for('home.home'))
          else:
            error = 'Invalid Credentials. Please try again.'
  return render_template('login.html',form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
  session.pop('logged_in', None)
  flash("You were just logged out")
  return redirect(url_for("home.welcome"))
