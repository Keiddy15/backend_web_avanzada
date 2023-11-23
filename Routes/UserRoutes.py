
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from Config.db import db
import Services.index as Services
import Utils.index as Utils

user = Blueprint("user", __name__)

@user.route('/create', methods=['POST'])
def create():
    #Getting the token
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = Utils.Token.verify_token(token)
    #Verifying the token
    if vf["error"] == False:
        data = request.get_json()
        name = data['name']
        email = data['email']
        role = data['role']
        id_number = data['id_number']
        #validate if user exist
        user = Services.Users.get_user(email)
        if user:
            return jsonify({"error": True, "message": "User exist"}), 400
        else:
            #Creating a user
            new_user = Services.Users.create(name, email, role, id_number)
            if new_user:
                return jsonify(new_user=new_user), 200
            else:
                return jsonify({"error": True, "message": "User exist"}), 400
    else:
        return jsonify(vf), 401

@user.route('/find_all', methods=['GET'])
def find_all():
    if 'Authorization' in request.headers:
        print("test")
        token = request.headers['Authorization']
        token = token.replace("Bearer","")
        token = token.replace(" ","")
        vf = Utils.Token.verify_token(token)
        #Verifying the token
        if vf["error"] == False:
            #Getting all users
            users = Services.Users.get_all()
            return jsonify(users=users), 200
        else:
            return jsonify(vf), 401
    else:
        return jsonify({"error": True, "message": "You need to send the token"}), 401



@user.route('/find_one/<id_number>', methods=['GET'])
def find_one(id_number):
    #Getting the token
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = Utils.Token.verify_token(token)
    #Verifying the token
    if vf["error"] == False:
        #Getting a specific user
        users = Services.Users.get_by_id_number(id_number)
        if users == None:
            return jsonify({"error": True, "message": "User does not exist"}), 400
        else:
            return jsonify(users=users), 200
    else:
        return jsonify(vf), 401

@user.route('/update', methods=['PUT'])
def update():
    #Getting the token
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = Utils.Token.verify_token(token)
    #Verifying the token
    if vf["error"] == False:
        data = request.get_json()
        id_number = data["id_number"]
        name = data['name']
        password = data['password']
        role = data['role']
        #Updating the user
        users = Services.Users.update(id_number, name, password, role)
        if users == None:
            return jsonify({"error": True, "message": "User does not exist"}), 400
        else:
            return jsonify(users=users), 200
    else:
        return jsonify(vf), 401