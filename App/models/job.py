from App.database import db

class Job(db.Model):
    jobId = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(120), nullable=False)
    description= db.Column(db.String(120), nullable=False)

    def toDict(self):
        return{
            'jobId': self.jobId,
            'title': self.title,
            'description': self.description
        }