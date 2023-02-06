from dash import dcc, html

from components.CallbacksPage2 import page2, grafica

layout2 = html.Div([

    # dcc.Link('Go to Page 1', href='/page1'),
    # html.Br(),
    # dcc.Link('Go to Home', href='/'),

    html.Br(),
    html.H3('Page 2'),

    page2,

    grafica,

    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
])
