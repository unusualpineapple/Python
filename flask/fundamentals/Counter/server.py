from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key= 'dragon boy'


@app.route('/')
def count1():
    if "rick" not in session:
        session["rick"] = 0
    else:
        session["rick"] += 1
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)