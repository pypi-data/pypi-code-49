import os

from peek_platform import PeekPlatformConfig
from txhttputil.site.FileUnderlayResource import FileUnderlayResource
from vortex.VortexFactory import VortexFactory

mobileRoot = FileUnderlayResource()


def setupMobile():
    # Setup properties for serving the site
    mobileRoot.enableSinglePageApplication()

    # This dist dir is automatically generated, but check it's parent

    import peek_mobile
    frontendProjectDir = os.path.dirname(peek_mobile.__file__)
    distDir = os.path.join(frontendProjectDir, 'build-web', 'dist')

    distDirParent = os.path.dirname(distDir)
    if not os.path.isdir(distDirParent):
        raise NotADirectoryError(distDirParent)

    # Make the dist dir, otherwise addFileSystemRoot throws an exception.
    # It rebuilds at a later date
    os.makedirs(distDir, exist_ok=True)

    mobileRoot.addFileSystemRoot(distDir)

    addVortexServers(mobileRoot)
    addDocSite(mobileRoot)


desktopRoot = FileUnderlayResource()


def setupDesktop():
    # Setup properties for serving the site
    desktopRoot.enableSinglePageApplication()

    # This dist dir is automatically generated, but check it's parent

    import peek_desktop
    frontendProjectDir = os.path.dirname(peek_desktop.__file__)
    distDir = os.path.join(frontendProjectDir, 'build-web', 'dist')

    distDirParent = os.path.dirname(distDir)
    if not os.path.isdir(distDirParent):
        raise NotADirectoryError(distDirParent)

    # Make the dist dir, otherwise addFileSystemRoot throws an exception.
    # It rebuilds at a later date
    os.makedirs(distDir, exist_ok=True)

    desktopRoot.addFileSystemRoot(distDir)

    addVortexServers(desktopRoot)
    addDocSite(desktopRoot)


def addVortexServers(siteRootResource):
    # Add the websocket to the site root
    VortexFactory.createHttpWebsocketServer(
        PeekPlatformConfig.componentName,
        siteRootResource
    )

    # Add a HTTP vortex
    # VortexFactory.createServer(PeekPlatformConfig.componentName, siteRootResource)


def addDocSite(siteRootResource):
    # Setup properties for serving the site
    docSiteRoot = FileUnderlayResource()
    docSiteRoot.enableSinglePageApplication()

    # This dist dir is automatically generated, but check it's parent

    import peek_doc_user
    docProjectDir = os.path.dirname(peek_doc_user.__file__)
    distDir = os.path.join(docProjectDir, 'doc_dist')

    distDirParent = os.path.dirname(distDir)
    if not os.path.isdir(distDirParent):
        raise NotADirectoryError(distDirParent)

    # Make the dist dir, otherwise addFileSystemRoot throws an exception.
    # It rebuilds at a later date
    os.makedirs(distDir, exist_ok=True)

    docSiteRoot.addFileSystemRoot(distDir)

    siteRootResource.putChild(b'docs', docSiteRoot)
