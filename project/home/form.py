from flask_wtf import Form
from wtforms import TextField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class MessageForm(Form):
    title = TextField('username', validators=[DataRequired(),Length(min=3,max=25)])
    content = TextAreaField('content', validators=[DataRequired()])
    # author = HiddenField('author', validators=[DataRequired()])
