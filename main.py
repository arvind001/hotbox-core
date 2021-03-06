# imports 
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json

## global variables
app = Flask(__name__)
api = Api(app)
CORS(app)

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
  app.run(debug=True)