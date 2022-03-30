from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world():
    return ("Hellooooo World!!!!!")

@app.route('/dojo')
def dojo():
    return("Hey its the dojo!")

@app.route('/say/<string:name>')
def selectname(name):
    return f"Hello {name}"

@app.route('/say/flask')
def flask():
    return("Hi Flask!")

@app.route('/say/michael')
def michael():
    return("Hi Michael")

@app.route('/say/john')
def john():
    return("Hi John")

@app.route('/repeat/<int:num>/<string:hello>')
def rep_hello(num,hello):
    output = ''
    for i in range (0,num):
        output += f"<p>{hello}<p>"
    return output

if __name__ == "__main__":
    app.run(debug=True)
