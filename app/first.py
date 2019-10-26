# pandas.DataFrame( data, index, columns, dtype, copy)
#https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm
#https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python


import pandas as pd
import numpy as np
# import openpyxl


# '''empty df'''
# df = pd.DataFrame()
# print(df)

# # li = [1,2,3,4,5] #5/1
# # df1 = pd.DataFrame(li, columns=["num", "x"]) #5/2
# # print(df1)

# li = [['Alex',10],['Bob',12],['Clarke',13]]
# df2 = pd.DataFrame(li, columns=["name", "age"]) #5/2
# print(df2)  
# print("***")
# # df2.to_excel("output.xlsx")

# indexes = [1,2,3,4]
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data, index=indexes)
# print(df)
# print("***")

# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data)
# print(df)
# print("***")


data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20, 'p': 0}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print(df1)
print("***")
# df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
# # df2["k"] = np.where(df2['a']==1, 'palak', 'red')
# df2["ab"] = 5
# df2["abc"] = df2["a"] + df2["ab"] 
# df2["abcd"] = df2["a"] - df2["ab"] 
# print(df2)

# df3 = df2.copy()
# print(df3)

# df4 = df2.sub(df3)
# df4.drop(columns=['a', 'b1', 'ab'], inplace = True)
# print(df4)


a = df1.loc['first']
f = df1.iloc[1]
# print(a)
# print(f)

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df[2:4]) ## 2 included but not 4

s = "palak"
a = s[::-1]
print(a)