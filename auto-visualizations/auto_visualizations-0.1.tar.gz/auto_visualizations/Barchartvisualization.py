import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
from .Generalvisualization import Visualization

class Barchart(Visualization):
    
    def __init__(self):
        
        """ Bar chart class for showing the distribution of categorical variables
			
	    """
        Visualization.__init__(self)
    
    def plot_bar(self, file_name, id_var, metric_var):
        
        """ Plots sum of metric variable for all categorical variables
	
	    Attributes:
		    Dataframe, List of categorical variables and Metric/ Dependent variable
     
        Returns:
            Bar chart with labels
        
	    """
        
        # Call the 'separate_data_types' method from parent class and extract required variables to work with
        
        self.data, self.metric_var, self.categorical_vars, self.quantitative_vars = self.separate_data_types(file_name, id_var, metric_var)
        
       # Loop through all categorical variables and plot against the metric variable
        
        for i in self.categorical_vars:
            
            var = self.data[self.metric_var].groupby(self.data[i]).sum()
        
            # Plots in matplotlib reside within a figure object, plt.figure creates new figure
        
            fig = plt.figure() 
        
            # Create one or more subplots using add_subplot, because you can't create blank figure
      
            ax = fig.add_subplot(1,1,1)
        
            # Plot bars for the variables with labels
            
            ax.set_xlabel('{}'.format(i))
            
            ax.set_ylabel('Sum of {}'.format(self.metric_var))
            
            ax.set_title('{} wise Sum of {}'.format(i, self.metric_var))
            
            var.plot(kind = 'bar', color = 'green')
            
    def plot_stacked_bar(self, file_name, id_var, metric_var = None):
        
        """ Plots sum of metric variable for all combinations of categorical variables
	
	    Attributes:
		    Dataframe, List of categorical variables and Metric/ Dependent variable
     
        Returns:
            Bar chart with labels
        
	    """
        
        # Call the 'separate_data_types' method from parent class and extract required variables to work with
        
        self.data, self.metric_var, self.categorical_vars, self.quantitative_vars = self.separate_data_types(file_name, id_var, metric_var)
       
        # Loop through all categorical variable combinations and plot against the metric variable

        # Take only 2 variable combinations for ease
        
        for L in range(2, 3):
            
            for subset in itertools.combinations(self.categorical_vars, L):
                
                var = self.data.groupby(list(subset))[self.metric_var].sum()
                
                var.unstack().plot(kind = 'bar',
                                   stacked = True, 
                                   grid = False, 
                                   title = 'Stacked bar chart of {} and {} against sum of {}'\
                                   .format(subset[0], subset[1],self.metric_var)
                             )
        