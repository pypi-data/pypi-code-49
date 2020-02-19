import os
import unittest
from pathlib import Path

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.rhode_schwarz import RhodeSchwarz
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent


class TestRhodeSchwarz(unittest.TestCase):
    importer = RhodeSchwarz
    files_path = filedir / "../data_files"
    supported_files_path = files_path / "RhodeSchwarz"

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

    def test_missing_xUnit(self):
        file = filedir / "missing_xUnit.csv"
        data = self.read_file(file)
        self.assertEqual("x", data.index.name)

    def test_different_xUnit(self):
        file = filedir / "different_xUnit.csv"
        data = self.read_file(file)
        self.assertEqual("x", data.index.name)

    def test_correct_rows_singletrace(self):
        file = self.supported_files_path / "2010830P_001"
        data = self.read_file(file)

        # header
        self.assertEqual(327458.875000, data.header["CenterFrequency"])
        self.assertEqual("Hz", data.header["CenterFrequency-unit"])
        self.assertEqual(-25, data.header["Ref Level"])
        self.assertEqual("dBm", data.header["Ref Level-unit"])
        self.assertEqual("dBm", data.header["yUnit"])
        self.assertEqual("Hz", data.header["xUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(
            ["2010830P_001_1"], list(data.columns)
        )  # todo: remove the _1 for single trace
        self.assertEqual("Frequency", data.index.name)

        # data
        self.assertEqual(326958.875, data.index[0])
        self.assertEqual(327958.875, data.index[-1])
        self.assertEqual(326971.375, data.index[100])

        self.assertAlmostEqual(-105.30112457275391, data.iloc[0, 0])
        self.assertAlmostEqual(-104.64633178710937, data.iloc[-1, 0])
        self.assertAlmostEqual(-105.49134063720703, data.iloc[100, 0])

    def test_correct_rows_multitrace(self):
        file = self.supported_files_path / "FSV-4_multitrace_comma.DAT"
        data = self.read_file(file)
        # header
        self.assertEqual("FSV-4", data.header["Type"])
        self.assertEqual("3.40", data.header["Version"])
        self.assertEqual(800000.0, data.header["CenterFrequency"])
        self.assertEqual("Hz", data.header["CenterFrequency-unit"])
        self.assertEqual(-101.500000, data.header["Ref Level"])
        self.assertEqual("dBm", data.header["Ref Level-unit"])
        self.assertEqual("dBm", data.header["yUnit"])
        self.assertEqual("Hz", data.header["xUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(3, len(data.columns))
        self.assertEqual(
            [
                "FSV-4_multitrace_comma_1",
                "FSV-4_multitrace_comma_2",
                "FSV-4_multitrace_comma_3",
            ],
            list(data.columns),
        )
        self.assertEqual("Frequency", data.index.name)

        # data
        self.assertEqual(32001, len(data))

        self.assertEqual(300000, data.index[0])
        self.assertEqual(1300000, data.index[-1])
        self.assertEqual(303125, data.index[100])

        self.assertAlmostEqual(-136.19355773925781, data.iloc[0, 0])
        self.assertAlmostEqual(-139.02806091308594, data.iloc[-1, 0])
        self.assertAlmostEqual(-139.59083557128906, data.iloc[100, 0])

        self.assertAlmostEqual(-136.19355773925781, data.iloc[0, 1])
        self.assertAlmostEqual(-139.02806091308594, data.iloc[-1, 1])
        self.assertAlmostEqual(-139.59083557128906, data.iloc[100, 1])

        self.assertAlmostEqual(-135.19355773925781, data.iloc[0, 2])
        self.assertAlmostEqual(-138.02806091308594, data.iloc[-1, 2])
        self.assertAlmostEqual(-138.59083557128906, data.iloc[100, 2])
