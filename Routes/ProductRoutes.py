
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from Config.db import db
import Services.index as Services
import Utils.index as Utils

product = Blueprint("product", __name__)

@product.route('/create', methods=['POST'])
def create_product():
    #Getting the token
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = Utils.Token.verify_token(token)
    #Verifying the token  
    if vf["error"] == False:
        data = request.get_json()
        name = data['name']
        price = data['price']

        #validate if product exist
        product = Services.Product.get_by_name(name)
        if product == None:
            #Creating a product
            new_product = Services.Product.create(name, price)
            return jsonify(new_product=new_product), 200
        else:
            return jsonify({"error": True, "message": "Product exist"}), 400
    else:
        return jsonify(vf), 401
    
@product.route('/find_all', methods=['GET'])
def find_all():
    #Getting the token
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = Utils.Token.verify_token(token)
    #Verifying the token  
    if vf["error"] == False:
        products = Services.Product.get_all()
        return jsonify(products=products), 200
    else:
        return jsonify({'message': 'Incorrect credentials'}), 401
@product.route('/delete', methods=['DELETE'])
def delete_product():
    #Getting the token
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = Utils.Token.verify_token(token)
    #Verifying the token  
    if vf["error"] == False:
        data = request.get_json()
        name = data['name']

        #Deleting product
        product = Services.Product.delete(name)
        if product == None:
            return jsonify({"error": True, "message": "Product does not exist"}), 400
        else:
            return jsonify(product=product), 200
    else:
        return jsonify(vf), 401