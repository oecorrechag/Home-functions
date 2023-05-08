import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Crear un gráfico de dispersión con algunos datos de ejemplo
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 1, 4, 3, 5], mode='markers'))

# Crear una aplicación de Dash con el gráfico
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id='scatter-plot', figure=fig)
])

# Crear una función de callback para imprimir la posición del puntero del mouse
@app.callback(Output('scatter-plot', 'figure'), [Input('scatter-plot', 'hoverData')])
def display_hover_data(hoverData):

    fig.update_layout(hovermode='x unified', hoverlabel=dict(bgcolor='#333', font=dict(color='white')))   

    if hoverData is not None:

        x_new, y_new = 0,0
        x_new, y_new, x_old, y_old = hoverData['points'][0]['x'], hoverData['points'][0]['y'], x_new, y_new

        k = [x for x in range(10)]
        print(k)

        if (x_new != x_old) & (y_new != y_old):

            print(x_new, x_old, y_new, y_old)

            fig.add_trace(go.Scatter(x=[x_new], y=[y_new], mode='markers', marker=dict(color='red', size=10)))



            # new_trace = go.Scatter(x=[2], y=[3], mode='markers', marker=dict(color='red', size=10))
            # fig.add_trace(new_trace)

            # # Elimina el trazo que contiene el punto agregado
            # fig.delete_trace(fig.data.index(new_trace))

    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
