"""
Some usueful configurations for the project
"""
import os

# Flask Forms
WTF_CSRF_ENABLED = True
SECRET_KEY = 'ljkasdfnasdopibvxzchjdnkss94895kdkv0g93723tfgdvcjgfj478'

# Basedir of the project
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite for dev environment
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
