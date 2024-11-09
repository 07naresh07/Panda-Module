import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob', 'Charlie', 'David'],
    'Subject': ['Math', 'Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'Science'],
    'Score': [85, 90, 78, 92, 88, 75, 95, 80],
    'Age': [21, 23, 24, 26, 21, 23, 24, 26]
}
file = pd.DataFrame(data)
group = file.groupby(['Name', 'Subject'])
print(group.count())