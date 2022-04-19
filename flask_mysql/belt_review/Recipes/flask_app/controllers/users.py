from flask_app.models.user import User
from flask import render_template, request, redirect, session, flash
from flask_app.models import user
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def loginpage():
    return render_template('login.html')

@app.route('/save', methods=['POST'])
def saveuser():
    if not User.validation(request.form):
        print('not valid') 
        return redirect('/')
    hash_= bcrypt.generate_password_hash(request.form['password'])
    print(hash_)
    data={
        "firstName": request.form['firstName'],
        "lastName": request.form['lastName'],
        "email": request.form['email'],
        "password": hash_
    }
    user_id = User.createuser(data)
    session['user'] = user_id
    print("it was successful")
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {"email":request.form["email"]}
    emailInDB = User.getEmail(data)
    if not emailInDB:
        flash('wrong email')
        return redirect('/')
    if not bcrypt.check_password_hash(emailInDB.password, request.form['password']):
        flash('wrong password try again')
        return redirect('/')
    session['user'] = emailInDB.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dash():
    if 'user' not in session:
        return redirect('/logout')
    data = {
        "id": session['user']
    }
    return render_template('dashboard.html', user = User.getByID(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')