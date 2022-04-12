from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Email

class LogIn(FlaskForm):
  pass
