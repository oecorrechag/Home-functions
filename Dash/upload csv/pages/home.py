from dash import dcc, html, Input, Output, callback

import dash_bootstrap_components as dbc

from components.CallbacksHome import TableHome

home = html.Div([
    html.H3('Home Page'),
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),
    
    dbc.Row([
        TableHome,
    ]),
    
    ])
