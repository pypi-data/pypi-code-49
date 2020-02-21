from pathlib import Path
from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase(Path.home() / '.contacts.db')

class Contacts(Model):
    name = CharField()
    tlf = CharField()
    email = CharField()
    arbejdsplads = CharField()

    class Meta:
        database = db