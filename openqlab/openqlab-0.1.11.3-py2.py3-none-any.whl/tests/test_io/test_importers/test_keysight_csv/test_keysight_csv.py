import os
import unittest
from pathlib import Path

from pandas.errors import EmptyDataError

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.keysight_csv import KeysightCSV
from openqlab.io.importers.utils import UnknownFileType

filedir = Path(__file__).parent


class TestKeysightCSV(unittest.TestCase):
    importer = KeysightCSV
    files_path = filedir / "../data_files"
    supported_files_path = files_path / "KeysightCSV"

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

    def test_missing_data(self):
        file = filedir / "missing_data.csv"
        try:
            with self.assertRaises(EmptyDataError):
                self.read_file(file)
        except AssertionError as e:
            raise AssertionError(f"{file} did not raise {EmptyDataError}") from e

    def test_correct_rows_singletrace(self):
        file = self.supported_files_path / "20180606_004_1.csv"
        data = self.read_file(file)

        # header
        self.assertEqual("s", data.header["xUnit"])
        self.assertEqual("V", data.header["yUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["20180606_004_1_1"], list(data.columns))
        self.assertEqual("Time", data.index.name)

        # data
        self.assertEqual(-0.1, data.index[0])
        self.assertEqual(0.0999, data.index[-1])
        self.assertEqual(-0.09, data.index[100])  # line 103 in file

        self.assertAlmostEqual(2.18281, data.iloc[0, 0])
        self.assertAlmostEqual(0.141307, data.iloc[-1, 0])
        self.assertAlmostEqual(1.20111, data.iloc[100, 0])  # line 103 in file

    def test_correct_rows_multitrace(self):
        file = self.supported_files_path / "20180606_003.csv"
        data = self.read_file(file)
        # header
        self.assertEqual("s", data.header["xUnit"])
        self.assertEqual("V", data.header["yUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(
            ["20180606_003_1", "20180606_003_2", "20180606_003_3", "20180606_003_4"],
            list(data.columns),
        )
        self.assertEqual("Time", data.index.name)

        # data
        self.assertEqual(-0.1, data.index[0])
        self.assertEqual(0.0999, data.index[-1])
        self.assertEqual(-0.09, data.index[100])

        self.assertAlmostEqual(2.182814, data.iloc[0, 0])
        self.assertAlmostEqual(-2.552764e00, data.iloc[0, 1])
        self.assertAlmostEqual(-63.442e-03, data.iloc[0, 2])
        self.assertAlmostEqual(3.091e-03, data.iloc[0, 3])

        self.assertAlmostEqual(+139.447e-03, data.iloc[-1, 0])
        self.assertAlmostEqual(-2.552764e00, data.iloc[-1, 1])
        self.assertAlmostEqual(-63.442e-03, data.iloc[-1, 2])
        self.assertAlmostEqual(+3.091e-03, data.iloc[-1, 3])

        # line 103 in file
        self.assertAlmostEqual(+1.201106e00, data.iloc[100, 0])
        self.assertAlmostEqual(-2.552764e00, data.iloc[100, 1])
        self.assertAlmostEqual(-63.442e-03, data.iloc[100, 2])
        self.assertAlmostEqual(+3.272e-03, data.iloc[100, 3])
