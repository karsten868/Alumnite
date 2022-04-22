from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email
# 

class SignUp(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    email = StringField('email', validators=[Email(), InputRequired()])
    firstname= StringField('firstname', validators=[InputRequired()])
    lastname= StringField('lastname', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('confirm Password')
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

