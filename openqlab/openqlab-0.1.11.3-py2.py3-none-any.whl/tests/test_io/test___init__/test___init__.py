import sys
import unittest
from io import StringIO
from pathlib import Path

from openqlab import io
from openqlab.io.base_importer import BaseImporter

filedir = Path(__file__).parent


class TestInit(unittest.TestCase):
    expected_auto_importers = {
        "DataContainerCSV",
        "Gwinstek",
        "Gwinstek_LSF",
        "HP4395A",
        "KeysightBinary",
        "KeysightCSV",
        "KeysightFrequencyResponse",
        "KeysightVisa",
        "RhodeSchwarz",
        "Tektronix",
        "TektronixDPX",
        "TektronixSpectrogram",
    }
    expected_importers = {"ASCII", "ASCII_Header", "HP4395A_GPIB",}.union(
        expected_auto_importers
    )

    def test_expected_importers(self):
        self.assertEqual(self.expected_importers, set(BaseImporter.importers().keys()))

    def test_expected_auto_importers(self):
        self.assertEqual(
            self.expected_auto_importers, set(BaseImporter.auto_importers().keys())
        )

    def test_list_formats(self):
        captured_output = StringIO()  # Create StringIO object
        sys.stdout = captured_output

        io.list_formats()

        for f in self.expected_importers:
            self.assertIn(f, captured_output.getvalue())
