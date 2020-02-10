from .db import db

##__________________________________________________________________||
class Map(db.Model):
    __tablename__ = 'maps'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text(), nullable=False, unique=True, index=True)
    date_posted = db.Column(db.Date())
    mapper = db.Column(db.Text())
    note = db.Column(db.Text())

class Beam(db.Model):
    __tablename__ = 'beams'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text(), nullable=False, unique=True, index=True)
    path = db.Column(db.Text())
    input_map_id = db.Column(db.ForeignKey('maps.id'))
    input_beam_id = db.Column(db.ForeignKey('beams.id'))
    map = db.relationship("Map", backref=db.backref("beams"))
    parent_beam = db.relationship(lambda: Beam, remote_side=id, backref=db.backref("child_beams"))

class MapFilePath(db.Model):
    __tablename__ = 'map_path'
    id = db.Column(db.Integer(), primary_key=True)
    map_id = db.Column(db.ForeignKey('maps.id'))
    path = db.Column(db.Text())
    note = db.Column(db.Text())
    map = db.relationship("Map", backref=db.backref("map_file_paths"))

##__________________________________________________________________||
