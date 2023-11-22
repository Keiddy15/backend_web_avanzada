from Models.Users import Users
from Config.db import db

# Function to create a new user
def create(name, email, role, id_number):
    try:
        new_user = Users(name=name, email=email, password=None, role=role, id_number=id_number)
        db.session.add(new_user)
        db.session.commit()
        user_data = {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "role": new_user.role,
            "id_number": new_user.id_number,
        }
        return user_data
    except Exception as e:
        print("An error occurred while creating a new user", e)
        db.session.rollback()
        return None

# Function to get all users
def get_all():
    try:
        users = Users.query.all()
        users_data = []
        for user in users:
            user_data = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "id_number": user.id_number,
            }
            users_data.append(user_data)
        return users_data
    except Exception as e:
        print("An error occurred while getting all users", e)
        return None

# Function to get a user by their ID
def get_by_id_number(id_number):
    try:
        user = Users.query.filter_by(id_number=id_number).first()
        if(user):
            user_data = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "id_number": user.id_number,
            }
            return user_data
        else:
            return None
    except Exception as e:
        print("An error occurred while getting the user by id", e)
        return None

# Function to get a user by their ID
def get_user_by_email_and_password(email, password):
    try:
        user = Users.query.filter_by(email=email, password=password).first()
        return user
    except Exception as e:
        print("An error occurred while getting the admin", e)
        return None

# Function to update a user by their ID
def update(id_number, name, email, password, role):
    try:
        user = Users.query.filter_by(id_number=id_number).first()
        if user:
            user.name = name
            user.email = email
            user.password = password
            user.role = role
            db.session.commit()
            user_data = {
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "id_number": user.id_number,
            }
            return user_data
    except Exception as e:
        print("An error occurred while updating the user", e)
        db.session.rollback()
        return None

# Function to delete a user by their ID
def delete(id):
    try:
        user = Users.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
    except Exception as e:
        print("An error occurred while deleting the user", e)
        db.session.rollback()
        return None

# Function to get a user by their email
def get_user(email):
    try:
        user = Users.query.filter_by(email=email).first()
        if user: 
            user_data = {
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "id_number": user.id_number,
            }
            return user_data
        else: 
            return None
    except Exception as e:
        print("An error occurred while getting the user by email", e)
        return None