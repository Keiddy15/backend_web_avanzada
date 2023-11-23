from Models.Packages import Packages
from Models.PackageDetails import PackageDetails
from Config.db import db
import Utils.index as Utils
import Services.ProductServices as Product
import Services.UserServices as User

# Function to create a package

def create(id_user, product_quantity, cumulative_total):
    try:
        new_package = Packages(
            id_user=id_user, product_quantity=product_quantity, cumulative_total=cumulative_total, state="Completed" if product_quantity == 12 else "Pending", date=Utils.Common.DateNow())
        db.session.add(new_package)
        db.session.commit()
        package_data = {
            "id": new_package.id,
            "id_user": new_package.id_user,
            "date": new_package.date,
            "product_quantity": new_package.product_quantity,
            "cumulative_total": new_package.cumulative_total,
            "state": new_package.state,
        }
        return package_data
    except Exception as e:
        print("An error occurred while creating a new package", e)
        db.session.rollback()
        return None

# Function to add the details of a package


def add_package_detail(id_package, id_product):
    try:
        new_package = PackageDetails(
            id_package=id_package, id_product=id_product, date_time=Utils.Common.DateNow())
        db.session.add(new_package)
        db.session.commit()
        package_data = {
            "id_package": new_package.id_package,
            "id_product": new_package.id_product,
            "date_time": new_package.date_time,
        }
        return package_data
    except Exception as e:
        print("An error occurred while creating a new package", e)
        db.session.rollback()
        return None


# Function to get the last user package

def get_last_user_package(id_user):
    try:
        package = Packages.query.filter_by(
            id_user=id_user, state="Pending").first()
        if package:
            package_data = {
                "id": package.id,
                "id_user": package.id_user,
                "date": package.date,
                "product_quantity": package.product_quantity,
                "cumulative_total": package.cumulative_total,
                "state": package.state
            }
            return package_data
        else:
            return None
    except Exception as e:
        print("An error occurred while getting the last user package", e)
        return None
    
# Function to get package by id

def get_by_id(id_pck):
    try:
        package = Packages.query.filter_by(id=id_pck).first()
        if package:
            package_data = {
                "id": package.id,
                "id_user": package.id_user,
                "date": package.date,
                "product_quantity": package.product_quantity,
                "cumulative_total": package.cumulative_total,
                "state": package.state
            }
            return package_data
        else:
            return None
    except Exception as e:
        print("An error occurred while getting the last user package", e)
        return None

# Function to get all packages


def get_all():
    try:
        packages = Packages.query.all()
        packages_data = []
        for package in packages:
            user = User.get_by_id(package.id_user)
            package = {
                "id_user": package.id_user,
                "date": package.date,
                "product_quantity": package.product_quantity,
                "cumulative_total": package.cumulative_total,
                "state": package.state,
                "id_number": user["id_number"],
                "id_pck": package.id,
            }
            packages_data.append(package)
        return packages_data
    except Exception as e:
        print("An error occurred while getting all packages", e)
        return None


# Function to get package by id user


def get_by_user(id_user):
    try:
        packages = Packages.query.filter_by(id_user=id_user).all()
        print(packages)
        packages_data = []
        for package in packages:
            print("hi")
            package_data = {
                "id_user": package.id_user,
                "date": package.date,
                "product_quantity": package.product_quantity,
                "cumulative_total": package.cumulative_total,
                "state": package.state,
                "id_package": package.id
            }
            packages_data.append(package_data)
        return packages_data
    except Exception as e:
        print("An error occurred while getting the package by user id", e)
        return None


# Function to get package details by id user


def get_detail(id_package):
    try:
        package = Packages.query.filter_by(id=id_package).first()
        package_data = {
            "date": package.date,
            "product_quantity": package.product_quantity,
            "cumulative_total": package.cumulative_total,
            "state": package.state,
            "id_package": id_package
        }
        if package:
            package_details = PackageDetails.query.filter_by(
                id_package=package.id).all()
            package_details_data = []
            for pckg in package_details:
                product = Product.get_by_id(pckg.id_product)
                package_details = {
                    "product_name": product["name"],
                    "product_id": product["id"],
                    "date_time": pckg.date_time
                }
                package_details_data.append(package_details)
            package_data['package_details_data'] = package_details_data

            return package_data
        else:
            return None
    except Exception as e:
        print("An error occurred while getting the package details by user id", e)
        return None

# Function to update a package


def update(id, product_quantity, state, cumulative_total):
    try:
        package = Packages.query.filter_by(id=id).first()
        package.product_quantity = product_quantity
        package.state = state
        package.cumulative_total = cumulative_total
        db.session.commit()
        package_data = {
            "id_user": package.id_user,
            "date": package.date,
            "product_quantity": package.product_quantity,
            "cumulative_total": package.cumulative_total,
            "state": package.state
        }
        return package_data
    except Exception as e:
        print("An error occurred while updating the package", e)
        return None

# Function to get all user completed packages


def get_all_user_completed_packages(id_user):
    try:
        packages = Packages.query.filter_by(
            id_user=id_user, state="Completed").all()
        package_data = []
        if packages:
            for package in packages:
                pckg_data = {
                    "cumulative_total": int(package.cumulative_total),
                    "id_package": package.id
                }
                package_data.append(pckg_data)
            return package_data
        else:
            return None
    except Exception as e:
        print("An error occurred while getting all user completed packages", e)
        return None
