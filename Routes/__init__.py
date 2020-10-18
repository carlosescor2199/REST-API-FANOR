from API import app
from flask import request

from Database import db
from Model.Product import Product, products_schema, product_schema


@app.route('/products', methods=["POST"])
def create_product():
    name = request.json['name']
    description = request.json['description']
    price = float(request.json['price'])
    barcode = request.json['barcode']
    promotion = request.json['promotion']

    new_product = Product(name, description, price, barcode, promotion)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


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
    promotion = request.json['promotion']

    product.name = name
    product.description = description
    product.price = price
    product.barcode = barcode
    product.promotion = promotion

    db.session.commit()
    return product_schema.jsonify(product)


@app.route('/products/<id>', methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)


@app.route('/products/promotions', methods=["GET"])
def products_promotions():
    all_products = Product.query.all()

    result = products_schema.dump(all_products)
    print(result)
    res = []
    for product in result:
        if product['promotion'] == True:
            res.append(product)

    return products_schema.jsonify(res)


@app.route('/products/barcode/<barcode>', methods=["GET"])
def products_barcode(barcode):
    res = Product.query.filter_by(barcode=barcode).all()
    product = products_schema.dump(res)

    return products_schema.jsonify(product)
