from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, title = 'Grafico full',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Callbacks/chained_callback/social-capital-project.csv")

app.layout = html.Div([

    dcc.Dropdown(
        id='states',
        options=[{'label': 'ss', 'value': 'ss'}],
        value='ss',
        clearable=False
    ),

    html.Div(className="container-fluid", children=[
        dcc.Graph(id='display-map', figure={}, style={'width': '99vw', 'height': '95vh'}),
    ])

])

@callback(
    Output('display-map', 'figure'),
    Input('states', 'value')
)
def update_grpah(states):
    dff = df.copy()

    fig = px.scatter(dff, x='% without health insurance', y='% in fair or poor health',
                    color='% adults graduated high school',
                    trendline='ols',
                    size='bubble_size',
                    hover_name='County',
                    # hover_data={'bubble_size':False},
                    labels={'% adults graduated high school':'% graduated high school',
                            '% without health insurance':'% no health insurance',
                            '% in fair or poor health':'% poor health'}
                    )
    fig.update_layout(showlegend=False)
    fig.update_layout(yaxis_visible=False, yaxis_showticklabels=False, 
                      xaxis_visible=False, xaxis_showticklabels=False,
                      margin=dict(l=0, r=0, t=0, b=0),
                      showlegend=False, autosize=True,)
    
    # fig.update_layout(
    #     width=800,
    #     height=600,
    #     margin=dict(l=0, r=0, t=0, b=0),
    # )
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    