import abc
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.gridspec import GridSpec
from typing import List
from typing import Tuple

from cvplotlib import config
from cvplotlib.data_source import base


class BasePlotter(abc.ABC):
    """ Base class from which all plotters inherit.

    Attributes:


    """

    def __init__(self, data_source: base.BaseDataSource, *args,
                 **kwargs) -> None:
        super(BasePlotter, self).__init__()
        self.data_source = data_source

    @property
    def data(self):
        return self.data_source.data

    def plot(self):
        # figure and axis creation
        fig, axis = self.prepare_axis()

        # actual plotting
        for ax, metric in zip(axis, self.data.metrics()):
            self._plot_metric(ax, metric)

        # show the plots if wanted
        if not config.no_show:
            self.show()

        return fig, axis

    def prepare_axis(self) -> Tuple[plt.Figure, List[plt.Axes]]:
        n_metrics = len(self.data_source)
        n_cols = int(np.ceil(np.sqrt(n_metrics)))
        n_rows = int(np.ceil(n_metrics / n_cols))

        grid = GridSpec(n_rows, n_cols)

        figure = plt.figure()
        axis = []

        for i, metric in enumerate(self.data.metrics()):
            row, col = np.unravel_index(i, (n_rows, n_cols))
            ax = plt.subplot(grid[row, col])
            axis.append(ax)

        return figure, axis

    def show(self) -> None:
        plt.show()

    def tsplot(self):
        pass

    def _plot_metric(self, ax, metric) -> None:
        ax.set_title(f"Metric: {metric}")
        for i, setup in enumerate(self.data.setups(metric)):
            self._plot_setup(ax, metric, setup)

    @abc.abstractmethod
    def _plot_setup(self, ax, metric, setup) -> None:
        raise NotImplementedError
