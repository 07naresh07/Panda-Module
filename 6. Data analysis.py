import pandas as pd

data = pd.read_csv('surveys.csv', index_col=0)
df = pd.DataFrame(data)
result = df[(df.sex=='M')&(df.weight>40)].head(10)
print(result)