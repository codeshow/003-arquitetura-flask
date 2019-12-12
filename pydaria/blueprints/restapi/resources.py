from flask import jsonify, abort
from flask_restful import Resource
from pydaria.ext.database import Products


class ProductResource(Resource):
    def get(self):
        products = Products.query.all() or abort(204)
        return jsonify(
            {'products': [
                product.to_dict()
                for product in products
            ]}
        )


class ProductItemResource(Resource):
    def get(self, product_id):
        product = Products.query.filter_by(id=product_id).first() or abort(
            404
        )
        return jsonify(product.to_dict())
