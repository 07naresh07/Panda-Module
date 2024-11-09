import pandas as pd

datas = {
    'Names':['NA', 'UM', 'SU', 'SA', 'PR'],
    'Math':[80, 67, 60, 74, 90],
    'Science': [67, 54, 92, 90, 56],
    'Sports': ['Football', 'Cricket', 'Volleyball', 'Tekwando', 'Judo']
}
df = pd.DataFrame(datas, columns=['Names', 'Math', 'Science', 'Sports', 'help'])    #help prints NaN as it doesn't have any value to print
print(df)