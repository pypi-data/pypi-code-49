from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge, factor_cmap
import numpy as np

CHAN_LIST = ['Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5', 'Ch6', 'Ch7', 'Ch8']


output_file("periodic.html")

init_data = {'channel': CHAN_LIST,
             'impedance': ['NA' for i in range(1, len(CHAN_LIST)+1)],
             'row': ['1' for i in range(1, len(CHAN_LIST)+1)]}

source = ColumnDataSource(data=init_data)


p = figure(plot_width=600, plot_height=300, title="Impedance",
           x_range=list(reversed(CHAN_LIST)), y_range=[str(1)], toolbar_location=None)



show(p)
