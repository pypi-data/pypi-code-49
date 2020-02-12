# Copyright (C) 2018, 2019 Columbia University Irving Medical Center,
#     New York, USA
# Copyright (C) 2019 Novo Nordisk Foundation Center for Biosustainability,
#     Technical University of Denmark

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""Provide functions to plot concentrations and trajectories using pyplot."""


from typing import Dict, List, Optional

import matplotlib.pyplot as plt
from pandas import DataFrame


PALETTE = (  # scheme: http://geog.uoregon.edu/datagraphics/color/Cat_12.txt
    "#ff7f00",  # TODO: maybe use palletable for this
    "#32ff00",  # but I'm not sure if it is worh to install
    "#19b2ff",  # another dependency just for the color scheme
    "#654cff",
    "#e51932",
    "#000000",
    "#ffff32",
    "#ff99bf",
    "#ccbfff",
    "#a5edff",
    "#b2ff8c",
    "#ffff99",
    "#ffbf7f",
)


def plot_concentrations(
    results: DataFrame,
    metabolites: Optional[List[str]] = None,
    biomass: str = "Biomass",
    time: str = "time",
    labels: Optional[Dict[str, str]] = None,
    x_axis_title: str = r"Time $\left[ \mathrm{h} \right]$",
    left_y_axis_title: str = r"Biomass $\left[ \mathrm{g} \, \mathrm{L}^{-1} "
    r"\right]$",
    right_y_axis_title: str = r"Metabolites $\left[ \mathrm{mmol} \, "
    r"\mathrm{L}^{-1} \right]$",
):
    """
    Plot the concentration results of a dynamic FBA simulation.

    The resulting plot can be further customized using ``matplotlib.pyplot``.

    Parameters
    ----------
    results : pandas.DataFrame
        The concentration results of a simulation.
    metabolites : list of strings, optional
        The names of the metabolites in the data frame (default: all columns
        except for time and biomass).
    biomass : str, optional
        The name of biomass in the results (default "Biomass").
    time : str, optional
        The name of the time column in the results (default "time").
    labels : dict, optional
        A mapping from columns names to legend labels (default is the same).
    x_axis_title : str, optional
        The axis title for the horizontal axis (default time).
    left_y_axis_title : str, optional
        The left vertical axis title (default biomass).
    right_y_axis_title : str, optional
        The right vertical axis title (default metabolite concentration).

    """
    if metabolites is None:
        metabolites = results.columns.tolist()
        metabolites.remove(biomass)
        metabolites.remove(time)
    domain = results[time]

    if labels is None:
        labels = {}

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    # The colors of lines on different axes must not overlap.
    ax2.set_prop_cycle("color", PALETTE[1:])
    for name in metabolites:
        label = labels.get(name, name)
        ax2.plot(domain, results[name], linestyle="--", linewidth=0.8, label=label)
    label = labels.get(biomass, biomass)
    ax1.plot(domain, results[biomass], PALETTE[0], linewidth=0.8, label=label)

    ax1.set_xlabel(x_axis_title)
    ax1.set_ylabel(left_y_axis_title)
    ax2.set_ylabel(right_y_axis_title)
    # Set the legend outside the plot area.
    fig.legend(loc="center right", borderaxespad=0.1)
    plt.subplots_adjust(right=0.7)


def plot_trajectories(
    results: DataFrame,
    reactions: Optional[List[str]] = None,
    time: str = "time",
    labels: Optional[Dict[str, str]] = None,
    x_axis_title: str = r"Time $\left[ \mathrm{h} \right]$",
    y_axis_title: str = r"Flux $\left[ \mathrm{mmol} \, "
    r"\mathrm{g}_{\mathrm{DW}}^{-1} \, \mathrm{h}^{-1} \right]$",
):
    """
    Plot the flux trajectories of a dynamic FBA simulation.

    The resulting plot can be further customized using ``matplotlib.pyplot``.

    Parameters
    ----------
    results : pandas.DataFrame
        The flux results of a simulation.
    reactions : list of strings, optional
        The names of the reactions in the data frame (default: all columns
        except for time).
    time : str, optional
        The name of the time column in the results (default "time").
    labels : dict, optional
        A mapping from columns names to legend labels (default is the same).
    x_axis_title : str, optional
        The axis title for the horizontal axis (default time).
    y_axis_title : str, optional
        The vertical axis title (default flux).
        x-axis: time

    """
    if reactions is None:
        reactions = results.columns.tolist()
        reactions.remove(time)
    domain = results[time]

    if labels is None:
        labels = {}

    fig, ax = plt.subplots(1, 1)
    ax.set_prop_cycle("color", PALETTE)
    for name in reactions:
        label = labels.get(name, name)
        plt.plot(domain, results[name], label=label)

    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    # Set the legend outside the plot area.
    fig.legend(loc="center right", borderaxespad=0.1)
    plt.subplots_adjust(right=0.7)
