# import pandas as pd

# data = {
#     'Name' : ['Nikhil','Vishu','Tanmay'],
#     'Age' :[25,None,32],
#     'Salary' :[5000,6000,None]
    
# }
# df = pd.DataFrame(data)
# # print("Original Dataframe")
# # print(df)

# null_values = df.isnull().sum()
# print(null_values)

# replace_values = df.fillna(100)
# print(replace_values)

# remove_rows = df.dropna(axis=1)
# print(remove_rows)

# # # sir ka code
# # # handle missing values
# # import pandas as pd
 
# # data = {
# #     'Name':['Ram','Kamal','Ajay'],
# #     'Age':[25,None,32],
# #     'Salary':[5000,6000,None]
# # }
# # df = pd.DataFrame(data)
# # print("Original Dataframe")
# # print(df)
 
# # # null findoud | fillna | dropna
# # print(df.isnull().sum()) # sum of null
 
# # df_drop = df.dropna()
# # print(df_drop)
 
# # # fillna
# # df['Age'].fillna(df['Age'].mean(),inplace=True)
# # df['Salary'].fillna(df['Salary'].mean(),inplace=True)
# # print(df)


# # encoding categorical values
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# data = {
#     'Name' : ['Nikhil','Vishu','Tanmay','Bilal','sujaan'],
#     'Age' :[25,None,32,20,14],
#     'Salary' :[5000,6000,None,4000,2000],
#     'gender' :['male','male','male','male','female']
# }
# df= pd.DataFrame(data)
# print("orignal dataframe")
# print(df)

# #label encoder
# le = LabelEncoder()
# df_label = df.copy()
# df_label['gender']=df['gender'].fillna('unknown')
# df_label['gender_encoder'] = le.fit_transform(df_label['gender'])
# print("after label encoding : ")
# print(df_label)


# # one hot encoding 
# import pandas as pd
# data = {
#     'colors':['red','green','blue','purple','Blue']
    
# }
# df = pd.DataFrame(data)
# print("original data")
# print(df)

# # one hot encoding
# encoded_df = pd.get_dummies(df,columns=['colors'])
# print("after one hot encoder")
# print(encoded_df)


#date 24-06-2026

# #handle missing value
# import pandas as pd
# import numpy as np

# data = {
#     'colors': ['red','green','blue','orange',np.nan]
# }
# df = pd.DataFrame(data)
# # print(df)

# # #handle null value
# df.dropna(inplace = True)
# # print(df)

# #label encoding
# from sklearn.preprocessing import LabelEncoder

# le = LabelEncoder()
# df['colors_encoder'] = le.fit_transform(df['colors'])
# print(df)


# #one hot encoding
# from sklearn.preprocessing import OneHotEncoder
# print(df)
# df.drop(['colors_encoder'],axis=1,inplace = True)
# print(df)

# # One Hot Encoding(by the help od pandas)
# df_encoder = pd.get_dummies(df,columns=['colors'])
# print(df_encoder)

# #combination of handle missing value | label encoding | onehot encoding
# import pandas as pd
# import numpy as np

# from sklearn.preprocessing import LabelEncoder , OneHotEncoder

# data = {
#     "age":[10,20,np.nan,26,32],
#     "gender" : ['male','female','other','male',np.nan],
#     "name" : ['tanmay','sujaan','temp','vishu','nikhil']    
# }
# df = pd.DataFrame(data)

# #handle missing values
# df['age'] = df['age'], fillna(df['age'].mean)
# df.dropna(subset=['gender'],inplace=True)
# print(df)

# #label encoding
# le = LabelEncoder()
# df['gender1'] = le.fit_transform(df['gender'])
# print(df)

# #one hot encoding

# oe = OneHotEncoder()
# oe_e = oe.fit_transform(df[['gender']]).toarray()
# print(oe_e)


# date = 25/06/2026

# #feature
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler

# data = {
#     "experince" :[300,600,900,1500],
#     "salary" :[1000,2000,1500,3000]
# }
# # data frame
# df = pd.DataFrame(data)
# print(df)
 
# # standard scaler
# scaler = StandardScaler()
# df['experience'] = scaler.fit_transform(df[['experience']]) # 2d
# print(df)

# # split data exp-> x | sal -> y
# X = df['experience'] # capital X
# y = df['salary']
 
# print(X)
# print(y)

# # graph plot 
# plt.plot(X,y)
# plt.xlabel("experience")
# plt.ylabel("salary")
# plt.title("experience vs salary")



# data split training testing
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
data = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"
 
df = pd.read_csv(data)
# print(df)
 
# split data
X = df['experience'] # capital X
y = df['salary']
 
# train test split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("x train: ",x_train )
print("x test: ",x_test)
print("y train: ", y_train)
print("y test: ", y_test)

#simple linear reg
from sklearn.linear_model import LinearRegression

#modal fit
modal = LinearRegression()
modal.fit([x_train],[y_train])

#modal perdiction

new_data = {
    "experience":[10]
    
}

df1 = pd.DataFrame(new_data)
print(df1)


# simple linear reg | prediction
from sklearn.linear_model import LinearRegression
 
# model fit
model = LinearRegression()
model.fit(x_train,y_train) # 2d
 
# input from user
user = int(input("Enter your Experience: "))
# model prediction
 
new_data = {
    "experience":[user]
}
 
df1 = pd.DataFrame(new_data)
print(df1)
pred_data = model.predict(df1)
print(pred_data[0])