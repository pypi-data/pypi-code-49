# -*- coding: utf-8 -*-
# This tests https://github.com/plone-security/Issues/issues/129
from Products.CMFPlone.RegistrationTool import RegistrationTool
from Products.PloneHotfix20200121.tests import BaseTest


# The pasValidation method was introduced in Plone 4.3.
# Only if this method exists, do we need to test.
CHECK = hasattr(RegistrationTool, "pasValidation")


class TestAttackVector(BaseTest):
    def testTestPasswordValidityConfirm(self):
        # Basic test, not related to the hotfix.
        self.registration = self.portal.portal_registration
        self.assertTrue(
            self.registration.testPasswordValidity("validpassword", confirm=None)
            is None
        )
        self.assertFalse(
            self.registration.testPasswordValidity(
                "validpassword", confirm="anotherpassword"
            )
            is None
        )

    def testTestPasswordValidityPolicy(self):
        if not CHECK:
            print("Issue #129 test skipped on Plone 4.2 or lower.")
            return
        # Note: in CMFPlone 4.2.x testPasswordValidity did not exist in CMFPlone.
        # It did exist in the base tool in CMFDefault.
        # But pasValidation did not exist.  It was introduced in 4.3.
        self.registration = self.portal.portal_registration
        self.assertIsNone(self.registration.testPasswordValidity("abcde", confirm=None))
        self.assertEqual(
            self.registration.testPasswordValidity("abcd", confirm=None),
            "Your password must contain at least 5 characters.",
        )
        # Password validity is checked with an empty password
        # to get a nice help message to show for the input field.
        self.assertEqual(
            self.registration.testPasswordValidity("", confirm=None),
            "Minimum 5 characters.",
        )

    def testPasValidation(self):
        if not CHECK:
            print("Issue #129 test skipped on Plone 4.2 or lower.")
            return
        self.registration = self.portal.portal_registration
        self.assertIsNone(self.registration.pasValidation("password", "abcde"))
        self.assertEqual(
            self.registration.pasValidation("password", "abcd"),
            "Your password must contain at least 5 characters.",
        )
