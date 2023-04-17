from dash import dcc, html

from components.CallbacksPage1 import page1

layout1 = html.Div([

    html.Br(),
    html.H3('Page 1'),

    page1,

])
