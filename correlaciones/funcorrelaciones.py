def correlacionitas(dataframe, listaelementos):
    
    ''' Esta función tomara un dataframe y retornara la correlacion entre dos columnas '''
    
    e1 = listaelementos[0]
    e2 = listaelementos[1]
    
    
    Grap8 = dataframe.copy()
    Grap8 = Grap8.loc[Grap8['NOMBRE_PRODUCTO'].isin(listaelementos)]
    # facturas con los dos productos
    l2 = list(Grap8['id_factura'])
    
    # dataframe con los dos productos
    df_aux = dataframe.copy()
    df_aux = df_aux[df_aux['id_factura'].isin(l2)]
    df_aux = df_aux.loc[df_aux['NOMBRE_PRODUCTO'].isin(listaelementos)]
    df_aux = df_aux.loc[:,['id_factura','NOMBRE_PRODUCTO']].reset_index(drop=True)
    
    df_aux.insert(2, 'Unidades', 1)
    df_aux = df_aux.groupby(['id_factura','NOMBRE_PRODUCTO']).sum().reset_index()

    
    df_aux = df_aux.pivot_table(index=['id_factura'], 
                               columns = 'NOMBRE_PRODUCTO', 
                               values='Unidades').reset_index()
    #df_aux = df_aux.fillna(0)
    
    ###prueba
    df_aux = df_aux.dropna()
    ### fin prueba
    
    
    # valor de la correlacion entre los dos elementos
    cc = df_aux[e1].corr(df_aux[e2])
    cc = round(cc,2)

    return cc