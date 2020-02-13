import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools

class Visualization:
    
    def __init__(self):
        
        """Generic visualization class for commonly used visualization techniques
	
        """
    
    def read_data_file(self, file_name):
        
        """Function to read in data from a csv file.
				
		Args:
			file_name (string): name of a file to read from
		
		Returns:
			Dataframe
		
		"""
        
        self.data = pd.read_csv(file_name)
        
        # Check if the data frame is empty, if so, throw an error
        
        if not self.data.empty:
            pass
            # print(self.data)
            
        else:
            sys.exit('The dataframe is empty')
    
        return self.data
    
    def separate_data_types(self, file_name, id_var, metric_var):
        
        """Function to separate quantitative and categorical variables, drop id column from analysis
        
        Args:
			file_name (string): name of a file to read from, 
            id_var (string): name of the ID column
            metric_var (string): name of the dependent variable
		
		Returns:
			Dataset, Dependent Variable, Lists of Quantitative and Categorical variables
        
        """
        self.data = self.read_data_file(file_name)
        self.id_var = id_var
        self.metric_var = metric_var
        
        self.data = self.data.drop([self.id_var], axis=1)
        
        self.quantitative_vars = []
        self.categorical_vars = []
        
        for i in list(self.data):
            if np.issubdtype(self.data[i].dtype, np.number) == True:
                self.quantitative_vars.append(i)
            else:
                self.categorical_vars.append(i)
                
        return self.data, self.metric_var, self.categorical_vars, self.quantitative_vars 
    