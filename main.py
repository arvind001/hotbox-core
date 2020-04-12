# imports 
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import json

## global variables
app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/hotboxdb'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class BoxPost(db.Model):
    firstName = db.Column(db.String(), primary_key=True)
    lastName = db.Column(db.String())
    phoneNumber = db.Column(db.String())
    emailAddress = db.Column(db.String())
    boxAddress = db.Column(db.String())
    
    def __init__(self, firstName, lastName, phoneNumber, emailAddress, boxAddress):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.boxAddress = boxAddress

## declaration for the '/registerUser' endpoint
class RegisterUser(Resource) :
  ## '/registerUser' GET request
  def get(self):
    # get url query parameters
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    phoneNumber = request.args.get('phoneNumber')
    email = request.args.get('emailAddress')
    boxAddress = request.args.get('boxAddress')

    resp = {
      'statusMsg' : 'account sucessfuly recieved',
      'firstName' : firstName,
      'lastName' : lastName,
      'phoneNumber' : phoneNumber,
      'emailAddress' : email,
      'boxAddress' : boxAddress
    }

    return{
      'about':'GET ',
      'data_type':'text block',
      'response':resp
    }
    print(resp)

  ## '/registerUser' POST request
  def post(self):
    # get request payload data
    reqPayload = request.get_json(force=True)

    firstName = reqPayload['firstName']
    lastName = reqPayload['lastName']
    phoneNumber = reqPayload['phoneNumber']
    email = reqPayload['emailAddress']
    boxAddress = reqPayload['boxAddress']

    resp = {
      'statusMsg' : 'account sucessfuly recieved',
      'firstName' : firstName,
      'lastname' : lastName,
      'phoneNumber' : phoneNumber,
      'emailAddress' : email,
      'boxAddress' : boxAddress
    }

    return{
      'about':'POST ',
      'data_type':'text block',
      'response':resp
    }
    print(resp)

api.add_resource(RegisterUser, '/registerUser')

## global functions

## main function
if __name__ == '__main__':
  manager.run()

  # app.run(debug=True)