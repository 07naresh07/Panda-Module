import pandas as pd

data = pd.read_csv('surveys.csv')
print(data.dtypes.head(2)) #for getting the data type of the datas
result=data.set_index('record_id', inplace=True)
print(data.describe())  #If we want to know mean, standard deviation and other datas
print(data)
