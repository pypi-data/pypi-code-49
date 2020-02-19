import unittest
from pathlib import Path

from pandas.errors import EmptyDataError

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.gwinstek import Gwinstek
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent
datadir = filedir / "../data_files"


class TestGwinstek(unittest.TestCase):
    importer = Gwinstek
    files_path = datadir
    supported_files_path = datadir / "Gwinstek"

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

    def test_missing_data(self):
        files = [filedir / "missing_data.csv", filedir / "missing_data_1.csv"]
        for file in files:
            try:
                with self.assertRaises(EmptyDataError):
                    self.read_file(file)
            except AssertionError as e:
                raise AssertionError(f"{file} did not raise {EmptyDataError}") from e

    def test_wrong_savemode(self):
        file = filedir / "wrong_savemode.csv"
        try:
            with self.assertRaises(ImportFailed):
                self.read_file(file)
        except AssertionError as e:
            raise AssertionError(f"{file} did not raise {ImportFailed}") from e

    def test_missing_savemode(self):
        file = filedir / "missing_savemode.csv"
        try:
            with self.assertRaises(ImportFailed):
                self.read_file(file)
        except AssertionError as e:
            raise AssertionError(f"{file} did not raise {ImportFailed}") from e

    def test_correct_rows_singletrace_detail(self):
        file = self.supported_files_path / "mode_detail.csv"
        data = self.read_file(file)

        # header
        self.assertEqual("s", data.header["xUnit"])
        self.assertEqual("V", data.header["yUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["mode_detail_1"], list(data.columns))
        self.assertEqual("Time", data.index.name)

        # data
        self.assertAlmostEqual(-2.185000e-01, data.index[0])
        self.assertAlmostEqual(-2.184500e-01, data.index[1])
        self.assertAlmostEqual(-2.135000e-01, data.index[100])  # line 126 in file
        self.assertAlmostEqual(2.814500e-01, data.index[-1])

        self.assertAlmostEqual(0.00e00, data.iloc[0, 0])
        self.assertAlmostEqual(1.60e-04, data.iloc[1, 0])
        self.assertAlmostEqual(0.00e00, data.iloc[100, 0])  # line 126 in file)
        self.assertAlmostEqual(-1.20e-04, data.iloc[-1, 0])

    def test_correct_rows_singletrace_fast(self):
        file = self.supported_files_path / "mode_fast.csv"
        data = self.read_file(file)

        # header
        self.assertEqual("s", data.header["xUnit"])
        self.assertEqual("V", data.header["yUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["mode_fast_1"], list(data.columns))
        self.assertEqual("Time", data.index.name)

        # data
        self.assertAlmostEqual(-2.185000e-01, data.index[0])
        self.assertAlmostEqual(-2.184500e-01, data.index[1])
        self.assertAlmostEqual(-2.135000e-01, data.index[100])  # line 126 in file
        self.assertAlmostEqual(2.814500e-01, data.index[-1])

        self.assertAlmostEqual(0.00e00, data.iloc[0, 0])
        self.assertAlmostEqual(1.60e-04, data.iloc[1, 0])
        self.assertAlmostEqual(0.00e00, data.iloc[100, 0])  # line 126 in file)
        self.assertAlmostEqual(-1.20e-04, data.iloc[-1, 0])

    def test_correct_rows_multitrace_detail(self):
        file = self.supported_files_path / "ALL0001_detail.csv"
        data = self.read_file(file)
        # header
        self.assertEqual("s", data.header["xUnit"])
        self.assertEqual("V", data.header["yUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(
            [
                "ALL0001_detail_1",
                "ALL0001_detail_2",
                "ALL0001_detail_3",
                "ALL0001_detail_4",
            ],
            list(data.columns),
        )
        self.assertEqual("Time", data.index.name)

        # data
        self.assertAlmostEqual(-2.500000e-02, data.index[0])
        self.assertAlmostEqual(-2.450000e-02, data.index[100])
        self.assertAlmostEqual(2.499500e-02, data.index[-1])

        self.assertAlmostEqual(0.560000, data.iloc[0, 0])
        self.assertAlmostEqual(-0.002400, data.iloc[0, 1])
        self.assertAlmostEqual(7.600000, data.iloc[0, 2])
        self.assertAlmostEqual(-0.000400, data.iloc[0, 3])

        # line 126 in file
        self.assertAlmostEqual(0.576000, data.iloc[100, 0])
        self.assertAlmostEqual(-0.002080, data.iloc[100, 1])
        self.assertAlmostEqual(7.600000, data.iloc[100, 2])
        self.assertAlmostEqual(-0.000400, data.iloc[100, 3])

        self.assertAlmostEqual(0.568000, data.iloc[-1, 0])
        self.assertAlmostEqual(-0.002320, data.iloc[-1, 1])
        self.assertAlmostEqual(7.600000, data.iloc[-1, 2])
        self.assertAlmostEqual(-0.000400, data.iloc[-1, 3])

    def test_correct_rows_multitrace_fast(self):
        file = self.supported_files_path / "ALL0001_fast.csv"
        data = self.read_file(file)
        # header
        self.assertEqual("s", data.header["xUnit"])
        self.assertEqual("V", data.header["yUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(
            ["ALL0001_fast_1", "ALL0001_fast_2", "ALL0001_fast_3", "ALL0001_fast_4"],
            list(data.columns),
        )
        self.assertEqual("Time", data.index.name)

        # data
        self.assertAlmostEqual(-2.500000e-02, data.index[0])
        self.assertAlmostEqual(-2.450000e-02, data.index[100])
        self.assertAlmostEqual(2.499500e-02, data.index[-1])

        self.assertAlmostEqual(0.560000, data.iloc[0, 0])
        self.assertAlmostEqual(-0.002400, data.iloc[0, 1])
        self.assertAlmostEqual(7.600000, data.iloc[0, 2])
        self.assertAlmostEqual(-0.000400, data.iloc[0, 3])

        # line 126 in file
        self.assertAlmostEqual(0.576000, data.iloc[100, 0])
        self.assertAlmostEqual(-0.002080, data.iloc[100, 1])
        self.assertAlmostEqual(7.600000, data.iloc[100, 2])
        self.assertAlmostEqual(-0.000400, data.iloc[100, 3])

        self.assertAlmostEqual(0.568000, data.iloc[-1, 0])
        self.assertAlmostEqual(-0.002320, data.iloc[-1, 1])
        self.assertAlmostEqual(7.600000, data.iloc[-1, 2])
        self.assertAlmostEqual(-0.000400, data.iloc[-1, 3])
