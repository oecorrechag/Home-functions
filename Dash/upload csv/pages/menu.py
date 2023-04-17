from dash import dcc, html
import dash_bootstrap_components as dbc


menu = html.Div([

    html.H3('Home Page'),
    dcc.Link('Go to Page home', href='/home'),

    dbc.Row([
        dcc.Upload(id="upload-data", children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
            style={ "width": "100%", "height": "60px", "lineHeight": "60px", "borderWidth": "1px", "borderStyle": "dashed", "borderRadius": "5px", "textAlign": "center", "margin": "10px"},
            multiple=True,
        ),
    ]),

])
    