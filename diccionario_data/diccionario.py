import pandas as pd
import numpy as np

def crear_diccionario(data):

    ''' Esta función ingresa un dataframe y retorna un dataframe con:
        - Columnas: Nombre de columna
        - Categorias: Categorias que tiene la columna [solo si se tiene 5 o menos categorias]
        - Unicidad: Unicidad de coilumna
        - Significado: Columna vacia para insertar el significado de dicha columna
    '''

    lf = []
    lf2 = []

    lista_columnas = data.columns.values.tolist()
    diccionario_datos = {'Columnas': lista_columnas}
    diccionario_datos = pd.DataFrame.from_dict(diccionario_datos)

    for (colname, colval) in data.iteritems():
        
        # Seleccionar las categorias de la columna
        elementos = colval.unique()
        # Revisar si la columna cumple o no unicidad
        respuesta = data[colname].nunique() == data.shape[0]
        
        if len(elementos) > 5:
            elementos = []
        
        lf.append(elementos)
        lf2.append(respuesta)

    # Agregar al dataframe diccionario_datos            
    diccionario_datos['Categorias'] = lf
    diccionario_datos['Unicidad'] = lf2
    diccionario_datos['Unicidad'] = np.where(diccionario_datos['Unicidad'] == True, 'Si', 'No')
    diccionario_datos = diccionario_datos.explode('Categorias')
    diccionario_datos.insert(3, 'Significado', '')
    diccionario_datos = diccionario_datos.fillna('')

    return diccionario_datos