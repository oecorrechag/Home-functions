import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px


df = pd.read_parquet('data/df.parquet.gzip')
personas = pd.read_parquet('data/df_personas.parquet.gzip')

# Construir el dash

app = Dash(__name__)
app.layout = html.Div([
    html.Button(id='btn_menu',style={'display':'none'}), 
    dcc.Graph(id='Graph1', figure={}),
    html.Div(id='container'),
    dcc.Graph(id='Graph2', figure={}),
])

##### Server ---------------------

# Create graph with data
@callback(
        Output('Graph1', 'figure'),
        Input('btn_menu','n_clicks')
)            
def testfunc(clicks):
    px.set_mapbox_access_token(open("mapbox_token").read())
    mapa = df.copy()
    Graph1 = px.scatter_mapbox(mapa, lat="latitud", lon="longitud", 
                               color="departamento", 
                               # size="municipio",
                               hover_data=['id_persona'],
                               color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=3)
    return Graph1

# IMPRIME LOS DATOS SELECCIONADOS POR LAZO O CAJA
@callback(
        Output('container','children'),
        Input('Graph1','selectedData')
        )
def selectData(selectedData):
    return str('Selecting points produces a nested dictionary: {}'.format(selectedData))
    

# EL OTRO GRAFICO
@callback(
        Output('Graph2','figure'),
        Input('Graph1','selectedData')
)
def update_graph(selectedData):
    if selectedData is None:
        data_canada = px.data.gapminder().query("country == 'Canada'")
        Graph2 = px.bar(data_canada, x='year', y='pop')
        return Graph2
    else:
        lista_usuarios = []
        lista_usuarios2 = []
        for i in range(len(selectedData['points'])):
            lis = selectedData['points'][i]['customdata']
            lista_usuarios.append(lis[0])
        lista_usuarios2 = list(set(lista_usuarios))

        print(len(lista_usuarios2))
        print(lista_usuarios2)
        
        mapa2 = df.copy()
        mapa2 = mapa2[mapa2['id_persona'].isin(lista_usuarios2)]

        Graph2 = px.scatter_mapbox(mapa2, lat="latitud", lon="longitud", 
                                   color="municipio", 
                                   # size="municipio",
                                   hover_data=['id_persona'],
                                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=3)
        return Graph2

if __name__ == '__main__':
    app.run_server(debug=True)