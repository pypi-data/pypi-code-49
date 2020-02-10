import contextlib

from distutils.version import StrictVersion as V

from pip import __version__
from pip._internal.operations.prepare import RequirementPreparer

try:
    from pip._internal.index.package_finder import PackageFinder
except ImportError:
    from pip._internal.index import PackageFinder


PIP_VERSION = V(__version__)


if PIP_VERSION >= V("19.3"):

    def is_dir_url(link):
        return link.is_existing_dir()

    def is_file_url(link):
        return link.is_file

    def is_vcs_url(link):
        return link.is_vcs


else:
    from pip._internal.download import (  # NOQA
        is_dir_url,
        is_file_url,
        is_vcs_url,
    )


def get_dist_from_abstract_dist(abstract_dist, finder):
    if PIP_VERSION >= V("19.2"):
        return abstract_dist.get_pkg_resources_distribution()
    elif PIP_VERSION >= V("19.0"):
        return abstract_dist.dist()
    else:
        return abstract_dist.dist(finder)


def get_package_finder(session):
    if PIP_VERSION >= V("19.2"):
        from pip._internal.models.search_scope import SearchScope
        from pip._internal.models.selection_prefs import SelectionPreferences

        search_scope = SearchScope.create(find_links=[], index_urls=[])

        if PIP_VERSION >= V("19.3"):
            if PIP_VERSION >= V("20.0"):
                from pip._internal.index.collector import LinkCollector
            else:
                from pip._internal.collector import LinkCollector

            kwargs = {
                "link_collector": LinkCollector(
                    session=session, search_scope=search_scope
                )
            }
        else:
            kwargs = {
                "search_scope": search_scope,
                "session": session,
            }

        return PackageFinder.create(
            selection_prefs=SelectionPreferences(allow_yanked=False), **kwargs
        )
    else:
        return PackageFinder(find_links=[], index_urls=[], session=session)


if PIP_VERSION >= V("20.0"):
    from pip._internal.req.req_tracker import get_requirement_tracker
else:
    @contextlib.contextmanager
    def get_requirement_tracker():
        from pip._internal.req.req_tracker import RequirementTracker

        yield RequirementTracker()


def get_requirement_preparer(finder, session, req_tracker):
    kwargs = {}
    if PIP_VERSION >= V("20.0"):
        from pip._internal.network.download import Downloader

        kwargs.update(
            {
                "require_hashes": False,
                "finder": finder,
                "downloader": Downloader(session, progress_bar=None),
                "use_user_site": False,
            }
        )
    else:
        kwargs["progress_bar"] = None

    preparer = RequirementPreparer(
        build_dir=None,
        download_dir=None,
        src_dir=None,
        wheel_download_dir=None,
        build_isolation=True,
        req_tracker=req_tracker,
        **kwargs
    )

    def prepare_editable_reqs(req):
        if PIP_VERSION >= V("20.0"):
            return preparer.prepare_editable_requirement(req)
        else:
            return preparer.prepare_editable_requirement(
                req, False, False, finder
            )

    return prepare_editable_reqs
