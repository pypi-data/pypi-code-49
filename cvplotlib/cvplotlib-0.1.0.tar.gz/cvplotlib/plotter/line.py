import numpy as np

from cvplotlib.plotter.base import BasePlotter


class LinePlotter(BasePlotter):

    def __init__(self, *args, fill_between_std: bool = True, **kwargs):
        super(LinePlotter, self).__init__(*args, **kwargs)

        self.fill_between_std = fill_between_std

    def _plot_setup(self, ax, metric, setup):
        data = self.data.get_setup(metric, setup)
        data = np.array(data)
        if len(data) == 0:
            return

        data_mean = data.mean(axis=0)
        data_std = data.std(axis=0)
        xs = np.arange(len(data_mean))
        ax.plot(xs, data_mean, label=setup)
        if self.fill_between_std:
            ax.fill_between(xs,
                            data_mean - data_std,
                            data_mean + data_std,
                            alpha=.3)

        ax.legend()
