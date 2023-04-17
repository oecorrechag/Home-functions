from dash import Dash, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

app = Dash(__name__, title = 'Modificar className example 3',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

server = app.server

app.layout = html.Div([

        dbc.Row(id='ocultar', children=[
    
            html.Br(),html.Br(),html.Br(),
    
        ], style= {'display': 'none'}),

        dbc.Row([
    
            dbc.Col(id='menu', className="bg-primary col-6 offset-3", children=[
    
                dbc.Button("Cambiar tamaño", id="boton", color="success", className="me-1"),

                html.H6("Este es un ejemplo de texto"),

            ]),

        
        ]),



])

###########################################################################################################
################################################# Ocultar #################################################
###########################################################################################################

@callback(
    Output('ocultar', 'style'),
    Input("boton", "n_clicks")
)
def show_hide_element(n_clicks):
    print(n_clicks)
    if n_clicks is None:
        return {}
    elif n_clicks % 2 == 0:
        return {}
    else:
        return {"display": "none"}


###########################################################################################################
################################################ className ################################################
###########################################################################################################

@callback(
    Output("menu", "className"),
    Input("boton", "n_clicks"),
    State("menu", "className"),
)
def reduce(n_clicks, class_name):
    if n_clicks and "col-6" in class_name:
        return class_name.replace("col-6 offset-3", "col-12")
    elif n_clicks and "col-12" in class_name:
        return class_name.replace("col-12", "col-6 offset-3")
    else:
        return class_name

    
if __name__ == '__main__':
    app.run_server(debug=True)
