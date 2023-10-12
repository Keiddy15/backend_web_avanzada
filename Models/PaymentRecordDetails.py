from Config.db import ma, db, app


class PaymentRecordDetails(db.Model):
    __tablename__ = 'tblpaymentrecorddetails'

    id = db.Column(db.Integer, primary_key=True)
    id_payment_record = db.Column(db.Integer, db.ForeignKey('tblpaymentrecords.id'))
    id_package = db.Column(db.Integer, db.ForeignKey('tblpackages.id'))

    def __init__(self, id_payment_record, id_package):
        self.id_payment_record = id_payment_record
        self.id_package = id_package


with app.app_context():
    db.create_all()


class PaymentRecordDetailsShema(ma.Schema):
    class Meta:
        fields = ('id', 'id_payment_record')
