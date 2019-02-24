from flask import Flask, flash, redirect, url_for, render_template, request, Response, send_file, make_response, abort
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

import json
import datetime

from models.users import Users
from models.judges import Judges
from models.teams import Teams

# Configure Flask app and SQL database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)		# database

<<<<<<< Updated upstream:src/main.py
=======
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

def allowed_file(filename, ALLOWED_EXTENSIONS):
    """Check whether image is in valid format
    Return"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

<<<<<<< Updated upstream:src/main.py
>>>>>>> Stashed changes:main.py
=======
>>>>>>> Stashed changes:main.py
#Login Page
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        form_username = request.form['username']
        form_password = request.form['password']
        real_username = Users.query.filter_by(username=username).first()

        if real_username:
            if real_username.username != form_username: error = 'Invalid credentials. Please try again!'
            else:
                real_password = real_username.password
                if real_password == form_password:
                    #Define Account Data and Parameters
                    return render_template('home.html')

        else: error = 'Invalid credentials. Please try again!'

    return render_template('login.html', error=error)


#Register New User
@app.route('/register', methods=['GET'])
def chooseType():
    return render_template('chooseType.html')

@app.route('/register/team', methods=['GET', 'POST'])
def newTeam():

    if request.method == 'POST':
        teamName = request.form['teamName']
        password = request.form['password']
        teamDescription = request.form['description']

        if 'file' not in request.files:
            #ADD CHANGES TO DATABASES
            user = Users(username=teamName, password=password, userType='team')
            team = Teams(teamName=teamName, teamDescription=teamDescription, totalPoints=0)
            db.session.add(user)
            db.session.add(team)
            db.session.commit()

        else:
            image_file = request.files['file']

            # if image filename is empty string
            if image_file.filename == '':
                #ADD CHANGES TO DATABASES
                user = Users(username=teamName, password=password, userType='team')
                team = Teams(teamName=teamName, teamDescription=teamDescription, totalPoints=0)
                db.session.add(user)
                db.session.add(team)
                db.session.commit()

            # if image is allowed
            elif image_file and allowed_file(image_file.filename, ALLOWED_EXTENSIONS):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                user = Users(username=teamName, password=password, userType='team')
                team = Teams(teamName=teamName, teamDescription=teamDescription, teamPhoto=str(filename), totalPoints=0)
                db.session.add(user)
                db.session.add(team)
                db.session.commit()


    return render_template('teamForm.html')

@app.route('/register/judge', methods=['GET', 'POST'])
def newJudge():
    return render_template('judgeForm.html')



#User Pages

@app.route('/judgeHome', methods=['GET', 'POST'])
def Jhome():
    return render_template("judgeHome.html")

@app.route('/teamHome', methods=['GET', 'POST'])
def Thome():
    return render_template("teamHome.html")




if __name__ == '__main__':
    app.run(debug=True)
