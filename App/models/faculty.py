from App.database import db


class Faculty(db.Model):
    facultyId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def toDict(self):
        return{
            'facultyId': self.facultyId,
            'name': self.name
        }