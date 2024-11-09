import pandas as pd

data = pd.read_csv('surveys.csv', index_col=0)
file = data.groupby(['day', 'year', 'weight', 'plot_id'])
print(file.size())
print(file.count()) #count how many times does that ibject entered