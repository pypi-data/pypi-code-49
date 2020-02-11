import logging
import pkg_resources


logger = logging.getLogger("Products.PloneHotfix20200121")

# First import any current CMFPlone patches.
try:
    pkg_resources.get_distribution("Products.CMFPlone")
    HAS_PLONE = True
except pkg_resources.DistributionNotFound:
    HAS_PLONE = False
else:
    from Products.CMFPlone import patches  # noqa

# General hotfixes for all, including zope.
hotfixes = ["sql_quote"]
if HAS_PLONE:
    # Extra hotfixes for Plone:
    hotfixes.append("in_portal")
    hotfixes.append("password_validation")
    # Extra hotfixes for Plone add-ons:
    try:
        pkg_resources.get_distribution("plone.app.contenttypes")
        hotfixes.append("pac")
    except pkg_resources.DistributionNotFound:
        pass
    try:
        pkg_resources.get_distribution("plone.app.content")
        hotfixes.append("content")
    except pkg_resources.DistributionNotFound:
        pass
    try:
        pkg_resources.get_distribution("plone.app.layout")
        hotfixes.append("layout")
    except pkg_resources.DistributionNotFound:
        pass
    try:
        pkg_resources.get_distribution("plone.restapi")
        hotfixes.append("restapi_local_roles")
    except pkg_resources.DistributionNotFound:
        pass


# Apply the fixes
for hotfix in hotfixes:
    try:
        __import__("Products.PloneHotfix20200121.%s" % hotfix)
        logger.info("Applied %s patch" % hotfix)
    except:  # noqa
        # This is an error that the user should investigate.
        # Log an error and continue.
        logger.exception("Could not apply %s" % hotfix)
if not hotfixes:
    logger.info("No hotfixes were needed.")
else:
    logger.info("Hotfix installed")
