def remplazamientos(dataframe_name, variable_name):
    
    ll = []
    i = 1
    j = 1
    while i != 'ok':
        i = input('Entrada valor viejo: ')
        if i != 'ok':
            j = input('Entrada valor nuevo: ')
            sentencia = '{}[\'{}\'] = np.where({}[\'{}\'] == \'{}\', \'{}\', {}[\'{}\'])'.format(dataframe_name,variable_name,dataframe_name,variable_name,i,j,dataframe_name,variable_name)
            ll.append(sentencia)
    ll = '  \n'.join(ll)

    print(ll)