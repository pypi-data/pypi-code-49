import os
import tempfile
import unittest

from cvplotlib import data_source as ds


class FileSourceTests(unittest.TestCase):

    def setUp(self):

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as self.file:
            self.file.write("""Some content""")

    def tearDown(self):
        os.unlink(self.file.name)

    @unittest.skip
    def test_file_read(self):
        source = ds.FileDataSource(self.file.name)
