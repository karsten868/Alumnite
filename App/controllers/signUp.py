from App.models import User
from App.database import db


def add_formData_to_db(data):
    newuser = User(username=data['username'], email=data['email'], firstname=['firstname'], lastname=['lastname'] ) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    return User.query.all()
