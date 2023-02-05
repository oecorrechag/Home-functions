import pandas as pd
import plotly.express as px
from dash import dcc, html, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc


page1 = html.Div([
    dbc.Row(children=[
        dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[
            html.Div(id='info1'),
        ]),
        dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[
            html.Div(id='infow2'),
        ]),
    ]),

    dbc.Row(children=[
        dcc.Graph(id='grafico', figure={})
    ]),

])
@callback(
    Output('info1', 'children'),
    Output('infow2', 'children'),
    Output('grafico', 'figure'),
    Input('filter_data', 'data'),
    Input('selectMenu', 'value'),
    )
def display_value(data, value):

    data = pd.read_json(data, orient='split')

    print('*'*100)
    print(data.head())
    print('*'*100)
    print('value ', value)

    df2 = data[data['City'] == value]

    info1 = value
    grafico = px.bar(df2, x="Fruit", y="Amount", color="City", barmode="group")

    infow2 = html.Div([
        dash_table.DataTable(
            data=df2.to_dict("rows"),
            columns=[{"id": x, "name": x} for x in df2.columns],
            page_size=20,
            style_cell={'textAlign': 'center'},
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold'
            }
        )
    ])

    return info1, infow2, grafico
