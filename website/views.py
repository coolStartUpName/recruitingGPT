from flask import Blueprint, render_template, request
from website import db
from .models import Applicants
from .gpt import gptTest

views = Blueprint('views', __name__)

@views.route("/")
def index():
    return render_template('home.html')

@views.route("/jobDescription", methods=['GET', 'POST'])
def job_description():
    if request.method == 'POST':
        resume = request.form.get('resume')
        job_description = request.form.get('jobDescription')
        applicant = Applicants(resume=resume, job_description=job_description)
        db.session.add(applicant)
        db.session.commit()
        gptTest()
        return render_template('applicants.html', resume=resume, jd=job_description)
    else:
        return render_template('jobDescription.html')

@views.route("/applicants")
def applicants():
    return render_template('applicants.html')


# new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
# db.session.add(new_user)
# db.session.commit()