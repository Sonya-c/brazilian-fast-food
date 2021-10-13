from datetime import date, datetime
from web_app import app
#from flask_sqlalchemy import sqlalchemy

#app.config['SQLALCHEMY_DATABASE_URI'] = '' 
#db = sqlalchemy(app)

def get_available_jobs():
    return [('co', 'Courier'), ('cj', 'Chef Jefe'), ('ch', 'Chef'), ('ms','Mesero'), ('ad', 'Administrador')]

def get_available_branches():
    return [('baq', 'Barranquilla'), ('bog', 'Bogota'), ('cal', 'Cali'), ('mtr','Monteria'), ('ctg', 'Cartagena'), ('mde', 'Medellin')]

def populate_genders():
    return [('M', 'Masculino'), ('F', 'Femenino')]

item_Collection = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]

dummy_Employee = {
    'employee_id': '1129498258', 
    'name' : 'Tony',
    'lastname' : 'Stark',
    'email_address' : 'dummy_add@domain.com',
    'address' : '92560 Malibu Street, CA',
    'gender' : 'M',
    'branch' : 'Barranquilla',
    'job_title' : 'cj',
    'contract' : '246323AR12F',
    'salary' : 6500000,
    'contract_start' : date.fromisoformat('2021-01-01'),
    'contract_end' : date.fromisoformat('2021-12-31')
}

'''
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=200), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
'''