#!/usr/local/bin/python3

from flask import Flask, render_template, request
import datetime

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', body="Custom body")

@app.route("/owner")
def Owner():
    return "Hello, World from Pragati!"

@app.route("/datetime")
def DateTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/login',methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user=request.form["email_address"]
		pw=request.form["password"]
		return f"email={user} password={pw}" 
	else:
		return render_template('login.html')

@app.route('/bye')
def goodbye():
    return 'Goodbye'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
