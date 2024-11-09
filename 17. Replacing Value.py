import pandas as pd


data = pd.read_csv('sample.csv', index_col=0)
data.loc[10, 'X']=500

for i in data.index:
    if data.loc[i, 'X']>2000:
        data.loc[i, 'X']=500
print(data)