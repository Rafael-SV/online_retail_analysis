
import pandas as pd
import numpy as np
from sklearn import preprocessing
from matplotlib import pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn
#seaborn.set(style="white")
#seaborn.set(style="whitegrid", color_codes=True)
#
data = pd.read_csv("data.csv")
data = data.dropna()
print(data.shape)
print(list(data.columns))
data.head()
