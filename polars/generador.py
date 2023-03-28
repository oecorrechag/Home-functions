import pandas as pd
import numpy as np
import random

import warnings
warnings.filterwarnings("ignore")


start_date = '2022-01-01'
end_date = '2022-12-31'
date_range = pd.date_range(start=start_date, end=end_date)

products = ['producto1', 'producto2', 'producto3', 'producto4', 'producto5']

stores = ['tienda1', 'tienda2', 'tienda3', 'tienda4', 'tienda5']

sales_data = pd.DataFrame(columns=['Fecha', 'Producto', 'Tienda', 'Cantidad', 'Precio'])

for date in date_range:
    for store in stores:
        for product in products:
            quantity = random.randint(1, 10)
            price = round(random.uniform(10, 20), 2)
            sales_data = sales_data.append({'Fecha': date, 'Producto': product, 'Tienda': store, 'Cantidad': quantity, 'Precio': price}, ignore_index=True)


sales_data.to_csv('sales_data.csv', encoding = 'utf-8-sig', index = False)
sales_data.to_parquet('sales_data.parquet.gzip', compression='gzip')

