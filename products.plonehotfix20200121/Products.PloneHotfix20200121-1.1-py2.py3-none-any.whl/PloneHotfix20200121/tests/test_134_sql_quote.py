# -*- coding: utf-8 -*-
# This tests https://github.com/plone-security/Issues/issues/134
import unittest


class TestAttackVector(unittest.TestCase):
    def test_basic_python(self):
        # You can write some texts in multiple ways in Python.
        # Here we test this, to get a basic understanding for the rest of the tests.
        # Note: you can easily get a SyntaxError, for example: 'Can\\'t' is wrong.
        self.assertEqual(b"Can't", b"Can\'t")
        self.assertEqual(b"Can't", b'Can\'t')
        self.assertEqual(br"Can\'t", b"Can\\'t")
        self.assertEqual(br"Can\ I", b"Can\\ I")
        self.assertEqual(u"Can't", u"Can\'t")
        self.assertEqual(u"Can't", u'Can\'t')
        # The next lines work fine on Python 2, but give a SyntaxError on Python 3.
        # A try/except SyntaxError does not work, because parsing the entire file fails.
        # self.assertEqual(ur"Can\'t", u"Can\\'t")
        # self.assertEqual(ur"Can\ I", u"Can\\ I")

    def test_bytes_sql_quote(self):
        from ..sql_quote import bytes_sql_quote
        self.assertEqual(bytes_sql_quote(b""), b"")
        self.assertEqual(bytes_sql_quote(b"a"), b"a")

        self.assertEqual(bytes_sql_quote(b"Can't"), b"Can''t")
        self.assertEqual(bytes_sql_quote(b"Can\'t"), b"Can''t")
        self.assertEqual(bytes_sql_quote(br"Can\'t"), b"Can\\''t")

        self.assertEqual(bytes_sql_quote(b"Can\\ I?"), b"Can\\ I?")
        self.assertEqual(bytes_sql_quote(br"Can\ I?"), b"Can\\ I?")

        self.assertEqual(
            bytes_sql_quote(b'Just say "Hello"'), b'Just say "Hello"')

        self.assertEqual(
            bytes_sql_quote(b'Hello\x00World'), b'HelloWorld')
        self.assertEqual(
            bytes_sql_quote(b'\x00Hello\x00\x00World\x00'), b'HelloWorld')

        self.assertEqual(
            bytes_sql_quote(b"carriage\rreturn"), b"carriagereturn")
        self.assertEqual(bytes_sql_quote(b"line\nbreak"), b"line\nbreak")
        self.assertEqual(bytes_sql_quote(b"tab\t"), b"tab\t")

    def test_text_sql_quote(self):
        from ..sql_quote import text_sql_quote
        self.assertEqual(text_sql_quote(u""), u"")
        self.assertEqual(text_sql_quote(u"a"), u"a")

        self.assertEqual(text_sql_quote(u"Can't"), u"Can''t")
        self.assertEqual(text_sql_quote(u"Can\'t"), u"Can''t")
        # SyntaxError on Python 3.
        # self.assertEqual(text_sql_quote(ur"Can\'t"), u"Can\\\\''t")

        self.assertEqual(text_sql_quote(u"Can\\ I?"), u"Can\\ I?")
        # SyntaxError on Python 3.
        # self.assertEqual(text_sql_quote(ur"Can\ I?"), u"Can\\\\ I?")

        self.assertEqual(
            text_sql_quote(u'Just say "Hello"'), u'Just say "Hello"')

        self.assertEqual(
            text_sql_quote(u'Hello\x00World'), u'HelloWorld')
        self.assertEqual(
            text_sql_quote(u'\x00Hello\x00\x00World\x00'), u'HelloWorld')

        self.assertEqual(
            text_sql_quote(u"carriage\rreturn"), u"carriagereturn")
        self.assertEqual(text_sql_quote(u"line\nbreak"), u"line\nbreak")
        self.assertEqual(text_sql_quote(u"tab\t"), u"tab\t")

    def test_sql_quote(self):
        from ..sql_quote import dtml_sql_quote
        self.assertEqual(dtml_sql_quote(u""), u"")
        self.assertEqual(dtml_sql_quote(u"a"), u"a")
        self.assertEqual(dtml_sql_quote(b"a"), b"a")

        self.assertEqual(dtml_sql_quote(u"Can't"), u"Can''t")
        self.assertEqual(dtml_sql_quote(u"Can\'t"), u"Can''t")
        # SyntaxError on Python 3.
        # self.assertEqual(dtml_sql_quote(ur"Can\'t"), u"Can\\\\''t")

        self.assertEqual(dtml_sql_quote(u"Can\\ I?"), u"Can\\ I?")
        # SyntaxError on Python 3.
        # self.assertEqual(dtml_sql_quote(ur"Can\ I?"), u"Can\\\\ I?")

        self.assertEqual(
            dtml_sql_quote(u'Just say "Hello"'), u'Just say "Hello"')

        self.assertEqual(
            dtml_sql_quote(u'Hello\x00World'), u'HelloWorld')
        self.assertEqual(
            dtml_sql_quote(u'\x00Hello\x00\x00World\x00'), u'HelloWorld')

        self.assertEqual(
            dtml_sql_quote(u'\x00Hello\x00\x00World\x00'), u'HelloWorld')

        self.assertEqual(u"\xea".encode("utf-8"), b"\xc3\xaa")
        self.assertEqual(dtml_sql_quote(u"\xea'"), u"\xea''")
        self.assertEqual(dtml_sql_quote(b"\xc3\xaa'"), b"\xc3\xaa''")

        self.assertEqual(
            dtml_sql_quote(b"carriage\rreturn"), b"carriagereturn")
        self.assertEqual(
            dtml_sql_quote(u"carriage\rreturn"), u"carriagereturn")
        self.assertEqual(dtml_sql_quote(u"line\nbreak"), u"line\nbreak")
        self.assertEqual(dtml_sql_quote(u"tab\t"), u"tab\t")

    def test_connection_sql_quote(self):
        from ..sql_quote import connection_sql_quote

        conn = object()
        # This is a method, so it needs self (or a mock connection)
        # and it surrounds the result with single quotes.
        self.assertEqual(connection_sql_quote(conn, u""), u"''")
        self.assertEqual(connection_sql_quote(conn, u"a"), u"'a'")
        self.assertEqual(connection_sql_quote(conn, b"a"), b"'a'")

        self.assertEqual(connection_sql_quote(conn, u"Can't"), u"'Can''t'")
        self.assertEqual(connection_sql_quote(conn, u"Can\'t"), u"'Can''t'")
        # SyntaxError on Python 3.
        # self.assertEqual(connection_sql_quote(conn, ur"Can\'t"), u"'Can\\\\''t'")

        self.assertEqual(connection_sql_quote(conn, u"Can\\ I?"), u"'Can\\ I?'")
        # SyntaxError on Python 3.
        # self.assertEqual(connection_sql_quote(conn, ur"Can\ I?"), u"'Can\\ I?'")

        self.assertEqual(connection_sql_quote(conn, u'Just say "Hello"'), u"'Just say \"Hello\"'")
        self.assertEqual(connection_sql_quote(conn, u'Just say "Hello"'), u"""'Just say "Hello"'""")

        self.assertEqual(connection_sql_quote(conn, u'Hello\x00World'), u"'HelloWorld'")
        self.assertEqual(connection_sql_quote(conn, u'\x00Hello\x00\x00World\x00'), u"'HelloWorld'")

        self.assertEqual(connection_sql_quote(conn, u'\x00Hello\x00\x00World\x00'), u"'HelloWorld'")

        self.assertEqual(u"\xea".encode("utf-8"), b"\xc3\xaa")
        self.assertEqual(connection_sql_quote(conn, u"\xea'"), u"'\xea'''")
        self.assertEqual(connection_sql_quote(conn, b"\xc3\xaa'"), b"'\xc3\xaa'''")

    def test_dtml_var_patched(self):
        from ..sql_quote import dtml_sql_quote

        try:
            from DocumentTemplate import DT_Var
        except ImportError:
            return

        self.assertIs(DT_Var.sql_quote, dtml_sql_quote)
        if "sql-quote" in DT_Var.special_formats:
            self.assertIs(DT_Var.special_formats["sql-quote"], dtml_sql_quote)
        for name, function in DT_Var.modifiers:
            if name == "sql_quote":
                self.assertIs(function, dtml_sql_quote)

    def test_python_scripts_patched(self):
        from ..sql_quote import dtml_sql_quote

        try:
            from Products.PythonScripts import standard
        except ImportError:
            return

        self.assertIs(standard.sql_quote, dtml_sql_quote)

    def test_connection_patched(self):
        from ..sql_quote import connection_sql_quote  # noqa

        try:
            from Shared.DC.ZRDB.Connection import Connection
        except ImportError:
            return

        # On Plone 5.1 and lower this gives an AssertionError:
        # <unbound method Connection.connection_sql_quote> is not <function connection_sql_quote at ...>
        # When you initialize a Connection object, it becomes a bound method, so still different.
        # self.assertIs(Connection.sql_quote__, connection_sql_quote)
        self.assertEqual(Connection.sql_quote__.__module__, 'Products.PloneHotfix20200121.sql_quote')
