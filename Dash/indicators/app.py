from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

app = Dash(__name__, title = 'Indicators',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

server = app.server

app.layout = html.Div([

    html.Br(),html.Br(),html.Br(),

    dbc.Input(id="texto", placeholder="Type something...", type="text"),
    dcc.Graph(id='fig_indicator', figure={}),

])


@callback(
    Output("fig_indicator", "figure"),
    Input("texto", "value"),
)
def func(value):



    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 100,
        title = {"text": " Indicator 1 <br><span style='font-size:0.8em;color:gray'> Subtitle </span><br><span style='font-size:0.8em;color:gray'> Subsubtitle </span>"},
        domain = {'x': [0.0, 0.2], 'y': [0.5, 1.0]},
        delta = {'reference': 1000, 'relative': True, 'position' : "top"}))

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 1,
        title = {"text": " Indicator 2 <br><span style='font-size:0.8em;color:gray'> Subtitle </span><br><span style='font-size:0.8em;color:gray'> left </span>"},
        domain = {'x': [0.2, 0.4], 'y': [0.5, 1.0]},
        delta = {'reference': 1000, 'relative': True, 'position' : "left"}))

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 523,
        title = {"text": " Indicator 3 <br><span style='font-size:0.8em;color:gray'> Subtitle </span><br><span style='font-size:0.8em;color:gray'> bottom </span>"},
        domain = {'x': [0.4, 0.6], 'y': [0.5, 1.0]},
        delta = {'reference': 1000, 'relative': True, 'position' : "bottom"}))

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 5253,
        title = {"text": " Indicator 4 <br><span style='font-size:0.8em;color:gray'> Subtitle </span><br><span style='font-size:0.8em;color:gray'> right </span>"},
        domain = {'x': [0.6, 0.8], 'y': [0.5, 1.0]},
        delta = {'reference': 1000, 'relative': True, 'position' : "right"}))
    
    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 100000,
        title = {"text": " Indicator 5 <br><span style='font-size:0.8em;color:gray'> Subtitle </span><br><span style='font-size:0.8em;color:gray'> top </span>"},
        domain = {'x': [0.8, 1.0], 'y': [0.5, 1.0]},
        delta = {'reference': 1000, 'relative': True, 'position' : "top"}))



    fig.add_trace(go.Indicator(
        mode = "number",
        value = 5423,
        title = {"text": " Indicator 6 <br><span style='font-size:0.8em;color:gray'> Subtitle </span><br><span style='font-size:0.8em;color:gray'> bottom </span>"},
        domain = {'x': [0.0, 0.33], 'y': [0.0, 0.4]},
        # delta = {'reference': 99, 'relative': True, 'position' : "bottom"}
        ))

    fig.add_trace(go.Indicator(
        mode = "number+gauge",
        value = 823,
        title = {"text": " Indicator 7 "},
        domain = {'x': [0.33, 0.66], 'y': [0.0, 0.4]},
        delta = {'reference': 99, 'relative': True, 'position' : "bottom"}
        ))
    
    fig.add_trace(go.Indicator(
        mode = "number",
        value = 74,
        title = {"text": " Indicator 8 <br><span style='font-size:0.8em;color:gray'> Subtitle </span><br><span style='font-size:0.8em;color:gray'> bottom </span>"},
        domain = {'x': [0.66, 1.0], 'y': [0.0, 0.4]},
        # delta = {'reference': 99, 'relative': True, 'position' : "bottom"}
        ))


    fig.update_layout(width=1500, height=600)



    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
