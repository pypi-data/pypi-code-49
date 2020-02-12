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


"""Provide functions to plot concentrations and trajectories using plotly."""


from typing import Dict, List, Optional

import plotly.graph_objects as go
from pandas import DataFrame
from plotly.subplots import make_subplots


def plot_concentrations(
    results: DataFrame,
    metabolites: Optional[List[str]] = None,
    biomass: str = "Biomass",
    time: str = "time",
    labels: Optional[Dict[str, str]] = None,
    x_axis_title: str = r"$\textrm{Time} \left[ \textrm{h} \right]$",
    left_y_axis_title: str = r"$\textrm{Biomass} \left[ \textrm{g} \, "
    r"\textrm{L}^{-1} \right]$",
    right_y_axis_title: str = r"$\textrm{Metabolites} \left[ \textrm{mmol} \, "
    r"\textrm{L}^{-1} \right]$",
) -> go.Figure:
    """
    Plot the concentration results of a dynamic FBA simulation.

    The resulting plot can be further customized using the plotly backend.

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

    Returns
    -------
    plotly.graph_objects.Figure
        2 y-axes: biomass on the left, (concentration / time)
                  metabolites on the right (concentration / time)
        x-axis: time

    """
    if metabolites is None:
        metabolites = results.columns.tolist()
        metabolites.remove(biomass)
        metabolites.remove(time)
    domain = results[time]

    if labels is None:
        labels = {}

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    for name in metabolites:
        label = labels.get(name, name)
        fig.add_trace(
            go.Scatter(
                x=domain,
                y=results[name],
                mode="lines",
                name=label,
                line={"dash": "dot"},
            ),
            secondary_y=True,
        )

    label = labels.get(biomass, biomass)
    fig.add_trace(
        go.Scatter(x=domain, y=results[biomass], mode="lines", name=label),
        secondary_y=False,
    )
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(
        title_text=left_y_axis_title, secondary_y=False,
    )
    fig.update_yaxes(
        title_text=right_y_axis_title, secondary_y=True,
    )
    return fig


def plot_trajectories(
    results: DataFrame,
    reactions: Optional[List[str]] = None,
    time: str = "time",
    labels: Optional[Dict[str, str]] = None,
    x_axis_title: str = r"$\textrm{Time} \left[ \textrm{h} \right]$",
    y_axis_title: str = r"$\textrm{Flux} \left[ \textrm{mmol} \, "
    r"\textrm{g}_{\textrm{DW}}^{-1} \, \textrm{h}^{-1} "
    r"\right]$",
):
    """
    Plot the flux trajectories of a dynamic FBA simulation.

    The resulting plot can be further customized using the plotly backend.

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

    Returns
    -------
    plotly.graph_objects.Figure
        y-axis: flux trajectories (concentration / cell mass / time).
        x-axis: time

    """
    if reactions is None:
        reactions = results.columns.tolist()
        reactions.remove(time)
    domain = results[time]

    if labels is None:
        labels = {}

    fig = go.Figure()
    for name in reactions:
        label = labels.get(name, name)
        fig.add_trace(go.Scatter(x=domain, y=results[name], mode="lines", name=label))
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text=y_axis_title)
    return fig
