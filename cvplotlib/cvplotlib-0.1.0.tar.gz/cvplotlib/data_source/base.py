from typing import Optional, Sequence, Generator, KeysView
import abc
import contextlib

from collections import OrderedDict
from typing import Dict
from typing import List
from typing import NewType
from typing import Union
from typing import Tuple


class BaseDataSource(abc.ABC):
    """docstring for BaseDataSource"""

    def __init__(self, *args, **kwargs) -> None:
        super(BaseDataSource, self).__init__()

        self._data: Data = Data()
        self.preprocess()
        self.load_data()
        self.postprocess()

    @property
    def data(self):
        return self._data

    @abc.abstractmethod
    def load_data(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def preprocess(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def postprocess(self) -> None:
        raise NotImplementedError

    def __iter__(self):
        for metric, run_values in self.data.items():
            yield metric, run_values

    def __len__(self):
        return len(self.data)


class Data(OrderedDict):
    """Extension of the OrderedDict class.

    Attributes:
        _current_metric:
        _current_setup:

    """

    def __init__(self, *args, **kwargs) -> None:
        super(Data, self).__init__(*args, **kwargs)

        self._current_metric: Optional[str] = None
        self._current_setup: Optional[str] = None

    def get_metric(self, metric: str) -> Dict[str, List[List[float]]]:
        """ returns metric data for a given metric """
        return self[metric]

    def get_setup(self, metric: str, setup: str) -> List[List[float]]:
        """ returns metric data for a given metric and setup """
        return self.get_metric(metric)[setup]

    def metrics(self) -> KeysView[str]:
        """ returns metric names"""
        return self.keys()

    def setups(self, metric: str) -> KeysView[str]:
        """ returns setup names for a given metric"""
        return self.get_metric(metric).keys()

    @property
    def metric_data(self) -> Dict[str, List[List[float]]]:
        """ returns currently selected metric data """
        assert self._current_metric is not None, \
            "Please create Data.using_metric(<metric_key>) context!"

        return self[self._current_metric]

    @property
    def setup_data(self) -> List[List[float]]:
        """ returns currently selected setup data """
        assert self._current_setup is not None, \
            "Please create Data.using_setup(<setup_key>) context!"

        return self.metric_data[self._current_setup]

    @contextlib.contextmanager
    def using_metric(self, metric_key: str) -> Generator[None, None, None]:
        """ creates a context, where the given metric is selected """
        if metric_key not in self:
            self[metric_key] = OrderedDict()

        self._current_metric = metric_key
        yield
        self._current_metric = None

    @contextlib.contextmanager
    def using_setup(self, setup_key: str) -> Generator[None, None, None]:
        """ creates a context, where the given setup is selected. needs a metric to be selected before """
        assert self._current_metric is not None, \
            "Please create Data.using_metric(<metric_key>) context before using this context!"

        data = self.metric_data
        if setup_key not in data:
            data[setup_key] = []

        self._current_setup = setup_key
        self.pre_using_setup()
        yield
        self.post_using_setup()
        self._current_setup = None

    def pre_using_setup(self):
        pass

    def post_using_setup(self):
        run_lens = set(map(len, self.setup_data))
        if len(run_lens) == 1:
            # all runs have the same length, so we are fine
            return
        # we have setups or runs with different amount of entries
        max_len = max(run_lens)
        filled_data = []
        for data in self.setup_data:
            # fill missing entries with the last value for each run
            filled_data.append(data +
                               [data[-1] for _ in range(max_len - len(data))])
        self.metric_data[self._current_setup] = filled_data
