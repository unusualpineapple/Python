from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.message import Message
from flask_app.models import message

@app.route('/savemessage', methods=['POST'])
def savemessage():
    if not Message.validatemessage(request.form):
        return redirect('/submission')
    data = {
        "receiver_name": request.form['receiver_name'],
        "sender_name": request.form['sender_name'],
        "message": request.form['message'],
        "created_at": request.form['created_at'],
        "updated_at": request.form['updated_at']
    }
    Message.savemessage(request.form)
    Message.getfromid(data)
    return redirect('/submission', message = Message.getfromid(data))

    
@app.route('/submission')
def subpage():

    return render_template('submission.html')

@app.route('/delete/<int:sender_id>')
def deletemessage():
    Message.removemessage()
    

