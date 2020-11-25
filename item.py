from flask_restful import Resource, reqparse
from flask import Flask,request
from flask_jwt import jwt_required
import sqlite3
items=[]
class Student(Resource):
        
        #table_name="student"
        def get(self,name):
                item=self.get_data_by_name(name)
		#item=next(filter(lambda x:x["name"]==name ,items),None)
                return item,200 if item else 404
        def get_data_by_name(self,name):
                connection=sqlite3.connect("data.db")
                cursor=connection.cursor()
                query="select * from {table} where name=?".format(table="student")
                result=cursor.execute(query,(name,))
                #print(result,"result")
                row=result.fetchone()
                print(row,"row")
                connection.close()
                if row:
                    return {'student_name': {'name': row[0], 'city': row[1]}}
        @jwt_required()
        def post(self,name):
                data=request.get_json(force=True)
                if self.get_data_by_name(name):
                        
		##data=request.get_json(force=True)
		##if next(filter(lambda x:x['name']==data["name"],items),None):
                        return{"message":"student already registered"},400
                ##data=request.get_json(force=True)
                else:
                        self.insert_into_database(data)
			#items.append(data)
			#print(items)
                        return {"data":data},201
        def insert_into_database(self,item):
                
                connection=sqlite3.connect("data.db")
                cursor=connection.cursor()
                query="INSERT INTO {table} VALUES(?,?)".format(table="student")
                cursor.execute(query,(item["name"],item["city"]))
                connection.commit()
                connection.close()
