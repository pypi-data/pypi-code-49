import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import flask

app = dash.Dash(
    __name__,
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
)
# app.config.suppress_callback_exceptions=True

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    dcc.Link('Navigate to "/page-1"', href='/page-1'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),
])

layout_page_1 = html.Div([
    html.H2('Page 1'),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),
])

layout_page_2 = html.Div([
    html.H2('Page 2'),
    dcc.Dropdown(
        id='page-2-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-2-display-value'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-1"', href='/page-1'),
])


def serve_layout():
    if flask.has_request_context():
        print('flask has request context')
        return url_bar_and_content_div
    print('flask has no request context!')
    return html.Div([
        url_bar_and_content_div,
        layout_index,
        layout_page_1,
        layout_page_2,
    ])


app.layout = serve_layout



# Page 1 callbacks
def generate_page_1_callback(app):
    @app.callback(Output('output-state', 'children'),
                  [Input('submit-button', 'n_clicks')],
                  [State('input-1-state', 'value'),
                   State('input-2-state', 'value')])
    def update_output(n_clicks, input1, input2):
        return ('The Button has been pressed {} times,'
                'Input 1 is "{}",'
                'and Input 2 is "{}"').format(n_clicks, input1, input2)


# Page 2 callbacks
def generate_page_2_callback(app):
    @app.callback(Output('page-2-display-value', 'children'),
                  [Input('page-2-dropdown', 'value')])
    def display_value(value):
        print('display_value')
        return 'You have selected "{}"'.format(value)


# Index callbacks
def generate_index_callbacks(app):
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == "/page-1":
            try:
                generate_page_1_callback(app)
            except Exception as m:
                print(m)
                pass
            return layout_page_1
        elif pathname == "/page-2":
            try:
                generate_page_2_callback(app)
            except Exception as m:
                print(m)
                pass
            return layout_page_2
        else:
            return layout_index

generate_index_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)