# # import pandas as pd
# # d = {
# #     "name ": ["vishu", "nikhil", "bilal"],
# #     "roll_no":[1,2,4]
# # }
# # df = pd.DataFrame(d)
# # print(df)

# #csv file
# import pandas as pd
# url = "file.csv"
# df = pd.read_csv(url)
# print(df)

# # csv file import from github
# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# df
# # head -> starting 5 rows
# df.head(2)
# # head -> 2 rows data
# df.head(-3)
# # head -> negative number

# """What is DataFrame()?
# -> A DataFrame is a two-dimensional labeled data structure in Pandas that organizes data into 
#    rows and columns and allows efficient data analysis and manipulation.
   
#    Difference between CSV(Comma Separated Values), JSON(JavaScript Object Notation), and Excel 
# |    Feature      | CSV            | JSON            | Excel            |
# | syntax          | .csv           | .json           | .xlsx            |
# | Format          | Plain text     | Key-value pairs | Spreadsheet      |
# | Human readable  | Yes            | Yes             | Through Excel    |
# | Multiple sheets | No             | No              | Yes              |
# | File size       | Small          | Medium          | Larger           |
# | Common use      | Data exchange  | APIs/Web apps   | Business reports |
# | Import          | pd.read_csv(fn)| pd.read_json(fn)| pd.read_excel(fn)|
#    """

# # df = pd.read_csv("file1.csv")
# # print(df)

# # df1 = pd.read_excel("file1.xlsx")
# # print(df1)

# # df2 = pd.read_json("file1.json")
# # print(df2)