import pandas as pd

data = pd.read_csv('surveys.csv', index_col=0)
result = data.hindfoot_length.tail(10)
print(result<40)
print(result[result<40])