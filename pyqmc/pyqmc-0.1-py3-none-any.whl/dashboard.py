import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import h5py
import glob

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    dcc.Graph(id='energytrace'),
    dcc.Graph(id='energyvsN'),
    dcc.Graph(id='energyvsS')

])


def energytrace(en,fname):
    return dict(   
        x=list(range(en.shape[0])),
        y=list(en[:,1]),
        mode='marker',
        name=fname
    )

def energytrace_plot(traces):
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'Step' } ,
            yaxis={'title': 'Energy'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }

def NvsEnergytrace(N, en, fname):
    return dict(   
        x=list(N[:,1]),
        y=list(en[:,1]),
        mode='markers',
        name=fname,
        marker={
            'size': 15,
            'opacity': 0.5,
            'line': {'width': 0.5, 'color': 'white'}
        }
    )
 
def NvsEnergy_plot(traces):
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'N' } ,
            yaxis={'title': 'Energy'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }

def SvsEnergytrace(S, en, fname):
    return dict(   
        x=list(S[:,1,0]),
        y=list(en[:,1]),
        mode='markers',
        name=fname,
        marker={
            'size': 15,
            'opacity': 0.5,
            'line': {'width': 0.5, 'color': 'white'}
        }
    )

def SvsEnergy_plot(traces):
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'Overlap' } ,
            yaxis={'title': 'Energy'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }

@app.callback(
    [Output('energytrace', 'figure'),
    Output('energyvsN', 'figure'),
    Output('energyvsS', 'figure'),
    ],
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    fnames = sorted(glob.glob("*ortho*.hdf5"))
    traces_energy = []
    traces_N = []
    traces_S = []
    for fname in fnames:
        with h5py.File(fname) as f:
            en = f['energies'][...]
            N = f['N'][...]
            S = f['overlap'][...]
        traces_energy.append(energytrace(en, fname))
        traces_N.append(NvsEnergytrace(N,en,fname))
        traces_S.append(SvsEnergytrace(S,en,fname))


    
    return [energytrace_plot(traces_energy), 
        NvsEnergy_plot(traces_N),
        SvsEnergy_plot(traces_S) ]


if __name__ == '__main__':
    app.run_server(debug=True)