from pathlib import Path

import matplotlib
from numpy import array_equal
from tests.test_plots.test_plots_tear_down import TestPlotTearDown

from openqlab import io
from openqlab.plots.frequency_domain import relative_input_noise

filedir = Path(__file__).parent
datadir = filedir / "data"


class TestRelativeInputNoise(TestPlotTearDown):
    def setUp(self):
        files = [datadir / f"flipper{i}.TXT" for i in range(1, 4)]
        self.data = io.read(files)

    def test_default_values(self):
        plot = relative_input_noise(self.data, 6)
        self.assertIsInstance(plot, matplotlib.axes.Axes)
        self.assertEqual(plot.get_ylabel(), r"RIN ($1/\sqrt{\mathrm{Hz}}$)")
        self.assertEqual(plot.get_xlabel(), "Frequency (Hz)")
        self.assertEqual(plot.get_title(), "")
        self.assertEqual(plot.get_xscale(), "log")
        self.assertEqual(plot.get_yscale(), "log")

    def test_different_parameters(self):
        plot = relative_input_noise(
            self.data,
            6.5,
            logf=False,
            logy=False,
            title="testtitle",
            ylabel="testylabel",
        )
        self.assertEqual(plot.get_ylabel(), "testylabel")
        self.assertEqual(plot.get_title(), "testtitle")
        self.assertEqual(plot.get_xscale(), "linear")
        self.assertEqual(plot.get_yscale(), "linear")

    def test_kwargs(self):
        plot = relative_input_noise(self.data, 6.5, figsize=(4, 3))
        self.assertTrue(array_equal(plot.figure.get_size_inches(), [4, 3]))
