from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import JWT

from user import UserRegister
from item import Student
from security import authenticate,identity

app=Flask(__name__)
app.secret_key="123@123"
api=Api(app)

#items=[]
jwt = JWT(app, authenticate, identity)
		
		
api.add_resource(Student,'/student/<string:name>')
api.add_resource(UserRegister, '/register')
if __name__ == "__main__":
	app.run()
		
	
