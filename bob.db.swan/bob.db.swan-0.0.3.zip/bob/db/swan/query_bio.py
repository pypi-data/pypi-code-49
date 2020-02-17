#!/usr/bin/env python

from bob.bio.spear.database import AudioBioFile
import bob.bio.base
import bob.io.base
import bob.io.video
from bob.extension import rc
from .common import SwanVideoFile, SwanAudioFile, SwanVideoDatabase


class SwanAudioBioFile(SwanAudioFile, AudioBioFile):
    """SwanAudioBioFile are video files actually"""


class SwanVideoBioFile(SwanVideoFile):
    """SwanVideoBioFile are video files actually"""


class Database(bob.bio.base.database.FileListBioDatabase, SwanVideoDatabase):
    """Wrapper class for the SWAN database for speaker recognition
    (http://www.idiap.ch/dataset/swan). This class defines a simple protocol
    for training, dev and and by splitting the audio files of the database in
    three main parts.
    """

    def __init__(self, original_directory=rc['bob.db.swan.directory'],
                 bio_file_class=SwanAudioBioFile,
                 annotation_directory=rc['bob.db.swan.annotation_dir'],
                 annotation_extension='.json',
                 annotation_type='json',
                 name='swan', **kwargs):
        # call base class constructor
        from pkg_resources import resource_filename
        folder = resource_filename(__name__, 'lists')
        super(Database, self).__init__(
            folder, name=name, bio_file_class=bio_file_class,
            annotation_directory=annotation_directory,
            annotation_extension=annotation_extension,
            annotation_type=annotation_type,
            original_directory=original_directory,
            training_depends_on_protocol=False, models_depend_on_protocol=True,
            **kwargs
        )

    def objects(self, groups=None, protocol=None, purposes=None,
                model_ids=None, classes=None, filter_samples=None, **kwargs):
        files = super(Database, self).objects(
            groups=groups, protocol=protocol, purposes=purposes,
            model_ids=model_ids, classes=classes, **kwargs)
        files = self.update_files(files)
        if filter_samples is None:
            return files
        files = list(filter(filter_samples, files))
        return files
