"""Document set.

Copyright (C) Zooper Inc 2019.
"""
import os
import shutil


class DocumentSet:
    """ Consists of iterable documents.

    The documents can be local file(s) or remote file(s).
    Supported remote file: ['s3://', 'gs://']

    Arguments:
    prefix: one of ['s3://', 'gs://'].
    """

    def __init__(self, prefix='local://'):
        self._uris = []
        self._root_uri = None
        if prefix == 'local://' or prefix == '':
            self._store_type = 'local'
        elif prefix == 'gs://':
            self._store_type = 'gcs'
        elif prefix == 's3://':
            self._store_type = 's3'
        else:
            raise ValueError('Not supported prefix: {}'.format(prefix))

    def export(self, target):
        """ Export document set to target location. """
        if target.startswith('s3://'):
            # TODO(open): implement this
            pass
        elif target.startswith('gs://'):
            # TODO(open): implement this
            pass
        else:
            if os.path.isdir(target):
                shutil.rmtree(target)
            os.makedirs(target)
            for uri in self._uris:
                target_uri = os.path.join(target, os.path.basename(uri))
                if target_uri != uri:
                    os.symlink(uri, target_uri)

    @staticmethod
    def create(path):
        """ Create DocumentSet from a path.

        TODO(zooper): support non-local path such as s3://, gs://.
        """
        assert os.path.isdir(path), "Path {} must be a directory.".format(path)
        uris = [os.path.join(path, f) for f in os.listdir(path)]
        print('Created {} documents.'.format(len(uris)))
        ds = DocumentSet()
        ds.uris = uris
        ds.root_uri = path
        return ds

    @property
    def uris(self):
        return self._uris

    @uris.setter
    def uris(self, uris):
        self._uris = uris

    @property
    def root_uri(self):
        """ If set, indicates the root uri for this doc set.

        For example, this could indicate a root directory.
        """
        return self._root_uri

    @root_uri.setter
    def root_uri(self, root_uri):
        self._root_uri = root_uri

