from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required
from App.models import User




jobBoard_views = Blueprint('jobBoard_views', __name__, template_folder='../templates')


@jobBoard_views.route('/jobBoard', methods=['GET'])
@login_required
def job_board():
    return render_template('jBoard.html') # pass form object to template
