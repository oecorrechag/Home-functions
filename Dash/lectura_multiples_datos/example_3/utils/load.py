import pandas as pd

estructura = {
    "opcion1": ["data/archivo1.csv", "data/archivo2.csv"],
    "opcion2": ["data/archivo3.csv", "data/archivo4.csv"]
}

data = {}
for opcion, archivos in estructura.items():
    dfs = [pd.read_csv(archivo) for archivo in archivos]
    data[opcion] = dfs