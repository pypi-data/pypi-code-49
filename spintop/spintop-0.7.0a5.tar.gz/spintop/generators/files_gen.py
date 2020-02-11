import os
import zipfile
from hashlib import md5

from glob import glob

from .base import Generator

class FileGenerator(Generator):
    def __call__(self, *filenames):
        for filename in filenames:
            with open(filename, 'rb') as subfile:
                yield subfile
    

class ZipFilesGenerator(Generator):
    
    def __call__(self, source):
        # We instantiate our OpenHTF test with the phases we want to run as args.
        zip_file = zipfile.ZipFile(source, "r")
        filenames = list(zip_file.namelist())
        for index, name in enumerate(filenames):
            print('Processing file %s. %d/%d' % (name, index, len(filenames)))
            with zip_file.open(name) as subfile:
                yield subfile

    def hash_fn(self, source):
        m = md5()
        with open(source, "rb") as f:
            data = f.read() #read file in chunk and call update on each chunk if file is large.
            m.update(data)
        return m.hexdigest()