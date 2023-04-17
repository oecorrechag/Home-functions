import pandas as pd
import numpy as np


def Pmf(data, column1, column2):

    ''' 
    Esta funcion retorna la funcion de probabilidad

    data = dataframe
    column1 = category
    column2 = units

    y retora un df con las dos columnas y el Pmf

    '''
    
    data_aux = data.copy()
    data_aux = data_aux.loc[:,[column1, column2]]

    salida = data_aux.groupby([column1]).sum().reset_index()
    total = salida[column2].sum()

    salida['pmf'] = salida[column2] / total
    
    return salida


def Cdf(data, column1, column2):

    ''' 
    Esta funcion retorna la funcion de probabilidad acumulada

    data = dataframe
    column1 = category
    column2 = units

    nota usa el -Pmf-

    y retora un df con las dos columnas y el Pmf

    '''
    
    data_aux = Pmf(data, column1, column2)
    data_aux['cdf'] = data_aux['pmf'].cumsum()
    
    return data_aux

def inverse_Cdf(data, column, inverse):

    ''' 
    Esta funcion retorna la invera de la funcion de probabilidad acumulada

    data = dataframe
    column1 = category
    inverse = valor que se desea saber

    y retora el valor de la inversa

    '''

    value = data[column].quantile(inverse)
    return value
