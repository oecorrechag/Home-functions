from dash import dcc, html

from components.CallbacksPage2 import page2, grafica

layout2 = html.Div([

    html.Br(),
    html.H3('Page 2'),

    page2,

    grafica,

])
