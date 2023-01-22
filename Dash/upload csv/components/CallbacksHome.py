import pandas as pd
from dash import dcc, dash_table, html, Input, Output, State, callback
import dash_bootstrap_components as dbc


TableHome = html.Div([
    dbc.Table(id='table_home')
])
@callback(
    Output('table_home', "children"),
    Input("filter_data", "data")
)
def graphics_table(fil):
    datos = pd.read_json(fil, orient='split')

    print("="*64)
    print(datos.head())
    print("="*64)

    columns = [{"name": i, "id": i,} for i in datos.columns]
    df_data = datos.to_dict('rows')

    table = html.Div([
        dash_table.DataTable(data=df_data, columns=columns)
    ])

    return table
