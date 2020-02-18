import numpy as np

from typing import Callable
from typing import List
from typing import Tuple

from itertools import starmap
from tabulate import tabulate

from cvplotlib.plotter.base import BasePlotter


class BoxPlotter(BasePlotter):

    def __init__(self,
                 *args,
                 showfliers: bool = False,
                 print_statistics: bool = False,
                 data_selection: Callable = lambda data: data[:, -1],
                 setup_to_label: Callable = lambda setup: str(setup),
                 **kwargs):
        super(BoxPlotter, self).__init__(*args, **kwargs)

        self.showfliers = showfliers
        self.print_statistics = print_statistics
        self.data_selection = data_selection
        self.setup_to_label = setup_to_label

    def _plot_setup(self, ax, metric, setup):
        pass

    def transform(self, setup, data) -> Tuple[str, List[float]]:
        data = np.array(data)
        return self.setup_to_label(setup), self.data_selection(data)

    def _plot_metric(self, ax, metric):
        ax.set_title(f"Metric: {metric}")
        data = self.data.get_metric(metric)
        labels, values = zip(*starmap(self.transform, data.items()))

        ax.boxplot(values, labels=labels, showfliers=self.showfliers)

        if not self.print_statistics:
            return

        data = []

        # print(f"Metric \"{metric}\"")
        for lab, vals in zip(labels, values):
            data.append([lab, f"{vals.mean():.2%}", f"\u00B1 {vals.std():.2%}"])
            # print(f"{lab:<10s} (\u00B1 {vals.std():.2%})")

        tab = tabulate(data,
                       headers=["Label", "Mean Value", "Value Std"],
                       tablefmt="fancy_grid")
        print(tab)
