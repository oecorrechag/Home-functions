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
    
            dbc.Col(id='menu', className="bg-primary col-8 offset-2", children=[
    
                dbc.Button("Cambiar tamaño", id="boton", color="success", className="me-1"),

                html.H6("Columna 1"),

            ]),

            dbc.Col(id='menu2', className="bg-success col-6", children=[

                html.H6("Columna 2"),

            ], style= {'display': 'none'}),

        ]),



])

###########################################################################################################
################################################# Ocultar #################################################
###########################################################################################################

@callback(
    Output('ocultar', 'style'),
    Output('menu2', 'style'),
    Input("boton", "n_clicks")
)
def show_hide_element(n_clicks):
    if n_clicks is None:
        return {},{"display": "none"}
    elif n_clicks % 2 == 0:
        return {},{"display": "none"}
    else:
        return {"display": "none"},{}


###########################################################################################################
################################################ className ################################################
###########################################################################################################

@callback(
    Output("menu", "className"),
    Input("boton", "n_clicks"),
    State("menu", "className"),
)
def reduce(n_clicks, class_name):
    if n_clicks and "col-8" in class_name:
        return class_name.replace("col-8 offset-2", "col-6")
    elif n_clicks and "col-6" in class_name:
        return class_name.replace("col-6", "col-8 offset-2")
    else:
        return class_name

    
if __name__ == '__main__':
    app.run_server(debug=True)