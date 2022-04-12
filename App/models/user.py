from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    photoId = db.Column(db.String, nullable=True)
    departmentId = db.Column('departmentId', db.Integer, db.ForeignKey('department.departmentId'))
    facultyId = db.Column('facultyId', db.Integer, db.ForeignKey('faculty.facultyId'))

    def __init__(self, username, password, firstname, lastname, email, photoId, departmentId, facultyId ):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.photoId = photoId
        self.set_password(password)
        self.departmentId = departmentId
        self.facultyId = facultyId

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'photoId': self.photoId,
            'departmentId': self.departmentId,
            'facultyId': self.facultyId,

        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


