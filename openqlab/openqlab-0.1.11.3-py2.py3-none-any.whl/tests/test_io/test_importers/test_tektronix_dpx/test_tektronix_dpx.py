import os
import unittest
from pathlib import Path

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.tektronix_dpx import TektronixDPX
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent


class TestTektronix(unittest.TestCase):
    importer = TektronixDPX
    files_path = filedir / "../data_files"
    supported_files_path = Path(fr"{files_path}/TektronixDPX")

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

    # def test_correct_rows_singletrace(self):
    #     file = self.supported_files_path / 'cable_resonance_115_singletrace.csv'
    #     data = self.read_file(file)
    #
    #     # header
    #     self.assertEqual(110992136.491227, data.header['CenterFrequency'])
    #     self.assertEqual('Hz', data.header['CenterFrequency-unit'])
    #     self.assertEqual(0, data.header['Reference Level'])
    #     # self.assertEqual('dBm', data.header['Reference Level-unit'])
    #     self.assertEqual('dBm', data.header['yUnit'])
    #     self.assertEqual('Hz', data.header['xUnit'], )
    #     self.assertNotIn('Detector-unit', data.header)
    #
    #     # columns and index
    #     self.assertEqual(['cable_resonance_115_singletrace_1'],
    #                      list(data.columns))  # todo: remove the _1 for single trace
    #     self.assertEqual('Frequency', data.index.name)
    #
    #     # data
    #     self.assertEqual(103204128.991227, data.index[0])
    #     self.assertEqual(118780143.991227, data.index[-1])
    #     self.assertEqual(103208022.994977, data.index[1])
    #
    #     self.assertAlmostEqual(-93.08514404296875, data.iloc[0, 0])
    #     self.assertAlmostEqual(-93.164268493652344, data.iloc[-1, 0])
    #     self.assertAlmostEqual(-93.1149673461914, data.iloc[1, 0])

    def test_correct_rows_multitrace(self):
        """Testing multiple traces from one file for Zero Span (DPX) measurement
        Reads data from TektronixDPX test data file '001.csv' and compares
        with known hard coded values for that file"""
        file = self.supported_files_path / "0001.csv"
        data = self.read_file(file)
        # header
        self.assertEqual(4500000, data.header["Span"])
        self.assertEqual(5020000, data.header["CenterFrequency"])
        self.assertEqual("Hz", data.header["CenterFrequency-unit"])
        self.assertEqual(300000, data.header["RBW"])
        # self.assertEqual('dBm', data.header['Ref Level-unit'])
        self.assertEqual("dBm", data.header["yUnit"])
        self.assertEqual("s", data.header["xUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["0001_1", "0001_2", "0001_3"], list(data.columns))
        self.assertEqual("Time", data.index.name)

        # data
        self.assertEqual(0.0, data.index[0])
        self.assertEqual(0.3, data.index[-1])
        self.assertEqual(0.000375, data.index[1])

        self.assertAlmostEqual(-71.087905883789063, data.iloc[0, 0])
        self.assertAlmostEqual(-71.548393249511719, data.iloc[-1, 0])
        self.assertAlmostEqual(-71.473007202148438, data.iloc[1, 0])
        self.assertAlmostEqual(-71.329536437988281, data.iloc[100, 0])

        self.assertAlmostEqual(-63.104297637939453, data.iloc[0, 1])
        self.assertAlmostEqual(-63.046291351318359, data.iloc[-1, 1])
        self.assertAlmostEqual(-63.600967407226563, data.iloc[1, 1])
        self.assertAlmostEqual(-62.926795959472656, data.iloc[345, 1])

        self.assertAlmostEqual(-57.607028961181641, data.iloc[0, 2])
        self.assertAlmostEqual(-65.948104858398438, data.iloc[-1, 2])
        self.assertAlmostEqual(-57.945648193359375, data.iloc[1, 2])
        self.assertAlmostEqual(-50.219039916992188, data.iloc[540, 2])
