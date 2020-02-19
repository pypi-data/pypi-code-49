from pathlib import Path

import matplotlib
from tests.test_plots.test_plots_tear_down import TestPlotTearDown

from openqlab import io
from openqlab.plots.frequency_domain import power_spectrum

filedir = Path(__file__).parent
datadir = filedir / "data"


class TestPowerSpectrum(TestPlotTearDown):
    def setUp(self):
        self.data = io.read(datadir / "power_spectrum.txt")

    def test_default_plot(self):
        plot = power_spectrum(self.data)
        self.assertIsInstance(plot, matplotlib.figure.Figure)

    def test_normalize_to(self):
        plot = power_spectrum(self.data, normalize_to=2 * self.data.iloc[0])
        self.assertIsInstance(plot, matplotlib.figure.Figure)
