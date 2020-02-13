import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt


class SetUp:
    path_e_values = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
                    "3-Vencode/Fantom5/VEnCodes/A549-atlas 200 val vencodes - samp/" \
                    "lung adenocarcinoma cell line-A549_evalues.csv"

    path_vencodes = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
                    "3-Vencode/Fantom5/VEnCodes/A549-atlas 200 val vencodes - samp"

    path_out_heat = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
                   "3-Vencode/Fantom5/Validations/2- Figures - py/heatmap 200 val vens - A549_samp"

    name_cell_type = "A549"


class ValidatedVEnCodesHeatmap:
    def __init__(self, set_up, to_drop):
        self.set_up = set_up
        self.to_drop = to_drop
        self.e_values = pd.read_csv(set_up.path_e_values, sep=";", engine="python", header=None, names=["chr", "value"])

        files = [f for f in glob.iglob(set_up.path_vencodes + "**/{}.csv".format("*vencode*"), recursive=True)]
        self.df_from_each_file = (pd.read_csv(f, sep=";", engine="python", index_col=0) for f in files)

        self.df_heatmap = self._data_cleaner()

    def _data_generator(self):
        for df in self.df_from_each_file:
            re_ven = tuple(df.index.values)
            cond = [all([True if x in y else False for x in re_ven]) for y in self.e_values["chr"]]
            e_value = self.e_values.loc[cond].value.values[0]
            drop_list = list(range(-self.to_drop, 0))
            df.drop(df.columns[drop_list], axis=1, inplace=True)
            df[df.columns[-1]] = df[df.columns[-1]].map(lambda x: 1)
            df = df.groupby(np.arange(len(df)) // 4).sum()
            df["e-value"] = e_value
            if len(df.index.values) == 1 and isinstance(df["e-value"].values[0], float):
                yield df
            else:
                raise ValueError("Something went wrong while appending e-value to VEnCode")

    def _data_cleaner(self):
        df_concatenated = pd.concat(self._data_generator(), ignore_index=True)
        df_concatenated.sort_values(by="e-value", inplace=True)
        df_concatenated = df_concatenated.append(df_concatenated.sum(numeric_only=True), ignore_index=True)
        df_concatenated.sort_values(by=df_concatenated.index[200], axis=1, inplace=True)
        df_heatmap = df_concatenated.drop("e-value", axis=1)
        df_heatmap = df_heatmap.drop(df_concatenated.index[200], axis=0)
        df_heatmap.rename(columns={df_heatmap.columns[-1]: self.set_up.name_cell_type}, inplace=True)
        return df_heatmap

    def plot(self):
        plt.figure(figsize=(15, 15))
        plot = plt.pcolormesh(self.df_heatmap.T, cmap=plt.cm.get_cmap("inferno_r", 5))
        plt.clim(-0.5, 5 - 0.5)
        plt.yticks(np.arange(0.5, len(self.df_heatmap.T.index), 1), self.df_heatmap.T.index)
        plt.tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            labelbottom=False  # label numbers are removed
        )
        plt.tick_params(
            axis="y",
            which="both",
            labelsize=5  # label number size is reduced to fit
        )
        cbar = plt.colorbar(plot, ticks=range(5), shrink=0.7)
        cbar.ax.tick_params(labelsize=20)
        plt.axes().set_aspect(2)
        plt.savefig(self.set_up.path_out_heat, transparent=True)


if __name__ == "__main__":
    setup = SetUp()
    ven = ValidatedVEnCodesHeatmap(setup, 0)
    ven.plot()
