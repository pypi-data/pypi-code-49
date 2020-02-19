import os
import re
import unittest
from pathlib import Path

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.tektronix import Tektronix
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

filedir = Path(__file__).parent


class TestTektronix(unittest.TestCase):
    importer = Tektronix
    files_path = filedir / "../data_files"
    supported_files_path = files_path / "Tektronix"

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
        with self.assertRaises(ImportFailed):
            data = self.importer(file).read()

    def test_wrong_number_points(self):
        file = filedir / "wrong_number_points.csv"
        error_message = (
            f"'Tektronix' importer: Number of points does not fit number of "
            f"values in file '{file}'.".replace("\\", "\\\\")
        )
        with self.assertRaisesRegex(ImportFailed, error_message):
            self.importer(file).read()

    def test_different_frequency_axis(self):
        file = filedir / "different_frequency_axis.csv"
        error_message = (
            f"'Tektronix' importer: Traces in file '{file}' do "
            f"not have equal frequency axis.".replace("\\", "\\\\")
        )
        with self.assertRaisesRegex(ImportFailed, error_message):
            self.importer(file).read()

    def test_correct_rows_singletrace(self):
        file = self.supported_files_path / "cable_resonance_115_singletrace.csv"
        data = self.read_file(file)

        # header
        self.assertEqual(110992136.491227, data.header["CenterFrequency"])
        self.assertEqual("Hz", data.header["CenterFrequency-unit"])
        self.assertEqual(0, data.header["Reference Level"])
        # self.assertEqual('dBm', data.header['Reference Level-unit'])
        self.assertEqual("dBm", data.header["yUnit"])
        self.assertEqual("Hz", data.header["xUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(
            ["cable_resonance_115_singletrace_1"], list(data.columns)
        )  # todo: remove the _1 for single trace
        self.assertEqual("Frequency", data.index.name)

        # data
        self.assertEqual(103204128.991227, data.index[0])
        self.assertEqual(118780143.991227, data.index[-1])
        self.assertEqual(103208022.994977, data.index[1])

        self.assertAlmostEqual(-93.08514404296875, data.iloc[0, 0])
        self.assertAlmostEqual(-93.164268493652344, data.iloc[-1, 0])
        self.assertAlmostEqual(-93.1149673461914, data.iloc[1, 0])

    def test_correct_rows_multitrace(self):
        file = self.supported_files_path / "30003_multitrace.csv"
        data = self.read_file(file)
        # header
        self.assertEqual(132865, data.header["CenterFrequency"])
        self.assertEqual("Hz", data.header["CenterFrequency-unit"])
        # self.assertEqual(-101.500000, data.header['Ref Level'])
        # self.assertEqual('dBm', data.header['Ref Level-unit'])
        self.assertEqual("dBm", data.header["yUnit"])
        self.assertEqual("Hz", data.header["xUnit"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(
            ["30003_multitrace_1", "30003_multitrace_2", "30003_multitrace_3"],
            list(data.columns),
        )
        self.assertEqual("Frequency", data.index.name)

        # data
        self.assertEqual(132665, data.index[0])
        self.assertEqual(133065, data.index[-1])
        self.assertEqual(132665.025, data.index[1])

        self.assertAlmostEqual(-123.01148986816406, data.iloc[0, 0])
        self.assertAlmostEqual(-122.67952728271484, data.iloc[-1, 0])
        self.assertAlmostEqual(-122.88975524902344, data.iloc[1, 0])

        self.assertAlmostEqual(-86.617645263671875, data.iloc[0, 1])
        self.assertAlmostEqual(-88.9977035522461, data.iloc[-1, 1])
        self.assertAlmostEqual(-86.640922546386719, data.iloc[1, 1])

        self.assertAlmostEqual(-93.083061218261719, data.iloc[0, 2])
        self.assertAlmostEqual(-90.4854736328125, data.iloc[-1, 2])
        self.assertAlmostEqual(-93.077568054199219, data.iloc[1, 2])
