import os
from pathlib import Path
import pandas as pd
import glob


def stack_columns(file, sep=";"):
    """ Stacks all columns of a DataFrame into one, called 'stack' """
    df = pd.read_csv(file, sep=sep, engine="python")
    df = df.stack()
    filename = file[:-4] + "_stacked.csv"
    df.to_csv(filename, index=False, sep=sep, header=False)


def convert_to_heatmap_style(file, sep=";"):
    """
    Converts a file from the validation assays into a R project Heatmap-ready normalized values file
    """
    df = pd.read_csv(file, sep=sep, engine="python")
    df_final = pd.DataFrame(data=[0, 1, 2, 3, 4], columns=["REs"])
    for column in df.columns:
        count_list = []
        for i in [0, 25, 50, 75, 100]:
            count = sum((df[column].values == i))
            count_list.append(count)
        list_sum = sum(count_list)
        count_list[:] = [x / list_sum * 100 for x in count_list]
        df_final[column] = pd.Series(count_list, index=df_final.index)

    filename = file[:-4] + "-normalized.csv"
    df_final.to_csv(filename, index=False, sep=sep)


def pool_main_celltypes_together(dir_, sep=";"):
    """
    Pools the second column from each file in a folder into a new file.
    """

    path = os.path.join(str(Path(__file__).parents[2]), dir_)
    folders = [f for f in glob.iglob(path + "**/*normalized.csv", recursive=True)]
    df_final = pd.DataFrame(data=[0, 1, 2, 3, 4], columns=["REs"])
    for f in folders:
        df = pd.read_csv(f, sep=sep, engine="python")
        df_final[df.columns.values[1]] = df.iloc[:, 1]

    filename = os.path.join(path, "Pooled data.csv")
    df_final.to_csv(filename, index=False, sep=sep)


if __name__ == "__main__":
    # stack_columns("D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/\
    # 3-Vencode/Fantom5/Cross-Validations/Barakat2018/validation control all celltypes - heuristic.csv")

    convert_to_heatmap_style(
        "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/3-Vencode/\
        Fantom5/R projects/Validations/Liu2017_ProstCancer_-sampling.csv")

    # pool_main_celltypes_together("R projects\Validations")
