from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(Form):
    username = TextField('username', validators=[DataRequired(), Length(min=3,max=25)])
    email = TextField('email', validators=[DataRequired(), Email(message=None), Length(min=3,max=40)])
    password = PasswordField('password', validators=[DataRequired()])
    confirmPassword = PasswordField('same password', validators=[DataRequired(), EqualTo(
        'password', message="Passwods but match")])
