import pandas as pd

data = pd.read_csv('Sample.csv', index_col=0, usecols=[0, 1, 2, 3, 4], names=['S.N.', 'X', 'Y', 'Z', 'Dec'])
result = data.to_csv('Final.csv')

page = pd.read_csv('Final.csv')
show = ['X', 'Y', 'Z']
print(page[page.X>412918.6085])