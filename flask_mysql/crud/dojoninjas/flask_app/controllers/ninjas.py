from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models import ninja, dojo

@app.route('/ninjas')
def ninjas():
    return render_template('create_ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/create/ninja', methods=['post'])
def createninja():
    ninja.Ninja.save(request.form)
    return redirect ('/')