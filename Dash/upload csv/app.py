import pandas as pd
from dash import Dash, dcc, html, Input, Output, State, callback

from layouts import header, footer
from pages import menu, home, page1, page2

from utils.utils import parse_data


# app = Dash(__name__, suppress_callback_exceptions=True)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets)

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
def display_page(path):
    print('path', path)
    if path == "" or path == "/menu":
         return menu.menu
    elif path == "/" or path == "/home":
         return home.home
    # elif path == '/page1':
    #      return page1.layout1
    # elif path == '/page2':
    #      return page2.layout2
    else:
        return '404'





if __name__ == '__main__':
    app.run_server(debug=True)