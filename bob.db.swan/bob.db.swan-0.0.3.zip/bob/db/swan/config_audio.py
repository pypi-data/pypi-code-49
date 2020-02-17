#!/usr/bin/env python

from bob.db.swan import Database, SwanAudioBioFile

database = Database(
    bio_file_class=SwanAudioBioFile,
    annotation_directory=None,  # no annotations for the voice part
    new_rate=16000,
)
