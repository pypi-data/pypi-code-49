"""
Contains the test DB data and the unittest for the example map format.
Dependency: apt install sqlite3 libsqlite3-mod-spatialite"""

import unittest
import sqlite3
import os
from openlr import Coordinates
from ..example_sqlite_map import ExampleMapReader, SRID

INIT_SQL = f"""SELECT InitSpatialMetaData(1);

CREATE TABLE nodes (id INTEGER PRIMARY KEY);
SELECT AddGeometryColumn('nodes', 'coord', {SRID}, 'POINT', 2, 1);

CREATE TABLE lines (startnode INT, endnode INT, frc INT, fow INT);
SELECT AddGeometryColumn('lines', 'path', {SRID}, 'LINESTRING', 2, 1);

INSERT INTO nodes (id, coord) VALUES
    (0, MakePoint(13.41, 52.525, {SRID})),
    (1, MakePoint(13.413, 52.522, {SRID})),
    (2, MakePoint(13.414, 52.525, {SRID})),
    (3, MakePoint(13.4145, 52.529, {SRID})),
    (4, MakePoint(13.416, 52.525, {SRID})),
    (5, MakePoint(13.4175, 52.52, {SRID})),
    (6, MakePoint(13.418, 52.53, {SRID})),
    (7, MakePoint(13.4185, 52.525, {SRID})),
    (8, MakePoint(13.42, 52.527, {SRID})),
    (9, MakePoint(13.421, 52.53, {SRID})),
    (10, MakePoint(13.4215, 52.522, {SRID})),
    (11, MakePoint(13.425, 52.525, {SRID})),
    (12, MakePoint(13.427, 52.53, {SRID})),
    (13, MakePoint(13.429, 52.523, {SRID}));

INSERT INTO lines (startnode, endnode, frc, fow, path) VALUES
    (0, 2, 1, 3, ST_GeomFromText("LINESTRING(13.41 52.525, 13.413 52.522)", {SRID})),
    (1, 2, 2, 3, ST_GeomFromText("LINESTRING(13.413 52.522, 13.4145 52.529)", {SRID})),
    (2, 3, 2, 3, ST_GeomFromText("LINESTRING(13.414 52.525, 13.4145 52.529)", {SRID})),
    (3, 4, 2, 3, ST_GeomFromText("LINESTRING(13.4145 52.529, 13.416 52.525)", {SRID})),
    (2, 4, 1, 3, ST_GeomFromText("LINESTRING(13.414 52.525, 13.416 52.525)", {SRID})),
    (4, 5, 2, 3, ST_GeomFromText("LINESTRING(13.416 52.525, 13.4175 52.52)", {SRID})),
    (5, 7, 2, 3, ST_GeomFromText("LINESTRING(13.4175 52.52, 13.4185 52.525)", {SRID})),
    (4, 7, 1, 3, ST_GeomFromText("LINESTRING(13.416 52.525, 13.4185 52.525)", {SRID})),
    (7, 8, 2, 3, ST_GeomFromText("LINESTRING(13.4185 52.525, 13.42 52.527)", {SRID})),
    (8, 9, 2, 3, ST_GeomFromText("LINESTRING(13.42 52.527, 13.421 52.53)", {SRID})),
    (9, 6, 2, 3, ST_GeomFromText("LINESTRING(13.421 52.53, 13.418 52.53)", {SRID})),
    (6, 8, 2, 3, ST_GeomFromText("LINESTRING(13.418 52.53, 13.42 52.527)", {SRID})),
    (8, 11, 2, 3, ST_GeomFromText("LINESTRING(13.42 52.527, 13.425 52.525)", {SRID})),
    (7, 11, 1, 3, ST_GeomFromText("LINESTRING(13.4185 52.525, 13.425 52.525)", {SRID})),
    (10, 11, 2, 3, ST_GeomFromText("LINESTRING(13.4215 52.522, 13.425 52.525)", {SRID})),
    (11, 12, 2, 3, ST_GeomFromText("LINESTRING(13.425 52.525, 13.427 52.53)", {SRID})),
    (11, 13, 1, 3, ST_GeomFromText("LINESTRING(13.425 52.525, 13.429 52.523)", {SRID}));
"""

def setup_testdb(db_file: str):
    "Creates a sqlite DB with all the test data"
    conn = sqlite3.connect(db_file)
    conn.enable_load_extension(True)
    conn.load_extension('mod_spatialite.so')
    cur = conn.cursor()
    cur.executescript(INIT_SQL)
    conn.close()

def remove_db_file(db_file: str):
    "Removes the sqlite DB file, and does not raise when nonexistent"
    try:
        os.remove(db_file)
    except FileNotFoundError:
        pass

class SQLiteMapTest(unittest.TestCase):
    "A few unit tests for the example sqlite mapformat"
    db = 'db.sqlite'

    def setUp(self):
        remove_db_file(self.db)
        setup_testdb(self.db)
        self.reader = ExampleMapReader(self.db)

    def test_line_length(self):
        "Check the length of the line with ID 1"
        line = self.reader.get_line(1)
        self.assertAlmostEqual(line.length, 391, delta=1)

    def test_linepoints(self):
        "Test the point count of every line"
        for line in self.reader.get_lines():
            self.assertEqual(line.num_points(), 2)

    def test_nearest(self):
        "Test the find_nodes_close_to with a manually chosen location"
        nodes = []
        nodes = [node.node_id for node \
            in self.reader.find_nodes_close_to(Coordinates(13.41, 52.523), 500)]
        self.assertSequenceEqual(nodes, [0, 1, 2, 4])

    def test_line_enumeration(self):
        "Test if a sorted list of line IDs is as expected"
        lines = []
        lines = [line.line_id for line in self.reader.get_lines()]
        self.assertEqual(len(lines), 17)
        self.assertSequenceEqual(sorted(lines), range(1, 18))

    def test_get_line(self):
        "Get a test line"
        _line = self.reader.get_line(17)

    def test_node_enumeration(self):
        "Test if a sorted list of point IDs is as expected"
        nodes = []
        nodes = [node.node_id for node in self.reader.get_nodes()]
        self.assertEqual(len(nodes), 14)
        self.assertSequenceEqual(sorted(nodes), range(14))

    def tearDown(self):
        self.reader.connection.close()
        remove_db_file(self.db)
