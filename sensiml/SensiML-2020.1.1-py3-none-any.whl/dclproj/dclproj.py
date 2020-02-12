import sqlite3
import os
import pandas as pd
from sensiml.datamanager.datasegments import DataSegments, DataSegment


class DCLProject:
    def __init__(self):
        self._path = None
        self._conn = None
        self._tables = None

    @property
    def data_dir(self):

        if self._path is None:
            raise Exception("Path is not set!")

        return os.path.join(self._path, "data")

    def _set_table_list(self):
        cursorObj = self._conn.cursor()

        cursorObj.execute('SELECT name from sqlite_master where type= "table"')

        self._tables = [x[0] for x in cursorObj.fetchall()]

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        self._path = os.path.dirname(db_file)
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as e:
            print(e)

        self._conn = conn
        self._set_table_list()

    def _list_table(self, tablename):

        if tablename not in self._tables:
            print("Table is not part of the database.")
            return None
        cur = self._conn.cursor()
        cur.execute("SELECT * FROM {}".format(tablename))

        header = [x[0] for x in cur.description]
        rows = cur.fetchall()

        results = []
        for row in rows:
            results.append(row)

        return pd.DataFrame(results, columns=header)

    def list_captures(self):
        return self._list_table("Capture")

    def list_capture_labels(self, capture_name):
        cur = self._conn.cursor()
        cur.execute(
            'SELECT * FROM CaptureLabelValue JOIN Capture on CaptureLabelValue.capture=Capture.id where Capture.name="{}"'.format(
                capture_name
            )
        )

        header = [x[0] for x in cur.description]
        rows = cur.fetchall()

        results = []
        for row in rows:
            results.append(row)

        return pd.DataFrame(results, columns=header)

    def get_capture_segments(self, capture_name):

        labels = self.list_capture_labels(capture_name)

        tmp_df = pd.read_csv(
            os.path.join(self.data_dir, capture_name), index_col="sequence"
        )

        M = DataSegments()

        for index, label in enumerate(
            labels[
                ["capture_sample_sequence_start", "capture_sample_sequence_end"]
            ].values
        ):
            M.append(
                DataSegment(
                    tmp_df.loc[label[0] : label[1]],
                    metadata={"segment": index, "capture": capture_name},
                )
            )

        return M

