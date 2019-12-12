from flask import render_template, abort
from pydaria.ext.database import Products


def index():
    products = Products.query.all()
    return render_template("index.html", products=products)


def product(product_id):
    product = Products.query.filter_by(id=product_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("product.html", product=product)

