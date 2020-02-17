#!/usr/bin/env python

from bob.pad.voice.database import PadVoiceFile as VoicePadFile
from bob.pad.face.database import VideoPadFile
from bob.pad.base.database import FileListPadDatabase
from bob.extension import rc
from .common import SwanVideoFile, SwanAudioFile, SwanVideoDatabase


class SwanAudioPadFile(SwanAudioFile, VoicePadFile):
    """SwanAudioPadFile are video files actually"""


class SwanVideoPadFile(SwanVideoFile, VideoPadFile):
    """SwanVideoPadFile are video files actually"""


class Database(FileListPadDatabase, SwanVideoDatabase):
    """Wrapper class for the SWAN database for PAD
    (http://www.idiap.ch/dataset/swan).
    """

    def __init__(self, original_directory=rc['bob.db.swan.directory'],
                 pad_file_class=SwanAudioPadFile,
                 annotation_directory=rc['bob.db.swan.annotation_dir'],
                 annotation_extension='.json',
                 annotation_type='json',
                 name='swan', **kwargs):
        # call base class constructor
        from pkg_resources import resource_filename
        folder = resource_filename(__name__, 'lists')
        super(Database, self).__init__(
            folder, name=name, pad_file_class=pad_file_class,
            annotation_directory=annotation_directory,
            annotation_extension=annotation_extension,
            annotation_type=annotation_type,
            original_directory=original_directory,
            training_depends_on_protocol=True, models_depend_on_protocol=True,
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
