from API import app
from flask import request

from Database import db
from Model.Product import Product
from Model.Product import products_schema, product_schema


@app.route('/products', methods=["POST"])
def create_product():
    name = request.json['name']
    description = request.json['description']
    price = float(request.json['price'])
    barcode = request.json['barcode']

    new_product = Product(name, description, price, barcode)
    db.session.add(new_product)
    db.session.commit()

    return  product_schema.jsonify(new_product)

@app.route('/products', methods=["GET"])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return products_schema.jsonify(result)

@app.route('/products/<id>', methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

@app.route('/products/<id>', methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = float(request.json['price'])
    barcode = request.json['barcode']

    product.name = name
    product.description = description
    product.price = price
    product.barcode = barcode

    db.session.commit()
    return product_schema.jsonify(product)

@app.route('/products/<id>', methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)
