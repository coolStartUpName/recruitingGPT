from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/jobDescription", methods=['GET', 'POST'])
def job_description():
    if request.method == 'POST':
        return render_template('applicants.html')
    else:
        return render_template('jobDescription.html')

@app.route("/applicants")
def applicants():
    return render_template('applicants.html')