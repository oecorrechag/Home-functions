import pandas as pd
import numpy as np

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