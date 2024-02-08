from website import db 
from sqlalchemy.sql import func

class Applicants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume = db.Column(db.String(1000000000))
    jobDescription = db.Column(db.String(1000000000))
    job_description_embedding = db.Column(db.String(1000000000000000))
    resume_embedding = db.Column(db.String(1000000000000000))
    distance = db.Column(db.String(1000000000000000))

    # id 
    # resume
    # job_description_embedding
    # resume_embedding
    # distance