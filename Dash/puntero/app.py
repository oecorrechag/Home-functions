import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from funciones import hover_hover, hover_sho

df = pd.DataFrame(dict(
    x = [1, 3, 2, 4],
    y = [1, 2, 3, 4]
))


# Definimos la aplicación de Dash
app = dash.Dash(__name__)

prev_x = None
prev_y = None

# Definimos el layout de la aplicación
app.layout = html.Div([

    dcc.Input(id='x-input', type='number', value=5),

    dcc.Graph(id='graph2',),

    html.Div(id='hover-data'),

])

@app.callback(
    Output('graph2', 'figure'),
    Output('hover-data', 'children'),
    Input('x-input', 'value'),
    Input('graph2', 'hoverData')
)
def update_graph(x, hoverData):

    global prev_x, prev_y

    fig = px.line(df, x="x", y="y", title="Unsorted Input", markers=True, line_shape='spline') 
    fig.update_traces(hoverinfo='none')
    fig.update_layout(showlegend=False) 
        
    fig.update_layout(
        hovermode="closest",
        xaxis=dict(
            hoverformat=".2f",
            showspikes=True,
            spikethickness=1,
            spikedash="dot",
            spikecolor="#999999",
            spikemode="across"
        ),
        yaxis=dict(
            hoverformat=".2f",
            showspikes=True,
            spikethickness=1,
            spikedash="dot",
            spikecolor="#999999",
            spikemode="across"
        )
    )

    if hoverData is not None:

        x_hover = hoverData['points'][0]['x']
        y_hover = hoverData['points'][0]['y']
        color_hover = hoverData['points'][0]['curveNumber']
        # name = hoverData['points'][0]['customdata'][0]
        # print('ASDASD', x_hover, y_hover, color_hover)


        hover_info = hover_hover(prev_x, prev_y, x_hover, y_hover)
        fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', name="Spline", showlegend=False, marker=dict(color='blue', size=10)))
        fig.update_traces(
            hovertemplate="<br>".join([
                "Sepal length: %{x}",
                "Sepal width: %{y}",
            ])
        )
    else:
        hover_info = ''

    return fig, hover_info










# Ejecutamos la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
