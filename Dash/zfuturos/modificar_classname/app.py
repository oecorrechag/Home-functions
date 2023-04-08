import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.Button("Cambiar color", id="boton"),
        html.Div("Este es un ejemplo de texto", id="texto", className="bg-primary p-3 mt-3 col-12"),
    ]
)

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

if __name__ == "__main__":
    app.run_server()
