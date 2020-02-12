#! /usr/bin/env python

import unittest

from base import ARGS

from dynamo_consistency import datatypes

class TestTreeName(unittest.TestCase):
    def test_getfile(self):
        filelist = ['/test/dir/file.txt']
        for name in ['/test', '/']:

            tree = datatypes.DirectoryInfo(name)
            tree.add_file_list([(f, 10, 0) for f in filelist])

            self.assertEqual(tree.name, name)
            self.assertEqual(tree.get_files(), filelist)
            self.assertEqual(tree.get_file(filelist[0])['size'], 10)

if __name__ == '__main__':
    unittest.main(argv=ARGS)
