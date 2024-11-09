import pandas as pd
import matplotlib.pyplot as pt

file = pd.read_csv('surveys.csv', index_col=0)
#result = file.groupby('weight').size().sort_values(ascending=False)[:50]
data = file.pivot_table(index=['year'], columns=['sex'], values = 'weight', fill_value=0)
data['diff']=data.M-data.F  #adds another column called diff and do the assigned task
pt.title('Difference of Male and Female weight')
pt.xlabel('Year')
pt.ylabel('Difference of Weight')
data['diff'].plot(kind='bar', figsize=[12, 10])
pt.savefig('graph.jpg', dpi=1200)
pt.show()