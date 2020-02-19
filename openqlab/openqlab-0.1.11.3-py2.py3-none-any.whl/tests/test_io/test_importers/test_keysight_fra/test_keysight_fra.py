import os
import unittest
from pathlib import Path

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.keysight_fra import KeysightFRA
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent


class TestKeysightFRA(unittest.TestCase):
    importer = KeysightFRA
    files_path = filedir / "../data_files"
    supported_files_path = Path(fr"{files_path}/KeysightFRA")

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
            with self.assertRaises(ImportFailed):
                self.read_file(file)
        except AssertionError as e:
            raise AssertionError(f"{file} did not raise {ImportFailed}") from e

    def test_correct_rows_multitrace(self):
        file = self.supported_files_path / "scope_0_comma.csv"
        data = self.read_file(file)
        # columns and index
        self.assertEqual(
            ["Amplitude (Vpp)", "Gain (dB)", "Phase (deg)"], list(data.columns)
        )
        self.assertEqual("Frequency (Hz)", data.index.name)

        # data
        self.assertEqual(20.0, data.index[0])
        self.assertEqual(100000.0, data.index[-1])
        self.assertEqual(42986.6, data.index[100])  # line 102 in file

        self.assertEqual(2.0, data.iloc[0, 0])
        self.assertEqual(2.0, data.iloc[-1, 0])
        self.assertEqual(2.0, data.iloc[100, 0])  # line 102 in file

        self.assertEqual(0.0, data.iloc[0, 1])
        self.assertEqual(-74.56, data.iloc[-1, 1])
        self.assertEqual(-3.09, data.iloc[100, 1])  # line 102 in file

        self.assertEqual(-0.18, data.iloc[0, 2])
        self.assertEqual(-85.46, data.iloc[-1, 2])
        self.assertEqual(51.29, data.iloc[100, 2])  # line 102 in file
