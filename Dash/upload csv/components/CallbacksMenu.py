import pandas as pd
from dash import dcc, dash_table, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

from utils.utils import parse_data

# @callback(
#     Output('filter_data', "data"),
#     Input("upload-data", "contents"), 
#     State("upload-data", "filename"),
#     # prevent_initial_call=True,
#     # memoize=True
# )
# def update_table(contents, filename):

#     print(filename)

#     if contents:
#         contents = contents[0]
#         filename = filename[0]
#         df = parse_data(contents, filename)
#     else:
#         df = pd.read_csv('help.csv', sep = ',', decimal = '.', header = 0, encoding = 'utf-8')


#     print(" tabla "*64)
#     print(df.head())
#     print("="*64)

#     df.to_csv('output/df_output.csv', encoding = 'utf-8-sig', index = False)

#     return df.to_json(date_format='iso', orient='split') 


