import pandas as pd
data = pd.read_csv('surveys.csv', index_col=0)
result = data[(data.year<2000)&(data.month>11)|(data.sex=='M')&(data.weight>60)].tail() #OR operator
print(result)