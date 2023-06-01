from dash import html
import plotly.graph_objects as go

def hover_hover(prev_x, prev_y, x_hover, y_hover):

    # Compara el valor actual de 'x' con el valor anterior
    if x_hover == prev_x:
        hover_info = f'Posición del puntero: x={x_hover}, y={y_hover}'
        # fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', showlegend=False, marker=dict(color='gray', size=20)))
        # fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', name="Spline", showlegend=False, marker=dict(color='blue', size=10)))
        # fig.update_traces(
        #     hovertemplate="<br>".join([
        #         "Sepal length: %{x}",
        #         "Sepal width: %{y}",
        #     ])
        # )
    else:
        prev_x = x_hover
        prev_y = y_hover
        hover_info = f'Posición del puntero nuevo: x={x_hover}, y={y_hover}'
        # print(x_hover, y_hover)
        # fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', showlegend=False, marker=dict(color='gray', size=20)))
        # fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers', name="Spline", showlegend=False, marker=dict(color='blue', size=10)))
        # fig.update_traces(
        #     hovertemplate="<br>".join([
        #         "Sepal length: %{x}",
        #         "Sepal width: %{y}",
        #     ])
        # )
    
    return hover_info


def hover_sho(fig, hoverData, name, color):
    global prev_x, prev_y
    if hoverData is not None:

        print(hoverData['points'][0])
        x_hover = hoverData['points'][0]['x']
        y_hover = hoverData['points'][0]['y']
        # color_hover = hoverData['points'][0]['curveNumber']

        fig.add_trace(go.Scatter(x=[x_hover], y=[y_hover], mode='markers',
                                 name=name, showlegend=False, 
                                 marker=dict(color=color, size=10)))
        fig.update_traces(hoverinfo="none", hovertemplate=None)
        fig = fig.update_layout(uirevision="Don't change")
        # fig.update_traces(
        #     hovertemplate="<br>".join([
        #         "X value: %{x}",
        #         "Y value: %{y}",
        #     ])
        # )
        

        return fig
    