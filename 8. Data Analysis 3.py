import pandas as pd
data = pd.read_csv('surveys.csv', index_col=0)
result = data[(data.weight<40)&(data.sex=='F')&(data.year>2000)&(data.species_id=='OT')&(data.plot_id<5)&(data.month>5)].head()
print(result)