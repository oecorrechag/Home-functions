from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

app = Dash(__name__, title = 'Modificar className',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

server = app.server

app.layout = html.Div([

        html.Div(id='ocultar_html', children=[
    
            html.Br(),html.Br(),html.Br(),
    
        ], style= {'display': 'block'}),

        dbc.Row([
    
            dbc.Col(className="bg-primary p-3 mt-3 col-12", children=[
    
                dbc.Button("Cambiar tamaño", id="boton", color="success", className="me-1"),

                html.H6("Este es un ejemplo de texto"),

            ]),

        
        ]),



])

# Esconder html
@callback(
    Output('ocultar_html', 'style'),
    Input("boton", "n_clicks")
)
def show_hide_element(n_clicks):
    if (n_clicks is not None) and (n_clicks % 2 != 0):
        return {'display': 'block'}
    elif (n_clicks is not None) and (n_clicks % 2 == 0):
        return {'display': 'none'}
    elif n_clicks is None:
        return {'display': 'none'}



# @app.callback(
#     Output("texto", "className"),
#     Input("boton", "n_clicks"),
#     State("texto", "className")
# )
# def cambiar_color(n_clicks, class_name):
#     if n_clicks and "col-6" in class_name:
#         return class_name.replace("col-6", "col-12")
#     elif n_clicks and "col-12" in class_name:
#         return class_name.replace("col-12", "col-6")
#     else:
#         return class_name
    
if __name__ == '__main__':
    app.run_server(debug=True)
