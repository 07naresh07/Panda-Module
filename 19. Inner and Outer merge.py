import pandas as pd

# Create two sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3, 4],
                    'Name': ['Alice', 'Bob', 'Charlie', 'David']})

df2 = pd.DataFrame({'ID': [1, 2, 3, 5],
                    'Age': [25, 30, 35, 40]})

# Merge the DataFrames on the 'ID' column
result = pd.merge(df1, df2, on='ID', how='outer')   #Prints all data and gives NaN value to empty shells
result = pd.merge(df1, df2, on='ID', how='inner')   #Merges common shells only

print(result)