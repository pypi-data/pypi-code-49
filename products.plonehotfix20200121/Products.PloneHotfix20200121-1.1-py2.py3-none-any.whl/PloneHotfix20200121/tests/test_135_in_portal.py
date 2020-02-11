# -*- coding: utf-8 -*-
# This tests https://github.com/plone-security/Issues/issues/135
from Products.PloneHotfix20200121.tests import BaseTest

# Python 2 has chr    which works in range(256) and returns string (bytes).
# Python 2 has unichr which works in range(0x10ffff) and returns unicode.
# Python 3 has chr    which works in range(0x10ffff) and returns unicode (string).
# When out of range, you get a ValueError.
try:
    # Python2 has chr, but only works below 256
    makechar = unichr
except NameError:
    # Python 3
    makechar = chr


class TestAttackVector(BaseTest):
    def test_escape(self):
        url_tool = self.portal.portal_url
        iURLiP = url_tool.isURLInPortal
        # For a few of these, pylint complains about an anomalous backslash
        # and says "string constant may be missing an r prefix".
        # Let's try both with and without the r prefix.
        # And let's try bytes and unicode while we are at it.
        self.assertFalse(iURLiP(b"\/\/www.example.com"))
        self.assertFalse(iURLiP(r"\/\/www.example.com"))
        self.assertFalse(iURLiP(u"\/\/www.example.com"))
        self.assertFalse(iURLiP(b"\%2F\%2Fwww.example.com"))
        self.assertFalse(iURLiP(r"\%2F\%2Fwww.example.com"))
        self.assertFalse(iURLiP(u"\%2F\%2Fwww.example.com"))
        self.assertFalse(iURLiP(b"\%2f\%2fwww.example.com"))
        self.assertFalse(iURLiP(r"\%2f\%2fwww.example.com"))
        self.assertFalse(iURLiP(u"\%2f\%2fwww.example.com"))
        self.assertFalse(iURLiP(b"%2F%2Fwww.example.com"))
        self.assertFalse(iURLiP(r"%2F%2Fwww.example.com"))
        self.assertFalse(iURLiP(u"%2F%2Fwww.example.com"))
        self.assertFalse(iURLiP(b"%2f%2fwww.example.com"))
        self.assertFalse(iURLiP(r"%2f%2fwww.example.com"))
        self.assertFalse(iURLiP(u"%2f%2fwww.example.com"))

    def test_isURLInPortal_from_core_plone(self):
        # Adapted from CMFPlone/tests/testURLTool.py
        # But there the site url is http://www.foobar.com/bar/foo
        self.assertEqual(self.portal.absolute_url(), "http://nohost/plone")

        url_tool = self.portal.portal_url
        iURLiP = url_tool.isURLInPortal
        self.assertTrue(iURLiP("http://nohost/plone/folder"))
        self.assertTrue(iURLiP("http://nohost/plone"))
        self.assertFalse(iURLiP("http://nohost/plon"))
        self.assertTrue(iURLiP("https://nohost/plone/folder"))
        self.assertFalse(iURLiP("http://nohost:8080/plone/folder"))
        self.assertFalse(iURLiP("http://nohost/"))
        self.assertFalse(iURLiP("/images"))
        self.assertTrue(iURLiP("/plone/foo"))
        # The next tests are extra:
        self.assertTrue(iURLiP("//nohost/plone"))
        self.assertFalse(iURLiP("///nohost/plone"))
        self.assertFalse(iURLiP("http:///nohost/plone"))
        self.assertFalse(iURLiP("https:///nohost/plone"))
        self.assertFalse(iURLiP("http:////nohost/plone"))
        # relative urls:
        self.assertTrue(iURLiP("bar/foo/foo"))
        self.assertTrue(iURLiP("./bar/foo/foo"))
        self.assertTrue(iURLiP("../bar/foo/foo"))
        self.assertTrue(iURLiP(""))
        # special urls
        self.assertFalse(iURLiP(" "))
        self.assertTrue(iURLiP("@@view"))
        self.assertTrue(iURLiP("++resource++"))

    def test_unicode_control_characters(self):
        import string
        import unicodedata

        allowed_ascii = string.ascii_letters + string.digits + "./@+"
        iURLiP = self.portal.portal_url.isURLInPortal
        self.assertTrue(iURLiP("a"))
        # Python 2 has chr    which works in range(256) and returns string (bytes).
        # Python 2 has unichr which works in range(0x10ffff) and returns unicode.
        # Python 3 has chr    which works in range(0x10ffff) and returns unicode (string).
        # When out of range, you get a ValueError.
        # On Python 2 you may have less range:
        # ValueError: unichr() arg not in range(0x10000) (narrow Python build)
        # So 0x0ffff (65535) is the maximum there.
        # That may be a practical limit for the tests anyway, otherwise it takes long.
        i = 0
        # while True:
        while i <= 65535:
            try:
                u_char = makechar(i)
            except ValueError:
                print("Breaking off isURLInPortal tests at code point {0}".format(i))
                break
            u_result = iURLiP(u_char)
            try:
                b_char = u_char.encode("utf-8")
            except UnicodeEncodeError:
                # Only happens on Python 3, with i between 55296 and 57343.  For the first one:
                # *** UnicodeEncodeError: 'utf-8' codec can't encode character '\ud800' in position 0: surrogates not allowed
                # I get the same when simply printing that character.
                # print("UnicodeEncodeError for i={0}".format(i))
                b_char = u_char.encode("utf-8", "xmlcharrefreplace")
            try:
                b_result = iURLiP(b_char)
            except TypeError:
                # Only happens on Python 3, for all characters that are not caught earlier.
                # It is in the original isURLInPortal:
                #   File "/Users/maurits/shared-eggs/cp37m/Products.CMFPlone-5.2rc3-py3.7.egg/Products/CMFPlone/URLTool.py", line 59, in isURLInPortal
                #     url = re.sub('^[\x00-\x20]+', '', url).strip()
                #   File "/Users/maurits/pythons/3.7/lib/python3.7/re.py", line 192, in sub
                #     return _compile(pattern, flags).sub(repl, string, count)
                # TypeError: cannot use a string pattern on a bytes-like object
                # I guess the url that is passed to isURLInPortal is always a string-like object,
                # so this does not happen in practice.
                # print("TypeError for i={0} ({1})".format(i, u_char))
                b_result = u_result
            self.assertEqual(
                b_result,
                u_result,
                "Result for bytes ({0}) and unicode ({1})  is not the same for i={2}.".format(
                    b_result, u_result, i
                ),
            )
            result = b_result
            if u_char == u"/":
                # Not allowed because / points to the Zope root, not the Plone root.
                self.assertFalse(result, "Unexpectedly True for slash i={0}".format(i))
                # / For sanity, check that /plone still works.
                self.assertTrue(iURLiP(u_char + u"plone"))
            elif u_char in allowed_ascii:
                self.assertTrue(
                    result, "Unexpectedly False for standard ascii i={0}".format(i)
                )
            elif i < 128:
                # ascii but not white listed
                self.assertFalse(
                    result, "Unexpectedly True for forbidden ascii i={0}".format(i)
                )
            elif unicodedata.category(u_char)[0] == "C":
                self.assertFalse(
                    result, "Unexpectedly True for control char i={0}".format(i)
                )
            else:
                self.assertTrue(
                    result, "Unexpectedly False for standard unicode i={0}".format(i)
                )
            i += 1

    def test_latin1(self):
        # All text that Plone passes around, should be unicode or a utf-8 encoded string.
        # latin-1 is not supported.  Our method could stumble here, so let's test it.
        iURLiP = self.portal.portal_url.isURLInPortal
        for i in range(128, 256):
            u_char = makechar(i)
            b_char = u_char.encode("latin-1")
            self.assertFalse(iURLiP(b_char))
