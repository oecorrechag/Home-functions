from dash import html
import dash_bootstrap_components as dbc

header = html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
        ]),
    ])

footer = dbc.Container([
            dbc.Row(children=[

                html.Footer('© copyright, Build with Plotly and ❤ by'),
                html.A('Oscar', href='https://github.com/oecorrechag', target="_blank"),

            ], className="row text-center"), 
        ], fluid=True, id="footer", className="pb-2 pt-2"),