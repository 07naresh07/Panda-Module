import pandas as pd
import numpy as np

x = np.random.randint(5000, size = 50)
y = np.random.randint(12450, size = 50)
z = np.random.randint(367, size = 50)
data = pd.DataFrame({'X':x, 'Y':y, 'Z':z})
data.index.name='S.N.'
data.index+=1
file = data.to_csv('sample.csv')
print(f'CSV file is saved to sample.csv')
