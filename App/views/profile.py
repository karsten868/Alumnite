from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required
from App.models import User




profile_views = Blueprint('profile_views', __name__, template_folder='../templates')


@profile_views.route('/profile', methods=['GET'])
@login_required
def profile_page():
    return render_template('profile.html') # pass form object to template

