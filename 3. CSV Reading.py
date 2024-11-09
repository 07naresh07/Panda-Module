import pandas as pd

#pd.read_csv("Sample.csv")
#data = pd.read_csv("Sample.csv", names=['Nos', 'X', 'Y', 'Z', 'Description'], header=0) #If we hace default header from CSV then we can use header=0 tp remove header
#print(data)
data1 = pd.read_csv("Sample.csv", usecols=[1, 2, 3, 4], index_col=0, names=['X', 'Y', 'Z', 'Description'])  #To print the desired columns
print(data1)
