from dash import Input, Output, callback, html, dash_table

import pandas as pd
import plotly.express as px


# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# @callback(
#     Output('info1', 'children'),
#     Output('infow2', 'children'),
#     Output('grafico', 'figure'),
#     Input('hide2', 'value'))
# def display_value(value):

#     df2 = df[df['City'] == value]

#     info1 = value
#     grafico = px.bar(df2, x="Fruit", y="Amount", color="City", barmode="group")

#     infow2 = html.Div([
#         dash_table.DataTable(
#             data=df2.to_dict("rows"),
#             columns=[{"id": x, "name": x} for x in df2.columns],
#             page_size=20,
#             # style_table={'height': '400px', 'overflowY': 'auto'},
#             style_cell={'textAlign': 'center'},
#             style_header={
#                 'backgroundColor': 'white',
#                 'fontWeight': 'bold'
#             }
#         )
#     ])

#     return info1, infow2, grafico







    

@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'