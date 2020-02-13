from extensions import db

class User(db.Model):
    __tablename__ = 'user'
    _id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    picture = db.Column(db.String)
    email = db.Column(db.String)
