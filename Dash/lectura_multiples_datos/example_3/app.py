from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from utils.load import estructura, data

app = Dash(__name__, title = 'Carga y reemplazo de archivos, example 3',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

app.layout = html.Div([
    html.H1("Dashboard de ejemplo"),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': k, 'value': k} for k in estructura.keys()],
        value=list(estructura.keys())[0]
    ),
    html.Div([
        dcc.Graph(id='grafico1'),
        dcc.Graph(id='grafico2')
    ])
])


@callback(
    [Output('grafico1', 'figure'), Output('grafico2', 'figure')],
    Input('dropdown', 'value')
)
def actualizar_graficos(opcion):
    dfs = data[opcion]
    fig1 = px.bar(dfs[0], x="Fruit", y="Amount", color="City", barmode="group")
    fig2 = px.bar(dfs[1], x="Fruit", y="Amount", color="City", barmode="group")
    return fig1, fig2


if __name__ == '__main__':
    app.run_server(debug=True)










