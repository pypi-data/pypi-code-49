from .core import *

# module level doc-string
__doc__ = """
broompy - a simple data cleaning tool for Python
===================================================

**broompy** is a Python library designed to help 
data scientists observe a summary of their 
Dataset and facilitate data cleaning. It reveals 
features that require cleaning or inspection. 
This library also displays charts to view the normal 
approximation of variable distributions and generates 
scatter plot to visualize correlation.

https://github.com/juanduranc/broompy

Main Features
-------------
  - Display count of null and available data.
  - Display mean, median and 1.5 IQR outliers count.
  - Identify data types of each variable.
  - Identify count of unique values per variable.
  - Identify the normal approximation using pvalue.
  - Show a dataset sample to understand data content.
  - Visualize trends with histograms and scatter plot.
"""