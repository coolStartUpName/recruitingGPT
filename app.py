from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
engine = db.create_engine("sqlite:///applicants.sqlite")

conn = engine.connect() 
metadata = db.MetaData()

Applicants = db.Table('Applicants', metadata,
              db.Column('Id', db.Integer(),primary_key=True),
              db.Column('Name', db.String(255), nullable=False),
              db.Column('Resume', db.String(10000), nullable=False),
              db.Column('Email', db.String(255), nullable=False)
              )

metadata.create_all(engine) 

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