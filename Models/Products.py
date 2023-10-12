from Config.db import ma, db, app


class Products(db.Model):
    __tablename__ = 'tblproducts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=True)
    price = db.Column(db.String(250))

    def __init__(self, name, price):
        self.name = name
        self.price = price


with app.app_context():
    db.create_all()


class ProductsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price')
