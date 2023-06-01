from dash import Dash, dcc, html, Input, Output, callback, no_update

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from funciones import hover_hover, hover_sho

df = pd.DataFrame(dict(
    x = [1, 3, 2, 4],
    y = [1, 2, 3, 4], 
    tipo=['A','A','B','B']
))


# Definimos la aplicación de Dash
app = Dash(__name__)

prev_x = None
prev_y = None

# Definimos el layout de la aplicación
app.layout = html.Div([

    dcc.Input(id='x-input', type='number', value=5),

    dcc.Graph(id='graph',),
    dcc.Tooltip(id="graph_1"),

])

@callback(
    Output('graph', 'figure'),
    Input('x-input', 'value'),
    Input('graph', 'hoverData')
)
def update_graph(x, hoverData):
    fig = px.line(df, x="x", y="y", color='tipo', title="Unsorted Input", markers=True, line_shape='spline') 
    fig.update_traces(hoverinfo="none", hovertemplate=None)
    hover_sho(fig, hoverData, name='Plano', color='#FF5733')

    # fig.update_layout(
    #     hovermode="closest",
    #     xaxis=dict(
    #         hoverformat=".2f",
    #         showspikes=True,
    #         spikethickness=1,
    #         spikedash="dot",
    #         spikecolor="#999999",
    #         spikemode="across"
    #     ),
    #     yaxis=dict(
    #         hoverformat=".2f",
    #         showspikes=True,
    #         spikethickness=1,
    #         spikedash="dot",
    #         spikecolor="#999999",
    #         spikemode="across"
    #     )
    # )
    # hover_sho(fig, hoverData)

    return fig


@callback(
    Output("graph_1", "show"),
    Output("graph_1", "bbox"),
    Output("graph_1", "children"),
    Input("graph", "hoverData"),
)

def update_tooltip_content(hoverData):
    if hoverData is None:
        return no_update

    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    children = [html.Small([f"X value: {pt['x']}", html.Br(), f"Y value: {pt['y']}"]),]

    return True, bbox, children








if __name__ == '__main__':
    app.run_server(debug=True)
