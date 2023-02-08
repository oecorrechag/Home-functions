from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc

from utils.consts import LOGO, TITLE

from components.CallbacksHeader import modal


header = html.Nav([
            dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=LOGO, height="30px")),
                                    dbc.Col(dbc.NavbarBrand(TITLE, className="ms-2")),
                                ],
                                align="center",
                                className="g-0",
                            ),
                            href="/",
                            style={"textDecoration": "none"},
                        ),
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(className="navbar", children=[

                            dbc.NavLink("Home", href="/home", active="partial"),
                            
                            dbc.NavLink("Page 1", href="/page1", active="partial"),

                            dbc.NavLink("Page 2", href="/page2", active="partial"),

                            modal,

                        ], id="navbar-collapse", is_open=False, navbar=True,
                        ),
                    ]
                ),
                color="dark",
                dark=True,
            ), 

    ], className='fixed-top'),




@callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open





footer = dbc.Container([
            dbc.Row(children=[

                html.Footer('© copyright, Build with Plotly and ❤ by'),
                html.A('Oscar', href='https://github.com/oecorrechag', target="_blank"),

            ], className="row text-center"), 
        ], fluid=True, id="footer", className="pb-4 pt-4"),

































# modals = html.Div(
#     [
#         html.A(dbc.Button("Quiero ser orador", outline=True, color="dark", className="me-1"), href="#conviertete-en-orador", className='text-light font-weight-bold'),
#         dbc.Button("Comprar tickets", id='modalCompra', className="btn-platzi"), 
#         dbc.Modal(
#             [
#                 dbc.ModalHeader(dbc.ModalTitle("Comprar tickets"), close_button=True),
#                 dbc.Row(className="m-3", children=[
#                         dbc.Label("Email: ", html_for="example-email-row", width=2),
#                         dbc.Col(
#                             dbc.Input(
#                                 type="email", id="example-email-row", placeholder="Enter email"
#                             ), width=10
#                         ),
#                         dbc.Alert("You have a mail", color="warning", className="m-3"),  
#                     ],
#                 ),

#                 dbc.ModalFooter([
#                     dbc.Button("Cancel", id="close-centered", n_clicks=0, color="secondary", className="me-1"),
#                     dbc.Button("Comprar", className="btn-platzi"),
#                 ]),
#             ],
#             id="modal-centered",
#             centered=True,
#             is_open=False,
#         ),
#     ]
# )

# @callback(
#     Output("modal-centered", "is_open"),
#     [Input("modalCompra", "n_clicks"), 
#      Input("close-centered", "n_clicks"),
#      Input("modal_comprar", "n_clicks")],
#     [State("modal-centered", "is_open")],
# )
# def toggle_modal(n1, n2, modal_comprar, is_open):
#     if n1 or n2 or modal_comprar:
#         return not is_open
#     return is_open
