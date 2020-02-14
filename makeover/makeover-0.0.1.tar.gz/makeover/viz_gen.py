import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
import dash_core_components as dcc

import itertools
import pandas as pd

from makeover.utils import _get_continuous_categorical_columns


def generate_single_column_plots(feat, label=None):
    '''
    returns a list of dcc.Graph objects

    feat must be pandas DataFrame object
    label must be pandas Series object
    '''
    continuous_columns, categorical_columns = _get_continuous_categorical_columns(
        feat)

    plots = []
    for col in continuous_columns:
        fig = _generate_histogram_plot_V2(feat=feat[col], label=label)
        graph_obj = dcc.Graph(figure=fig)
        plots.append(graph_obj)

    for col in categorical_columns:
        fig = _generate_freq_count_bar_plot(feat=feat[col], label=label)
        graph_obj = dcc.Graph(figure=fig)
        plots.append(graph_obj)

    return plots


def generate_multi_column_plots(feat, label=None):
    '''
    returns a list of dcc.Graph objects

    feat must be pandas DataFrame object
    label must be pandas Series object
    '''
    continuous_columns, categorical_columns = _get_continuous_categorical_columns(
        feat)
    continuous_column_pairs = [
        pair for pair in itertools.combinations(continuous_columns, 2)]

    plots = []
    for pair in continuous_column_pairs:
        first_col, second_col = pair[0], pair[1]
        fig = _generate_scatter_plot_V2(
            feat[first_col], feat[second_col], label)
        graph_obj = dcc.Graph(figure=fig)
        plots.append(graph_obj)

    corr_graph = dcc.Graph(figure=_generate_corr_heatmap(feat, label))
    plots.append(corr_graph)

    return plots


def _generate_histogram_plot(feat, label=None):
    '''
    feat and label must be pandas Series object (single column)
    '''
    if label is not None:
        data = []
        for target_class in label.unique():
            trace = go.Histogram(
                x=feat[label == target_class], name=str(target_class))
            data.append(trace)
    else:
        trace = go.Histogram(x=feat)
        data = [trace]

    layout = go.Layout(
        title=feat.name,
        hovermode='closest'
    )

    fig = go.Figure(data=data, layout=layout)
    return fig


def _generate_histogram_plot_V2(feat, label=None):
    '''
    feat and label must be pandas Series object (single column)

    this Version (V2) uses plotly express to generate a more
    advanced plot (with marginal box plot)
    '''
    df = pd.DataFrame()
    df[feat.name] = feat
    if label is not None:
        df[label.name] = label
        fig = px.histogram(df, x=feat.name, color=label.name,
                           marginal="box", opacity=0.8, title=feat.name)
    else:
        fig = px.histogram(df, x=feat.name, marginal="box",
                           opacity=0.8, title=feat.name)

    return fig


def _generate_dist_plot(feat, label=None):
    '''
    feat and label must be pandas Series object (single column)
    '''
    if label is not None:
        data = []
        names = []
        for target_class in label.unique():
            data.append(feat[label == target_class])
            names.append(str(target_class))
    else:
        data = [feat]

    fig = ff.create_distplot(data, names)
    fig.update_layout(title_text=feat.name)
    return fig


def _generate_freq_count_bar_plot(feat, label=None):
    '''
    feat and label must be pandas Series object (single column)
    '''
    if label is not None:
        data = []
        for target_class in label.unique():
            categories, frequencies = zip(
                *sorted(feat[label == target_class].value_counts().to_dict().items(),
                        key=lambda x: x[1],
                        reverse=True))

            trace = go.Bar(
                x=frequencies,
                y=categories,
                orientation='h',
                name=str(target_class)
            )
            data.append(trace)

    else:
        categories, frequencies = zip(
            *sorted(feat.value_counts().to_dict().items(),
                    key=lambda x: x[1],
                    reverse=True))
        trace = go.Bar(
            x=frequencies,
            y=categories,
            orientation='h'
        )
        data = [trace]

    layout = go.Layout(
        title=feat.name,
        xaxis=dict(title='freq'),
        yaxis=dict(title=feat.name),
        hovermode='closest'
    )

    fig = go.Figure(data=data, layout=layout)
    return fig


def _generate_scatter_plot(x, y, label=None):
    '''
    x, y and label must be pandas Series object (single column)
    '''
    if label is not None:
        data = []
        for target_class in label.unique():
            trace = go.Scatter(
                x=x[label == target_class],
                y=y[label == target_class],
                name=str(target_class),
                mode='markers',
                marker=dict(
                    size=10,
                    line=dict(width=1)
                )
            )
            data.append(trace)
    else:
        trace = go.Scatter(
            x=x,
            y=y,
            mode='markers',
            marker=dict(
                size=10,
                line=dict(width=1)
            )
        )
        data = [trace]

    layout = go.Layout(
        title='{} VS {}'.format(x.name, y.name),
        xaxis=dict(title=x.name),
        yaxis=dict(title=y.name),
        hovermode='closest'
    )

    fig = go.Figure(data=data, layout=layout)
    return fig


def _generate_scatter_plot_V2(x, y, label=None):
    '''
    x, y and label must be pandas Series object (single column)

    this Version (V2) uses plotly express to generate a more
    advanced plot (with marginal box plot and trendlines)
    '''
    df = pd.DataFrame()
    df[x.name] = x
    df[y.name] = y
    if label is not None:
        df[label.name] = label
        fig = px.scatter(df, x=x.name, y=y.name, color=label.name,
                         marginal_x='box', marginal_y='box', trendline='ols',
                         title='{} VS {}'.format(x.name, y.name))

    else:
        fig = px.scatter(df, x=x.name, y=y.name, marginal_x='box', marginal_y='box',
                         trendline='ols', title='{} VS {}'.format(x.name, y.name))

    return fig


def _generate_corr_heatmap(feat, label=None):
    '''
    returns a correlation heatmap figure

    feat must be pandas DataFrame object
    label must be pandas Series object
    '''
    df = pd.DataFrame(feat)
    if label is not None:
        df[label.name] = label

    df_corr = df.corr()

    fig = go.Figure(data=go.Heatmap(
        z=df_corr.values,
        x=df_corr.index,
        y=df_corr.index,
        hoverongaps=False,
        colorscale='RdYlBu'))

    return fig
