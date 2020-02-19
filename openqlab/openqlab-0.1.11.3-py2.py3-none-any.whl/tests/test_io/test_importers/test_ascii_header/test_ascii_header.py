import logging
import re
import unittest
from pathlib import Path

from openqlab.io.data_container import DataContainer
from openqlab.io.importers.ascii_header import ASCII_Header
from openqlab.io.importers.utils import UnknownFileType

filedir = Path(__file__).parent
datadir = filedir / "../data_files"

logger = logging.getLogger(__name__)
logger.getChild("ascii_header")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filedir / f"{__name__}.log", mode="w")

logger.addHandler(file_handler)
# logger.addHandler(logging.StreamHandler())


class TestASCII_Header(unittest.TestCase):
    importer = ASCII_Header
    files_path = datadir
    supported_files_path = datadir / "ASCII_Header"
    multiline_comment = re.compile(
        "This is a multiline comment.\s+It continues at the next line.\s+And another line\s+with newline."
    )

    def read_file(self, file):
        logger.info(f"\n{file}")
        try:
            data = self.importer(file).read()
            self.assertTrue(isinstance(data, DataContainer))
            self.assertFalse(data.empty)
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

    @unittest.skip("Importer cannot recognize unsupported files")
    def test_unsupported_files(self):
        for file in self.unsupported_files:
            try:
                with self.assertRaises(UnknownFileType):
                    self.read_file(file)
            except AssertionError as e:
                raise AssertionError(f"{file} did not raise {UnknownFileType}") from e

    def test_correct_rows_singletrace_header_hashtag(self):
        file = self.supported_files_path / "header_#.csv"
        data = self.read_file(file)

        # header
        self.assertEqual("5 V", data.header["voltage"])
        self.assertEqual("6 m/s", data.header["speed"])
        self.assertEqual("7", data.header["septab"])
        self.assertTrue(self.multiline_comment.match(data.header["comment"]))
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["values"], list(data.columns))
        self.assertEqual("time", data.index.name)

        # data
        self.assertAlmostEqual(+1.280000e002, data.index[0])
        self.assertAlmostEqual(+2.560000e002, data.index[1])
        self.assertAlmostEqual(+1.408000e003, data.index[10])  # line 19 in file
        self.assertAlmostEqual(+2.560000e003, data.index[-1])

        self.assertAlmostEqual(-4.078996e001, data.iloc[0, 0])
        self.assertAlmostEqual(-5.155923e001, data.iloc[1, 0])
        self.assertAlmostEqual(-7.461130e001, data.iloc[10, 0])  # line 19 in file)
        self.assertAlmostEqual(-7.951345e001, data.iloc[-1, 0])

    def test_correct_rows_singletrace_header_hashtag_comma(self):
        file = self.supported_files_path / "header_#_comma.csv"
        data = self.read_file(file)

        # header
        self.assertEqual("5 V", data.header["voltage"])
        self.assertEqual("6 m/s", data.header["speed"])
        self.assertEqual("7", data.header["septab"])
        self.assertTrue(self.multiline_comment.match(data.header["comment"]))
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["values"], list(data.columns))
        self.assertEqual("time", data.index.name)

        # data
        self.assertAlmostEqual(+1.280000e002, data.index[0])
        self.assertAlmostEqual(+2.560000e002, data.index[1])
        self.assertAlmostEqual(+1.408000e003, data.index[10])  # line 19 in file
        self.assertAlmostEqual(+2.560000e003, data.index[-1])

        self.assertAlmostEqual(-4.078996e001, data.iloc[0, 0])
        self.assertAlmostEqual(-5.155923e001, data.iloc[1, 0])
        self.assertAlmostEqual(-7.461130e001, data.iloc[10, 0])  # line 19 in file)
        self.assertAlmostEqual(-7.951345e001, data.iloc[-1, 0])

    def test_correct_rows_singletrace_header_dollar(self):
        file = self.supported_files_path / "header_$.csv"
        data = self.read_file(file)

        # header
        self.assertEqual("5 V", data.header["voltage"])
        self.assertEqual("6 m/s", data.header["speed"])
        self.assertEqual("7", data.header["septab"])
        self.assertTrue(self.multiline_comment.match(data.header["comment"]))
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["values"], list(data.columns))
        self.assertEqual("time", data.index.name)

        # data
        self.assertAlmostEqual(+1.280000e002, data.index[0])
        self.assertAlmostEqual(+2.560000e002, data.index[1])
        self.assertAlmostEqual(+1.408000e003, data.index[10])  # line 19 in file
        self.assertAlmostEqual(+2.560000e003, data.index[-1])

        self.assertAlmostEqual(-4.078996e001, data.iloc[0, 0])
        self.assertAlmostEqual(-5.155923e001, data.iloc[1, 0])
        self.assertAlmostEqual(-7.461130e001, data.iloc[10, 0])  # line 19 in file)
        self.assertAlmostEqual(-7.951345e001, data.iloc[-1, 0])

    def test_correct_rows_singletrace_header_percent(self):
        file = self.supported_files_path / "header_%.csv"
        data = self.read_file(file)

        # header
        self.assertEqual("5 V", data.header["voltage"])
        self.assertEqual("6 m/s", data.header["speed"])
        self.assertEqual("7", data.header["septab"])
        self.assertTrue(self.multiline_comment.match(data.header["comment"]))
        self.assertNotIn("Detector-unit", data.header)

        # columns and index
        self.assertEqual(["values"], list(data.columns))
        self.assertEqual("time", data.index.name)

        # data
        self.assertAlmostEqual(+1.280000e002, data.index[0])
        self.assertAlmostEqual(+2.560000e002, data.index[1])
        self.assertAlmostEqual(+1.408000e003, data.index[10])  # line 19 in file
        self.assertAlmostEqual(+2.560000e003, data.index[-1])

        self.assertAlmostEqual(-4.078996e001, data.iloc[0, 0])
        self.assertAlmostEqual(-5.155923e001, data.iloc[1, 0])
        self.assertAlmostEqual(-7.461130e001, data.iloc[10, 0])  # line 19 in file)
        self.assertAlmostEqual(-7.951345e001, data.iloc[-1, 0])
