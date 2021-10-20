from enum import unique
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model,UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self):
        if not self.id:
            db.session.add(self)

        db.session.commit()

    def delete(self):
        db.session.delete(self)

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def delete_user(email):
        User.query.filter_by(email=email).delete()
        db.session.commit()

class Employee(db.Model):
    _tablename_ = 'employess'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True,nullable=False)
    employee_id= db.Column(db.String(80), unique=True,nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    job = db.Column(db.String(100), nullable=False)
    contract = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Numeric(65,2),nullable=False)
    start = db.Column(db.Date(), nullable=False)
    end = db.Column(db.Date(), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return '<Employee {}>'.format(self.email)

    @staticmethod
    def delete_employee(email):
        db.session.delete(Employee.query.filter_by(email=email).first())
        db.session.commit()
        

    @staticmethod
    def getAll():
        return Employee.query.all()


""" class Employee(UserMixin):
    def __init__(self, id, name, email, password, address,branch,job,contract,salary,contract_start
    , contract_end,is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.address = address
        self.branch = branch
        self.job = job
        self.contract = contract
        self.salary = salary
        self.start = contract_start
        self.end = contract_end
        self.is_admin = is_admin
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<Employee {}>'.format(self.email) """


