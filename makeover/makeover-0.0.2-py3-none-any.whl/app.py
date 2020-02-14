import dash
import dash_html_components as html

import sys
import pandas as pd

from makeover.viz_gen import generate_single_column_plots, generate_multi_column_plots
from makeover.config import EXTERNAL_STYLESHEETS, EXTERNAL_SCRIPTS, DATA_DIR

app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS,
                external_scripts=EXTERNAL_SCRIPTS)

dataset_path = sys.argv[1]
df = pd.read_csv(dataset_path)

try:
    target_column_name = sys.argv[2]
    feat = df.drop(columns=[target_column_name])
    label = df[target_column_name]

except IndexError:
    feat = df
    label = None

plots = generate_single_column_plots(feat, label) + \
    generate_multi_column_plots(feat, label)

title = html.H1(children=dataset_path, style={
    'textAlign': 'center', 'fontFamily': 'Montserrat'})

body_children = []
for graph_obj in plots:
    body_children.append(
        html.Div(className='col-md-4', children=[graph_obj])
    )

body = html.Div(
    children=html.Div(
        className='row', children=body_children
    )
)
app.layout = html.Div(children=[title, body])

if __name__ == '__main__':
    app.run_server(debug=True)
