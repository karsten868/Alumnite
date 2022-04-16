from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required
from App.models import User


''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

''' End Flask Login Functions '''



homePage_views = Blueprint('homePage_views', __name__, template_folder='../templates')


@homePage_views.route('/homePage', methods=['GET'])
@login_required
def home_page():
    return render_template('homePage.html') # pass form object to template

