import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc


# Data
df = pd.DataFrame({'a': [1, 2, 3, 4, 1, 2], 
                   'b': [2, 1, 5, 6, 9, 2],
                   'c': ['x', 'x', 'y', 'y', 'x', 'y']})


app = Dash(__name__, title = 'Page test',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server

app.layout = html.Div([

    html.Br(),html.Br(),html.Br(),
    
    html.Div([
    
            dbc.Button("Download", id="btn", className="btn-platzi me-2"),
            dcc.Download(id="download"),

    ])

])

@app.callback(
    Output("download", "data"), 
    [Input("btn", "n_clicks")])
def func(n_nlicks):
    if n_nlicks is None:
        return dash.no_update
    else:
        df2 = df.copy()
        enviaros = dcc.send_data_frame(df2.to_csv, "mydf.csv", index = False)
        #enviaros = dcc.send_data_frame(df.to_excel, "mydf.xls", index = False)
    return enviaros


if __name__ == '__main__':
    app.run_server(debug=True)
