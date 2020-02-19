import unittest
from pathlib import Path

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.gwinstek_lsf import Gwinstek_LSF
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent
datadir = filedir / "../data_files"


class TestGwinstek_LSF(unittest.TestCase):
    importer = Gwinstek_LSF
    files_path = datadir
    supported_files_path = datadir / "Gwinstek_LSF"

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

    def test_correct_rows_singletrace(self):
        file = self.supported_files_path / "mode_binary_4.LSF"
        data = self.read_file(file)

        # header
        self.assertEqual("s", data.header["xUnit"])
        self.assertEqual("V", data.header["yUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["mode_binary_4"], list(data.columns))
        self.assertEqual("Time", data.index.name)

        # data
        self.assertAlmostEqual(-1.000000e-02, data.index[0])
        self.assertAlmostEqual(-9.998000e-03, data.index[1])
        self.assertAlmostEqual(-9.800000e-03, data.index[100])  # line 126 in file
        self.assertAlmostEqual(9.998000e-03, data.index[-1])

        self.assertAlmostEqual(1.60e-03, data.iloc[0, 0])
        self.assertAlmostEqual(-8.00e-04, data.iloc[1, 0])
        self.assertAlmostEqual(0.00e00, data.iloc[100, 0])  # line 126 in file)
        self.assertAlmostEqual(-8.00e-04, data.iloc[-1, 0])

    def test_missing_beginning_hashtag(self):
        with self.assertRaises(ImportFailed):
            self.importer(filedir / "data/missing_hashtag.LSF").read()

    def test_missing_x_unit(self):
        with self.assertRaises(ImportFailed):
            self.importer(filedir / "data/missing_x_unit.LSF").read()
