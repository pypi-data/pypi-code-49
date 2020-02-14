import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from ipywidgets import fixed
from ipywidgets import interactive
from ipywidgets import SelectionSlider

from ..plotting import p_ball_plot
from ..utils import throw_darts


def p_ball_widget(callback):
    """
    callback is intended to be the dart_did_land_in_ball function students making in the notebook
    """
    figure = plt.figure()
    axis = figure.add_subplot(111)

    non_log_scale = np.concatenate(
        [np.linspace(0, 1, 51), np.linspace(1, 3, 26)[1:], np.linspace(3, 10, 26)[1:]]
    )
    values_of_p = np.round(2 ** non_log_scale, decimals=2)

    slider_options = {
        "options": values_of_p,
        "value": 2,
        "description": "p",
        "continuous_update": False,
    }
    plot_options = {
        "figure": fixed(figure),
        "axis": fixed(axis),
        "trials": fixed(10000),
        "callback": fixed(callback),
    }

    widget = interactive(
        p_ball_plot, p=SelectionSlider(**slider_options), **plot_options
    )
    return widget


class p_ball_widget_3d(widgets.VBox):
    def __init__(self, callback, num_trials=10000):
        self.callback = callback
        self.num_trials = num_trials

        non_log_scale = np.concatenate(
            [
                np.linspace(0, 1, 51),
                np.linspace(1, 3, 26)[1:],
                np.linspace(3, 10, 26)[1:],
            ]
        )
        values_of_p = np.round(2 ** non_log_scale, decimals=2)
        slider_options = {
            "options": values_of_p,
            "value": 2,
            "description": "p",
            "continuous_update": False,
        }
        self.slider = widgets.SelectionSlider(**slider_options)
        self.slider.observe(self.p_event, names="value")

        self.generate_data(self.slider.value)

        axis_settings = {"range": [-1.0, 1.0], "tickmode": "linear", "dtick": 0.5}
        axis_titles = {
            "xaxis_title": "$x_1$",
            "yaxis_title": "$x_2$",
            "zaxis_title": "$x_3$",
        }

        figure = go.Figure()
        figure.add_trace(
            go.Scatter3d(
                x=self.darts_in["First Dimension"].values,
                y=self.darts_in["Second Dimension"].values,
                z=self.darts_in["Third Dimension"].values,
                mode="markers",
                marker={"size": 1.5, "opacity": 0.7},
            )
        )
        figure.add_trace(
            go.Scatter3d(
                x=self.darts_out["First Dimension"].values,
                y=self.darts_out["Second Dimension"].values,
                z=self.darts_out["Third Dimension"].values,
                mode="markers",
                marker={"size": 1.5, "opacity": 0.7},
            )
        )
        figure.update_layout(
            title="The ratio of the L-{} unit ball to box is {}".format(
                self.slider.value, self.ball_to_box_ratio
            ),
            showlegend=False,
            # https://plot.ly/python/custom-buttons/
            updatemenus=[
                go.layout.Updatemenu(
                    type="buttons",
                    direction="right",
                    buttons=[
                        {
                            "label": "All Points",
                            "method": "update",
                            "args": [
                                {"visible": [True, True]},
                                # {"title" : "All Points (Including Those Outside the Ball)"}
                            ],
                        },
                        {
                            "label": "Inside Only",
                            "method": "update",
                            "args": [
                                {"visible": [True, False]},
                                # {"title": "Points Inside the Ball Only"}
                            ],
                        },
                    ],
                )
            ],
        )
        figure.update_layout(
            scene={
                "aspectmode": "cube",
                "xaxis": axis_settings,
                "yaxis": axis_settings,
                "zaxis": axis_settings,
                "xaxis_title": "x1",
                "yaxis_title": "x2",
                "zaxis_title": "x3",
            }
        )
        self.figure = go.FigureWidget(figure)

        # 21 chunks, each of length 5% except for two edge chunks of length 2.5%
        slice_slider_options = {
            "value": 0.5,
            "step": 0.05,
            "min": 0,
            "max": 1.0,
            "continuous_update": False,
        }
        self.slice_slider = widgets.FloatSlider(**slice_slider_options)
        self.slice_slider.observe(self.slice_event, names="value")

        self.slice_data(self.slice_slider.value)
        slice_figure = go.Figure(
            data=go.Scatter3d(
                x=self.darts_slice["First Dimension"].values,
                y=self.darts_slice["Second Dimension"].values,
                z=self.darts_slice["Third Dimension"].values,
                mode="markers",
                marker={"size": 1.5, "opacity": 0.7},
            )
        )
        slice_figure.update_layout(
            title="Cross section centered at {}% plus or minus 2.5%".format(
                int(round(self.slice_slider.value * 100))
            )
        )

        slice_figure.update_layout(
            scene={
                "aspectmode": "cube",
                "xaxis": axis_settings,
                "yaxis": axis_settings,
                "zaxis": axis_settings,
                "xaxis_title": "x1",
                "yaxis_title": "x2",
                "zaxis_title": "x3",
            }
        )

        self.slice_figure = go.FigureWidget(slice_figure)

        super().__init__(
            children=[self.slider, self.figure, self.slice_slider, self.slice_figure]
        )

    def p_event(self, change):
        self.update_p(change.new)
        self.update_slice(self.slice_slider.value)

    def slice_event(self, change):
        self.update_slice(change.new)

    def update_p(self, p):
        # https://plot.ly/python/slider-widget/#sliders-with-3d-plots
        self.generate_data(p)

        self.figure.data[0].x = self.darts_in["First Dimension"].values
        self.figure.data[0].y = self.darts_in["Second Dimension"].values
        self.figure.data[0].z = self.darts_in["Third Dimension"].values

        self.figure.data[1].x = self.darts_out["First Dimension"].values
        self.figure.data[1].y = self.darts_out["Second Dimension"].values
        self.figure.data[1].z = self.darts_out["Third Dimension"].values

        self.figure.layout.title.text = "The ratio of the L-{} unit ball to box is {}".format(
            p, self.ball_to_box_ratio
        )

    def update_slice(self, quantile_number):
        self.slice_data(quantile_number)

        self.slice_figure.data[0].x = self.darts_slice["First Dimension"].values
        self.slice_figure.data[0].y = self.darts_slice["Second Dimension"].values
        self.slice_figure.data[0].z = self.darts_slice["Third Dimension"].values

        self.slice_figure.layout.title.text = "Cross section centered at {}% plus or minus 2.5%".format(
            int(round(quantile_number * 100))
        )

    def generate_data(self, p):
        self.darts = throw_darts(self.num_trials, lambda: self.callback(p))
        self.darts_in = self.darts.loc[self.darts["Inside Ball"] == True]
        self.darts_out = self.darts.loc[self.darts["Inside Ball"] == False]

        self.ball_to_box_ratio = len(self.darts_in) / len(self.darts)

    def slice_data(self, quantile_number):
        # 21 chunks, each of length 5% except for two edge chunks of length 2.5%
        # then take data that's within +- 2.5% of the center value
        upper_bound = 2 * (quantile_number + 0.025) - 1
        lower_bound = 2 * (quantile_number - 0.025) - 1
        # slice along xz plane since z plane is compressed out for 2d plots
        # and want slicing for 2d to also work and return 1d things
        upper_mask = self.darts_in["Second Dimension"] <= upper_bound
        lower_mask = self.darts_in["Second Dimension"] >= lower_bound
        self.darts_slice = self.darts_in.loc[lower_mask & upper_mask]
        self.darts_slice["Second Dimension"].values[:] = 2 * quantile_number - 1
