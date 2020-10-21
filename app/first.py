import pandas as pd
import numpy as np
from pandas import DataFrame

List11={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],'Age':[25,40,35,90,14,92]}
df = pd.DataFrame(List11)
print(df)

df['Name'] = df['Name'].str.lower()
df16 = df.sort_values('Name')
print(df16)