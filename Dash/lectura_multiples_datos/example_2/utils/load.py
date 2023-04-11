import pandas as pd

data = {
    "grupo1": {
        "archivo1.csv": pd.read_csv("data/archivo1.csv"),
        "archivo2.csv": pd.read_csv("data/archivo2.csv")
    },
    "grupo2": {
        "archivo3.csv": pd.read_csv("data/archivo3.csv"),
        "archivo4.csv": pd.read_csv("data/archivo4.csv")
    }
}