import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
from .Generalvisualization import Visualization

class Bubblechart(Visualization):
    
    def __init__(self):
        
        """ Bubble chart class for showing correlation between two or more continuous variables
        
	    """
        Visualization.__init__(self)
    
    def plot_bubble(self, file_name, id_var, metric_var):
        
        """ Plots relation between two continuous variables and uses a metric/ dependent 
        variable as size of the bubbles
	
	    Attributes:
		    Dataframe, List of quantitative variables
     
        Returns:
            Scatter plot with bubble sizes indicating dependent variable
        
	    """
        
        # Call the 'separate_data_types' method from parent class and extract required variables to work with
        
        self.data, self.metric_var, self.categorical_vars, self.quantitative_vars = self.separate_data_types(file_name, id_var, metric_var)
        
        # Loop through all continuous variable combinations and create bubble plots
        
        for L in range(2, 3):
            
            for subset in itertools.permutations(self.quantitative_vars, L):
            
            # Plots in matplotlib reside within a figure object, plt.figure creates new figure

                fig = plt.figure() 

                # Create one or more subplots using add_subplot, because you can't create blank figure

                ax = fig.add_subplot(1,1,1)

                # Scatter plot of 2 variables and third variable is size of the bubble
                
                ax.scatter(self.data[subset[0]], self.data[subset[1]], 
                           s = self.data[list(set(self.quantitative_vars)-set(subset))]) 

                plt.title('Bubble Chart')
                
                plt.xlabel(subset[0])
                
                plt.ylabel(subset[1])
                
                plt.text(0.5, 
                         0.9, 
                         'Bubble Size indicates {}'.format(set(self.quantitative_vars)-set(subset)),
                         transform=plt.gca().transAxes
                )
                
                plt.show()
                      