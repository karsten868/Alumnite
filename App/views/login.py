from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required
from App.models import User
from App.database import db

#from forms import logInForm



''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

''' End Flask Login Functions '''


login_views = Blueprint('login_views', __name__, template_folder='../templates')


@login_views.route('/', methods=['GET'])
def index():
  return render_template('login.html') #, form=form)

# @login_views.route('/login', methods=['POST'])
# def login_page():
#   form = Login()
#   if form.validate_on_submit(): # respond to form submission
#       data = request.form
#       user = User.query.filter_by(username = data['username']).first()
#       if user and user.check_password(data['password']): # check credentials
#         flash('Logged in successfully.') # send message to next page
#         login_user(user) # login the user
#         return redirect(url_for('todos')) # redirect to main page if login successful
#   flash('Invalid credentials')
#   return redirect(url_for('login'))
