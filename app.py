from dynaconf import FlaskDynaconf
from flask import Flask, abort, render_template
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_bootstrap import Bootstrap
from flask_simplelogin import SimpleLogin, login_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
FlaskDynaconf(app)
Bootstrap(app)
db = SQLAlchemy(app)


def verify_login(user):
    return user.get("username") == "admin" and user.get("password") == "1234"


SimpleLogin(app, login_checker=verify_login)

# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin(app, name=app.config.TITLE, template_mode="bootstrap3")


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)


admin.add_view(sqla.ModelView(Products, db.session))


@app.cli.command()
def createdb():
    """Creates sqlite database"""
    db.create_all()


@app.route("/")
def index():
    products = Products.query.all()
    return render_template("index.html", products=products)


@app.route("/product/<product_id>")
def product(product_id):
    product = Products.query.filter_by(id=product_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("product.html", product=product)
