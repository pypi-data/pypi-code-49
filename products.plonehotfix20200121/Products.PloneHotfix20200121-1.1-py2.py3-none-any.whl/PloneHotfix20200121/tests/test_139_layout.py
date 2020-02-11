# -*- coding: utf-8 -*-
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from Products.PloneHotfix20200121.tests import BaseTest
from plone.testing.z2 import Browser
from zExceptions import NotFound

import json
import transaction


ESCAPED = "&lt;script&gt;"
HACKED = '<script>alert("hacked")</script>'


class TestAttackVector(BaseTest):
    def get_browser(self):
        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        browser.addHeader(
            "Authorization",
            "Basic {0}:{1}".format(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
        )
        return browser

    def test_normal_title(self):
        # Create a folder and page with normal title.
        normal = "'Normal title"
        self.portal.invokeFactory("Folder", id="folder1", title=normal)
        folder1 = self.portal.folder1
        self.assertEqual(folder1.Title(), normal)
        folder1.invokeFactory("Document", id="page1", title=normal)
        page1 = folder1.page1
        self.assertEqual(page1.Title(), normal)
        transaction.commit()

        # Check the output of the normal case for comparison.
        browser = self.get_browser()
        browser.open(folder1.absolute_url())
        self.assertNotIn(ESCAPED, browser.contents)
        browser.open(page1.absolute_url())
        self.assertNotIn(ESCAPED, browser.contents)
        browser.open(folder1.absolute_url() + "/folder_contents")
        self.assertNotIn(ESCAPED, browser.contents)

        # The next exists only on Plone 5.0+.
        try:
            browser.open(folder1.absolute_url() + "/@@fc-contextInfo")
        except NotFound:
            pass
        else:
            self.assertNotIn(ESCAPED, browser.contents)

    def test_xss_from_title(self):
        # Does a script tag as title show up anywhere in the html?
        # It might end up in the main menu.

        # Create a folder and page with a hacked title.
        self.portal.invokeFactory("Folder", id="folder2", title=HACKED)
        folder2 = self.portal.folder2
        self.assertEqual(folder2.Title(), HACKED)
        folder2.invokeFactory("Document", id="page2", title=HACKED)
        page2 = folder2.page2
        self.assertEqual(page2.Title(), HACKED)
        transaction.commit()

        # Check the output of this hacked case.
        browser = self.get_browser()
        browser.open(folder2.absolute_url())
        self.assert_not_hacked(browser)
        browser.open(page2.absolute_url())
        self.assert_not_hacked(browser)
        browser.open(folder2.absolute_url() + "/folder_contents")
        self.assert_not_hacked(browser)

        # The next exists only on Plone 5.0+.
        try:
            browser.open(folder2.absolute_url() + "/@@fc-contextInfo")
        except NotFound:
            pass
        else:
            self.assert_not_hacked(browser)

    def assert_not_hacked(self, browser):
        body = browser.contents
        hacked = HACKED
        if not browser.isHtml:
            # Assume json.
            # data = json.loads(body)
            hacked = json.dumps(HACKED)

        # This gives a too verbose error message, showing the entire body:
        # self.assertNotIn(HACKED, body)
        # So we roll our own less verbose version.
        if hacked in body:
            index = body.index(hacked)
            start = max(0, index - 50)
            end = min(index + len(hacked) + 50, len(body))
            assert False, "Hacked script found in body: ... {0} ...".format(
                body[start:end]
            )
        # The escaped version of the HACKED text should be in the response text.
        self.assertIn(ESCAPED, body)
