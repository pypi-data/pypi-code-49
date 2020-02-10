from ctrlv_client.app import db


class Tag(db.Model):
    __tablename__ = 'tags'
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(255), unique=True)
    snippets = db.relationship(
        "SnippetTag",
        backref='tags',
        cascade="all,delete"
    )


class SnippetTag(db.Model):
    __tablename__ = 'snippet_tags'
    snippet_tag_id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'))
    snippet_id = db.Column(db.Integer, db.ForeignKey('snippets.snippet_id'))
