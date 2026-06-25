# # import pandas as pd
# # url = "https://raw.githubusercontent.com/tanmaykumawat192-byte/data-science-for-45-days/refs/heads/main/file1.json"
# # df = pd.read_json(url)
# # df.loc[len(df)] = ["tanmay","5854"]
# # df.rename(columns={"name":"role"},inplace=True)
# # # df["role"] = df["salary"]
# # df["salary"] = [299,453,463,535,343,245]
# # print(df)

# import pandas as pd
# d = {
#     "name": ["vishal","virat","vineet"],
#     "salary" :[100,200,300]
# }
# df = pd.DataFrame(d )
# # df["holidays"] = df ["salary"] / 100
# # df["decrement"] = [10,20,30]

# # df.drop("salary",axis=1,inplace=True)
# # print(df.loc[2,"name"])
# # print(df.iloc[2,0])
# #get single row data
# # print(df.loc[1])
# #get multipal rows
# # print(df.loc[0:3])


# #sub data get using iloc
# # df1 = df.iloc[0:2,[0]] 
# # print(df1)

# #sub data get using loc
# df1 = df.loc[0:3,["name"]]
# print(df1)

# # print(df)
# import pandas as pd

# data = {
#     "Emp_ID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
#     "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
#     "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
#     "Experience": [2, 3, 5, 4, 1, 3]
# }
# df = pd.DataFrame(data)
# df.loc[df["Name"] == "Amit" , "Name"] ="Rahul"

# print(df)


import pandas as pd
url = "https://raw.githubusercontent.com/tanmaykumawat192-byte/data-science-for-45-days/refs/heads/main/student-data.json"

df = pd.read_json(url)
# df["science"] = df["english"]
# df.loc[df["name"] == "arun","name"] = "tanmay"
# print(df["name"][3:5])
# print(df)
# male_data = df[df["gender"] == "Male"]
# print(male_data)
# female_data = df[df["gender"] == "Female"]
# print(female_data)

# df = df[df["english"] == 95]
# df = df[df["maths"] < 60]
print(df[(df["physics"] >= 60) &(df["maths"] >= 60) & (df["english"] >= 60)])
# print(df)