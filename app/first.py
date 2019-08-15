import sqlalchemy
from sqlalchemy.orm import sessionmaker
import pandas as pd 
import flask

# engine = sqlalchemy.create_engine('mssql+pyodbc://LAPTOP-QDH3PMIF/master?driver=SQL+Server+Native+Client+11.0')
# connection = engine.connect()
# metadata = sqlalchemy.MetaData()
# sqlQ = sqlalchemy.Table('userinfo', metadata, autoload=True, autoload_with=engine)
# # print(sqlQ.columns.keys())

# qAns = sqlalchemy.select([sqlQ])
# ResultProxy = connection.execute(qAns)
# ResultSet = ResultProxy.fetchall()
# # print(ResultSet)
# df = pd.DataFrame(ResultSet, columns=['firstname', 'lastname', 'ID'])
# jsonData = df.to_json(orient="records")
# print(jsonData)

# url ()

df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
print(df)
print("*****split")
split = df.to_json(orient='split')
print(split)

print("*****records")
records = df.to_json(orient='records')
print(records)

print("*****index")
index = df.to_json(orient='index')
print(index)

print("*****columns")
columns = df.to_json(orient='columns')
print(columns)

print("*****values")
values = df.to_json(orient='values')
print(values)

print("*****table")
table = df.to_json(orient='table')
print(table)