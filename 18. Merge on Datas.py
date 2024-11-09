import pandas as pd

frame1 = pd.DataFrame({'key':range(5), 'frame1':['a', 'b', 'c', 'd', 'e']})
frame2 = pd.DataFrame({'key':range(2, 7), 'frame2':['s', 't', 'u', 'v', 'w']})
print(pd.merge(frame1, frame2, on='key', how='left'))   #Takes left data as main data i.e. fame1 and prints the all data for frame1 and common data only for frame2