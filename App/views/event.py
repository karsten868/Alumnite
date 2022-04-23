from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required
from App.models import User




event_views = Blueprint('event_views', __name__, template_folder='../templates')


@event_views.route('/event', methods=['GET'])
@login_required
def event_page():
    return render_template('event.html') # pass form object to template
