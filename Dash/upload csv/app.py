import pandas as pd
from dash import Dash, dcc, html, Input, Output, State, callback

from pages import menu, home, page1, page2, header, footer

import dash_bootstrap_components as dbc

from utils.utils import parse_data


app = Dash(__name__, title = 'App UPLOAD',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server

app.layout = html.Div([

    dcc.Location(id="url", pathname="", refresh=False),
    dcc.Store(id='filter_data'),

    # Header
    html.Div(id='header'),

    # Pagina
    html.Div(id='page-content'),

    # Footer
    html.Div(id='footer'),

])


@callback(
    Output('filter_data', "data"),
    Input("upload-data", "contents"), 
    State("upload-data", "filename"),
    prevent_initial_call=True,
)

def update_table(contents, filename):

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_data(contents, filename)
    else:
        df = pd.read_csv('help.csv', sep = ',', decimal = '.', header = 0, encoding = 'utf-8')

    df.to_csv('output/df_output.csv', encoding = 'utf-8-sig', index = False)

    return df.to_json(date_format='iso', orient='split') 




# Para menu
@callback(Output('header', 'children'),
          Output('footer', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    return  header, footer  


# Para las paginas
@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "" or pathname == "/menu":
         return menu.menu
    elif pathname == "/" or pathname == "/home":
         return home.home
    elif pathname == '/page1':
         return page1.layout1
    elif pathname == '/page2':
         return page2.layout2
    else:
        return '404'





if __name__ == '__main__':
    app.run_server(debug=True)