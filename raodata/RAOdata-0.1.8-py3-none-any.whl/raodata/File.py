#!/usr/bin/env python3

import os
import errno
import urllib
import hashlib
from dateutil import parser
from raodata import exceptions


class File():
    """Class representing a file from RAO data archive"""

    CACHE_PATH = os.path.expanduser('~') + "/.cache/raodata"

    def __init__(self, name, url, hash, date):
        """
        This class provides API access to RAO data archive.
        It carries original file name, its URL, MD5 hash, date/time and
        local location of the file if it is already downloaded
        """
        try:
            date = parser.parse(str(date))
        except ValueError:
            raise exceptions.InvalidTime(
                  "Time should be in ISO 8601 format: '%Y-%m-%dT%H:%M:%S'")

        self.name = name
        self.url = url
        self.hash = hash
        self.date = date
        self.local_name = self.CACHE_PATH + "/" + hash
        self.downloaded = False

    def name(self):
        """Get file name"""
        return self.name

    def hash(self):
        """Get file hash"""
        return self.hash

    def url(self):
        """Get file URL"""
        return self.url

    def date(self):
        """Get file date"""
        return self.date

    def download(self):
        """
        Downloads file if it is not downloaded yet and
        saves it into cache folder
        """

        self.downloaded = False

        if os.path.exists(self.local_name):
            _file = open(self.local_name, "rb")
            content = _file.read()
            _file.close()

            try:
                md5 = hashlib.md5(content).hexdigest()
            except BaseException:
                md5 = ""

            if md5 == self.hash:
                self.downloaded = True
            else:
                os.remove(self.local_name)

        attempts = 0
        while not self.downloaded:
            try:
                while True:
                    try:
                        _file = urllib.request.urlopen(self.url)
                        if _file.getcode() != 504:
                            break
                    except BaseException:
                        pass

                content = _file.read()
            except BaseException:
                raise exceptions.CannotDownloadFile("Cannot download file")

            try:
                md5 = hashlib.md5(content).hexdigest()
            except BaseException:
                md5 = ""

            if md5 != self.hash:
                if attempts <= 3:
                    attempts += 1
                else:
                    raise exceptions.InvalidFileHash("Invalid file hash")
            else:
                self._save_to_cache(content, self.local_name)
                self.downloaded = True

    def _save_to_cache(self, content, path):
        """Save file into cache"""
        if not os.path.exists(path):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError:
                pass

            with open(path, "wb") as _f:
                _f.write(content)
            _f.close()

    def handle(self):
        """Returns open file handler"""
        if self.downloaded is False:
            self.download()

        return open(self.local_name, "rb")

    def local(self):
        """Returns file name in local file system"""
        if self.downloaded is False:
            self.download()

        return self.local_name

    def contents(self):
        """Returns file content"""
        if self.downloaded is False:
            self.download()

        with open(self.local_name, "rb") as _f:
            _content = _f.read()
        _f.close()

        return _content

    def save_to(self, filepath):
        """Save file into a specific file on local file system"""
        if self.downloaded is False:
            self.download()

        if not os.path.exists(os.path.dirname(filepath)):
            try:
                os.makedirs(os.path.dirname(filepath))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise exceptions.CannotCreateDirectory(
                          "Can not create directory")

        with open(filepath, "wb") as _f:
            _f.write(self.contents())

        _f.close()
