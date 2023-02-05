import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

from layouts import header, footer
from pages.home import home
from pages.page1 import layout1
from pages.page2 import layout2

import callbacks


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

data_store = html.Div([dcc.Store(id="original_data", data=df.to_json()),
                       dcc.Store(id="filter_data"),
                       ])

app = Dash(__name__, title = 'Page test',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server

app.layout = dbc.Container([
    
    dcc.Location(id='url', refresh=False),
    data_store,

    # html.Div([
    #     # html.Br(),
    #     dcc.Dropdown(['Uno', 'Dos', 'Tres'], 'Uno', id='hide'),
    #     # html.Br(),
    #     dcc.Dropdown({f'{i}': f'{i}' for i in ['SF', 'Montreal']}, 'Montreal', id='hide2'),
    # ], style= {'display': 'block'}),

    # Header
    html.Div(id='header'),

    # Pagina
    html.Div(id='page-content'),

    # Footer
    html.Div(id='footer'),

], fluid=True)





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
    if (pathname == '/home') | (pathname == '/'):
         return home
    elif pathname == '/page1':
         return layout1
    elif pathname == '/page2':
         return layout2
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)