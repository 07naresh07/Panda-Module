import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob', 'Charlie', 'David'],
    'Subject': ['Math', 'Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'Science'],
    'Score': [85, 90, 78, 92, 88, 75, 95, 80],
    'Age': [21, 23, 24, 26, 21, 23, 24, 26]
}
group = pd.DataFrame(data)
file = group.groupby('Name')
#print(file.count().head())  #Object counting
#print(file['Age'].mean())   #Calculates the mean of Age for each element of group Name
print(file['Score'].agg(['mean', 'min', 'max', 'median', 'std']))