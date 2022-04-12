from App.database import db

class Department(db.Model):
    departmentId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    facultyId = db.Column('facultyId', db.Integer, db.ForeignKey('faculty.facultyId'))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'departmentId': self.departmentId,
            'name': self.name,
            'facultyId': self.facultyId
        }
