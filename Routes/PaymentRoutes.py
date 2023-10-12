
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from Config.db import db
import Services.index as Services
import Utils.index as Utils

payment = Blueprint("payment", __name__)


@payment.route('/create', methods=['POST'])
def create_pay():
    # Getting the token
    token = request.headers['Authorization']
    token = token.replace("Bearer", "")
    token = token.replace(" ", "")
    vf = Utils.Token.verify_token(token)
    # Verifying the token
    if vf["error"] == False:
        data = request.get_json()
        user_id_number = data['user_id_number']

        # Get user
        user = Services.Users.get_by_id_number(user_id_number)
        user_id = user["id"]
        if user == None:
            return jsonify({"error": True, "message": "User does not exist"}), 400
        else:
            # Getting all users completed packages
            package_data = Services.Package.get_all_user_completed_packages(
                user_id)
            if package_data == None:
                return jsonify({"error": True, "message": "Unable to create payment due to no package outstanding"}), 400
            else:
                # Getting the amount
                amount = 0
                for pckg in package_data:
                    amount = amount + pckg["cumulative_total"]

                # Create payment
                new_pay = Services.Payment.create(user_id, amount)
                
                for pckg in package_data:
                    # Updaye package status
                    Services.Package.update(
                        pckg["id_package"], 12, "Closed", pckg["cumulative_total"])
                    # Create payment record_detail
                    Services.Payment.add_payment_detail(new_pay["id"], pckg["id_package"])
                return jsonify(new_pay=new_pay), 200
    else:
        return jsonify(vf), 401

@payment.route('/find_all', methods=['GET'])
def find_all():
    try:
        # Getting the token
        token = request.headers['Authorization']
        token = token.replace("Bearer", "")
        token = token.replace(" ", "")
        vf = Utils.Token.verify_token(token)
        # Verifying the token
        if vf["error"] == False:
            # Getting all payments
            payments = Services.Payment.get_all()
            return jsonify(payments=payments), 200
        else:
            return jsonify(vf), 401
    except Exception as e:
        print("An error occurred while getting the package", e)
        return jsonify({"error": True, "message": "Unable to get all the packages"}), 500
    

@payment.route('/find_one/<id_number>', methods=['GET'])
def find_by_user(id_number):
    try:
        # Getting the token
        token = request.headers['Authorization']
        token = token.replace("Bearer", "")
        token = token.replace(" ", "")
        vf = Utils.Token.verify_token(token)
        # Verifying the token
        if vf["error"] == False:
            # Getting payment by user
            user = Services.Users.get_by_id_number(id_number)
            if user == None:
                return jsonify({"error": True, "message": "User does not exist"}), 400
            else:
                package = Services.Payment.get_by_user(user["id"])
                if package:
                    return jsonify(package=package), 200
                else:
                    return jsonify({"error": True, "message": "No package found"}), 404
        else:
            return jsonify(vf), 401
    except Exception as e:
        print("An error occurred while getting the package", e)
        return jsonify({"error": True, "message": "Unable to get the package"}), 500
