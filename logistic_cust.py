
import pandas as pd
import numpy as np
import time, warnings
import datetime as dt

warnings.filterwarnings("ignore")

# read file
data_raw = pd.read_csv("data.csv", encoding="ISO-8859-1", dtype={'CustomerID': str, 'InvoiceNo': str})
# take a peak at structure of raw input
print(data_raw.shape)
print(list(data_raw.columns))
data_raw.head()
print(data_raw.shape)

# time to start cleaning the data
data = data_raw.dropna()
print(data.shape)

# remove returned items
data = data[data['Quantity']>0]
# check for how many were removed
print(data.shape)
#check for dupes
print('duplicate entries: {}'.format(data.duplicated().sum()))

# take a look at value counts
pd.DataFrame([{'products': len(data['StockCode'].value_counts()), 'transactions': len(data['InvoiceNo'].value_counts()), 'customers': len(data['CustomerID'].value_counts()), }], columns = ['products', 'transactions', 'customers'])

# now groupby customer to count items per invoice (per order)
tmp = data.groupby(by=['CustomerID', 'InvoiceNo'], as_index=False)['InvoiceDate'].count()
tmp.head()
number_prod_per_basket = tmp.rename(columns = {'InvoiceDate':'Number_of_products'})
print(number_prod_per_basket[:10].sort_values('CustomerID'))
