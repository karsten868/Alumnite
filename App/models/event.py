from App.database import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facultyId = db.Column('facultyId', db.Integer, db.ForeignKey('faculty.id'))
    name = db.Column(db.String, nullable=False)
    description= db.Column(db.String(120), nullable=True)
    faculty = db.relationship('Faculty')

    def toDict(self):
        return{
            'id': self.id,
            'facultyId': self.facultyId,
            'name': self.name,
            'description': self.description,
            'faculty': self.faculty
        }