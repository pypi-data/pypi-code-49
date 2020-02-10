import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State, ClientsideFunction
from plotly.subplots import make_subplots
import plotly.graph_objects as go

app = dash.Dash(__name__)

fig_data = {
    "data": [{"type": "bar", "x": [1, 2, 3], "y": [1, 3, 2]}],
    "layout": {"title": {"text": ""}}
}


fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4"))

graph_dict = {
  'fig1': go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
  'fig2': go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
  'fig3': go.Scatter(x=[300, 400, 500], y=[600, 700, 800]),
  'fig4': go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
  }

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
              row=1, col=1)

fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
              row=1, col=2)

fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]),
              row=2, col=1)

fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
              row=2, col=2)

fig.update_layout(height=500, width=700,
                  title_text="Multiple Subplots with Titles")

print(fig)

app.layout = html.Div([
    dcc.Store("fig-data", data=fig),
    dcc.Store("fig-data2", data = graph_dict),
    dcc.Dropdown(
        id="city",
        options=[ {'label': z, "value": z} for z in ["Sydney", "Montreal"] ],
        value="Sydney"
    ),
    dcc.Graph(id="graph"),
    dcc.Input(id="input_n", type='number', value = 2),
    dcc.Graph(id="graph-subplot"),
])

app.clientside_callback(
    ClientsideFunction("clientside", "figure"),
    Output(component_id="graph", component_property="figure"),
    [Input("fig-data", "data"), Input("city", "value")],
)

@app.callback(Output('fig-data2', 'data'),
  [Input('input_n', 'value')],[State('fig-data2', 'data')])
def update_data(in_, state):
  state['fig1'] = go.Scatter(x=[1, 2, 3], y=[4, 5, in_])
  return state
  # return go.Scatter(x=[1, 2, 3], y=[in_, 5, 6])

app.clientside_callback(
    ClientsideFunction("clientside", "subplot"),
    Output(component_id="graph-subplot", component_property="figure"),
    [Input("fig-data2", "data"), Input("input_n", "value")],
)


app.run_server(host="0.0.0.0", debug=True, port = "8080")





