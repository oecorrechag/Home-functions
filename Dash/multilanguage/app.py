import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

from pages.header import header
from pages.footer import footer
from pages.home import home
from pages.page1 import layout1en
from pages.page1 import layout1es
from pages.page2 import layout2


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

data_store = html.Div([dcc.Store(id="original_data", data=df.to_json()),
                       dcc.Store(id="filter_data"),
                       ])

app = Dash(__name__, title = 'App multilanguage',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server

app.layout = dbc.Container([
    
    dcc.Location(id='url', refresh=False),
    data_store,

    # Header
    html.Div(id='header'),

    html.Div([
     
        dbc.Col(className='col-2 offset-10 pt=6', children=[

            html.Br(),html.Br(),html.Br(),

            dbc.Checklist(
                options=[
                    {"label": "English", "value": 1},
                ],
                value=[1],
                id="select_language",
                switch=True,
            ),

        ]),

    ]),

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
    return header, footer

# Para las paginas
@callback(Output('page-content', 'children'),
          Input('url', 'pathname'),
          Input('select_language', 'value'),
          )
def display_page(pathname, select_language):
    # print('value: ', select_language)
    if (pathname == '/home') | (pathname == '/'):
         return home
    elif (pathname == '/page1') & (select_language == [1]):
         return layout1en
    elif (pathname == '/page1') & (select_language == []):
         return layout1es
    elif pathname == '/page2':
         return layout2
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
    