from web_app import app
from flask_sqlalchemy import sqlalchemy

app.config['SQLALCHEMY_DATABASE_URI'] = '' 
db = sqlalchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)