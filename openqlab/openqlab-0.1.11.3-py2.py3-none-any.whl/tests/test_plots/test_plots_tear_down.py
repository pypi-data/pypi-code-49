from unittest import TestCase

import matplotlib.pyplot as plt


class TestPlotTearDown(TestCase):
    def tearDown(self) -> None:
        figs = list(map(plt.figure, plt.get_fignums()))
        for fig in figs:
            plt.close(fig)
