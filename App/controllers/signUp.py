from App.models import User
from App.database import db


def add_formData_to_db(data):
    word = "help me"

    newuser = User(username=data['username'], email=data['email'], firstname=data['firstname'], lastname=data['lastname'], password=data['password'], photoId="No Data", departmentId=9999, facultyId=9999) # create user object
    db.session.add(newuser) # save new user
    print(data)
    db.session.commit()
    return User.query.all()