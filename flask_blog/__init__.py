from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views import views, entries


"""
modelsディレクトリ配下が読まれないので暫定対処
"""
from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)
