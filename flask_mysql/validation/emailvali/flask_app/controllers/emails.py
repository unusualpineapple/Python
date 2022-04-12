from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def initialform():
    return render_template ("index.html")

# @app.route('/save', methods = ['POST'])
# def emailsub():
#     Email.submitemail(request.form)
#     return redirect('/success')

@app.route('/success')
def successfulemail():
    return render_template ('success.html', email = Email.grabemails())

@app.route('/delete/<int:id>')
def deleteemail(id):
    data = {
        "id":id
    }
    Email.deleteemail(data)
    return redirect ('/success')

@app.route('/', methods=['POST'])
def validate():
    if Email.validate(request.form):
        Email.submitemail(request.form)
        return redirect('/')
    return redirect('/')
