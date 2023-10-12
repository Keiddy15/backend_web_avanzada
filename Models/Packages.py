from Config.db import ma, db, app


class Packages(db.Model):
    __tablename__ = 'tblpackages'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('tblusers.id'))
    date = db.Column(db.DateTime)
    product_quantity = db.Column(db.String(250))
    cumulative_total = db.Column(db.String(250))
    state = db.Column(db.String(250))

    def __init__(self, id_user, product_quantity, cumulative_total, state, date):
        self.id_user = id_user
        self.product_quantity = product_quantity
        self.cumulative_total = cumulative_total
        self.state = state
        self.date = date


with app.app_context():
    db.create_all()


class PackagesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_user', 'date', 'product_quantity',
                  'cumulative_total', 'state')
