from flask import render_template, redirect
from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')
    
# @app.route('/dojos')
# def getinthedojo():
#     all = Dojo.get_all()
#     return render_template('showthedojos.html', all_dojos = all)

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("showthedojos.html",all_dojos = dojos)

@app.route('/dojo/<int:id>')
def showmethemoney():
    data={
    "id":id
    }
    
    # all_ninjas = Ninja.get_all()
    return render_template("getonedojo.html", dojo = Dojo.getoneandninjas(data) )
