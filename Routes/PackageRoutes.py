
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from Config.db import db
import Services.index as Services
import Utils.index as Utils

package = Blueprint("package", __name__)


@package.route('/find_all', methods=['GET'])
def find_all():
    try:
        # Getting the token
        token = request.headers['Authorization']
        token = token.replace("Bearer", "")
        token = token.replace(" ", "")
        vf = Utils.Token.verify_token(token)
        # Verifying the token
        if vf["error"] == False:
            # Getting all packages
            packages = Services.Package.get_all()
            return jsonify(packages=packages), 200
        else:
            return jsonify(vf), 401
    except Exception as e:
        print("An error occurred while getting the package", e)
        return jsonify({"error": True, "message": "Unable to get all the packages"}), 500


@package.route('/find_one/<id_number>', methods=['GET'])
def find_by_user(id_number):
    try:
        # Getting the token
        token = request.headers['Authorization']
        token = token.replace("Bearer", "")
        token = token.replace(" ", "")
        vf = Utils.Token.verify_token(token)
        # Verifying the token
        if vf["error"] == False:
            # Getting package by user
            user = Services.Users.get_by_id_number(id_number)
            print(user)
            if user == None:
                return jsonify({"error": True, "message": "User does not exist"}), 400
            else:
                package = Services.Package.get_by_user(user["id"])
                if package:
                    return jsonify(package=package), 200
                else:
                    return jsonify({"error": True, "message": "No package found"}), 404
        else:
            return jsonify(vf), 401
    except Exception as e:
        print("An error occurred while getting the package", e)
        return jsonify({"error": True, "message": "Unable to get the package"}), 500


@package.route('/find_detail_one/<id_number>', methods=['GET'])
def find_details_by_user(id_number):
    try:
        # Getting the token
        token = request.headers['Authorization']
        token = token.replace("Bearer", "")
        token = token.replace(" ", "")
        vf = Utils.Token.verify_token(token)
        # Verifying the token
        if vf["error"] == False:
            # Getting package by user
            user = Services.Users.get_by_id_number(id_number)
            if user == None:
                return jsonify({"error": True, "message": "User does not exist"}), 400
            else:
                package = Services.Package.get_details_by_user(user["id"])
                if package:
                    return jsonify(package=package), 200
                else:
                    return jsonify({"error": True, "message": "No package found"}), 404
        else:
            return jsonify(vf), 401
    except Exception as e:
        print("An error occurred while getting the package", e)
        return jsonify({"error": True, "message": "Unable to get the package"}), 500
