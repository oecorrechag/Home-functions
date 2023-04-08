from dash import dcc, html

from components.CallbacksPage1 import page1

layout1en = html.Div([

    html.Br(),
    html.H3('Page 1: This page is on English'),

    page1,

])

layout1es = html.Div([

    html.Br(),
    html.H3('Page 1: Esta pagina esta en español'),

    page1,

])
