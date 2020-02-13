from sqlalchemy.orm import relationship

from extensions import db


class Status(db.Model):
    __tablename__ = 'status'
    _id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    date = db.Column(db.String)
    date_created = db.Column(db.String)
    date_modified = db.Column(db.String)
    hours = db.Column(db.Integer)
    comment = db.Column(db.String)
    is_all_day = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user._id'))
    user = relationship("User", backref="user")
