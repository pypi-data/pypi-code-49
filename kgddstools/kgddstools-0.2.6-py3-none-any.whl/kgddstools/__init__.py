import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def plot_cont(input_df, cols):
    print(cols)

def plot_cat(input_df, cols):
    print(cols)

def eda(input_df, target_var, type, cat = [], cont = []):

    if type == 'df_summary':
        #missingno, etc.

        #Spit out column names

        print('zzzzzz')

    elif type == 'var_plots':
        if(len(cat) >= 1):
            print('cat var')

            plot_cat(input_df, cols = cat)

        if(len(cont) >= 1):
            print('cont var')

            plot_cont(input_df, cols = cont)

        elif (len(cat) + len(cont)) == 0:
            raise ValueError("You need to define at least column in a list via either cat or cont arguments.")
    else:
        raise ValueError("Inputs for type are 'df_summary' and 'var_plots'.")
