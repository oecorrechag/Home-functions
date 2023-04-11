from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from utils.load import data

app = Dash(__name__, title = 'Carga y reemplazo de archivos, example 1',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

app.layout = html.Div([
    html.H1("Dashboard de ejemplo"),
    dcc.Dropdown(
        id='archivo-dropdown',
        options=[{'label': k, 'value': k} for k in data.keys()],
        value=list(data.keys())[0]
    ),
    dcc.Graph(id='grafico')
])


@callback(
    Output('grafico', 'figure'),
    Input('archivo-dropdown', 'value')
)
def actualizar_grafico(nombre_archivo):
    df = data[nombre_archivo]
    return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


if __name__ == '__main__':
    app.run_server(debug=True)
