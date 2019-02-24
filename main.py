#Main.py: Flask backend main page

from flask import Flask, flash, redirect, url_for, render_template, request, Response, send_file, make_response, abort
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

import json
import datetime

# Configure Flask app and SQL database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)		# database

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	userType = db.Column(db.String(40), nullable=False)

	def __repr__(self):
		return f"User('{self.username}', '{self.userType}')"

class Judges(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	judgeName = db.Column(db.String(80), unique=True, nullable=False)
	totalMoney = db.Column(db.Integer)

	def __repr__(self):
		return f"Judge('{self.judgeName}', '{self.totalMoney}')"

class Teams(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	teamName = db.Column(db.String(80), unique=True, nullable=False)
	teamDescription = db.Column(db.String(500), nullable=False)
	teamPhoto = db.Column(db.String(20), nullable=False, default='team_photo.jpg')
	totalPoints = db.Column(db.Integer)

	def __repr__(self):
		return f"Team('{self.teamName}', '{self.totalPoints}')" 

#Login Page
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	form_username = request.get
	form_password = request.get
	return render_template('login.html', error=error)


#Register New User

@app.route('/register', methods=['GET'])
def chooseType():
	return render_template('chooseType.html')

@app.route('/register/team', methods=['GET', 'POST'])
def newTeam():
	return render_template('teamForm.html')

@app.route('/register/judge', methods=['GET', 'POST'])
def newJudge():
	return render_template('judgeForm.html')



#User Pages

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template("home.html")




if __name__ == '__main__':
    app.run(debug=True)
