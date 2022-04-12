from App.database import db

class JobBoard(db.Model):
    job_board_id = db.Column(db.Integer, primary_key=True)
    jobId= db.Column('jobId', db.Integer, db.ForeignKey('job.jobId'))
    form_date = db.Column(db.Date, nullable=False, server_default=db.text('CURRENT_TIMESTAMP') )
   

    def toDict(self):
        return{
            'job_board_id': self.job_board_id,
            'jobId': self.jobId,
            'form_date': self.form_date
           
        }