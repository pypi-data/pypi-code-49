import os
import unittest
import xml.etree.ElementTree as ET
from io import StringIO
from pathlib import Path

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.tektronix_spectrogram import TektronixSpectrogram
from openqlab.io.importers.utils import UnknownFileType

filedir = Path(__file__).parent


class TestTekSpectrogram(unittest.TestCase):
    importer = TektronixSpectrogram
    files_path = filedir / "../data_files"
    supported_files_path = files_path / "TektronixSpectrogram"

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

    def test_missing_required_key(self):
        file = filedir / "missing_required_keys.mat"
        with self.assertRaises(UnknownFileType):
            self.read_file(file)

    def test_correct_rows_multitrace(self):
        file = self.supported_files_path / "test2.mat"
        data = self.read_file(file)
        # header
        self.assertEqual(12525000.0, data.header["CenterFrequency"])
        self.assertEqual(50000.0, data.header["StartFrequency"])
        self.assertEqual(25000000.0, data.header["StopFrequency"])
        self.assertEqual(24950000.0, data.header["Span"])
        self.assertEqual(10000.0, data.header["RBW"])
        self.assertEqual(0.0049152, data.header["DeltaT"])
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual([50000.0, 81187.5, 112375.0], list(data.columns[0:3]))
        self.assertEqual("Frequency (Hz)", data.columns.name)
        self.assertEqual("Time (s)", data.index.name)

        # data
        self.assertEqual(0, data.index[0])
        self.assertAlmostEqual(0.811008, data.index[-1])
        self.assertAlmostEqual(0.009830, data.index[2], places=6)

        self.assertAlmostEqual(-82.080, data.iloc[0, 0], places=4)
        self.assertAlmostEqual(-82.880, data.iloc[0, 1], places=4)
        self.assertAlmostEqual(-87.470, data.iloc[0, -2], places=4)
        self.assertAlmostEqual(-87.830, data.iloc[0, -1], places=4)

        self.assertAlmostEqual(-82.510, data.iloc[1, 0], places=4)
        self.assertAlmostEqual(-83.110, data.iloc[1, 1], places=4)
        self.assertAlmostEqual(-88.420, data.iloc[1, -2], places=4)
        self.assertAlmostEqual(-87.660, data.iloc[1, -1], places=4)

        self.assertAlmostEqual(-81.840, data.iloc[-1, 0], places=4)
        self.assertAlmostEqual(-82.790, data.iloc[-1, 1], places=4)
        self.assertAlmostEqual(-87.970, data.iloc[-1, -2], places=4)
        self.assertAlmostEqual(-87.840, data.iloc[-1, -1], places=4)

        self.assertAlmostEqual(-81.780, data.iloc[16, 0], places=4)
        self.assertAlmostEqual(-83.220, data.iloc[16, 1], places=4)
        self.assertAlmostEqual(-87.400, data.iloc[16, -2], places=4)
        self.assertAlmostEqual(-87.520, data.iloc[16, -1], places=4)

    def test_get_xml_text_default(self):
        xml_data = """<?xml version="1.0"?>
        <data>
             <titel>Wikipedia Städteverzeichnis</titel>
        </data>
		"""
        it = ET.iterparse(StringIO(xml_data))
        for _ in it:
            pass
        root = it.root
        print(root)
        self.assertIsNone(self.importer._get_xml_text(root, "notexisting"))
        self.assertEqual(self.importer._get_xml_text(root, "notexisting", 84), 84)
        self.assertEqual(
            self.importer._get_xml_text(root, "titel"), "Wikipedia Städteverzeichnis"
        )
