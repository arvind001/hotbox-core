# imports 
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

## global variables
app = Flask(__name__)
api = Api(app)

## declaration for the '/registerUser' endpoint
class RegisterUser(Resource) :
  ## '/registerUser' GET request
  def get(self):
    firstName = request.args.get('firstname')
    lastname = request.args.get('lastname')
    phoneNumber = request.args.get('phoneNumber')
    email = request.args.get('email')
    boxAddress = request.args.get('boxAddress')

    resp = {
      'statusMsg' : 'account sucessfuly recieved',
      'firstName' : firstName,
      'lastname' : lastname,
      'phoneNumber' : phoneNumber,
      'email' : email,
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
    firstName = request.args.get('firstname')
    lastname = request.args.get('lastname')
    phoneNumber = request.args.get('phoneNumber')
    email = request.args.get('email')
    boxAddress = request.args.get('boxAddress')

    resp = {
      'statusMsg' : 'account sucessfuly recieved',
      'firstName' : firstName,
      'lastname' : lastname,
      'phoneNumber' : phoneNumber,
      'email' : email,
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