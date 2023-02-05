from dash import Input, Output, callback

import pandas as pd
import plotly.express as px


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

@callback(
    Output('info1', 'children'),
    Output('grafico', 'figure'),
    Input('hide2', 'value'))
def display_value(value):

    df2 = df[df['City'] == value]

    info1 = value
    grafico = px.bar(df2, x="Fruit", y="Amount", color="City", barmode="group")
    
    return info1, grafico
