from Products.CMFPlone.URLTool import URLTool
import pkg_resources
import string
import unicodedata


# Several other hotfixes override isURLInPortal too.
# They must be loaded first, when available.
# This makes sure the import order is correct.

try:
    pkg_resources.get_distribution("Products.PloneHotfix20160830")
except pkg_resources.DistributionNotFound:
    pass
else:
    import Products.PloneHotfix20160830  # noqa
try:
    pkg_resources.get_distribution("Products.PloneHotfix20171128")
except pkg_resources.DistributionNotFound:
    pass
else:
    import Products.PloneHotfix20171128  # noqa


# Determine allowed ascii characters.
# We want to allow most printable characters,
# but no whitespace, and no punctuation, except for a few exceptions.
# This boils down to ascii letters plus digits plus exceptions.
# Exceptions:
# - dot and slash for relative or absolute paths.
# - @ because we have views starting with @@
# - + because we have ++resource++ urls
allowed_ascii = string.ascii_letters + string.digits + "./@+"

orig = URLTool.isURLInPortal


def wrapped_in_portal(self, url, context=None):
    if url:
        # For character code points higher than 127, the bytes representation of a character
        # is longer than the unicode representation, so url[0] may give different results
        # for bytes and unicode.  On Python 2:
        # >>> unichr(128)
        # u'\x80'
        # >>> len(unichr(128))
        # 1
        # >>> unichr(128).encode("latin-1")
        # '\x80'
        # >>> len(unichr(128).encode("latin-1"))
        # 1
        # >>> unichr(128).encode("utf-8")
        # '\xc2\x80'
        # >>> len(unichr(128).encode("utf-8"))
        # 2
        # >>> unichr(128).encode("utf-8")[0]
        # '\xc2'
        # So make sure we have unicode here for comparing the first character.
        if isinstance(url, bytes):
            # Remember, on Python 2, bytes == str.
            try:
                first = url.decode("utf-8")[0]
            except UnicodeDecodeError:
                # We don't trust this
                return False
        else:
            first = url[0]
        if ord(first) < 128:
            if first not in allowed_ascii:
                # The first character of the url is ascii but not in the allowed range.
                return False
        else:
            # This is non-ascii, which has lots of control characters, which may be dangerous.
            # Check taken from django.utils.http._is_safe_url.  See
            # https://github.com/django/django/blob/2.1.5/django/utils/http.py#L356-L382
            # Forbid URLs that start with control characters. Some browsers (like
            # Chrome) ignore quite a few control characters at the start of a
            # URL and might consider the URL as scheme relative.
            # For categories, see 5.7.1 General Category Values here:
            # http://www.unicode.org/reports/tr44/tr44-6.html#Property_Values
            # We look for Control categories here.
            if unicodedata.category(first)[0] == "C":
                return False
    try:
        return orig(self, url, context)
    except TypeError as e:
        if "isURLInPortal() takes exactly 2 arguments" in e.args[0]:
            return orig(self, url)
        else:
            raise


wrapped_in_portal.__doc__ = orig.__doc__
URLTool.isURLInPortal = wrapped_in_portal
