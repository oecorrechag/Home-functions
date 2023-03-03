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


from dash import dcc
languages = ['English', 'Español'] # lista de idiomas disponibles
selected_language = 'English' # idioma seleccionado por defecto


app = Dash(__name__, title = 'Page test',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server

app.layout = dbc.Container([
    
    dcc.Location(id='url', refresh=False),
    data_store,

    # Header
    html.Div(id='header'),

    # Pagina
    html.Div(id='page-content'),

    # Create Div to place a conditionally visible element inside
    html.Div(id='slider-container', children=[

        html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
        dcc.Dropdown(
            options=[{'label': language, 'value': language} for language in languages],
            value=selected_language,
            id='language_dropdown'
        ),

    ], style= {'display': 'block'}), # <-- This is the line that will be changed by the dropdown callback

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
          Input('language_dropdown', 'value'),
          Input('switches-input', 'value'),
          )
def display_page(pathname, value, value2):
    print('value: ', value2)
    if (pathname == '/home') | (pathname == '/'):
         return home
    elif (pathname == '/page1') & (value == 'English'):
         return layout1en
    elif (pathname == '/page1') & (value == 'Español'):
         return layout1es
    elif pathname == '/page2':
         return layout2
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
    