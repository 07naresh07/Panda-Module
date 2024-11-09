import pandas as pd

data = pd.read_csv('sample.csv', index_col=0)
data.drop_duplicates(inplace=True)
for i in data.index:
    if data.loc[i,'Z']>20000:
        data.drop(i, inplace=True)

print(data)