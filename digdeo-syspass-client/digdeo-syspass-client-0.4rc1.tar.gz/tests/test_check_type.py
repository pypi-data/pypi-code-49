import unittest

from syspassclient.check_type import is_str_or_raise
from syspassclient.check_type import is_int_or_raise
from syspassclient.check_type import is_float_or_raise
from syspassclient.check_type import is_url_or_raise
from syspassclient.check_type import is_dict_or_raise
from syspassclient.check_type import is_list_or_raise
from syspassclient.check_type import is_bool_or_raise
from syspassclient.check_type import is_ascii_or_raise


class TestCheckType(unittest.TestCase):
    def test_is_str_or_raise(self):
        self.assertRaises(TypeError, is_str_or_raise, None)
        self.assertIsNone(is_str_or_raise("Hello"))

    def test_is_int_or_raise(self):
        self.assertRaises(TypeError, is_int_or_raise, None)
        self.assertIsNone(is_int_or_raise(42))

    def test_is_float_or_raise(self):
        self.assertRaises(TypeError, is_float_or_raise, None)
        self.assertIsNone(is_float_or_raise(42.24))

    def test_is_list_or_raise(self):
        self.assertRaises(TypeError, is_list_or_raise, None)
        self.assertIsNone(is_list_or_raise([42, 42]))

    def test_is_dict_or_raise(self):
        self.assertRaises(TypeError, is_dict_or_raise, None)
        self.assertIsNone(is_dict_or_raise({"anwser": 42}))

    def test_is_bool_or_raise(self):
        self.assertRaises(TypeError, is_bool_or_raise, None)
        self.assertIsNone(is_bool_or_raise(True))
        self.assertIsNone(is_bool_or_raise(False))

    def test_is_url_or_raise(self):
        self.assertRaises(TypeError, is_url_or_raise, None)
        self.assertRaises(ValueError, is_url_or_raise, "42")
        self.assertIsNone(is_url_or_raise("http://127.0.0.1"))

    def test_is_ascii_or_raise(self):
        self.assertRaises(TypeError, is_ascii_or_raise, None)
        self.assertRaises(ValueError, is_ascii_or_raise, "\xe2")
        self.assertIsNone(is_ascii_or_raise("coucou"))


if __name__ == "__main__":
    unittest.main()
