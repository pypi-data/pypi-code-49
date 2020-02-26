import warnings
from collections import OrderedDict
from typing import Dict

from dli.models.paginator import Paginator
from dli.client.components.urls import me_urls, search_urls, package_urls
from dli.models.package import PackageModel


class PackageModule:

    def __call__(self, search_term=None, only_mine=True) \
            -> Dict[str, PackageModel]:
        """
        See packages we can access at the top level.

        :param str search_term: The search phrase to search the catalogue
        with, and to pull back packages based on name, description etc.

        :param bool only_mine: Specify whether to collect packages only
        accessible to you (user) or to discover packages that you may
        want to discover.

        :returns: Ordered dictionary of id to PackageModel.
        :rtype: OrderedDict[id: str, PackageModel]
        """

        if only_mine:
            p = Paginator(me_urls.consumed_packages, self._client._Package)
        else:
            p = Paginator(search_urls.search_packages,  self._client._Package)

        # todo this should change to (v.shortcode, v) in future
        return OrderedDict([(v.name, v) for v in p])

    def _get(self, short_code) -> PackageModel:
        """
        Find a PackageModel with the matching short code. If not found then
        returns None.

        :param str short_code: The short code of the package to collect
        :returns: PackageModel with matching short code.
        :rtype: PackageModel
        """
        warnings.warn(
            'Getting a dataset by name, and package name or package ID'
            'will be deprecated in future. Short-codes will replace this.',
            PendingDeprecationWarning
        )
        params = {}

        # todo this should be by short code but EP doesnt seem to exist for this yet
        # so pass p_id
        params["package_id"] = short_code
        response = self._client.session.get(
            package_urls.package_index, params=params
        )
        return self._client._Package(response.json())