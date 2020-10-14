from Database import db, ma


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    barcode = db.Column(db.String(100))

    def __init__(self, name, description, price, barcode):
        self.name = name
        self.description = description
        self.price = price
        self.barcode = barcode


db.create_all()


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'barcode')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
