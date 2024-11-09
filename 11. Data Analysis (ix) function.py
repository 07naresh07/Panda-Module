import pandas as pd

data = pd.read_csv('surveys.csv')
result = data.set_index('record_id', inplace=True)  #sets index to record_id
print(data['sex'])  #To get the column of sex or other desired columns
