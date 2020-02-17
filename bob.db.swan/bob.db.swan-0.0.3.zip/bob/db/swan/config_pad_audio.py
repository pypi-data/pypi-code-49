#!/usr/bin/env python

from bob.db.swan.query_pad import Database, SwanAudioPadFile

database = Database(
    pad_file_class=SwanAudioPadFile,
    annotation_directory=None,  # no annotations for the voice part
    new_rate=16000,
)
