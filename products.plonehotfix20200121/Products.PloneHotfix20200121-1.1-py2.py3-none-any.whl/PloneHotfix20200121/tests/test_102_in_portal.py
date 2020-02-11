# -*- coding: utf-8 -*-
# Adapted copy of PloneHotfix20160830/tests/test_102_in_portal.py
from Products.PloneHotfix20200121.tests import BaseTest


class TestAttackVector(BaseTest):
    # Several tests taken over from testURLTool.py in CMFPlone.

    def test_regression(self):
        self.assertTrue(self.portal.portal_url.isURLInPortal("foobar"))

    def test_isURLInPortal(self):
        # First test what the absolute url of the site is, otherwise these
        # tests look really weird.
        # In the CMFPlone tests, apparently our domain is www.foobar.com/bar/foo.
        # Here it is more what we expect.
        self.assertEqual(self.portal.absolute_url(), "http://nohost/plone")
        iURLiP = self.portal.portal_url.isURLInPortal
        self.assertTrue(iURLiP("http://nohost/plone/bar/foo/folder"))
        self.assertTrue(iURLiP("http://nohost/plone/bar/foo"))
        # self.assertFalse(iURLiP('http://nohost/plone/bar2/foo'))
        self.assertTrue(iURLiP("https://nohost/plone/bar/foo/folder"))
        self.assertFalse(iURLiP("http://nohost/plone:8080/bar/foo/folder"))
        # self.assertFalse(iURLiP('http://nohost/plone/bar'))
        # NEXT LINE IS THE REAL EXTRA TEST:
        self.assertTrue(iURLiP("//nohost/plone/bar/foo"))
        self.assertFalse(iURLiP("/images"))
        # self.assertTrue(iURLiP('/bar/foo/foo'))
        self.assertTrue(iURLiP("/plone/bar/foo/foo"))

    def test_script_tag_url_not_in_portal(self):
        self.assertFalse(
            self.portal.portal_url.isURLInPortal('<sCript>alert("hi");</script>')
        )
        self.assertFalse(
            self.portal.portal_url.isURLInPortal(
                "%3CsCript%3Ealert(%22hi%22)%3B%3C%2Fscript%3E"
            )
        )

    def test_inline_url_not_in_portal(self):
        self.assertFalse(self.portal.portal_url.isURLInPortal("jaVascript%3Aalert(3)"))
        self.assertFalse(self.portal.portal_url.isURLInPortal("jaVascript:alert(3)"))

    def test_double_back_slash(self):
        self.assertFalse(self.portal.portal_url.isURLInPortal("\\\\www.google.com"))

    def test_escape(self):
        iURLiP = self.portal.portal_url.isURLInPortal
        self.assertFalse(iURLiP("\/\/www.example.com"))
        self.assertFalse(iURLiP("\%2F\%2Fwww.example.com"))
        self.assertFalse(iURLiP("\%2f\%2fwww.example.com"))
        self.assertFalse(iURLiP("%2F%2Fwww.example.com"))
        self.assertFalse(iURLiP("%2f%2fwww.example.com"))
