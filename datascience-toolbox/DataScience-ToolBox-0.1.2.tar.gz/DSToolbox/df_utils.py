'''
Utility functions for working with DataFrames
'''

import pandas
import numpy
import matplotlib.pyplot


class Explore:
    def __init__(self, dataframe):
        pass


    def display_all(self, dataframe):
        '''
        Function to set notebook display options
        Arguments
        =========
        dataframe: pandas dataframe
        Returns
        =======
        Pandas dataframe with max rows and cols of 1000
        '''
        with pd.option_context("display.max_rows", 1000):
            with pd.option_context("display.max_columns", 1000):
                display(dataframe)


    def categorical_summarized(self, dataframe, x=None, y=None, hue=None, palette='Set1', verbose=True):
        '''
        Helper function that gives a quick summary of a given column of categorical data
        Arguments
        =========
        dataframe: pandas dataframe
        x: str. horizontal axis to plot the labels of categorical data, y would be the count
        y: str. vertical axis to plot the labels of categorical data, x would be the count
        hue: str. if you want to compare it another variable (usually the target variable)
        palette: array-like. Colour of the plot
        Returns
        =======
        Quick Stats of the data and also the count plot
        '''
        if x == None:
            column_interested = y
        else:
            column_interested = x
        series = dataframe[column_interested]
        print(series.describe())
        print('mode: ', series.mode())
        if verbose:
            print('='*80)
            print(series.value_counts())

        sns.countplot(x=x, y=y, hue=hue, data=dataframe, palette=palette)
        plt.show()


    def quantitative_summarized(self, dataframe, x=None, y=None, hue=None, palette='Set1', ax=None, verbose=True, swarm=False):
        '''
        Helper function that gives a quick summary of quantattive data
        Arguments
        =========
        dataframe: pandas dataframe
        x: str. horizontal axis to plot the labels of categorical data (usually the target variable)
        y: str. vertical axis to plot the quantitative data
        hue: str. if you want to compare it another categorical variable (usually the target variable if x is another variable)
        palette: array-like. Colour of the plot
        swarm: if swarm is set to True, a swarm plot would be overlayed
        Returns
        =======
        Quick Stats of the data and also the box plot of the distribution
        '''
        series = dataframe[y]
        print(series.describe())
        print('mode: ', series.mode())
        if verbose:
            print('='*80)
            print(series.value_counts())

        sns.boxplot(x=x, y=y, hue=hue, data=dataframe, palette=palette, ax=ax)

        if swarm:
            sns.swarmplot(x=x, y=y, hue=hue, data=dataframe,
                          palette=palette, ax=ax)

        plt.show()
