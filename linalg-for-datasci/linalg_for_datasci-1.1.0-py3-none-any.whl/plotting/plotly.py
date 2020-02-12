import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ..tests import typecheck_vector


def scatter_3D(data):
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=data.iloc[:, 0].values,
                y=data.iloc[:, 1].values,
                z=data.iloc[:, 2].values,
                mode="markers",
                marker=dict(
                    size=2,
                    color=data.iloc[:, 3].values,
                    colorscale="Rainbow",  # choose a colorscale
                    opacity=0.8,
                ),
            )
        ]
    )
    fig.update_layout(
        scene=dict(), width=700, height=700, margin=dict(r=10, l=10, b=10, t=10)
    )
    fig.show()


def scatter_3D_collinear(matrix, xlim=1, num=10000):
    darts = np.array([])
    for i in range(num):
        dart = np.random.rand(2) * xlim - xlim / 2
        if dart[0] > 0 and dart[1] > 0:
            color = 0
        elif dart[0] > 0 and dart[1] < 0:
            color = 1
        elif dart[0] < 0 and dart[1] > 0:
            color = 2
        else:
            color = 3
        darts = np.append(darts, np.append(dart, np.array([0, color])))
    darts = darts.reshape(-1, 4)
    darts[:, :2] = darts[:, :2] @ matrix.T
    darts = pd.DataFrame(darts)
    scatter_3D(darts)
    return  # darts


def plot_vectors_in_space(*vectors):
    for vector in vectors:
        typecheck_vector(vector)

    column_names = {0: "First Dimension", 1: "Second Dimension", 2: "Third Dimension"}

    fig = go.Figure()

    for vector in vectors:
        raw_data = np.append(vector, np.array([0, 0, 0]))
        data = pd.DataFrame(raw_data.reshape(-1, 3)).rename(columns=column_names)
        fig.add_trace(
            go.Scatter3d(
                x=data["First Dimension"].values,
                y=data["Second Dimension"].values,
                z=data["Third Dimension"].values,
                mode="lines",
                line=dict(width=2),
            )
        )
    fig.update_layout(
        scene=dict(
            xaxis=dict(nticks=4, range=[-1, 1],),
            yaxis=dict(nticks=4, range=[-1, 1],),
            zaxis=dict(nticks=4, range=[-1, 1],),
        ),
        width=700,
        margin=dict(r=20, l=10, b=10, t=10),
    )
    fig.update_layout(showlegend=False)
    fig.show()


from ..utils import throw_darts


def p_ball_plot_3d(num_trials, callback, inside_only=False):
    """
    `callback` is supposed to be the `throw_dart` function
    which students write, possibly a lambda version with
    some parameters filled in
    """
    darts = throw_darts(num_trials, callback)

    if inside_only == True:
        darts = darts.loc[darts["Inside Ball"] == True]

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=darts["First Dimension"].values,
                y=darts["Second Dimension"].values,
                z=darts["Third Dimension"].values,
                mode="markers",
                marker=dict(
                    size=1,
                    color=darts["Inside Ball"].values,
                    colorscale="Viridis",  # choose a colorscale
                    opacity=0.8,
                ),
            )
        ]
    )
    fig.show()
