import unittest
from pathlib import Path

from openqlab import io
from openqlab.io.data_container import DataContainer

filedir = Path(__file__).parent


class TestReads(unittest.TestCase):
    """
    Test files starting with a dot (".") will be ignored.
    """

    files_path = filedir / "../test_importers/data_files"

    @classmethod
    def setUpClass(cls):
        cls.ignore_files = []

        cls.files = cls.files_path.glob("*/*")
        cls.files = [file for file in cls.files if file not in cls.ignore_files]
        cls.files = [file for file in cls.files if not file.stem.startswith(".")]

        cls.binary_files = [
            filedir / "../test_importers/data_files/KeysightBinary/keysight_binary.bin",
            filedir / "../test_importers/data_files/KeysightBinary/agilent_0.bin",
            filedir / "../test_importers/data_files/KeysightBinary/agilent_1.bin",
            filedir / "../test_importers/data_files/TektronixSpectrogram/test2.mat",
        ] + list((cls.files_path / "Gwinstek_LSF").glob("*"))

        cls.ignore_text_files = [
            filedir / "../test_importers/data_files/KeysightFRA/scope_0_comma.csv",
            filedir / "../test_importers/data_files/KeysightFRA/scope_1_semicolon.csv",
        ]
        cls.text_files = [
            file
            for file in cls.files
            if file not in cls.binary_files + cls.ignore_text_files
        ]

    def read_file(self, file):
        try:
            data = io.reads(file)
            self.assertTrue(isinstance(data, DataContainer) and not data.empty)
            self.assertTrue(data._is_numeric_mixed_type)
            for column in data.columns:
                self.assertFalse(data[column].isna().values.all())
            return data
        except Exception as e:
            raise type(e)(f'"{file}" raised Exception: {e}') from e

    def test_reads_text_files(self):
        for file in self.text_files:
            with open(file, mode="rt") as f:
                self.read_file(f.read())

    @unittest.skip("not yet implemented")
    def test_read_list_of_files(self):
        l = []
        for file in self.text_files[:5]:
            with open(file, mode="rt") as f:
                l.append(f.read())
        self.read_file(self.files)

    def test_correct_rows_singletrace(self):
        file = self.files_path / "RhodeSchwarz/2010830P_001"
        with open(file) as f:
            data = self.read_file(f.read())

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
            ["StringIO_1"], list(data.columns)
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
        from openqlab.io.importers.rhode_schwarz import RhodeSchwarz

        file = self.files_path / "RhodeSchwarz/FSV-4_multitrace_comma.DAT"
        with open(file) as f:
            data = self.read_file(f.read())
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
        self.assertEqual(["StringIO_1", "StringIO_2", "StringIO_3"], list(data.columns))
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
