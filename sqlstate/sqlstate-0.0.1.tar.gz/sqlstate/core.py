import sqlite3
import json


class State:
    def __init__(self, file: str) -> None:
        self.file = file
        self.connect_sqlite3()
        self.prepare_sqlite3()

    def connect_sqlite3(self) -> None:
        self.connection = sqlite3.connect(self.file)
        self.cursor = self.connection.cursor()

    def prepare_sqlite3(self) -> None:
        table_definition = 'CREATE TABLE IF NOT EXISTS state (key string UNIQUE, data text)'
        self.cursor.execute(table_definition)

    def store(self, key: str, payload: any) -> None:
        try:
            statement = 'INSERT INTO state(key, data) VALUES(?, ?)'
            self.cursor.execute(statement, [key, json.dumps(payload)])
        except sqlite3.IntegrityError:
            statement = 'UPDATE state SET data = ? WHERE key = ?'
            self.cursor.execute(statement, [json.dumps(payload), key])
        finally:
            self.connection.commit()

    def get(self, key: str) -> any:
        try:
            statement = 'SELECT data FROM state WHERE key = ?'
            response = self.cursor.execute(statement, [key])
            return json.loads(response.fetchone()[0])
        except TypeError:
            raise Exception(f'\'{key}\' was not found not found.')
