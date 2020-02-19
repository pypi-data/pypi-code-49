from pathlib import Path

import matplotlib.pyplot as plt
from tests.test_plots.test_plots_tear_down import TestPlotTearDown

from openqlab import io, plots

filedir = Path(__file__).parent
datadir = filedir / "data"


class TestTimeDomain(TestPlotTearDown):
    def setUp(self):
        self.data = io.read(datadir / "20180606_001.csv")

    def test_scope(self):
        plots.scope(self.data)
        fig = plots.scope(self.data.iloc[:, 0])
        self.assertIsInstance(fig, plt.Figure)

    def test_scope_4_traces(self):
        data = io.read(datadir / "traces_4.csv")
        fig = plots.scope(data)
        self.assertIsInstance(fig, plt.Figure)

    def test_scope_5_traces(self):
        data = io.read(datadir / "traces_5.csv")
        with self.assertRaises(Exception):
            plots.scope(data)

    def test_zero_span(self):
        data = io.read(datadir / "zero_span.csv")
        data = data.rename(columns={"zero_span_1": "vac"})
        print(data.head())
        fig = plots.zero_span(data)
        self.assertIsInstance(fig, plt.Figure)
