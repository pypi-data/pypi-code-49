import os
import unittest
from pathlib import Path

from pandas.errors import EmptyDataError

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.hp4395a import HP4395A
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent


class TestHP4395A(unittest.TestCase):
    importer = HP4395A
    files_path = filedir / "../data_files"
    supported_files_path = files_path / "HP4395A"

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
        files = [filedir / "missing_data.txt"]
        for file in files:
            try:
                with self.assertRaises(EmptyDataError):
                    self.read_file(file)
            except AssertionError as e:
                raise AssertionError(f"{file} did not raise {EmptyDataError}") from e

    def test_correct_rows_multitrace(self):
        file = self.supported_files_path / "ADDHAG.txt"
        data = self.read_file(file)
        # header
        self.assertEqual("Hz", data.header["xUnit"])
        self.assertEqual("dB", data.header["yUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        column_names = [
            "ADDHAG_Ch1_DataReal",
            "ADDHAG_Ch1_DataImag",
            "ADDHAG_Ch1_MemReal",
            "ADDHAG_Ch1_MemImag",
            "ADDHAG_Ch2_DataReal",
            "ADDHAG_Ch2_DataImag",
            "ADDHAG_Ch2_MemReal",
            "ADDHAG_Ch2_MemImag",
        ]
        self.assertEqual(column_names, list(data.columns))
        self.assertEqual("Frequency (Hz)", data.index.name)

        # data
        self.assertAlmostEqual(1.00000000000e03, data.index[0])
        self.assertAlmostEqual(1.00000000000e05, data.index[100])
        self.assertAlmostEqual(1.00000000000e07, data.index[-1])

        self.assertAlmostEqual(-1.227111e01, data.iloc[0, 0])
        self.assertEqual(0, data.iloc[0, 1])
        self.assertAlmostEqual(-1.516244e00, data.iloc[0, 4])
        self.assertEqual(0, data.iloc[0, 5])

        # line 126 in file
        self.assertAlmostEqual(-1.233819e01, data.iloc[100, 0])
        self.assertEqual(0, data.iloc[100, 1])
        self.assertAlmostEqual(-3.203341e00, data.iloc[100, 4])
        self.assertEqual(0, data.iloc[100, 5])

        self.assertAlmostEqual(-1.749125e01, data.iloc[-1, 0])
        self.assertEqual(0, data.iloc[-1, 1])
        self.assertAlmostEqual(-1.238039e02, data.iloc[-1, 4])
        self.assertEqual(0, data.iloc[-1, 5])
