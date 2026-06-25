# import pandas as pd
# url = "https://raw.githubusercontent.com/tanmaykumawat192-byte/data-science-for-45-days/refs/heads/main/student-data.json"

# df = pd.read_json(url)
#add column total = phy+maths+eng
# df["total"] = df["english"]+ df["maths"]+ df["physics"]

#add rows
# df.loc[14] = ["tanmay","male",96,78,87]

#update rows and column

#delete column
# df.drop("total",axis=1)

#delete row
# df = df.drop(13)

#add date 

# print(df)

# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# df['date'] = ['2025-01-10','2025-02-10','2025-03-10','2025-04-10','2025-05-10']

# print(df)


import pandas as pd

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df.loc[df["marks"] == 50,"marks"] = "null"
print(df)