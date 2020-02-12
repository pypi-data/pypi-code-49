import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
from .Generalvisualization import Visualization

class Histogram(Visualization):
    
    def __init__(self):
        
        """ Histogram class for showing the distribution of continuous 
        variables
	
	    """
        Visualization.__init__(self)
    
    def plot_hist(self, file_name, id_var, metric_var = None):
        
        """ Plots distributions of all quantitative variables in the dataframe
	
	    Attributes:
		    Dataframe, List of quantitative variables
     
        Returns:
            Histograms with labels
        
	    """
        
        # Call the 'separate_data_types' method from parent class and extract required variables to work with
        
        self.data, self.metric_var, self.categorical_vars, self.quantitative_vars = self.separate_data_types(file_name, id_var, metric_var)
        
        # Loop through all quantitative variables and plot the histograms
        
        for i in self.quantitative_vars:
            
            # Plots in matplotlib reside within a figure object, plt.figure creates new figure

            fig = plt.figure() 

            # Create one or more subplots using add_subplot, because you can't create blank figure

            ax = fig.add_subplot(1,1,1)

            # bins = "auto" uses the maximum of the Sturges and Freedman-Diaconis bin choice.
            
            ax.hist(self.data[i], bins = 'auto')
            
            # Labels

            plt.title('{} Distribution'.format(i))
            
            plt.xlabel(i)
            
            plt.ylabel('Count')
            
            plt.show()
                        