from dataclasses import dataclass
from pdb import post_mortem
from tkinter import NoDefaultRoot
from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.recipe import Creation
from flask_app.models.user import User

@app.route('/new/creation')
def newCreation():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('newRecipe.html', user = User.getByID(data))

@app.route('/create/creation', methods=['POST'])
def createCreation():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Creation.validate(request.form):
        return redirect('/new/creation')
    data={
        "name":request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "date":request.form['date'],
        "time":request.form['time'],
        'user_id':session['user_id']
    }
    Creation.save(data)
    return redirect('/dashboard')

@app.route('/edit/creation/<int:id>')
def editCreation(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    userdata = {
        "id":session['user_id']
    }
    return render_template("edit.html", creation=Creation.getOneCreation(data), user=User.getByID(userdata))

@app.route('/update/creation', methods=['POST'])
def updateCreation():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Creation.validate(request.form):
        return redirect('/edit/creation/<int:id>')
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date": request.form['date'],
        "time": request.form['time'],
        "id": session['user_id']
    }
    Creation.updateCreation(data)
    return redirect('/dashboard')

@app.route('/view/creation/<int:id>')
def viewCreation(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    userdata={
        "id":session['user_id']
    }
    return render_template("show.html", creation=Creation.getOneCreation(data), user=User.getByID(userdata))

@app.route('/delete/creation/<int:id>')
def deleteCreation(id):
    if 'user_id' not in session:
        redirect('/logout')
    data={
        "id":id
    }
    Creation.deleteCreation(data)
    return redirect('/dashboard')
