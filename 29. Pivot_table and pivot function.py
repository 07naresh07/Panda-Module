import pandas as pd

# Create a sample DataFrame with duplicate entries
df = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
    'product': ['A', 'B', 'A', 'A', 'B', 'A'],
    'sales': [100, 150, 120, 90, 180, 110]
})
#data = df.pivot(index=['date'],columns=['product'], values='sales') = In this line pivot table raises duplicate error as 2023-01-01 has two sales vale for A
data = df.pivot_table(index=['date'],columns=['product'], values='sales', aggfunc='sum')    #addfunc='sum' adds the duplicate value to make one i.e. 100+120=220
print(data)