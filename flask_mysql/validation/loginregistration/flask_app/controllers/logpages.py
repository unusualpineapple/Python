from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect
from flask_app.models.logpage import User
bcrypt = Bcrypt(app)


@app.route('/')
def loginpage():
    return render_template('index.html')

@app.route('/save')
def saveuser():
    User.insertuser(request.form)
    return redirect('/')