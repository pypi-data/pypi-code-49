import warnings
from collections import OrderedDict
from typing import Dict

from dli.models.paginator import Paginator
from dli.client.components.urls import search_urls, dataset_urls
from dli.models.dataset import DatasetModel


class DatasetModule:

    def __call__(self, search_term=None, only_mine=True) \
            -> Dict[str, DatasetModel]:
        """
        See datasets.

        :param str search_term: The search phrase to search the catalogue
        with, and to pull back datasets based on name, description etc.

        :param bool only_mine: Specify whether to collect datasets only
        accessible to you (True) or to discover packages that you may
        want to discover but may not have access to (False).

        If any combination of the two, then search term takes precedence
        of routing, followed by the application of only_mine flag.

        :returns: Ordered dictionary of ids to DatasetModel.
        :rtype: OrderedDict[id: str, DatasetModel]
        """
        p = Paginator(
            search_urls.search_datasets,
            self._client.Dataset,
            self._client.Dataset._from_v1_response_unsheathed
        )

        # todo this should change to (v.shortcode, v) in future
        return OrderedDict([(v.name, v) for v in p])

    def _get(self, short_code) -> DatasetModel:
        """
        Returns a DatasetModel if it exists else None

        :param str short_code: The short code of the dataset to collect

        :returns: Dataset model with matching short code.
        :rtype: DatasetModel
        """
        warnings.warn(
            'Getting a dataset by name, and package name or package ID'
            'will be deprecated in future. Short-codes will replace this.',
            PendingDeprecationWarning
        )
        params = {}

        # todo this should be by short code but EP doesnt seem to exist for this yet
        # so pass d_id
        params["dataset_id"] = short_code
        response = self._client.session.get(
            dataset_urls.v2_instance.format(id=short_code)
        )
        return self._client.Dataset._from_v2_response(response.json())