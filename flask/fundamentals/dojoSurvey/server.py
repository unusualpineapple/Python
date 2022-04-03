from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key = "let the dragons in"

@app.route('/')
def initialForm():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def bigForm():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['coding_language'] = request.form['coding_language']
    session['comments'] = request.form['comments']
    return redirect('/submission')    

@app.route('/submission')
def submitForm():
    print(session)
    return render_template('submission.html')

@app.route('/clears')
def clearroute():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)