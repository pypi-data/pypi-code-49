#!/usr/bin/env python

from bob.db.swan import Database, SwanVideoBioFile

database = Database(
    bio_file_class=SwanVideoBioFile,
)
