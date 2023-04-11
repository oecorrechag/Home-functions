from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from utils.load import data


app = Dash(__name__, title = 'Carga y reemplazo de archivos, example 2',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

app.layout = html.Div([
    html.H1("Dashboard de ejemplo"),
    dcc.Dropdown(
        id='grupo-dropdown',
        options=[{'label': k, 'value': k} for k in data.keys()],
        value=list(data.keys())[0]
    ),
    dcc.Dropdown(
        id='archivo-dropdown',
        value=list(data[list(data.keys())[0]].keys())[0]
    ),
    dcc.Graph(id='grafico')
])


@callback(
    Output('archivo-dropdown', 'options'),
    Input('grupo-dropdown', 'value')
)
def actualizar_archivos(nombre_grupo):
    return [{'label': k, 'value': k} for k in data[nombre_grupo].keys()]

@callback(
    Output('grafico', 'figure'),
    Input('archivo-dropdown', 'value')
)
def actualizar_grafico(nombre_archivo):
    for grupo in data.values():
        if nombre_archivo in grupo:
            df = grupo[nombre_archivo]
            break
    return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


if __name__ == '__main__':
    app.run_server(debug=True)
