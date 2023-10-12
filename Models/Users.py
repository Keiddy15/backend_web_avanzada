from Config.db import ma, db, app


class Users(db.Model):
    __tablename__ = 'tblusers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250))
    password = db.Column(db.String(250))
    role = db.Column(db.String(250))
    id_number = db.Column(db.String(250), unique=True)

    def __init__(self, name, email, password, role, id_number):
        self.name = name
        self.email = email
        self.password = password
        self.role = role,
        self.id_number = id_number


with app.app_context():
    db.create_all()


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'role', 'id_number')
