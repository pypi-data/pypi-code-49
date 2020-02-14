import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import fixed

from ..plotting import does_function_preserve_addition
from ..plotting import does_function_preserve_scalar_multiplication


class scalar_multiplication_widget(widgets.VBox):
    def __init__(self, callback):

        # Set up the slider for the scalar
        scalar_values = np.round(np.linspace(0, 5, num=101), decimals=2)

        scalar_slider_options = {
            "options": scalar_values,
            "value": 1,
            "description": "scalar",
            "continuous_update": False,
        }
        self.scalar_slider = widgets.SelectionSlider(**scalar_slider_options)

        # Set up the slider for the vector
        angle_values = np.round(np.linspace(0, 2 * np.pi, num=100), decimals=2)

        vector_slider_options = {
            "options": angle_values,
            "value": 0,
            "description": "vector (angle from horizontal axis in radians)",
            "continuous_update": False,
        }
        self.vector_slider = widgets.SelectionSlider(**vector_slider_options)

        # Put both sliders on top
        self.sliders = widgets.VBox(children=[self.scalar_slider, self.vector_slider])

        # widget that actually contains the resulting plot
        self.plot_widget = widgets.interactive_output(
            does_function_preserve_scalar_multiplication,
            {
                "angle": self.vector_slider,
                "scalar": self.scalar_slider,
                "function": fixed(callback),
            },
        )

        super().__init__(children=[self.sliders, self.plot_widget])


class addition_widget(widgets.VBox):
    def __init__(self, callback):

        # Set up the sliders for both vectors
        angle_values = np.round(np.linspace(0, 2 * np.pi, num=101), decimals=2)
        vector1_slider_options = {
            "options": angle_values,
            "value": 0,
            "description": "vector 1",
            "continuous_update": False,
        }
        vector2_slider_options = {
            "options": angle_values,
            "value": np.round(np.pi / 2, decimals=2),
            "description": "vector 2",
            "continuous_update": False,
        }
        self.vector1_slider = widgets.SelectionSlider(**vector1_slider_options)
        self.vector2_slider = widgets.SelectionSlider(**vector2_slider_options)

        # Put both sliders on top
        self.sliders = widgets.VBox(children=[self.vector1_slider, self.vector2_slider])

        # widget that actually contains the resulting plot
        self.plot_widget = widgets.interactive_output(
            does_function_preserve_addition,
            {
                "angle1": self.vector1_slider,
                "angle2": self.vector2_slider,
                "function": fixed(callback),
            },
        )

        super().__init__(children=[self.sliders, self.plot_widget])
