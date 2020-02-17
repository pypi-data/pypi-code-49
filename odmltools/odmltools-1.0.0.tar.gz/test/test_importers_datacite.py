"""
test_importers_datacite tests the basic functions
and methods of the DataCite importer script.
"""

import os
import unittest

import odmltools.importers.import_datacite as dimp


class TestDatacite(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.resources = os.path.join(dir_path, "resources")

    def test_camel_to_snake(self):
        camel = "GeoLocationPoint"
        snake = "geo_location_point"

        conv = dimp.camel_to_snake(camel)
        self.assertEqual(conv, snake)

    def test_dict_from_xml(self):
        invalid_file = os.path.join(self.resources, "noxml.md")
        valid_file = os.path.join(self.resources, "load.xml")

        with self.assertRaises(dimp.ParserException):
            _ = dimp.dict_from_xml(invalid_file)

        res_dict = dimp.dict_from_xml(valid_file)
        self.assertIsInstance(res_dict, dict)
