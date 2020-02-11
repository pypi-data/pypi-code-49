from io import BytesIO
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing import z2
from zope.configuration import xmlconfig
from ZPublisher import HTTPResponse

import base64
import os
import pkg_resources
import Products.PloneHotfix20200121
import re
import sys
import transaction
import unittest


try:
    pkg_resources.get_distribution("plone.app.contenttypes")
except pkg_resources.DistributionNotFound:
    HAS_PACT = False
else:
    HAS_PACT = True
try:
    pkg_resources.get_distribution("plone.app.dexterity")
except pkg_resources.DistributionNotFound:
    HAS_DEXTERITY = False
else:
    HAS_DEXTERITY = True
try:
    pkg_resources.get_distribution("plone.protect")
except pkg_resources.DistributionNotFound:
    # When plone.protect is not there, we don't have to do anything special.
    def createToken():
        return ""


else:
    try:
        from plone.protect import createToken
    except ImportError:
        # Not all versions have factored out createToken.
        from zope.component import getUtility
        from plone.keyring.interfaces import IKeyManager
        from plone.protect.authenticator import _getUserName
        import hmac

        try:
            from hashlib import sha1 as sha
        except ImportError:
            import sha

        def createToken():
            manager = getUtility(IKeyManager)
            secret = manager.secret()
            user = _getUserName()
            return hmac.new(secret, user, sha).hexdigest()


class HotfixLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Fix subrequest not fallbacking to wrong encoding in test environment:
        HTTPResponse.default_encoding = "utf-8"
        super(HotfixLayer, self).setUpZope(app, configurationContext)

        # Load ZCML if we have it.
        if "configure.zcml" in os.listdir(
            os.path.dirname(Products.PloneHotfix20200121.__file__)
        ):
            xmlconfig.file(
                "configure.zcml", Products.PloneHotfix20200121, context=configurationContext
            )

        if HAS_DEXTERITY:
            import plone.app.dexterity

            xmlconfig.file(
                "configure.zcml", plone.app.dexterity, context=configurationContext
            )

        if HAS_PACT:
            # prepare installing plone.app.contenttypes
            z2.installProduct(app, "Products.DateRecurringIndex")

            import plone.app.contenttypes

            xmlconfig.file(
                "configure.zcml", plone.app.contenttypes, context=configurationContext
            )

    def setUpPloneSite(self, portal):
        super(HotfixLayer, self).setUpPloneSite(portal)

        if HAS_PACT:
            # Install into Plone site using portal_setup
            applyProfile(portal, "plone.app.contenttypes:default")


HOTFIX_FIXTURE = HotfixLayer()
HOTFIX_PLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(HOTFIX_FIXTURE,), name="HotfixTesting:Functional"
)
HOTFIX_PLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(HOTFIX_FIXTURE,), name="HotfixTesting:Integration"
)


class BaseTest(unittest.TestCase):
    layer = HOTFIX_PLONE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def publish(
        self,
        path,
        basic=None,
        env=None,
        extra=None,
        request_method="GET",
        stdin=None,
        handle_errors=True,
    ):
        """
        Mostly pulled from Testing.functional
        """
        from ZPublisher.Request import Request
        from ZPublisher.Response import Response

        # Note: the next import fail in Python 3, because it needs ZServer.
        from ZPublisher.Publish import publish_module

        transaction.commit()

        if env is None:
            env = {}
        if extra is None:
            extra = {}

        env["SERVER_NAME"] = self.request["SERVER_NAME"]
        env["SERVER_PORT"] = self.request["SERVER_PORT"]
        env["REQUEST_METHOD"] = request_method

        p = path.split("?")
        if len(p) == 1:
            env["PATH_INFO"] = p[0]
        elif len(p) == 2:
            [env["PATH_INFO"], env["QUERY_STRING"]] = p
        else:
            raise TypeError("")

        if basic:
            env["HTTP_AUTHORIZATION"] = "Basic %s" % base64.encodestring(basic)

        if stdin is None:
            stdin = BytesIO()

        outstream = BytesIO()
        response = Response(stdout=outstream, stderr=sys.stderr)
        request = Request(stdin, env, response)
        if extra:
            # Needed on Plone 3 when adding things to the path in a querystring
            # is not enough.
            for key, value in extra.items():
                request[key] = value

        publish_module(
            "Zope2", debug=not handle_errors, request=request, response=response
        )

        return ResponseWrapper(response, outstream, path)

    def create_private_document(self, doc_id):
        """Set workflow chain and create document."""
        wf_tool = self.portal.portal_workflow
        wf_tool.setChainForPortalTypes(["Document"], "simple_publication_workflow")
        self.portal.invokeFactory("Document", doc_id)
        return self.portal[doc_id]


class ResponseWrapper:
    """Decorates a response object with additional introspective methods."""

    _bodyre = re.compile("\r\n\r\n(.*)", re.MULTILINE | re.DOTALL)

    def __init__(self, response, outstream, path):
        self._response = response
        self._outstream = outstream
        self._path = path

    def __getattr__(self, name):
        return getattr(self._response, name)

    def getOutput(self):
        """Returns the complete output, headers and all."""
        return self._outstream.getvalue()

    def getBody(self):
        """Returns the page body, i.e. the output par headers."""
        body = self._bodyre.search(self.getOutput())
        if body is not None:
            body = body.group(1)
        return body

    def getPath(self):
        """Returns the path used by the request."""
        return self._path

    def getHeader(self, name):
        """Returns the value of a response header."""
        return self.headers.get(name.lower())

    def getCookie(self, name):
        """Returns a response cookie."""
        return self.cookies.get(name)


class DummyTestCase(unittest.TestCase):
    """Dummy test case.

    Sometimes we want to override the entire test class because the
    thing it tests cannot be imported.  We need a dummy test then,
    otherwise we get an error:

    TypeError: Module X does not define any tests
    """

    def test_dummy(self):
        pass
