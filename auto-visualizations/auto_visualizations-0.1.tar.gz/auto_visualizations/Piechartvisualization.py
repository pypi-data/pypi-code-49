import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
from .Generalvisualization import Visualization

class Piechart(Visualization):
    
    def __init__(self):
        
        """ Pie chart class for showing distribution of a variable 
        
	    """
        Visualization.__init__(self)
    
    def plot_pie(self, file_name, id_var, metric_var):
        
        """ Plots pie chart for each categorical variables
	
	    Attributes:
		    Dataframe, List of categorical variables and Metric/ Dependent variable
     
        Returns:
            Pie chart with labels
        
	    """
        
        # Call the 'separate_data_types' method from parent class and extract required variables to work with
        
        self.data, self.metric_var, self.categorical_vars, self.quantitative_vars = self.separate_data_types(file_name, id_var, metric_var)
        
       # Loop through all categorical variables and plot against the metric variable
        
        for i in self.categorical_vars:
            
            # Plots in matplotlib reside within a figure object, plt.figure creates new figure

            fig = plt.figure() 
            
            var = self.data.groupby([i]).sum().stack()
            
            temp=var.unstack()
            
            type(temp)
            
            x_list = temp[self.metric_var]
            
            label_list = temp.index
            
            # The pie chart is oval by default. To make it a circle use pyplot.axis("equal")
            
            plt.axis("equal") 
            
            """To show the percentage of each pie slice, pass an output format
            to the autopctparameter plt.
            
            """
            plt.pie(x_list,labels=label_list,autopct="%1.1f%%") 
            
            plt.title("Percentage of {} by {}".format(self.metric_var, i)) 
            
            plt.show()

            