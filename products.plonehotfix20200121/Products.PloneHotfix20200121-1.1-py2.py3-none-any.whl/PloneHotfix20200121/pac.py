from plone.app.contenttypes.content import Collection
from plone.app.contenttypes.content import Document
from plone.app.contenttypes.content import File
from plone.app.contenttypes.content import Image

try:
    from AccessControl.class_init import InitializeClass
except ImportError:
    from Globals import InitializeClass
from Products.CMFCore import permissions

try:
    from AccessControl.security import _getSecurity
except ImportError:
    from Products.Five.security import _getSecurity


# Protect File and Image
read_methods = ("get_size", "content_type")
for klass in (File, Image):
    security = _getSecurity(klass)
    # security.declareProtected(permissions.View, *read_methods)
    for method in read_methods:
        if hasattr(klass, method):
            security.declareProtected(permissions.View, method)
    method = "PUT"
    if hasattr(klass, method):
        security.declareProtected(permissions.ModifyPortalContent, method)
    InitializeClass(klass)

# Protect Document
klass = Document
security = _getSecurity(klass)
method = "Format"
if hasattr(klass, method):
    security.declareProtected(permissions.View, method)
InitializeClass(klass)

# Protect Collection (mostly for backwards compatibility)
read_methods = (
    "listMetaDataFields",
    "selectedViewFields",
    "getQuery",
    "getRawQuery",
    "queryCatalog",
    "results",
    "getFoldersAndImages",
)
write_methods = ("setQuery", "setSort_on", "setSort_reversed")
klass = Collection
security = _getSecurity(klass)
for method in read_methods:
    if hasattr(klass, method):
        security.declareProtected(permissions.View, method)
for method in write_methods:
    if hasattr(klass, method):
        security.declareProtected(permissions.ModifyPortalContent, method)
InitializeClass(klass)
