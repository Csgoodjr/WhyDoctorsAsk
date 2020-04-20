# Required Imports
import os
import json 
from flask import Flask, render_template, url_for, jsonify, redirect
from firebase_admin import credentials, firestore, initialize_app

# Create Flask instance 
app = Flask(__name__)

# Init Firebase DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()

# Home/Main Page
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html',title="Home")

''' Questions Doctors Ask '''
@app.route("/questions_doctors_ask")
def qda():
    with open('./static/db/QuestionsDoctorsAsk/qda.json', 'r') as qda_json:
        qda_db = json.load(qda_json)
    return render_template('questions_doctors_ask.html',title="Questions Doctors Ask",db=qda_db)

# History of Present Illness Page
@app.route("/hpi")
def hpi():
    with open('./static/db/QuestionsDoctorsAsk/hpi.json', 'r') as hpi_json:
        hpi_db = json.load(hpi_json)
    return render_template('questions_doctors_ask_cards.html',title="HPI",db=hpi_db)

# Past Medical History
@app.route("/pmh")
def pmh():
    with open('./static/db/QuestionsDoctorsAsk/pmh.json', 'r') as pmh_json:
        pmh_db = json.load(pmh_json)
    return render_template('questions_doctors_ask_cards.html', title="PMH", db=pmh_db)

# Family History 
@app.route("/fhx")
def fhx():
    with open('./static/db/QuestionsDoctorsAsk/fhx.json', 'r') as fhx_json:
        fhx_db = json.load(fhx_json)
    return render_template('questions_doctors_ask_cards.html', title="FHX", db=fhx_db)

# Social History 
@app.route("/shx")
def shx():
    with open('./static/db/QuestionsDoctorsAsk/shx.json', 'r') as shx_json:
        shx_db = json.load(shx_json)
    return render_template('questions_doctors_ask_cards.html', title="SHX", db=shx_db)

# Substance History
@app.route("/subhx")
def subhx():
    with open('./static/db/QuestionsDoctorsAsk/subhx.json', 'r') as subhx_json:
        subhx_db = json.load(subhx_json)
    return render_template('questions_doctors_ask_cards.html', title="SUBHX", db=subhx_db)

# Sexual History
@app.route("/sexhx")
def sexhx():
    with open('./static/db/QuestionsDoctorsAsk/sexhx.json', 'r') as sexhx_json:
        sexhx_db = json.load(sexhx_json)
    return render_template('questions_doctors_ask_cards.html', title="SEXHX", db=sexhx_db)

# Review of Symptoms
@app.route("/rhx")
def rhx():
    with open('./static/db/QuestionsDoctorsAsk/rhx.json', 'r') as rhx_json:
        rhx_db = json.load(rhx_json)
    return render_template('questions_doctors_ask_cards.html', title="RHX", db=rhx_db)

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

# Server Error Handler
@app.errorhandler(500)
def server_error(e):
    return f"Something went wrong: {e}"

# Init the server with config items
port = int(os.environ.get('PORT',8080))
if __name__ == "__main__":
    app.run(threaded=True,host='127.0.0.1',port=port)
