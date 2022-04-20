from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, login_required
from App.models import SignUp, User


# ''' Begin Flask Login Functions '''
# login_manager = LoginManager()
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# ''' End Flask Login Functions '''

from App.controllers import (
    add_formData_to_db
)


signUp_views = Blueprint('signUp_views', __name__, template_folder='../templates')


@signUp_views.route('/signup', methods=['GET'])
def signUp_page():
    form = SignUp() # create form object
    return render_template('signUp.html', form=form) # pass form object to template

@signUp_views.route('/signup', methods=['POST'])
def signUp_submission():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form# get data from form submission
    newuser=add_formData_to_db(data)
    #flash('Account Created!')# send message
    return redirect('/login') # redirect to login page
  #flash('Error invalid input!')
  return redirect('/signup')
