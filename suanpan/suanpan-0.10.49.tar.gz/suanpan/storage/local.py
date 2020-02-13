# coding=utf-8
from __future__ import absolute_import, division, print_function

import os
import tempfile

from suanpan import path as spath
from suanpan import runtime
from suanpan.log import logger
from suanpan.storage import base


class Storage(base.Storage):
    def __init__(self, localTempStore=tempfile.gettempdir(), **kwargs):
        super(Storage, self).__init__(
            delimiter=os.sep, tempStore=localTempStore, **kwargs
        )

    def download(self, name, path, workers=None):  # pylint: disable=unused-argument
        logger.info(
            f"Downloading: {self.storageUrl(name)} -> {path} - ({self.name}) Nothing to do!"
        )
        return self.getPathInTempStore(path)

    def upload(self, name, path, workers=None):  # pylint: disable=unused-argument
        logger.info(
            f"Uploading: {self.storageUrl(name)} -> {path} - ({self.name}) Nothing to do!"
        )
        return path

    def copy(self, path, dist, workers=None):  # pylint: disable=unused-argument
        pathUrl = self.storageUrl(path)
        distUrl = self.storageUrl(dist)
        logger.info(f"Copying: {pathUrl} -> {distUrl}")
        _path = self.getPathInTempStore(path)
        _dist = self.getPathInTempStore(dist)
        spath.copy(_path, _dist)
        logger.info(f"Copied: {pathUrl} -> {distUrl}")
        return dist

    def remove(self, path, workers=None):  # pylint: disable=unused-argument
        spath.remove(self.getPathInTempStore(path))
        logger.info(f"Removed: {self.storageUrl(path)}")
        return path

    def walk(self, folderName):
        root = self.getPathInTempStore(folderName)
        return runtime.saferun(os.walk, default=iter(()))(root)

    def listAll(self, folderName):
        root = self.getPathInTempStore(folderName)
        return (self.storagePathJoin(root, p) for p in os.listdir(root))

    def listFolders(self, folderName):
        return (p for p in self.listAll(folderName) if os.path.isdir(p))

    def listFiles(self, folderName):
        return (p for p in self.listAll(folderName) if os.path.isfile(p))

    def isFolder(self, folderName):
        folder = self.getPathInTempStore(folderName)
        return os.path.isdir(folder)

    def isFile(self, objectName):
        file = self.getPathInTempStore(objectName)
        return os.path.isfile(file)

    def storagePathJoin(self, *paths):
        return self.localPathJoin(*paths)

    def storageRelativePath(self, path, basepath):
        return self.localRelativePath(path, basepath)

    def storageUrl(self, path):
        return "file://" + self.getPathInTempStore(path)

    def getStorageMd5(self, objectName):
        return self.getLocalMd5(self.getPathInTempStore(objectName))

    def getStorageSize(self, objectName):
        return self.getLocalSize(self.getPathInTempStore(objectName))
