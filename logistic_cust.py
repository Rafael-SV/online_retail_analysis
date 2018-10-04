
import pandas as pd
import numpy as np
import time, warnings
import datetime as dt

warnings.filterwarnings("ignore")


data = pd.read_csv("data.csv")
data = data.dropna()
print(data.shape)
print(list(data.columns))
data.head()
data = pd.read_csv("data.csv", encoding="ISO-8859-1", dtype={'CustomerID': str, 'InvoiceNO': str})
print(data.shape)
data = data.dropna()
print(data.shape)
data = data[data['Quantity']>0]
print(data.shape)
