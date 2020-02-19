import gzip
import unittest
from pathlib import Path

import openqlab.io
from openqlab.io import UndefinedImporter
from openqlab.io.data_container import DataContainer

filedir = Path(__file__).parent


class TestRead(unittest.TestCase):
    """
    Test files starting with a dot (".") will be ignored.
    """

    files_path = filedir / "../test_importers/data_files"
    gzip_files_path = filedir / "gzip_data_files"

    @classmethod
    def setUpClass(cls):
        # todo: remove this when ascii importer is ready
        # cls.ignore_files = list((cls.files_path / 'ASCII').glob('*'))
        cls.ignore_files = [] + list((cls.files_path / "Gwinstek_LSF").glob("*"))

        cls.files = cls.files_path.glob("*/*")
        cls.files = [file for file in cls.files if file not in cls.ignore_files]
        cls.files = [file for file in cls.files if not file.stem.startswith(".")]

        cls.binary_files = [
            filedir / "../test_importers/data_files/KeysightBinary/keysight_binary.bin",
            filedir / "../test_importers/data_files/KeysightBinary/agilent_0.bin",
            filedir / "../test_importers/data_files/KeysightBinary/agilent_1.bin",
            filedir / "../test_importers/data_files/TektronixSpectrogram/test2.mat",
        ]

        cls.ignore_text_files = [
            filedir / "../test_importers/data_files/KeysightFRA/scope_0_comma.csv",
            filedir / "../test_importers/data_files/KeysightFRA/scope_1_semicolon.csv",
        ]
        cls.text_files = [
            file
            for file in cls.files
            if file not in cls.binary_files + cls.ignore_text_files
        ]

        cls.gzip_files = []
        cls.create_gzip_files()

    @classmethod
    def create_gzip_file(cls, file, mode, **kwargs):
        suffix = file.suffix + ".gz"
        gzip_path = cls.gzip_files_path / file.relative_to(cls.files_path).with_suffix(
            suffix
        )
        cls.gzip_files.append(gzip_path)
        gzip_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file, mode=f"r{mode}", **kwargs) as f_in, gzip.open(
            gzip_path, mode=f"w{mode}"
        ) as gzfile:
            if mode == "t":
                gzfile.writelines(f_in.read())
            else:
                gzfile.writelines(f_in)

    @classmethod
    def create_gzip_files(cls):

        for file in cls.text_files:
            cls.create_gzip_file(file, mode="t")

        for file in cls.binary_files:
            cls.create_gzip_file(file, mode="b")

    def read_file(self, file):
        try:
            # print(f"\nTesting file: {file}")
            data = openqlab.io.read(file)
            self.assertTrue(isinstance(data, DataContainer) and not data.empty)
            self.assertTrue(data._is_numeric_mixed_type)
            for column in data.columns:
                self.assertFalse(data[column].isna().values.all())
            return data
        except Exception as e:
            raise type(e)(f'"{file}" raised Exception: {e}') from e

    def test_specified_importer(self):
        data = openqlab.io.read(
            self.files_path / "RhodeSchwarz/2010830P_001", importer="RhodeSchwarz"
        )
        self.assertTrue(isinstance(data, DataContainer) and not data.empty)
        self.assertTrue(data._is_numeric_mixed_type)
        for column in data.columns:
            self.assertFalse(data[column].isna().values.all())

    def test_as_list(self):
        files = [
            self.files_path / filename
            for filename in ["RhodeSchwarz/2010830P_001", "RhodeSchwarz/2010830P_002"]
        ]
        data = openqlab.io.read(files, as_list=True)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 2)
        for entry in data:
            self.assertTrue(isinstance(entry, DataContainer))

    def test_append(self):
        files = [
            self.files_path / filename
            for filename in ["RhodeSchwarz/2010830P_001", "RhodeSchwarz/2010830P_002"]
        ]
        data = openqlab.io.read(files, append=True)
        self.assertTrue(isinstance(data, DataContainer) and not data.empty)
        self.assertTrue(data._is_numeric_mixed_type)
        for column in data.columns:
            self.assertFalse(data[column].isna().values.all())

    def test_empty_file(self):
        with self.assertRaises(UndefinedImporter):
            print(openqlab.io.read(filedir / "empty_file.csv"))

    def test_unknown_file(self):
        with self.assertRaises(UndefinedImporter):
            print(openqlab.io.read(filedir / "unknown_file.csv"))

    def test_path_objects(self):
        for file in self.files:
            self.read_file(Path(file))

    def test_str_objects(self):
        for file in self.files:
            self.read_file(file)

    def test_TextIO_objects(self):
        for file in self.text_files:
            with open(file, mode="r") as f:
                self.read_file(f)

    def test_BinaryIO_objects(self):
        for file in self.binary_files:
            with open(file, mode="rb") as f:
                self.read_file(f)

    def test_gzip_objects(self):
        for file in self.gzip_files:
            self.read_file(file)

    def test_read_list_of_files(self):
        self.read_file(self.files[::4])


class TestDeprecations(unittest.TestCase):
    def test_deprecated_type_argument(self):
        with self.assertWarns(DeprecationWarning):
            try:
                openqlab.io.read("", type="TestType")
            except Exception:
                pass

    @unittest.expectedFailure
    def test_deprecated_type_argument_not_used(self):
        with self.assertWarns(DeprecationWarning):
            try:
                openqlab.io.read("")
            except Exception:
                pass
