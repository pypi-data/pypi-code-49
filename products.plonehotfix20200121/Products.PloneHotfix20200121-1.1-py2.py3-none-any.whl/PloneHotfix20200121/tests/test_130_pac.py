from plone.app.testing import login
from plone.app.testing import logout
from plone.app.testing import TEST_USER_NAME
from Products.PloneHotfix20200121.tests import BaseTest

# List various possibly read methods.
# Not all classes have all of them.
# Some may be inherited.
READ_METHODS = (
    "content_type",
    "Format",
    "get_size",
    "getFoldersAndImages",
    "getQuery",
    "getRawQuery",
    "index_html",
    "listMetaDataFields",
    "manage_DAVget",
    "manage_FTPget",
    "queryCatalog",
    "results",
    "selectedViewFields",
)
WRITE_METHODS = ("setQuery", "setSort_on", "setSort_reversed", "PUT")


class TestAttackVector(BaseTest):
    def test_put_gives_401(self):
        try:
            # pkg_resources.get_distribution("ZServer") is not good enough,
            # because ZServer may be included in the Zope2 package.
            import ZServer  # noqa
        except ImportError:
            print("Ignoring PUT request method tests, as we miss the ZServer.")
            return

        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory("Collection", id="collection")
        self.portal.invokeFactory("Document", id="page")
        self.portal.invokeFactory("File", id="file")
        self.portal.invokeFactory("Folder", id="folder")
        self.portal.invokeFactory("Image", id="image")
        collection = self.portal.collection
        fi = self.portal.file
        folder = self.portal.folder
        image = self.portal.image
        page = self.portal.page
        logout()

        path = "/" + collection.absolute_url(relative=True)
        response = self.publish(path=path, env={}, request_method="PUT")
        self.assertEqual(response.getStatus(), 401)

        path = "/" + fi.absolute_url(relative=True)
        response = self.publish(path=path, env={}, request_method="PUT")
        self.assertEqual(response.getStatus(), 401)

        path = "/" + folder.absolute_url(relative=True)
        response = self.publish(path=path, env={}, request_method="PUT")
        self.assertEqual(response.getStatus(), 401)

        path = "/" + image.absolute_url(relative=True)
        response = self.publish(path=path, env={}, request_method="PUT")
        self.assertEqual(response.getStatus(), 401)

        path = "/" + page.absolute_url(relative=True)
        response = self.publish(path=path, env={}, request_method="PUT")
        self.assertEqual(response.getStatus(), 401)

    def DISABLED_test_listDAVobjects_gives_401(self):
        # This actually gives 302, both with and without the patch.  It is
        # protected with AccessControl.Permissions.webdav_access.
        login(self.portal, TEST_USER_NAME)
        # only defined for folderish items
        self.portal.invokeFactory("Folder", id="folder")
        folder = self.portal.folder
        logout()

        folder_path = "/" + folder.absolute_url(relative=True)
        path = folder_path + "/listDAVObjects"
        response = self.publish(path=path, env={}, request_method="GET")
        self.assertEqual(response.getStatus(), 401)

    def get_permission_mapping(self, klass):
        permissions = klass.__ac_permissions__
        mapping = {}
        for permission in permissions:
            # permission can have two or three items:
            # ('WebDAV access',
            #  ('PROPFIND', 'listDAVObjects', 'manage_DAVget'),
            #  ('Manager', 'Authenticated'))
            perm, methods = list(permission)[:2]
            for method in methods:
                mapping[method] = perm
        return mapping

    def _test_class_patched(self, klass):
        mapping = self.get_permission_mapping(klass)
        for method in READ_METHODS:
            if method in klass.__dict__.keys():
                self.assertEqual(
                    mapping.get(method),
                    "View",
                    "Method {0} missing view protection".format(method),
                )
        for method in WRITE_METHODS:
            if method in klass.__dict__.keys():
                self.assertEqual(
                    mapping.get(method),
                    "Modify portal content",
                    "Method {0} missing edit protection".format(method),
                )

    def testCollection_patched(self):
        try:
            from plone.app.contenttypes.content import Collection
        except ImportError:
            return
        self._test_class_patched(Collection)

    def testDocument_patched(self):
        try:
            from plone.app.contenttypes.content import Document
        except ImportError:
            return
        self._test_class_patched(Document)

    def testFile_patched(self):
        try:
            from plone.app.contenttypes.content import File
        except ImportError:
            return
        self._test_class_patched(File)

    def testImage_patched(self):
        try:
            from plone.app.contenttypes.content import Image
        except ImportError:
            return
        self._test_class_patched(Image)
