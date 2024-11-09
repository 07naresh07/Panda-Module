import pandas as pd

data = pd.read_csv('Sample.csv', header=0, names=['X','Y','Z','Description'], index_col=0, usecols=[1, 2, 3, 4])    #reading old csv
newData = data.to_csv('Test.csv')   #creating new csv
datas = pd.read_csv('Test.csv', index_col=0)    #reading new csv
print(datas)