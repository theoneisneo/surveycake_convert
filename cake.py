import pandas as pd

filename = "data.xlsx"

df = pd.read_excel(filename)

# create a big table (by py dict).
# the "key" of big table is the ordinal of columns.
# the "value" of big table is a small table, convert option names to any new values you want (for each column).
# *note that in this example, the new values can be get from indexes of a list of option names.
# so I create a list of option names, then convert the list to a new table (called "mapping").
transform = dict()
transform[0] = ['', '非常不同意', '不同意', '普通', '同意', '非常同意']
transform[1] = ['', '一天不到一份訊息', '一天兩份訊息', '一天三份訊息', '一天超過四份訊息']
transform[2] = ['', '完全忽略', '偶爾會看', '累積很多則後會看', '有空時會看', '馬上看']
transform[3] = ['', '完全不看', '大概1/4', '大概一半', '大概3/4', '全部看完']
transform[4] = ['', '男性', '女性']
transform[5] = ['', '0-18歲', '18-34歲', '34歲以上']
transform[6] = ['', '國小', '國中', '高中', '大學', '碩士', '博士', '其他']
transform[7] = ['', '少於$22,000', '多於$22,000']

# convert the list to a new table "mapping".
for ordinal_of_columns in transform:
    mapping = dict()
    for i, option_name in enumerate(transform[ordinal_of_columns]):
        mapping[option_name] = i
    transform[ordinal_of_columns] = mapping

# replace things column by column
for ordinal_of_columns in transform:
    column_name = df.columns[ordinal_of_columns]
    # replace each options name to new value
    for option_name in transform[ordinal_of_columns]:
        df[column_name].replace(to_replace=option_name, replace=transform[ordinal_of_columns][option_name], inplace=True)


# if want to change column names
# new_columns = [''] * len(transform)
# new_columns = ...
# df.columns = new_columns

df.to_csv('data_coded.csv', index=False)
