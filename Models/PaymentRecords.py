from Config.db import ma, db, app


class PaymentRecords(db.Model):
    __tablename__ = 'tblpaymentrecords'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('tblusers.id'))
    pay_date = db.Column(db.DateTime)
    total_amount = db.Column(db.String(250))

    def __init__(self, id_user, total_amount, pay_date):
        self.id_user = id_user
        self.total_amount = total_amount
        self.pay_date = pay_date


with app.app_context():
    db.create_all()


class PaymentRecordsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_user', 'pay_date', 'total_amount')
