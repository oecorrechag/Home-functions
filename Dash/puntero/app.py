import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go

# Definimos la aplicación de Dash
app = dash.Dash(__name__)

prev_x = None
prev_y = None

# Definimos el layout de la aplicación
app.layout = html.Div([
    dcc.Input(
        id='x-input',
        type='number',
        value=5
    ),
    dcc.Input(
        id='y-input',
        type='number',
        value=10
    ),
    dcc.Graph(
        id='graph',
    ),
    html.Div(id='hover-data')
])

# Definimos el callback para construir el gráfico y obtener la posición del puntero
@app.callback(
    Output('graph', 'figure'),
    Output('hover-data', 'children'),
    Input('x-input', 'value'),
    Input('y-input', 'value'),
    Input('graph', 'hoverData')
)
def update_graph(x, y, hoverData):

    global prev_x, prev_y

    df = px.data.iris()

    fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species', hover_data=['species'])
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


    ###

    if hoverData is not None:

        x_hover = hoverData['points'][0]['x']
        y_hover = hoverData['points'][0]['y']
        color_hover = hoverData['points'][0]['curveNumber']

        print(hoverData['points'][0])

        # Compara el valor actual de 'x' con el valor anterior
        if x_hover == prev_x:
            hover_info = f'Posición del puntero: x={x_hover}, y={y_hover}'
            # fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', showlegend=False, marker=dict(color='gray', size=20)))
            fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', showlegend=False, marker=dict(color=color_hover, size=10)))
            fig.update_traces(
                hovertemplate="<br>".join([
                    "Sepal length: %{x}",
                    "Sepal width: %{y}",
                ])
            )
        else:
            prev_x = x_hover
            prev_y = y_hover
            hover_info = f'Posición del puntero nuevo: x={x_hover}, y={y_hover}'
            print(x_hover, y_hover, color_hover)
            # fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', showlegend=False, marker=dict(color='gray', size=20)))
            fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', showlegend=False, marker=dict(color=color_hover, size=10)))
            fig.update_traces(
                hovertemplate="<br>".join([
                    "Sepal length: %{x}",
                    "Sepal width: %{y}",
                ])
            )
    else:
        hover_info = ''

    ###

    return fig, hover_info

# Ejecutamos la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
