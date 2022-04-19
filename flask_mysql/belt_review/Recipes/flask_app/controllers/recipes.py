from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.recipe import Creation
from flask_app.models.user import User

@app.route('/new/creation')
def newCreation():
    if 'user' not in session:
        return redirect('/logout')
    data = {
        "id": session['user']
    }
    return render_template('newRecipe.html', user = User.getByID(data))