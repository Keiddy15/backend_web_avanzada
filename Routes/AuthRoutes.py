
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
    user = Services.Users.get_user_by_email_and_password(email=email, password=password)
    id_number = user.id_number
    role = user.role
    name = user.name
    #Validating user
    if user:
        access_token = Utils.Token.generate_token(email, id_number, role, name)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Incorrect credentials'}), 401