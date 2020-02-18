import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def plot_cont(input_df_cont, cont_cols, target_var):
    for c in cont_cols:
        print(c)
        sns.kdeplot(input_df_cont[c])

def plot_cat(input_df_cat, cat_cols, target_var):
    for c in cat_cols:
        print(c)
        sns.countplot(x = input_df_cat[c], data = input_df_cat, hue = target_var)
        plt.show()

def eda(input_df, target_var, eda_type, cat, cont):

    if eda_type == 'df_summary':
        #missingno, etc.

        #Spit out column names

        print('zzzzzz')

    elif eda_type == 'var_plots':
        if (len(cat) + len(cont)) >= 1:
            if (len(cat) >= 1):
                print('cat var')

                plot_cat(input_df_cat = input_df, cat_cols = cat, target_var = target_var)

            if (len(cont) >= 1):
                print('cont var')

                plot_cont(input_df_cont = input_df, cont_cols = cont, target_var = target_var)
        else:
            raise ValueError("You need to define at least column in a list via either cat or cont arguments.")
    else:
        raise ValueError("Inputs for type are 'df_summary' and 'var_plots'.")
