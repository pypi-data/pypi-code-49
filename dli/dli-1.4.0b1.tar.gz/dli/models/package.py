import textwrap
from collections import OrderedDict
from typing import Dict

from dli.models.paginator import Paginator
from dli.client.components.urls import package_urls
from dli.models.dataset import DatasetModel


class PackageModel:
    """
    Represents a package pulled back from Me consumables
    """
    def __init__(self, json):
        self.id = json["properties"]["packageId"]
        self.name = json["properties"].get("name", None)
        if json["properties"].get("data", None):
            # we have a package_access_request json
            root = json["properties"]["data"]
        else:
            # we have a package json
            root = json["properties"]

        self.description = root.get("description", "")
        self.sensitivity = root.get("dataSensitivity", "")
        self.keywords = ", ".join(root.get("keywords", []))
        self.documentation = root.get("documentation", "No documentation")
        self.has_access = root.get("has_access", "Unknown")
        self._paginator = Paginator(package_urls.v2_package_datasets.format(id=self.id),
                 self._client.Dataset,
                 self._client.Dataset._from_v2_response_unsheathed)
        self.__shape = None

    @property
    def shape(self):
        """
        :returns: Count the number of datasets.
        :rtype: Int
        """
        if self.__shape is None:
            self.__shape = len(self.datasets())
        return self.__shape

    def datasets(self) -> Dict[str, DatasetModel]:
        """
        :returns: Dictionary of datasets in a package.
        :rtype: OrderedDict[id: str, DatasetModel]
        """
        return OrderedDict([
            (v.name, v) for v in self._paginator
        ])

    def display(self):
        """Print information about all the datasets in this package."""
        for p in self.datasets().items():
            print(str(p[1]))

    def __str__(self):
        separator = "-"*80
        split_description = "\n".join(textwrap.wrap(self.description, 80))
        split_keywords = "\n".join(textwrap.wrap(self.keywords, 80))
        split_documentation = "\n".join(textwrap.wrap(self.documentation, 80))
        return f"\nPACKAGE \"{self.name}\" (Contains: {self.shape} datasets)\n" \
               f">> ID: {self.id} \n" \
               f">> Sensitivity: {self.sensitivity} / Accessible: {self.has_access}\n"\
               f"\n" \
               f"{split_description}\n" \
               f"Documentation: {split_documentation}\n\n" \
               f"Keywords: {split_keywords}\n"\
               f"{separator}"

    def __repr__(self):
        return f"{self.id}"