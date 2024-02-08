from flask import Blueprint, render_template, request
from website import db
from .models import Applicants
from .gpt import gptTest
#from .job_embedding import job_embedding
from scipy.spatial.distance import euclidean

views = Blueprint('views', __name__)

@views.route("/")
def index():
    return render_template('home.html')

@views.route("/jobDescription", methods=['GET', 'POST'])
def job_description():
    if request.method == 'POST':
        resume = request.form.get('resume')
        jobDescription = request.form.get('jobDescription')
        job_embedding = gptTest(jobDescription)
        resume_embedding = gptTest(resume)
        distance = euclidean(job_embedding, resume_embedding)
        string_distance = str(distance)
        string_job_embedding = str(job_embedding)
        string_resume_embedding = str(resume_embedding)
        applicant = Applicants(
            resume=resume,
            resume_embedding=string_resume_embedding,
            jobDescription=jobDescription,
            job_description_embedding=string_job_embedding,
            distance=string_distance
        )
        db.session.add(applicant)
        db.session.commit()
        applicants_data = Applicants.query.all()
        return render_template('applicants.html', applicants=applicants_data)
    else:
        return render_template('jobDescription.html')

@views.route("/applicants")
def applicants():
    applicants_data = Applicants.query.all()

    return render_template('applicants.html', applicants=applicants_data)

