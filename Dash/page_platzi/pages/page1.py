from dash import dcc, html, Input, Output, callback

layout1 = html.Div([

    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Home', href='/'), 

    html.H3('Page 1'),

    html.Div(id='info1'),

    dcc.Graph(id='grafico', figure={})


])