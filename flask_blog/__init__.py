from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('flask_blog.config')
    if test_config:
        app.config.from_mapping(test_config)

    db.init_app(app)


    from flask_blog.views.views import view
    app.register_blueprint(view)

    from flask_blog.views.entries import entry
    app.register_blueprint(entry, url_prefix='/users')

    return app


"""
modelsディレクトリ配下が読まれないので暫定対処
"""
#from flask_blog import db
#from datetime import datetime
#
#class Entry(db.Model):
#    __tablename__ = 'entries'
#    __table_args__ = {'extend_existing': True}
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(50), unique=True)
#    text = db.Column(db.Text)
#    created_at = db.Column(db.DateTime)
#
#    def __init__(self, title=None, text=None):
#        self.title = title
#        self.text = text
#        self.created_at = datetime.utcnow()
#
#    def __repr__(self):
#        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)
