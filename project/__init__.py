#########################
##### imports ###########
#########################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os


app = Flask(__name__)

###################
##### config ######
###################


app.config.from_object(os.environ['APP_SETTINGS'])

###################
#### Database #####
###################
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# import Models after you make the db object
from project.users.views import users_blueprint
from project.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
