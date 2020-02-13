import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import dabl

def (some_df):

    sns.set()

    print("Hello world")

    df_types = dabl.detect_types(some_df)

    print(type(df_types))

    print(df_types)

    for index, col in enumerate(some_df.columns):

        fig, axs = plt.subplots(len(some_df.columns), 1, figsize = (15, len(some_df)*5))

        axs.plot(plot_cat(column = some_df[col], target = 0))

        plt.show()

def plot_cat(column, target):
    fig, axs = plt.subplots(1, 3, figsize = (15, 5))

    axs[0, 1].plot(column)
    axs[0, 2].plot(column)
    axs[0, 3].plot(column)

    return fig
