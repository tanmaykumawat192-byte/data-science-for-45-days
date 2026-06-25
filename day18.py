# import pandas as pd
# import numpy as np
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# # df.loc[df["marks"] == 50,"marks"] = None
# # #sum
# # df= df.isnull().sum()

# # #drop null value by row
# # df.dropna()

# # #drop null value by col
# # df.dropna(axis = 1)

# # #fill by zero
# # df =df.fillna(0)

# #roll no -> 200 | marks -> 100
# # df.fillna({"roll no": 200 , "marks" : 100},inplace = True)
# # print(df)

# #marks -> mean 
# df =df['marks'].fillna(df['marks'].mean())
# print(df)

# #aggregation
# import pandas as pd

# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# #using manually
# df=df['marks'].sum()
# df=df['marks'].mea()
# df=df['marks'].min()
# df=df['marks'].max()
# #using aggregation
# # df =df['marks'].agg(['sum','mean','mix','max'])
# print(df)

# # concatenate
# import pandas as pd

# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)

# df1 = pd.read_json(url)
# #pd= pd.concat([df,df1]) #row
# df1.loc[2,'name'] ='tanmay'
# pd =pd.concat([df,df1],axis=1)

# print(pd)

import matplotlib.pyplot as plt
score = [10,20,30,40]
over = [1,2,3,4]
plt.plot(score, over)
plt.show()