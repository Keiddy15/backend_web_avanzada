from Models.PaymentRecordDetails import PaymentRecordDetails
from Models.PaymentRecords import PaymentRecords
from Config.db import db
import Utils.index as Utils


# Function to create pay

def create(id_user, total_amount):
    try:
        new_pay = PaymentRecords(
            id_user=id_user, total_amount=total_amount, pay_date=Utils.Common.DateNow())
        db.session.add(new_pay)
        db.session.commit()
        payment_data = {
            "id": new_pay.id,
            "id_user": new_pay.id_user,
            "pay_date": new_pay.pay_date,
            "total_amount": new_pay.total_amount
        }
        return payment_data
    except Exception as e:
        print("An error occurred while creating a new pay", e)
        db.session.rollback()
        return None

# Function to get all pay


def get_all():
    try:
        pays = PaymentRecords.query.all()
        payment_data = []
        for pay in pays:
            pay_data = {
                "id": pay.id,
                "id_user": pay.id_user,
                "pay_date": pay.pay_date,
                "total_amount": pay.total_amount
            }
            payment_data.append(pay_data)
        return payment_data
    except Exception as e:
        print("An error occurred while getting all pays", e)
        return None


# Function to get pay by user


def get_by_user(id_user):
    try:
        pays = PaymentRecords.query.filter_by(id_user=id_user).all()
        payment_data = []
        for pay in pays:
            pays = {
                "id": pay.id,
                "id_user": pay.id_user,
                "pay_date": pay.pay_date,
                "total_amount": pay.total_amount
            }
            payment_data.append(pays)
        return payment_data

    except Exception as e:
        print("An error occurred while getting the pay by user", e)
        return None


def add_payment_detail(id_payment_record, id_package):
    try:
        new_payment_detail = PaymentRecordDetails(
            id_payment_record=id_payment_record, id_package=id_package)
        db.session.add(new_payment_detail)
        db.session.commit()
        payment_data = {
            "id_package": new_payment_detail.id_package,
            "id_payment_record": new_payment_detail.id_payment_record,
        }
        return payment_data
    except Exception as e:
        print("An error occurred while adding a new payment detail", e)
        db.session.rollback()
        return None
