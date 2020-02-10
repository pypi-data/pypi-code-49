'''This test uses the new wildcards feature in development

pr here: https://github.com/plotly/dash/pull/1103

install with  pip install -e git+https://github.com/plotly/dash.git@475-wildcards#egg=dash
'''
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div('Dash To-Do list'),
    dcc.Input(id="new-item"),
    html.Button("Add", id="add"),
    html.Button("Clear Done", id="clear-done"),
    html.Div(id="list-container"),
    html.Hr(),
    html.Div(id="totals")
])

style_todo = {"display": "inline", "margin": "10px"}
style_done = {"textDecoration": "line-through", "color": "#888"}
style_done.update(style_todo)


@app.callback(
    [
        Output("list-container", "children"),
        Output("new-item", "value")
    ],
    [
        Input("add", "n_clicks"),
        Input("new-item", "n_submit"),
        Input("clear-done", "n_clicks")
    ],
    [
        State("new-item", "value"),
        State({"item": ALL}, "children"),
        State({"item": ALL, "action": "done"}, "value")
    ]
)
def edit_list(add, add2, clear, new_item, items, items_done):
    triggered = [t["prop_id"] for t in dash.callback_context.triggered]
    adding = len([1 for i in triggered if i in ("add.n_clicks", "new-item.n_submit")])
    clearing = len([1 for i in triggered if i == "clear-done.n_clicks"])
    new_spec = [
        (text, done) for text, done in zip(items, items_done)
        if not (clearing and done)
    ]
    if adding:
        new_spec.append((new_item, []))
    new_list = [
        html.Div([
            dcc.Checklist(
                id={"item": i, "action": "done"},
                options=[{"label": "", "value": "done"}],
                value=done,
                style={"display": "inline"}
            ),
            html.Div(text, id={"item": i}, style=style_done if done else style_todo)
        ], style={"clear": "both"})
        for i, (text, done) in enumerate(new_spec)
    ]
    return [new_list, "" if adding else new_item]


@app.callback(
    Output({"item": MATCH}, "style"),
    [Input({"item": MATCH, "action": "done"}, "value")]
)
def mark_done(done):
    return style_done if done else style_todo


@app.callback(
    Output("totals", "children"),
    [Input({"item": ALL, "action": "done"}, "value")]
)
def show_totals(done):
    count_all = len(done)
    count_done = len([d for d in done if d])
    result = "{} of {} items completed".format(count_done, count_all)
    if count_all:
        result += " - {}%".format(int(100 * count_done / count_all))
    return result


if __name__ == "__main__":
    app.run_server(debug=True)