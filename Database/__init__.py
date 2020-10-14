from API import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://uzgcyzzpwgcvfj45:M1Tb99Y5nBPQoIH9v2Is@bw5ji4lcz43jpz48znwf-mysql.services.clever-cloud.com/bw5ji4lcz43jpz48znwf"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)