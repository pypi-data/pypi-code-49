from tinydb import TinyDB
from tinydb_serialization import SerializationMiddleware
from jezdzenka.classes.DateTimeSerializer import DateTimeSerializer
from jezdzenka.classes.TypeSerializer import TypeSerializer
import os
import pathlib


class Jezdzenka:
    def __init__(self):
        self.configuration = self.config()
        self.connection = self.database()
        self.table = self.connection.table('objects')

    def config(self):
        try:
            file = open(os.path.join(str(pathlib.Path.home()), '.jezdzenka'), 'r')
            directory = file.read().strip()
        except IOError:
            directory = input(_("initial.not_found"))
            file = open(os.path.join(str(pathlib.Path.home()), '.jezdzenka'), 'w')
            file.write(directory)
            file.close()
        if directory is not None:
            if not os.path.exists(directory):
                os.makedirs(directory)
        return directory

    def database(self):
        database_file = os.path.join(self.configuration, 'database.json')
        serialization = SerializationMiddleware()
        serialization.register_serializer(DateTimeSerializer(), 'Date')
        serialization.register_serializer(TypeSerializer(), 'Type')
        return TinyDB(database_file, storage=serialization)


app = Jezdzenka()