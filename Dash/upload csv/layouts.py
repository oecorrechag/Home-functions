from dash import dcc, html

header = html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
        ]),
    ])

footer = html.Div([
     html.Br(),
     html.Footer('© copyright, Build with Plotly and ❤ by'),
     html.A('Oscar', href='https://github.com/oecorrechag', target="_blank")
     ])