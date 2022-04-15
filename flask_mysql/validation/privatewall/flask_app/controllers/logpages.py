from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.logpage import User
from flask_app.models import logpage
bcrypt = Bcrypt(app)

@app.route('/')
def loginpage():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def saveuser():
    if not User.validation(request.form):
        return redirect('/')
    hash_ = bcrypt.generate_password_hash(request.form['password'])
    print(hash_)
    data = {
        "firstname": request.form['firstname'],
        "lastname": request.form['lastname'],
        "email": request.form['email'],
        "password": hash_
    }
    user_id = User.insertuser(data)
    session['user'] = user_id
    print("IT WAS SUCCESSFUL GOOD JOB")
    return redirect('/submission')

@app.route('/login', methods = ['post'])
def login():
    data = {"email":request.form["email"]}
    email_in_db = User.get_by_email(data)
    if not email_in_db:
        flash("INVALID EMAIL MANGGGGG CANT REMEMBER??")
        return redirect('/')
    if not bcrypt.check_password_hash(email_in_db.password, request.form['password']):
        flash("AGAIN PASSWORD is not right TRY AGAIN")
        return redirect('/')
    session['user_id'] = email_in_db.id
    return redirect("/submission2")

@app.route('/submission')
def subpage():
    # if 'user_id' not in session:
    #     print('not in session')
    #     return redirect('/logout')
    data = {
        "id": session['user']
    }
    return render_template('submission.html', account = User.get_by_id(data))

@app.route('/submission2')
def subpage2():
    data = {
        "id":session['user_id']
    }
    return render_template('submission.html', account = User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')