# Import all children class modules and set alias

import .Histogramvisualization as hist
import .Barchartvisualization as bar
import .Bubblechartvisualization as bubble
import .Piechartvisualization as pie

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
