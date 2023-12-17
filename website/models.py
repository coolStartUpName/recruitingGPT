from website import db 
from sqlalchemy.sql import func

class Applicants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume = db.Column(db.String(10000))
    job_description = db.Column(db.String(10000))
    # email = db.Column(db.String(150), unique=True)
    # first_name = db.Column(db.String(150))