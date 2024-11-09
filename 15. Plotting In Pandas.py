import pandas as pd
import matplotlib.pyplot as pt

data = pd.read_csv('sample.csv')
data.plot()
data.plot(kind='scatter', x='X', y='Y')

data['X'].plot(kind='hist')

pt.show()