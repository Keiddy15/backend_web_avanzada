
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from Config.db import db
import Services.index as Services
import Utils.index as Utils

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    #Get the user
    user = Services.Users.get_admin(email=email, password=password)
    #Validating user
    if user:
        access_token = Utils.Token.generate_token(email, password)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Incorrect credentials'}), 401