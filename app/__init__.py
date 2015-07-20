# -*- coding: utf-8 -*-
"""

This is a Flask application designed to help aid in searching
for applicants. It uses a weighted system with thesaurus
lookups and string matching to create a score for each of the
applicants in the database and then ranks them according to score

"""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import basedir

app = Flask(__name__)
app.config.from_object('config') # Use the config files
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import views, models # Avoid circular dependancy

