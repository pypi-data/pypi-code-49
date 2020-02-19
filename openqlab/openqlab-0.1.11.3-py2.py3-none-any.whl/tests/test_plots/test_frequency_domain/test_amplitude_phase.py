from pathlib import Path

import matplotlib
from tests.test_plots.test_plots_tear_down import TestPlotTearDown

from openqlab import io, plots
from openqlab.plots.frequency_domain import amplitude_phase

filedir = Path(__file__).parent
datadir = filedir / "data"


class TestAmplitudePhase(TestPlotTearDown):
    def setUp(self):
        self.data = io.read(datadir / "scope_0.csv")

    def test_default_plot(self):
        plot = amplitude_phase(self.data["Gain (dB)"], self.data["Phase (deg)"])
        self.assertIsInstance(plot, matplotlib.figure.Figure)

    def test_bodeplot_false(self):
        plot = amplitude_phase(
            self.data["Gain (dB)"], self.data["Phase (deg)"], bodeplot=False
        )
        self.assertIsInstance(plot, matplotlib.figure.Figure)

    def test_dbunits_false(self):
        plot = amplitude_phase(
            self.data["Gain (dB)"], self.data["Phase (deg)"], dbunits=False
        )
        self.assertIsInstance(plot, matplotlib.figure.Figure)

    def test_clamp_phase_warns(self):
        with self.assertWarns(DeprecationWarning):
            plots.frequency_domain._clamp_phase(4)
