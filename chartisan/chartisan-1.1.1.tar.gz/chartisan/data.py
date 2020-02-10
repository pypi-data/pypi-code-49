from __future__ import annotations

from typing import List, Optional, Dict, Any


class ChartData:
    """"
    Represents the chart information.
    """

    def __init__(self) -> ChartData:
        """
        Creates a new chart data instance.
        """
        self.labels: List[float] = []
        self.extra: Optional[Dict[str, Any]] = None


class DatasetData:
    """
    Represents the dataset information.
    """

    def __init__(self, name: str, values: List[float], extra: Optional[Dict[str, Any]]) -> DatasetData:
        """
        Creates a new instance of DatasetData.
        """
        self.name = name
        self.values = values
        self.extra = extra


class ServerData:
    """
    ServerData represents how the server is expected
    to send the data to the chartisan client.
    """

    def __init__(self) -> ServerData:
        """
        Creates a new instance of a server data.
        """
        self.chart = ChartData()
        self.datasets: List[DatasetData] = []
