import pandas as pd

file = pd.read_csv('sample.csv')
#data = file.dropna(inplace=True)   #To remove the empty rows or coumns
#data1 = file.fillna(100, inplace=True)  #To replace the empty shell
file['X'].fillna(100, inplace=True) #Replace specific shell of specific column
file['Y'].fillna(1000, inplace=True)
file['Z'].fillna(500, inplace=True)
print(file)