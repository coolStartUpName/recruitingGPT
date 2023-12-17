from flask import Blueprint, render_template
from .models import Applicants

views = Blueprint('views', __name__)

@views.route("/")
def index():
    return render_template('home.html')

@views.route("/jobDescription", methods=['GET', 'POST'])
def job_description():
    if request.method == 'POST':
        resume = request.from.get('resume')
        return render_template('applicants.html')
    else:
        return render_template('jobDescription.html')

@views.route("/applicants")
def applicants():
    all_applicants = conn.execute("SELECT * FROM Applicants")
    return render_template('applicants.html', applicant=all_applicants)


# new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
# db.session.add(new_user)
# db.session.commit()