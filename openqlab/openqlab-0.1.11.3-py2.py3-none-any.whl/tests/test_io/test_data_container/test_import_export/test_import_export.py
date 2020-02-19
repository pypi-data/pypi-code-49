import io
import logging
import pickle
from pathlib import Path
from unittest import TestCase

from openqlab.io.data_container import DataContainer, _open_file_or_buff

log = logging.getLogger(__name__)

filedir = Path(__file__).parent
export_data = filedir / "export_data"
import_data = filedir / "import_data"


class TestImportExportBase(TestCase):
    def setUp(self) -> None:
        self.header = {
            "comment": "This is a comment",
            "RBW": 10,
        }
        self.index = [100, 200, 300, 400]
        self.columns = {
            "column_1": [4, 3, 2, 1],
            "column_2": [500, 600, 700, 800],
        }
        self.data = DataContainer(
            header=self.header, index=self.index, data=self.columns
        )
        self.data.index.name = "frequency"

    def check_header(self, lines):
        self.assertEqual(repr(DataContainer.JSON_PREFIX.strip()), lines.pop(0))
        self.assertEqual(repr(str(self.header).replace("'", '"')), lines.pop(0))
        self.assertEqual(repr(DataContainer.JSON_SUFFIX.strip()), lines.pop(0))


class TestOpenFileContextManager(TestCase):
    path = Path(__file__).parent / "test_file_open"

    def test_string(self):
        with _open_file_or_buff(str(self.path)) as file:
            self.assertIsInstance(file, io.IOBase)
            file_handler = file
        self.assertEqual(True, file_handler.closed)

    def test_path(self):
        with _open_file_or_buff(self.path) as file:
            self.assertIsInstance(file, io.IOBase)
            file_handler = file
        self.assertEqual(True, file_handler.closed)

    def test_buffer(self):
        with open(self.path) as buffer:
            with _open_file_or_buff(buffer) as file:
                self.assertIsInstance(file, io.IOBase)
                file_handler = file
            self.assertEqual(True, file_handler.closed)

    def test_None(self):
        with _open_file_or_buff(None) as file:
            self.assertIsInstance(file, io.StringIO)
            file_handler = file
        self.assertEqual(True, file_handler.closed)


class TestCSV(TestImportExportBase):
    def test_to_csv(self):
        filename = export_data / "data.csv"
        self.data.to_csv(filename)

        with open(filename) as file:
            lines = [repr(line) for line in file.read().splitlines()]
            self.check_header(lines)
            self.assertEqual(
                repr(",".join(["frequency"] + list(self.columns.keys()))), lines.pop(0)
            )

            rows = zip(*[self.index] + list(self.columns.values()))
            for line, row in zip(lines, rows):
                row_string = repr(",".join(map(str, row)))
                with self.subTest(line=line):
                    self.assertEqual(row_string, line)

    def test_to_csv_as_string(self):
        csv_string = self.data.to_csv()
        data = DataContainer.read_csv(io.StringIO(csv_string))

        self.assertTrue(self.data.equals(data))
        self.assertEqual(self.data.header, data.header)

    def test_read_csv(self):
        filename = import_data / "data.csv"
        imported_data = DataContainer.read_csv(filename)
        self.assertTrue(self.data.equals(imported_data))
        self.assertEqual(self.data.header, imported_data.header)

    def test_from_csv(self):
        filename = import_data / "data.csv"
        imported_data = DataContainer.from_csv(filename)
        self.assertTrue(self.data.equals(imported_data))
        self.assertEqual(self.data.header, imported_data.header)


class TestJSON(TestImportExportBase):
    def test_to_json_orient_table(self):
        filename = export_data / "data_orient_table.json"
        self.data.to_json(filename, orient="table")

        with open(filename) as file:
            lines = [repr(line) for line in file.read().splitlines()]
            self.check_header(lines)

    def test_to_json_orient_index(self):
        filename = export_data / "data_orient_index.json"
        self.data.to_json(filename, orient="index")

        with open(filename) as file:
            lines = [repr(line) for line in file.read().splitlines()]
            self.check_header(lines)

    def test_to_json_as_string(self):
        json_string = self.data.to_json(orient="table")
        data = DataContainer.read_json(io.StringIO(json_string), orient="table")

        self.assertTrue(self.data.equals(data))
        self.assertEqual(self.data.header, data.header)

    def test_read_json(self):
        pass


class TestHDF5(TestImportExportBase):
    def test_import_export(self):
        filename = export_data / "data.hdf"
        self.data.to_hdf(filename, key="test_data")
        data = DataContainer.read_hdf(filename, "test_data")

        self.assertTrue(self.data.equals(data))
        self.assertEqual(self.data.header, data.header)

    def test_from_hdf(self):
        filename = export_data / "data.hdf"
        self.data.to_hdf(filename, key="test_data")
        data = DataContainer.from_hdf(filename, "test_data")

        self.assertTrue(self.data.equals(data))
        self.assertEqual(self.data.header, data.header)


class TestPickle(TestImportExportBase):
    def test_import_export(self):
        filename = export_data / "data.pickle"
        self.data.to_pickle(filename)
        data = DataContainer.read_pickle(filename)

        self.assertTrue(self.data.equals(data))
        self.assertEqual(self.data.header, data.header)
