from flask_app.models.user import User
from flask import render_template, request, redirect, session, flash
from flask_app.models import user
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def loginpage():
    return render_template('login')

@app.route('/save', methods=['post'])
def saveuser():
    if not User.validation(request.form):
        return redirect('/')
    hash_= bcrypt.generate_password_hash(request.form['password'])
    print(hash_)
    data={
        "firstName": request.form['firstName'],
        "lastName": request.form['lastName'],
        "email": request.form['email'],
        "password": hash_
    }
    user_id = User.insertuser(data)
    session['user'] = user_id
    print("it was successful")
    return redirect('/dashboard')