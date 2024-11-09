import pandas as pd

frame1 = pd.DataFrame({'key':range(5), 'frame1':['a', 'b', 'c', 'd', 'e']})
frame2 = pd.DataFrame({'key':range(2, 7), 'frame2':['s', 't', 'u', 'v', 'w']})
print(pd.concat([frame1, frame2], axis=1))