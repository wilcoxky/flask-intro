#########################
##### imports ###########
#########################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
import os


app = Flask(__name__)

###################
##### config ######
###################


app.config.from_object(os.environ['APP_SETTINGS'])
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# import Models after you make the db object
from project.users.views import users_blueprint
from project.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
login_manager.login_view = "users.login"
login_manager.login_message = "you must log in first!"


from models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()
