import pandas as pd

headers = ['ID', 'Month', 'Day', 'Year', 'Plot ID', 'Special ID', 'Sex', 'Length', 'Weight']
data = pd.read_csv('surveys.csv', header=0, names=headers, index_col=0)
file = data.groupby('Day')
print(file.size().head())   #Counts the each entry  i.e. 1977 is entered 503 times for groupby 'Year'
print(file['Year'].agg(['mean', 'min', 'max']))