import pandas as pd
import numpy as np

###### Dataframe desde diccionario

df1 = {'integrantes': ['A','B','C','D','E'], 
       'valor': [1,np.nan,np.nan,np.nan,np.nan],
       'car': [1,2,4,5,6],
       'w2018w': ['a','s',np.nan,np.nan,'11']
      }
df1 = pd.DataFrame.from_dict(df1)
df1


df = pd.DataFrame(columns=['A','B','C','D','E','F','G'])
df.insert(0, "id", [1,2,3,4,5])
df.head()

###### Dataframe desde listas

# list of strings
lst = ['A','B','C','D','E']
# list of int
lst2 = [11, 22, 33, 44, 55]
  
# Calling DataFrame constructor after zipping
df = pd.DataFrame(list(zip(lst, lst2)),
               columns =['letter', 'val'])
df.head()