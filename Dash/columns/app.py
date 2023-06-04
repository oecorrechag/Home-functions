import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px


# data
df = pd.DataFrame({'a': [1, 2, 3, 4, 1, 2], 
                   'b': [2, 1, 5, 6, 9, 2],
                   'c': ['x', 'x', 'y', 'y', 'x', 'y']})


app = Dash(__name__, title = 'Descargar csv o excel',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

server = app.server

app.layout = dbc.Container([


    dbc.Row([
            dbc.Col([

                dbc.Row([
                    dcc.Graph(id='graph1', figure={})
                ]),

                dbc.Row([
                    dcc.Graph(id='graph2', figure={})
                ]),

            ]),

            dbc.Col([
                dbc.Button("Download", id="btn", className="btn-platzi me-2"),
                dcc.Graph(id='graph3', figure={})
            ]),
        ]),

], fluid=True)

@callback(
    Output("graph1", "figure"), 
    Output("graph2", "figure"), 
    Output("graph3", "figure"), 
    Input("btn", "n_clicks"),
)
def func(n_nlicks):

    graph1 = px.bar(df, x='a', y='b')
    graph1.update_layout(height=360)
    graph2 = px.bar(df, x='b', y='c')
    graph2.update_layout(height=360)
    graph3 = px.bar(df, x='c', y='a')
    graph3.update_layout(height=720)

    return graph1,graph2,graph3



if __name__ == '__main__':
    app.run_server(debug=True)
