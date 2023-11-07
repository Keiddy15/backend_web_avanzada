
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from Config.db import db
import Services.index as Services
import Utils.index as Utils

worker = Blueprint("worker", __name__)


@worker.route('/add_job', methods=['POST'])
def add_job():
    try:
        # Getting the token
        token = request.headers['Authorization']
        token = token.replace("Bearer", "")
        token = token.replace(" ", "")
        vf = Utils.Token.verify_token(token)
        # Verifying the token
        if vf["error"] == False:
            data = request.get_json()
            user_id_number = data['user_id_number']
            product_name = data['product_name']
            # Getting the user data
            user = Services.Users.get_by_id_number(user_id_number)

            # Getting the product data
            product = Services.Product.get_by_name(product_name)
            product_id = product["id"]

            # Find out if a user has an active package
            last_user_package = Services.Package.get_last_user_package(
                user["id"])
            if last_user_package:
                id_package = last_user_package["id"]
                # Adding the product to the package
                add_product_to_package = Services.Package.add_package_detail(
                    id_package, product_id)
                # Updating the product quantity and the state
                product_quantity = int(
                    last_user_package["product_quantity"]) + 1
                state = "Completed" if product_quantity == 12 else "Pending"
                cumulative_total = int(
                    last_user_package["cumulative_total"]) + int(product["price"])
                updated_package = Services.Package.update(
                    id_package, product_quantity, state, cumulative_total)
                return jsonify(updated_package), 200
            else:
                # Create a new package
                package = Services.Package.create(
                    user["id"], 1, product["price"])
                # Add package detail

                detail_package = Services.Package.add_package_detail(
                    package["id"], product_id)
                return jsonify(package), 200
        else:
            return jsonify({'message': 'Incorrect credentials'}), 401

    except Exception as e:
        print("An error occurred while adding the job", e)
        return jsonify({"error": True, "message": "Unable to add the product"}), 500
