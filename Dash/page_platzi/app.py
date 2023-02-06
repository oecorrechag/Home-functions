import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

from layouts import header, footer
from pages.home import home
from pages.page1 import layout1
from pages.page2 import layout2

LOGO = "assets\logo.png"
TITLE = 'Project Name'

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

    # Header
    html.Nav([
            dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=LOGO, height="30px")),
                                    dbc.Col(dbc.NavbarBrand(TITLE, className="ms-2")),
                                ],
                                align="center",
                                className="g-0",
                            ),
                            href="/",
                            style={"textDecoration": "none"},
                        ),
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(className="navbar", children=[

                            dbc.NavLink("Home", href="/home", active="partial"),
                            
                            dbc.NavLink("Page 1", href="/page1", active="partial"),

                            dbc.NavLink("Page 2", href="/page2", active="partial"),

                            # dbc.NavItem(dbc.NavLink(html.A("Tickets", id='modal_comprar', href="/",
                            #                 className='text-platzi font-weight-bold'))),

                        ], id="navbar-collapse", is_open=False, navbar=True,
                        ),
                    ]
                ),
                color="dark",
                dark=True,
            ), 

    ], className='fixed-top'),

    # Pagina
    html.Div(id='page-content'),

    # Footer
    html.Div(id='footer'),

], fluid=True)



# Para menu
@callback(Output('footer', 'children'), #Output('header', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    return footer # header,

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