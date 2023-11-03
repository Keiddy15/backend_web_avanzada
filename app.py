from flask import Flask, request, jsonify, redirect, render_template
from Config.db import app
import api.index
import Routes.index as Routes
from flask_cors import CORS

CORS(app)

app.register_blueprint(Routes.Auth.auth, url_prefix="/auth")
app.register_blueprint(Routes.User.user, url_prefix="/user")
app.register_blueprint(Routes.Product.product, url_prefix="/product")
app.register_blueprint(Routes.Worker.worker, url_prefix="/worker")
app.register_blueprint(Routes.Package.package, url_prefix="/package")
app.register_blueprint(Routes.Payment.payment, url_prefix="/payment")


@app.route("/")
def index():
    return "KOPAY Version 1.0.0"


if __name__ == "__main__":
    app.run(debug=True, port=4000, host='0.0.0.0')
