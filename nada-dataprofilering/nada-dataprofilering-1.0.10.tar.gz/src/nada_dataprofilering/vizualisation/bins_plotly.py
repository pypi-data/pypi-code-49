import pandas as pd
import plotly.graph_objects as go


def threshold_limit(df, column_name, threshold) -> bool:

    under_threshold = False
    if df.loc[df[column_name] < threshold].shape[0] != 0:
        under_threshold = True

    return under_threshold


def get_bins(df, column_name, threshold) -> pd.Series:

    df_count = df.groupby([column_name]).size().reset_index(name='count')

    under_threshold = threshold_limit(df_count, 'count', threshold)

    if under_threshold:
        loop = True
        i = 1
        prev_bins = df[column_name].value_counts(bins=1)
        while loop:

            current_bins = df[column_name].value_counts(bins=i)
            current_df = pd.DataFrame(current_bins)

            if threshold_limit(current_df, column_name, threshold):
                loop = False
                bins = prev_bins

            else:
                i += 1
                prev_bins = current_bins

    else:
        bins = df[column_name].value_counts(bins=df_count.shape[0])

    return bins


def make_plotly_hist(bins):
    bins = bins.sort_index(ascending=True)
    x_mid = []
    y_mid = []

    for i in range(bins.shape[0]):
        x_mid.append(bins.index[i].mid)
        y_mid.append(bins.values[i])

    fig = go.Figure(go.Bar(x=x_mid,
                           y=y_mid,
                           width=[i.length for i in bins.index]
                           ))
    fig.update_layout(xaxis=dict(tickformat=',g'),
                      yaxis=dict(tickformat=',g'),
                      separators=', ')

    return fig


def column_hist_plotly(df, column_name, threshold=5):

    bins = get_bins(df, column_name, threshold)

    fig = make_plotly_hist(bins)

    fig_json = fig.to_json()

    return fig_json





