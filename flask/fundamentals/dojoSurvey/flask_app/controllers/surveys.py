from flask import render_template, session, redirect, request
from flask_app.config.pymysqlconnection import connectToMySQL
from flask_app.models.survey import Survey
from flask_app import app


@app.route('/')
def initialForm():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create_survey():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/submission')
    return redirect('/')

@app.route('/submission')
def submission():
    return render_template('submission.html', survey = Survey.getone())

@app.route('/clears')
def clearroute():
    session.clear()
    return redirect('/')

@app.route('/surveys')
def getsurveys():
    survey = Survey.graball()
    return render_template("submission.html", all_surveys = survey)

