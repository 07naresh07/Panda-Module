import pandas as pd
import numpy as np

s = pd.Series([34, 23, 'Naresh', 34.9], index=['a','b','c','d'])
print(s)
print(s.iloc[0])
print(s.iloc[3])    #It can print without iloc as well
print(s['b'])   #printing as per indexing
print('************************************')
S = pd.Series({'Naresh':29, 'Uma':28, 'Sam':23.6, 'Amit':32})   #Dictionary
print(S)
print(S.iloc[0])
print(S['Sam'])
print(S[S>30])
print(S[S<30])
print(S<30)
print('************************************')
S['Uma']=31 #Replacing the original value
S[S<30]=35  #Replaces all values less than 30 to 35.
print(S)

print('**************************************')
print('Sam' in S)   #Checks if 'Sam' is in series S or not and returns boolean value
print('Gita' in S)

print('**************************************')
print(S/10) #Divides the integer part of dictionary by 10

print('**************************************')
print(np.square(S)) #Squares the integer value of S using numpy module

print('**************************************')
print(S.isnull())   #Checks if any element from S is null