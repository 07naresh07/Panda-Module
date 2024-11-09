import pandas as pd

df1 = pd.DataFrame({
    'year': [2021, 2021, 2022, 2022],
    'quarter': [1, 2, 1, 2],
    'revenue': [100, 200, 150, 250]
})

df2 = pd.DataFrame({
    'year': [2021, 2021, 2022, 2022],
    'quarter': [1, 2, 1, 2],
    'expenses': [80, 120, 100, 140]
})

# Merge on multiple columns
result = pd.merge(df1, df2, on=['year', 'quarter'])

print(result)