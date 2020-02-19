import platform
import unittest
from pathlib import Path

from openqlab.io.importers.keysight_visa import KeysightVisa
from openqlab.io.importers.utils import ImportFailed, UnknownFileType

from .mock_visa import MockVisa

filedir = Path(__file__).parent


class TestKeysightVisa(unittest.TestCase):
    def setUp(self):
        mock = MockVisa()
        self.importer = KeysightVisa("TCPIP::mockaddress", inst=mock)

    def test_idn(self):
        self.assertEqual(
            self.importer.idn,
            "KEYSIGHT TECHNOLOGIES,DSO-X 3024T,MY57452230,07.30.2019051434",
        )

    def test_read_data(self):
        self.importer._inst.channels_enabled = ["1"] * 4
        dc = self.importer.read()
        self.assertEqual(len(dc.columns), 4)
        self.assertEqual(dc.index.name, "Time")

    def test_index(self):
        self.importer._inst.channels_enabled = ["1"] * 4
        dc = self.importer.read()
        self.assertAlmostEqual(dc.index[5], 0)

    def test_missing_data(self):
        self.importer._inst.channels_enabled[0] = "1"
        self.importer._inst.channel_data["channel1"] = ""
        with self.assertRaises(ImportFailed):
            dc = self.importer.read()

    def test_wrong_data(self):
        self.importer._inst.channels_enabled[0] = "1"
        self.importer._inst.channel_data["channel1"] = "031243"
        with self.assertRaises(ImportFailed):
            dc = self.importer.read()

    def test_without_active_trace(self):
        with self.assertRaises(ImportFailed):
            dc = self.importer.read()

    def test_no_number_on_second_place(self):
        self.importer._inst.channels_enabled[1] = "1"
        self.importer._inst.channel_data["channel2"] = "#x3284023"
        with self.assertRaises(ImportFailed):
            dc = self.importer.read()

    def test_clipped_data(self):
        self.importer._inst.channels_enabled[0] = "1"
        self.importer._inst.channel_data[
            "channel1"
        ] = "#800000140 1.35683e-002,-1.19603e-002,-3.11608e-003, 6.33216e-003, 9.14623e-003, 7.13618e-003, 1.03523e-002, 3.11608e-003, 5.93015e-003, 1.19603e-002"
        with self.assertRaises(ImportFailed):
            dc = self.importer.read()

    def test_data_values(self):
        self.importer._inst.channels_enabled = ["1"] * 4
        dc = self.importer.read()
        print(dc)
        self.assertEqual(dc[1].iloc[0], 1.35683e-2)
        self.assertEqual(dc[2].iloc[0], 2.35683e-2)
        self.assertEqual(dc[3].iloc[0], 3.35683e-2)
        self.assertEqual(dc[4].iloc[0], 4.35683e-2)

        self.assertEqual(dc[1].iloc[1], -1.19603e-2)
        self.assertEqual(dc[2].iloc[1], -2.19603e-2)
        self.assertEqual(dc[3].iloc[1], -3.19603e-2)
        self.assertEqual(dc[4].iloc[1], -4.19603e-2)

        self.assertEqual(dc[1].iloc[-1], 1.19603e-2)
        self.assertEqual(dc[2].iloc[-1], 2.19603e-2)
        self.assertEqual(dc[3].iloc[-1], 3.19603e-2)
        self.assertEqual(dc[4].iloc[-1], 4.19603e-2)

    @unittest.skipIf(
        platform.system() == "Windows", "Windows throws Error that you cannot import"
    )
    def test_open_real_resource(self):
        with self.assertRaises((ConnectionRefusedError, BrokenPipeError)):
            self.importer = KeysightVisa("TCPIP::localhost::INSTR")

    def test_wrong_device_idn(self):
        mock = MockVisa()
        importer = KeysightVisa("TCPIP::mockaddress", inst=mock)
        importer._inst.idn = "Something wrong"
        with self.assertRaises(UnknownFileType):
            importer._check_connection()
