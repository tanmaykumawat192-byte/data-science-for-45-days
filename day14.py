# """Basic dataframes understanding
# 1. head()
# 2. tail()
# 3. shape
# 4. info()
# 5. rename
# 6. describe() -> count
# """

# # #info()
# # # csv file import from github
# # import pandas as pd
# # url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# # df = pd.read_json(url)
# # df.info()

# # #rename
# # # csv file import from github
# # import pandas as pd
# # url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# # df = pd.read_json(url)
# # df.rename(columns={"name":"student_name"},inplace=True)
# # #orignal variabledf ->value same
# # df

# # # csv file import from github
# # import pandas as pd
# # url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# # df = pd.read_json(url)
# # df.describe( )


# # data = {
# # "Emp_Id":[101,102,103,104,105,106],
# # "Name":["Amit","Riya","raj","Sara","john","Neha"],
# # "Department":["IT","HR","Finance","IT","Sales","HR"],
# # "Salary":[50000,45000,60000,55000,48000,52000],
# # "Experience":[2,3,5,4,1,3]
# # }
# # df = pd.DataFrame(data)
# # print(df)

# # print(df.head())
# # print(df.tail())
# # print(df.info)
# # print(df.shape)
# # print(df.describe())
# # df.rename(columns={"name":"department_name"},inplace=True)
# # print(df)

# # # csv file import from github
# # import pandas as pd
# # url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# # df = pd.read_json(url)
# # #get single column data
# # df["name"]
# # # add single column
# # df["salary"] = df["marks"] + 100
# # #add single column
# # df["salary"] = [100,200,300,400,500]
# # df

# import pandas as pd
# d = {
#     "name": ["vishal","virat","vineet"],
#     "salary" :[100,200,300]
# }
# df = pd.DataFrame(data= d )
# # df["marks"] = [10,20,40]
# df["marks"] =  df ["salary"]/2

# df["increment"] = df["salary"] * 1.10
# df.rename(columns={"increment":"increment_salary"},inplace=True)
# df