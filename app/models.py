import datetime
from app import db

class Post(db.Model):
    """
    Create a post model
    """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True)
    slug = db.Column(db.String(150), unique=True)
    markdown = db.Column(db.Text)
    html = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    published_at = db.Column(db.DateTime)
