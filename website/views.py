from flask import Blueprint, render_template, request
from website import db
from .models import Applicants
from .gpt import gptTest
from .job_embedding import job_embedding
from scipy.spatial.distance import euclidean

views = Blueprint('views', __name__)

@views.route("/")
def index():
    return render_template('home.html')

@views.route("/jobDescription", methods=['GET', 'POST'])
def job_description():
    if request.method == 'POST':
        resume = request.form.get('resume')
        # job_description = request.form.get('jobDescription')
        resume_embedding = gptTest(resume)
        distance = euclidean(resume_embedding, job_embedding)
        string_distance = str(distance)
        string_resume_embedding = str(resume_embedding)
        # job_embedding = gptTest(job_embedding)
        applicant = Applicants(resume=resume, resume_embedding=string_resume_embedding, distance=string_distance)
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


# new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
# db.session.add(new_user)
# db.session.commit()