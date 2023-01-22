#from dash import dcc, html, Input, Output, callback

from dash import dcc, html, Input, Output, callback, dash_table

layout1 = html.Div([

    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Home', href='/'), 

    html.H3('Page 1'),

    # html.Div(id='info1'),

    # html.Div(id='infow2'),


    # dcc.Graph(id='grafico', figure={})


])



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
#     Input('filter_data', 'data'),
#     Input('hide2', 'value'),
#     )
# def display_value(data, value):

#     data = pd.read_json(data, orient='split')

#     print(data.head())

#     df2 = data[data['City'] == value]

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
