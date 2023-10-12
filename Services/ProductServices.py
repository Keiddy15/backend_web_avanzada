from Models.Products import Products
from Config.db import db

# Function to create a product


def create(name, price):
    try:
        new_product = Products(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()
        product_data = {
            "id": new_product.id,
            "name": new_product.name,
            "price": new_product.price
        }
        return product_data
    except Exception as e:
        print("An error occurred while creating a new product", e)
        db.session.rollback()
        return None

# Function to get all product


def get_all():
    try:
        products = Products.query.all()
        products_data = []
        for product in products:
            product_data = {
                "id": product.id,
                "name": product.name,
                "price": product.price
            }
            products_data.append(product_data)
        return products_data
    except Exception as e:
        print("An error occurred while getting all products", e)
        return None

# Function to delete a product by their name


def delete(name):
    try:
        product = Products.query.filter_by(name=name).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            product_data = {
                "id": product.id,
                "name": product.name,
                "price": product.price
            }
        return product_data
    except Exception as e:
        print("An error occurred while deleting the product", e)
        db.session.rollback()
        return None

# Function to get product by name


def get_by_name(name):
    try:
        product = Products.query.filter_by(name=name).first()
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price
        }
        return product_data
    except Exception as e:
        print("An error occurred while getting the product by name", e)
        return None


# Function to get product by id
def get_by_id(id):
    try:
        product = Products.query.filter_by(id=id).first()
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price
        }
        return product_data
    except Exception as e:
        print("An error occurred while getting the product by id", e)
        return None
