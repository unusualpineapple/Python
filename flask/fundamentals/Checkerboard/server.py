from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", row = 8, col = 8, background1='red', background2='black')

@app.route('/<int:x>')
def index2(x):
    return render_template("index.html", row = x, col = 8, background1='red', background2='black')

@app.route('/<int:x>/<int:y>')
def index3(x,y):
    return render_template("index.html", row = x, col = y, background1='red', background2='black')

@app.route('/<int:x>/<int:y>/<string:this>/<string:that>')
def index4(x,y,this,that):
    return render_template("index.html", row = x, col = y, background1=this, background2=that)

# if __name__ == "__main__":
#     app.run(debug=True)
