# -*- coding: utf-8 -*-
# This tests https://github.com/plone-security/Issues/issues/137
try:
    from plone import api
    from plone.restapi.testing import PLONE_RESTAPI_DX_FUNCTIONAL_TESTING
    import requests

    IGNORE = False
except ImportError:
    IGNORE = True
    PLONE_RESTAPI_DX_FUNCTIONAL_TESTING = None

from Acquisition import aq_base
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from Products.CMFCore.utils import getToolByName
from Products.PloneHotfix20200121.tests import DummyTestCase

import transaction
import unittest


def sorted_roles(roles):
    results = []
    for line in roles:
        line = list(line)
        line[1] = sorted(line[1])
        results.append(line)
    return results


class TestAttackVector(unittest.TestCase):
    # This includes tests copied from plone.restapi, to check that our patch does not break things.
    if PLONE_RESTAPI_DX_FUNCTIONAL_TESTING is not None:
        layer = PLONE_RESTAPI_DX_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Member"])
        login(self.portal, SITE_OWNER_NAME)
        self.portal.invokeFactory("Folder", id="folder1", title="My Folder")
        wftool = getToolByName(self.portal, "portal_workflow")
        wftool.doActionFor(self.portal.folder1, "publish")

        self.portal.folder1.invokeFactory("Document", id="doc1", title="My Document")

        transaction.commit()

    def test_may_only_manage_roles_already_held(self):
        # This tests the patch.
        # Grant Editor role to our test user (which gives them the required
        # "plone.DelegateRoles" permission to manage local roles at all)
        api.user.grant_roles(
            username=TEST_USER_ID, obj=self.portal.folder1, roles=["Editor"]
        )
        transaction.commit()

        # Guard assertion - our test user starts with a limited set of roles
        existing_roles = api.user.get_roles(
            username=TEST_USER_ID, obj=self.portal.folder1
        )
        self.assertEqual(
            sorted(["Member", "Authenticated", "Editor"]), sorted(existing_roles)
        )

        # Attempt to gain additional roles not already held
        response = requests.post(
            self.portal.folder1.absolute_url() + "/@sharing",
            headers={"Accept": "application/json"},
            auth=(TEST_USER_NAME, TEST_USER_PASSWORD),
            json={
                "entries": [
                    {
                        u"id": TEST_USER_ID,
                        u"roles": {
                            u"Contributor": True,
                            u"Editor": True,
                            u"Reader": True,
                            u"Publisher": True,
                            u"Reviewer": True,
                            u"Manager": True,
                        },
                        u"type": u"user",
                    }
                ]
            },
        )

        transaction.commit()

        self.assertEqual(response.status_code, 204)
        new_roles = api.user.get_roles(username=TEST_USER_ID, obj=self.portal.folder1)

        # New roles should not contain any new roles that the user didn't
        # have permission to delegate.
        self.assertNotIn(u"Manager", new_roles)
        self.assertNotIn(u"Publisher", new_roles)
        self.assertNotIn(u"Reviewer", new_roles)
        self.assertNotIn(u"Contributor", new_roles)

        # 'Reader' gets added because the permission to delegate it is
        # assigned to 'Editor' by default (see p.a.workflow.permissions)
        self.assertEqual(
            sorted(["Member", "Authenticated", "Editor", "Reader"]), sorted(new_roles)
        )

    def test_set_local_roles_for_user(self):

        pas = getToolByName(self.portal, "acl_users")
        self.assertEqual(
            pas.getLocalRolesForDisplay(self.portal.folder1),
            (("admin", ("Owner",), "user", "admin"),),
        )

        response = requests.post(
            self.portal.folder1.absolute_url() + "/@sharing",
            headers={"Accept": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json={
                "entries": [
                    {
                        u"id": TEST_USER_ID,
                        u"roles": {
                            u"Contributor": False,
                            u"Editor": False,
                            u"Reader": True,
                            u"Reviewer": True,
                        },
                        u"type": u"user",
                    }
                ]
            },
        )

        transaction.commit()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(
            sorted_roles(pas.getLocalRolesForDisplay(self.portal.folder1)),
            [
                ["admin", ["Owner"], "user", "admin"],
                ["test-user", [u"Reader", u"Reviewer"], "user", u"test_user_1_"],
            ],
        )

    def test_unset_local_roles_for_user(self):
        api.user.grant_roles(
            username=TEST_USER_ID, obj=self.portal.folder1, roles=["Reviewer", "Reader"]
        )
        transaction.commit()

        pas = getToolByName(self.portal, "acl_users")
        self.assertEqual(
            sorted_roles(pas.getLocalRolesForDisplay(self.portal.folder1)),
            [
                ["admin", ["Owner"], "user", "admin"],
                ["test-user", ["Reader", "Reviewer"], "user", "test_user_1_"],
            ],
        )

        response = requests.post(
            self.portal.folder1.absolute_url() + "/@sharing",
            headers={"Accept": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json={
                "entries": [
                    {
                        u"id": TEST_USER_ID,
                        u"roles": {
                            u"Contributor": False,
                            u"Editor": False,
                            u"Reader": False,
                            u"Reviewer": True,
                        },
                        u"type": u"user",
                    }
                ]
            },
        )

        transaction.commit()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(
            pas.getLocalRolesForDisplay(self.portal.folder1),
            (
                ("admin", ("Owner",), "user", "admin"),
                ("test-user", (u"Reviewer",), "user", u"test_user_1_"),
            ),
        )

    def test_set_local_roles_on_site_root(self):

        pas = getToolByName(self.portal, "acl_users")
        self.assertEqual(
            pas.getLocalRolesForDisplay(self.portal),
            (("admin", ("Owner",), "user", "admin"),),
        )

        response = requests.post(
            self.portal.absolute_url() + "/@sharing",
            headers={"Accept": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json={
                "entries": [
                    {
                        u"id": TEST_USER_ID,
                        u"roles": {
                            u"Contributor": False,
                            u"Editor": False,
                            u"Reader": True,
                            u"Reviewer": True,
                        },
                        u"type": u"user",
                    }
                ]
            },
        )
        transaction.commit()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(
            sorted_roles(pas.getLocalRolesForDisplay(self.portal)),
            [
                ["admin", ["Owner"], "user", "admin"],
                ["test-user", [u"Reader", u"Reviewer"], "user", u"test_user_1_"],
            ],
        )

    def _get_ac_local_roles_block(self, obj):
        return bool(
            getattr(aq_base(self.portal.folder1), "__ac_local_roles_block__", False)
        )

    def test_set_local_roles_inherit(self):
        self.assertEqual(self._get_ac_local_roles_block(self.portal.folder1), False)

        # block local roles
        response = requests.post(
            self.portal.folder1.absolute_url() + "/@sharing",
            headers={"Accept": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json={"inherit": False},
        )

        transaction.commit()
        self.assertEqual(self._get_ac_local_roles_block(self.portal.folder1), True)
        # unblock local roles
        response = requests.post(
            self.portal.folder1.absolute_url() + "/@sharing",
            headers={"Accept": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json={"inherit": True},
        )
        transaction.commit()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self._get_ac_local_roles_block(self.portal.folder1), False)


if IGNORE:
    # Override the test class, otherwise we get an error:
    # TypeError: Module does not define any tests
    TestAttackVector = DummyTestCase  # noqa
    print("Skipping issue #137 tests because plone.restapi is not available.")
