import pandas as pd
import plotly.express as px

from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


page2 = html.Div([
    dbc.Row(children=[
        dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[
            dcc.Dropdown(
                {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
                id='menuPage2',
                value='London',
                placeholder='Choose a city',
            ),
        ]),
        dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[
        ]),
    ]),

    dbc.Row(children=[
        html.Div(id='info3'),
    ]),

])
@callback(
    Output('info3', 'children'),
    Input('menuPage2', 'value'))
def display_value(value):
    return f'You have selected {value}'


grafica = html.Div([
    dbc.Row(children=[
        dcc.Graph(id='grafico2', figure={})
    ]),

])
@callback(
    Output('grafico2', 'figure'),
    Input('filter_data', 'data'),
    )
def display_value(data):
    data = pd.read_json(data, orient='split')

    grafico2 = px.bar(data, x="Fruit", y="Amount", color="City", barmode="group")

    return grafico2
