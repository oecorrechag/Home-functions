
from dash import dcc, html

from components.CallbacksPage1 import page1

layout1 = html.Div([

    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Home', href='/'), 

    page1,

    html.Br(),html.Br(),html.Br(),

])
