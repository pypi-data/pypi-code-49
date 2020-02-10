from __future__ import annotations

from json import dumps
from .data import ServerData, DatasetData
from typing import List, Optional, Dict, Any, Tuple


class Chartisan:
    """
    Represents a chartisan chart instance.
    """

    def __init__(self, serverData: ServerData) -> Chartisan:
        """
        Creates a new instance of a chartisan chart.
        """
        self._serverData = serverData

    @staticmethod
    def build() -> Chartisan:
        """
        Creates a new instance of a chartisan chart.
        """
        return Chartisan(ServerData())

    def labels(self, labels: List[str]) -> Chartisan:
        """
        Sets the chart labels.
        """
        self._serverData.chart.labels = labels
        return self

    def extra(self, extra: Dict[str, Any]) -> Chartisan:
        """
        Adds extra information to the chart.
        """
        self._serverData.chart.extra = extra
        return self

    def advancedDataset(self, name: str, values: List[float], extra: Optional[Dict[str, Any]]) -> Chartisan:
        """
        AdvancedDataset appends a new dataset to the chart or modifies an existing one.
        If the ID has already been used, the dataset will be replaced with this one.
        """
        dataset = self._getDataset(name)
        if dataset:
            dataset.name = name
            dataset.values = values
            dataset.extra = extra
        else:
            self._serverData.datasets.append(DatasetData(name, values, extra))
        return self

    def dataset(self, name: str, values: List[float]) -> Chartisan:
        """"
        Dataset adds a new simple dataset to the chart. If more advanced control is
        needed, consider using `AdvancedDataset` instead.
        """
        return self.advancedDataset(name, values, None)

    def toJSON(self) -> str:
        """
        Returns the string representation JSON encoded.
        """
        json = self._serverData.__dict__
        json['chart'] = json['chart'].__dict__
        for i in range(len(json['datasets'])):
            json['datasets'][i] = json['datasets'][i].__dict__
        return dumps(self._serverData.__dict__)

    def toObject(self) -> ServerData:
        """
        Transforms it to an object.
        """
        return self._serverData

    def _getDataset(self, name: str) -> Optional[DatasetData]:
        """
        Gets the dataset with the given name.
        """
        for dataset in self._serverData.datasets:
            if dataset.name == name:
                return dataset
        return None
