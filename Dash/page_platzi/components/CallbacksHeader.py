from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc


modal = html.Div(
    [
        dbc.Button("Open modal", id="open", className='btn-platzi', n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)



