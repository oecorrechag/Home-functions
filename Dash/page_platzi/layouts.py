from dash import html
import dash_bootstrap_components as dbc

LOGO = "assets\logo.png"
TITLE = 'Project Name'

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

                            dbc.NavItem(dbc.NavLink(html.A("Home", href="/home",
                                            className='text-light font-weight-bold'))),

                            dbc.NavItem(dbc.NavLink(html.A("Page1", href="/page1",
                                            className='text-light font-weight-bold'))),

                            dbc.NavItem(dbc.NavLink(html.A("Page2", href="/page2",
                                            className='text-light font-weight-bold'))),

                            dbc.NavItem(dbc.NavLink(html.A("Tickets", id='modal_comprar', href="/",
                                            className='text-platzi font-weight-bold'))),

                        ], id="navbar-collapse", is_open=False, navbar=True,
                        ),
                    ]
                ),
                color="dark",
                dark=True,
            ), 

    ], className='fixed-top'),

footer = dbc.Container([
            dbc.Row(children=[

                html.Footer('© copyright, Build with Plotly and ❤ by'),
                html.A('Oscar', href='https://github.com/oecorrechag', target="_blank"),

            ], className="row text-center"), 
        ], fluid=True, id="footer", className="pb-4 pt-4"),