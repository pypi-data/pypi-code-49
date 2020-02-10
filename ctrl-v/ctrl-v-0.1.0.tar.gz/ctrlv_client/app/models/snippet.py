from datetime import datetime
from ctrlv_client.app import db


class Snippet(db.Model):
    __tablename__ = 'snippets'
    snippet_id = db.Column(db.Integer, primary_key=True)
    snippet_title = db.Column(db.String(255))
    snippet_text = db.Column(db.Text)
    # This way SQLAlchemy will call datetime.utcnow itself upon row insert.
    # This does not create a default constraint, atleast for sqlite
    snippet_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    tags = db.relationship("SnippetTag", backref='snippets')
