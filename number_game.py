from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = 'secret_key'

import random 

@app.route('/')
def index():
	session['result'] = ""
	session['secret_num'] = random.randrange(0,101) 
	return render_template("numbergame.html") 

@app.route('/user', methods=['POST'])
def user(): 
	session['guess'] = int(request.form['search'])
	
	if session['guess'] == session['secret_num']:
			session['result'] ="You Guessed the Number!"

	elif session['guess'] < session['secret_num']:
			session['result'] = "Too Low!"

	elif session['guess'] > session['secret_num']: 
			session['result'] ="Too High!"

	return render_template("numbergame.html")

app.run(debug=True)

	