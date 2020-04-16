# Required Imports
import os
import json 
import time 
from flask import Flask, render_template, url_for

# Create Flask instance 
app = Flask(__name__)

# Access the JSON DB
with open('./static/wda_db.json', 'r') as infile:
    db = json.load(infile)

# Load Database
with open('./static/db/QuestionsDoctorsAsk/rhx.json','r') as rhx_json:
    rhx_db = json.load(rhx_json)

# Format Server Time
def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)

# Define the routes for the site's nav
# Home/Main Page
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html',title="Home")

''' Questions Doctors Ask '''
@app.route("/questions_doctors_ask")
def qda():
    return render_template('questions_doctors_ask.html',title="Questions Doctors Ask",info=db[0])

# History of Present Illness Page
@app.route("/hpi")
def hpi():
    hpi_db = db[0]['questionsDoctorsAsk']['historyOfPresentIllness']['questions']
    return render_template('hpi.html',title="HPI",questions=hpi_db)

# Past Medical History
@app.route("/pmh")
def pmh():
    pmh_db = db[0]['questionsDoctorsAsk']['pastMedicalHistory']['questions']
    return render_template('pmh.html', title="PMH", questions=pmh_db)

# Family History 
@app.route("/fhx")
def fhx():
    fhx_db = db[0]['questionsDoctorsAsk']['familyHistory']['questions']
    return render_template('fhx.html', title="FHX", questions=fhx_db)

# Social History 
@app.route("/shx")
def shx():
    shx_db = db[0]['questionsDoctorsAsk']['socialHistory']['questions']
    return render_template('shx.html', title="SHX", questions=shx_db)

# Substance History
@app.route("/subhx")
def subhx():
    subhx_db = db[0]['questionsDoctorsAsk']['substanceHistory']['questions']
    return render_template('subhx.html', title="SUBHX", questions=subhx_db)

# Sexual History
@app.route("/sexhx")
def sexhx():
    sexhx_db = db[0]['questionsDoctorsAsk']['sexualHistory']['questions']
    return render_template('sexhx.html',title="SEXHX",questions=sexhx_db)

# Review of Symptoms
@app.route("/rhx")
def rhx():
    return render_template('rhx.html', title="RHX", db=rhx_db)

''' Physical Exams '''
@app.route("/physical_exams")
def physical_exams():
    return render_template('physical_exams.html',title="Physical Exams")

''' Common Labs '''
@app.route("/common_labs")
def common_labs():
    return render_template('common_labs.html',title="Common Labs")
# Intro
# Terms


''' Common Screening Tools '''
@app.route("/common_screening_tools")
def common_screening_tools():
    return render_template('common_screening_tools.html',title="Common Screening Tools")

''' Common Imaging Tools '''
@app.route("/common_imaging_tools")
def common_imaging_tools():
    return render_template('common_imaging_tools.html',title="Common Imaging Tools")

''' Common Vaccines '''
@app.route("/common_vaccines")
def common_vaccines():
    return render_template('common_vaccines.html',title="Common Vaccines")

''' Common Recommendations '''
@app.route("/common_recommendations")
def common_recommendations():
    return render_template('common_recommendations.html',title="Common Recommendations")

''' Questions to Ask '''
@app.route("/questions_to_ask")
def questions_to_ask():
    return render_template('questions_to_ask.html',title="Questions to Ask")

''' Common Medical Words '''
@app.route("/common_medical_words")
def common_medical_words():
    return render_template('common_medical_words.html',title="Common Medical Words")

# About Page
@app.route("/about")
def about():
    return render_template('about.html',title="About Us")

# Init the server with config items
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))
