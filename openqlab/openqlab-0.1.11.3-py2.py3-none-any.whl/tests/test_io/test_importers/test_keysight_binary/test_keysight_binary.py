import os
import unittest
from pathlib import Path

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.keysight_binary import KeysightBinary
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent


class TestKeysightBinary(unittest.TestCase):
    importer = KeysightBinary
    files_path = filedir / "../data_files"
    supported_files_path = Path(fr"{files_path}/KeysightBinary")

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

    def test_missing_AG_header(self):
        file = filedir / "missing_AG_header.bin"
        with self.assertRaises(UnknownFileType):
            self.read_file(file)

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

    def test_correct_rows_multitrace(self):
        file = self.supported_files_path / "keysight_binary.bin"
        data = self.read_file(file)

        # columns and index
        self.assertEqual(
            [
                "keysight_binary_1",
                "keysight_binary_2",
                "keysight_binary_3",
                "keysight_binary_4",
            ],
            list(data.columns),
        )
        self.assertEqual("Time", data.index.name)

        # data
        self.assertEqual(-0.004312546210625, data.index[0])
        self.assertEqual(-0.004302546210625, data.index[1])
        self.assertEqual(0.015677453789375, data.index[-1])

        self.assertAlmostEqual(-0.045201004, data.iloc[0, 0])
        self.assertAlmostEqual(-0.019346714, data.iloc[0, 3])

        self.assertAlmostEqual(-0.025100503, data.iloc[1, 0])
        self.assertAlmostEqual(0.00075376034, data.iloc[1, 3])

        self.assertAlmostEqual(-0.025100503, data.iloc[-1, 0])
        self.assertAlmostEqual(0.00075376034, data.iloc[-1, 3])
