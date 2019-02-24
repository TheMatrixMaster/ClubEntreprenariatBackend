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

#Home Page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
