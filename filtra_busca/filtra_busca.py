import pandas as pd
import numpy as np

def buscar_in(dataframe, columna, columnaNueva, palabraBuscar, palabraRemplazo):

    '''Esta función busca una palabra espeifica dentro de una columna y cambia toda la celda por un valor dado'''
    
    df_test2 = dataframe[dataframe[columna].str.contains(palabraBuscar, na=False)]
    
    ls = df_test2[columna].unique()
    
    for i in ls:
        dataframe[columnaNueva] = np.where(dataframe[columna] == i, palabraRemplazo, dataframe[columnaNueva])
    
    return dataframe

df = buscar_in(df, 'columna_buscar', 'columna_guardar', 'palabra_a_buscar', 'palabra_de_remplazo')
