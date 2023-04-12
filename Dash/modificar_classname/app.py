from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

app = Dash(__name__, title = 'Modificar className',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

server = app.server

app.layout = html.Div([

        dbc.Button("Cambiar tamaño", id="boton", color="success", className="me-1"),
        
        html.Div("Este es un ejemplo de texto", id="texto", className="bg-primary p-3 mt-3 col-12"),

])

@app.callback(
    Output("texto", "className"),
    Input("boton", "n_clicks"),
    State("texto", "className")
)
def cambiar_color(n_clicks, class_name):
    if n_clicks and "col-6" in class_name:
        return class_name.replace("col-6", "col-12")
    elif n_clicks and "col-12" in class_name:
        return class_name.replace("col-12", "col-6")
    else:
        return class_name
    
if __name__ == '__main__':
    app.run_server(debug=True)
