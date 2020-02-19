import unittest
from pathlib import Path

from pandas.errors import EmptyDataError

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.data_container_csv import DataContainerCSV
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent
datadir = filedir / "../data_files"


class TestDataContainerCSV(unittest.TestCase):
    importer = DataContainerCSV
    files_path = datadir
    supported_files_path = datadir / "DataContainerCSV"

    def read_file(self, file):
        try:
            data = self.importer(file).read()
            self.assertTrue(isinstance(data, DataContainer) and not data.empty)
            self.assertTrue(data._is_numeric_mixed_type)
            for column in data.columns:
                self.assertFalse(data[column].isna().values.all())
            return data
        except Exception as e:
            print(f"{file}")
            raise type(e)(f'"{file}" raised Exception: {e}') from e

    @classmethod
    def setUpClass(cls):
        cls.supported_files = list(cls.supported_files_path.glob("*"))
        cls.supported_files = [
            file for file in cls.supported_files if not file.stem.startswith(".")
        ]
        cls.test_files = list(cls.files_path.glob("*/*"))
        cls.unsupported_files = [
            file for file in cls.test_files if file not in cls.supported_files
        ]
        assert cls.supported_files
        assert cls.unsupported_files

    def test_supported_files(self):
        for file in self.supported_files:
            self.read_file(file)

    def test_unsupported_files(self):
        for file in self.unsupported_files:
            try:
                with self.assertRaises(UnknownFileType):
                    self.read_file(file)
            except AssertionError as e:
                raise AssertionError(f"{file} did not raise {UnknownFileType}") from e

    def test_correct_import(self):
        file = self.supported_files_path / "data_container_csv.csv"
        data = self.read_file(file)

        # header
        self.assertEqual(1, data.header["test"])

        # columns and index
        self.assertEqual(["0"], list(data.columns))

        # data
        self.assertEqual(1, data.index[0])
        self.assertEqual(2, data.index[1])

        self.assertAlmostEqual(1, data.iloc[0, 0])
        self.assertAlmostEqual(2, data.iloc[1, 0])

    def test_empty_file(self):
        file = filedir / "data_container_csv_empty.csv"
        with self.assertRaises(UnknownFileType):
            self.read_file(file)

    def test_empty_file_with_header(self):
        file = filedir / "data_container_csv_empty_with_header.csv"
        with self.assertRaises(EmptyDataError):
            self.read_file(file)
