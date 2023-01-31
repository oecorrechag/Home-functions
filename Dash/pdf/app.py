from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
app.layout = html.Div([
    html.Button("Download Image", id="btn_image"),
    dcc.Download(id="download-image")
])


@app.callback(
    Output("download-image", "data"),
    Input("btn_image", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("assets/dia.pdf"
    )


if __name__ == "__main__":
    app.run_server(debug=True)