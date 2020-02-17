#!/usr/bin/env python

from bob.db.swan.query_pad import Database, SwanVideoPadFile

database = Database(
    pad_file_class=SwanVideoPadFile,
)
