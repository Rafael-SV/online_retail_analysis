
import pandas as pd
import numpy as np
import time, warnings
import datetime as dt

warnings.filterwarnings("ignore")


data_raw = pd.read_csv("data.csv", encoding="ISO-8859-1", dtype={'CustomerID': str, 'InvoiceNo': str})
print(data_raw.shape)
print(list(data_raw.columns))
data_raw.head()
print(data_raw.shape)
data = data_raw.dropna()
print(data.shape)
data = data[data['Quantity']>0]
print(data.shape)
print('duplicate entries: {}'.format(data.duplicated().sum()))

pd.DataFrame([{'products': len(data['StockCode'].value_counts()), 'transactions': len(data['InvoiceNo'].value_counts()), 'customers': len(data['CustomerID'].value_counts()), }], columns = ['products', 'transactions', 'customers'])
