import pandas as pd
import numpy as np
from list_names import lista_nombres_femeninos, lista_nombres_masculinos

def buscar_sexo(data, variable_name):
    ''' 
        Esta funcion ingresa un dataframe, variable nombre
        retorna el dataframe con los sexos faltantes
    '''
    
    # copias de seguridad y lista de variables del dataframe original
    df_name = data.copy()

    # partir el nombre en nombres y apellidos
    df_name[variable_name] = df_name[variable_name].str.title()
    df_name[variable_name] = df_name[variable_name].str.replace('  ', ' ')
    nn = df_name[variable_name].str.split(pat = ' ', n = 4, expand = True)
    df_name['first_name'],df_name['first_name2'],df_name['last_name'],df_name['last_name2'],df_name['last_name3'] = nn[0],nn[1],nn[2],nn[3],nn[4]

    df_name.insert(1, 'sexo_f', np.nan)
    df_name.insert(2, 'sexo_m', np.nan)
    
    # revisar si el nombre corresponde a femenino o masculino
    df_name['sexo_f'] = np.where((df_name['first_name'].isin(lista_nombres_femeninos))
                                | (df_name['first_name2'].isin(lista_nombres_femeninos))
                                | (df_name['last_name'].isin(lista_nombres_femeninos))
                                | (df_name['last_name2'].isin(lista_nombres_femeninos))
                                | (df_name['last_name3'].isin(lista_nombres_femeninos)), 'F', 'N')

    df_name['sexo_m'] = np.where((df_name['first_name'].isin(lista_nombres_masculinos))
                                | (df_name['first_name2'].isin(lista_nombres_masculinos))
                                | (df_name['last_name'].isin(lista_nombres_masculinos))
                                | (df_name['last_name2'].isin(lista_nombres_masculinos))
                                | (df_name['last_name3'].isin(lista_nombres_masculinos)), 'M', 'N')

    conditions = [((df_name['sexo_f'] == 'F') & (df_name['sexo_m'] == 'N')),
                  ((df_name['sexo_f'] == 'N') & (df_name['sexo_m'] == 'M')),
                  ((df_name['sexo_f'] == 'N') & (df_name['sexo_m'] == 'N'))
                 ]
    values = ['F','M','N']
    df_name['sexo_asignado'] = np.select(conditions, values, default=np.nan)
    df_name['sexo_asignado'] = df_name['sexo_asignado'].replace(['N'],np.nan)

    # salida de dataframe
    df_salida = df_name.loc[:,[variable_name, 'sexo_asignado']]
    df_salida = df_salida.drop_duplicates()

    return df_salida