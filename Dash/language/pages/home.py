from dash import dcc, html
import dash_bootstrap_components as dbc

from components.CallbacksHome import menuHome

home = dbc.Container([

    html.Br(),
    html.H3('Home Page'),

    dbc.Row([
        dbc.Col(className="col col-md-10 offset-md-1 col-lg-8 offset-lg-2 pt-2", children=[

            menuHome,

            ])
    ]),

])
