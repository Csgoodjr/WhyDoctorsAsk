from flask import Flask, render_template, url_for
import json 
app = Flask(__name__)

with open('./static/wda_db.json', 'r') as infile:
    db = json.load(infile)
hpi_db = db[0]['questionsDoctorsAsk']['historyOfPresentIllness']['questions']
pmh_db = db[0]['questionsDoctorsAsk']['pastMedicalHistory']['questions']
fhx_db = db[0]['questionsDoctorsAsk']['familyHistory']['questions']
shx_db = db[0]['questionsDoctorsAsk']['socialHistory']['questions']
subhx_db = db[0]['questionsDoctorsAsk']['substanceHistory']['questions']
sexhx_db = db[0]['questionsDoctorsAsk']['sexualHistory']['questions']
rhx_db = db[0]['questionsDoctorsAsk']['reviewOfSymptoms']['questions']

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html',title="Home")

@app.route("/hpi")
def hpi():
    return render_template('hpi.html',title="HPI",questions=hpi_db)

@app.route("/pmh")
def pmh():
    return render_template('pmh.html', title="PMH", questions=pmh_db)

@app.route("/fhx")
def fhx():
    return render_template('fhx.html', title="FHX", questions=fhx_db)

@app.route("/shx")
def shx():
    return render_template('shx.html', title="SHX", questions=shx_db)

@app.route("/subhx")
def subhx():
    return render_template('subhx.html', title="SUBHX", questions=subhx_db)

@app.route("/sexhx")
def sexhx():
    return render_template('sexhx.html',title="SEXHX",questions=sexhx_db)

@app.route("/rhx")
def rhx():
    return render_template('rhx.html', title="RHX", questions=rhx_db)

@app.route("/about")
def about():
    return render_template('about.html',title="About Us")

if __name__ == "__main__":
    app.run(debug=True)
