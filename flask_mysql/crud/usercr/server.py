from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("allusers.html", users=User.get_all())

@app.route('/users/new')
def new():
    return render_template("addnewuser.html")

@app.route('/users/create',methods=['post'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True)