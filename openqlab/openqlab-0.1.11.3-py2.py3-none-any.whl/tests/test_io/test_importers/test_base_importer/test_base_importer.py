import unittest

from openqlab.io.base_importer import BaseImporter, StreamImporter, VisaImporter


class TestSubclasses(unittest.TestCase):
    def test_get_subclasses(self):
        self.assertTrue(
            {StreamImporter, VisaImporter}.issubset(set(BaseImporter.get_subclasses()))
        )

    def test_get_subclasses_with_new_class(self):
        class NewImporter(StreamImporter):
            name = "NewImporter"
            autoimporter = True
            _starting_lines = [""]

            def read(self):
                raise NotImplementedError()

        self.assertTrue(
            {StreamImporter, VisaImporter, NewImporter}.issubset(
                set(BaseImporter.get_subclasses())
            )
        )

    def test_get_subclasses_from_subclasses(self):
        class NewImporter(StreamImporter):
            name = "NewImporter"
            autoimporter = True
            _starting_lines = [""]

            def read(self):
                raise NotImplementedError()

        class NewNewImporter(NewImporter):
            name = "NewNewImporter"
            autoimporter = True
            _starting_lines = [""]

            def read(self):
                raise NotImplementedError()

        self.assertTrue(
            {StreamImporter, VisaImporter, NewImporter, NewNewImporter}.issubset(
                set(BaseImporter.get_subclasses())
            )
        )
