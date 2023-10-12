from Config.db import ma, db, app


class PackageDetails(db.Model):
    __tablename__ = 'tblpackagedetails'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_package = db.Column(db.Integer, db.ForeignKey('tblpackages.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('tblproducts.id'))
    date_time = db.Column(db.DateTime)

    def __init__(self, id_package, id_product, date_time):
        self.id_package = id_package
        self.id_product = id_product
        self.date_time = date_time


with app.app_context():
    db.create_all()


class PackageDetailsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_package', 'id_product', 'date_time')
