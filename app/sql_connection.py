import sqlalchemy
from sqlalchemy.orm import sessionmaker
import pandas as pd 
from app import app
from flask import jsonify, request
import json

@app.route('/firstpage')
def firstpage():
	# name = request.args.get("firstname")
	engine = sqlalchemy.create_engine('mssql+pyodbc://LAPTOP-QDH3PMIF/master?driver=SQL+Server+Native+Client+11.0')
	connection = engine.connect()
	metadata = sqlalchemy.MetaData()
	sqlQ = sqlalchemy.Table('userinfo', metadata, autoload=True, autoload_with=engine) # print(sqlQ.columns.keys())

	qAns = sqlalchemy.select([sqlQ])  ### select q
	ResultProxy = connection.execute(qAns)
	ResultSet = ResultProxy.fetchall()
	df = pd.DataFrame(ResultSet, columns=['firstname', 'lastname', 'ID'])
	# df = df[df['firstname']==name]
	print(df)
	jsonData = df.to_json(orient="records")
	return jsonData 