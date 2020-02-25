#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from syspassclient.constants import dd
from syspassclient.constants import Constants


class TestConstants(unittest.TestCase):
    def test_Constants_set(self):
        """Test Constants set"""
        const = Constants()
        const.hello = 42
        self.assertEqual(const.hello, 42)
        self.assertRaises(Constants.ConstError, const.__setattr__, "hello", 42)

    def test_Constants_get(self):
        """Test Constants get"""
        const = Constants()
        const.hello = 42
        self.assertEqual(const.__getattr__("hello"), 42)
        self.assertRaises(Constants.ConstError, const.__getattr__, "im_not")

    def test_whitespace(self):
        # whitespace -- a string containing all ASCII whitespace
        self.assertEqual(dd.__getattr__("whitespace"), " \t\n\r\v\f")

    def test_ascii_lowercase(self):
        # ascii_lowercase -- a string containing all ASCII lowercase letters
        self.assertEqual(dd.__getattr__("ascii_lowercase"), "abcdefghijklmnopqrstuvwxyz")

    def test_ascii_uppercase(self):
        # ascii_uppercase -- a string containing all ASCII uppercase letters
        self.assertEqual(dd.__getattr__("ascii_uppercase"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_ascii_letters(self):
        # ascii_letters -- a string containing all ASCII letters
        self.assertEqual(dd.__getattr__("ascii_letters"), "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_digits(self):
        # digits -- a string containing all ASCII decimal digits
        self.assertEqual(dd.__getattr__("digits"), "0123456789")

    def test_hexdigits(self):
        # hexdigits -- a string containing all ASCII hexadecimal digits
        self.assertEqual(dd.__getattr__("hexdigits"), "0123456789" + "abcdef" + "ABCDEF")

    def test_octdigits(self):
        # octdigits -- a string containing all ASCII octal digits
        self.assertEqual(dd.__getattr__("octdigits"), "01234567")

    def test_punctuation(self):
        # punctuation -- a string containing all ASCII punctuation characters
        self.assertEqual(dd.__getattr__("punctuation"), "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    def test_accent(self):
        # accent
        self.assertEqual(dd.__getattr__("accent"), "éèàùô")

    def test_api_version(self):
        self.assertEqual("3.1", dd.syspass["api"]["version"])

    def test_api_3_0_valid_methods(self):
        method_3_0_valid = [
            "account/search",
            "account/view",
            "account/viewPass",
            "account/editPass",
            "account/create",
            "account/edit",
            "account/delete",
            "category/search",
            "category/view",
            "category/create",
            "category/edit",
            "category/delete",
            "client/search",
            "client/view",
            "client/create",
            "client/edit",
            "client/delete",
            "tag/search",
            "tag/view",
            "tag/create",
            "tag/edit",
            "tag/delete",
            "usergroup/search",
            "usergroup/view",
            "usergroup/create",
            "usergroup/edit",
            "usergroup/delete",
            "config/backup",
            "config/export",
        ]
        for method in method_3_0_valid:
            self.assertTrue(method in dd.syspass["api"]["3.0"]["methods"])

    def test_api_3_1_valid_methods(self):
        method_3_1_valid = [
            "account/search",
            "account/view",
            "account/viewPass",
            "account/editPass",
            "account/create",
            "account/edit",
            "account/delete",
            "category/search",
            "category/view",
            "category/create",
            "category/edit",
            "category/delete",
            "client/search",
            "client/view",
            "client/create",
            "client/edit",
            "client/delete",
            "tag/search",
            "tag/view",
            "tag/create",
            "tag/edit",
            "tag/delete",
            "userGroup/search",
            "userGroup/view",
            "userGroup/create",
            "userGroup/edit",
            "userGroup/delete",
            "config/backup",
            "config/export",
        ]
        for method in method_3_1_valid:
            self.assertTrue(method in dd.syspass["api"]["3.1"]["methods"])


if __name__ == "__main__":
    unittest.main()
