# -*- coding: utf-8 -*-
# Adapted copy of PloneHotfix20171128/tests/test_122_124_in_portal.py
from Products.PloneHotfix20200121.tests import BaseTest


class TestAttackVector(BaseTest):
    def test_regression_query(self):
        # Python 2.4 could have trouble here.
        self.assertTrue(self.portal.portal_url.isURLInPortal("foobar?sound=miauw"))

    def test_regression_absolute_url(self):
        self.assertTrue(self.portal.portal_url.isURLInPortal(self.portal.portal_url()))
        self.assertTrue(
            self.portal.portal_url.isURLInPortal(
                self.portal.portal_url() + "/shrubbery?knights=ni#ekki-ekki"
            )
        )

    def test_mailto_simple(self):
        # Issue #122.
        self.assertFalse(
            self.portal.portal_url.isURLInPortal("mailto:someone@example.org")
        )

    def test_mailto_complex(self):
        # Issue #122.
        self.assertFalse(
            self.portal.portal_url.isURLInPortal(
                "mailto&#58;192&#46;168&#46;163&#46;154&#58;8080&#47;Plone&apos;"
                "&quot;&gt;&lt;html&gt;&lt;svg&#32;onload&#61;alert&#40;document"
                "&#46;domain&#41;&gt;&lt;&#47;html&gt;"
            )
        )

    def test_data(self):
        # Issue #124.
        self.assertFalse(
            self.portal.portal_url.isURLInPortal(
                "data:text/html%3bbase64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K"
            )
        )

    def test_double_slash(self):
        # I wondered if this might be a problem after reading
        # https://bugs.python.org/issue23505
        # Apparently not, but let's test it.
        self.assertFalse(self.portal.portal_url.isURLInPortal("//www.google.com"))
        self.assertFalse(self.portal.portal_url.isURLInPortal("////www.google.com"))
