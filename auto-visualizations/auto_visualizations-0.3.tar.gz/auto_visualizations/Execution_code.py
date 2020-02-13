# Import all children class modules and set alias

from auto_visualizations import Histogramvisualization as hist
from auto_visualizations import Barchartvisualization as bar
from auto_visualizations import Bubblechartvisualization as bubble
from auto_visualizations import Piechartvisualization as pie

# Create objects of the classes and call respective methods
visual_hist = hist.Histogram()
visual_hist.plot_hist('test_data.csv', 'EMPID')

visual_bar = bar.Barchart()
visual_bar.plot_bar('test_data.csv', 'EMPID', 'Sales')
visual_bar.plot_stacked_bar('test_data.csv', 'EMPID', 'Sales')

visual_bubble = bubble.Bubblechart()
visual_bubble.plot_bubble('test_data.csv', 'EMPID', 'Sales')

visual_pie = pie.Piechart()
visual_pie.plot_pie('test_data.csv', 'EMPID', 'Sales')
