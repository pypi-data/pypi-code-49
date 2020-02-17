"""
test_importers_datacite_integration tests parsing
whole datacite xml files.
"""

import os
import shutil
import tempfile
import unittest

import odml
import odmltools.importers.import_datacite as dimp


class TestDataciteIntegration(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.resources = os.path.join(dir_path, "resources")

        self.tmp_dir = tempfile.mkdtemp(suffix=".odmltools")

    def tearDown(self):
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)

    def test_complete_conversion(self):
        # This test should be split up into multiple tests
        # but for now converting a complete datacite xml
        # file to odml should at least not break when
        # changes to the code are made.

        invalid_file = os.path.join(self.resources, "noxml.md")
        with self.assertRaises(dimp.ParserException):
            _ = dimp.handle_document(invalid_file, self.tmp_dir)

        invalid_dc_file = os.path.join(self.resources, "load.xml")
        with self.assertRaises(dimp.ParserException):
            _ = dimp.handle_document(invalid_dc_file, self.tmp_dir)

        dc_fn = "fullDataCiteSchema.xml"
        dc_file = os.path.join(self.resources, dc_fn)
        dimp.handle_document(dc_file, self.tmp_dir)

        # make sure the file has been created and is an accessible odml file
        doc = odml.load(os.path.join(self.tmp_dir, dc_fn))
        self.assertGreater(len(doc), 0)

    def test_complete_conversion_namespaces(self):
        # This test should be split up into multiple tests
        # but for now converting a complete datacite xml
        # file to odml should at least not break when
        # changes to the code are made.

        dcns_fn = "fullDataCiteSchemaNS.xml"
        dc_file = os.path.join(self.resources, dcns_fn)
        dimp.handle_document(dc_file, self.tmp_dir)

        doc = odml.load(os.path.join(self.tmp_dir, dcns_fn))
        self.assertEqual(len(doc.sections['DataCite']), 19)
        self.assertEqual(len(doc.sections['DataCite'].sections), 15)
        self.assertEqual(len(doc.sections['DataCite'].properties), 4)

    def test_extra_namespaces(self):
        extra_fn = "unsupportedNS.xml"
        extra_file = os.path.join(self.resources, extra_fn)

        with self.assertRaises(dimp.ParserException):
            dimp.handle_document(extra_file, self.tmp_dir)

        extra_nspace = ["http://datacite.org/schema/kernel-2"]
        dimp.handle_document(extra_file, self.tmp_dir, extra_ns=extra_nspace)
