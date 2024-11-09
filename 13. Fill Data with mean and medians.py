import pandas
import pandas as pd
import os

data = pd.read_csv('sample.csv', index_col=0)
i = data['X'].mean()
data['X'].fillna(i, inplace=True)
j = data['Y'].mode()
data['Z'].fillna(j, inplace=True)
print(data)