from dash import dcc, html
import dash_bootstrap_components as dbc

from components.CallbacksHome import menuHome

home = dbc.Container([

    html.H3('Home Page'),
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),

    dbc.Row([
        dbc.Col(className="col col-md-10 offset-md-1 col-lg-8 offset-lg-2 pt-2", children=[
            menuHome,
            ])
    ]),

    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),

])