import pandas as pd
import matplotlib.pyplot as pt

data = pd.read_csv('surveys.csv', index_col=0)
#group = data.groupby(['weight','year']).size().sort_values(ascending=False).head(10)
#graph = group.weight.plot(kind='bar')
graph = data.weight.plot(kind='bar')

pt.show()