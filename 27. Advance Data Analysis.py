import pandas as pd

data = pd.read_csv('surveys.csv', index_col=0)
#file = data.groupby('weight').size().sort_values(ascending=False).head()
#print(file.to_string())
file1 = data.plot_id.value_counts().head()  #counts in descending order and gives similar result as previous file function.
print(file1)