import unittest
from pathlib import Path

import pandas as pd

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.ascii import ASCII
from openqlab.io.importers.utils import UnknownFileType

filedir = Path(__file__).parent
datadir = filedir / "../data_files"


class TestASCII(unittest.TestCase):
    importer = ASCII
    files_path = datadir
    supported_files_path = datadir / "ASCII"
    multiline_comment = "This is a multiline comment.\nIt continues at the next line.\nAnd another line\nwith newline."

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

    # @unittest.skip("Importer cannot recognize unsupported files")
    def test_unsupported_files(self):
        for file in self.unsupported_files:
            try:
                with self.assertRaises(UnknownFileType):
                    self.read_file(file)
            except AssertionError as e:
                raise AssertionError(f"{file} did not raise {UnknownFileType}") from e

    def test_correct_rows(self):
        file = self.supported_files_path / "dig0.TXT"
        data = self.read_file(file)

        # columns and index
        self.assertEqual(["dig0"], list(data.columns))
        self.assertEqual("x", data.index.name)

        # data
        self.assertAlmostEqual(+1.280000e002, data.index[0])
        self.assertAlmostEqual(+2.560000e002, data.index[1])
        self.assertAlmostEqual(+1.408000e003, data.index[10])  # line 11 in file
        self.assertAlmostEqual(+1.024000e005, data.index[-1])

        self.assertAlmostEqual(-4.078996e001, data.iloc[0, 0])
        self.assertAlmostEqual(-5.155923e001, data.iloc[1, 0])
        self.assertAlmostEqual(-7.461130e001, data.iloc[10, 0])  # line 11 in file)
        self.assertAlmostEqual(-9.785766e001, data.iloc[-1, 0])
