from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.fields.core import DecimalField, FloatField

class RegisterForm(FlaskForm):
    name = StringField(label='Nombre')
    lastname = StringField(label='Apellido')
    email_address = StringField(label='Correo Electronico')
    employee_id = StringField(label='Numero de Identificacion')
    address = StringField(label='Direccion de residencia')
    gender = SelectField(label="Sexo")
    branch = SelectField(label="Dependencia")
    job_title = SelectField(label="Cargo")
    contract = StringField(label='Num. de Contrato')
    salary = DecimalField(label='Salario', places=2, rounding=None, use_locale=False)
    contract_start = DateField(label='Fecha Inicio Contrato')
    contract_end = DateField(label='Fecha Finalizacion Contrato')
    password1 = PasswordField(label='Contrasena')
    password2 = PasswordField(label='Confirme la contrasena')
    
    submit = SubmitField(label='Crear usuario')

class EditForm(FlaskForm):
    email_address = StringField(label='Correo Electronico')
    address = StringField(label='Direccion de residencia')
    branch = SelectField(label="Dependencia")
    job_title = SelectField(label="Cargo")
    contract = StringField(label='Num. de Contrato')
    salary = DecimalField(label='Salario', places=2, rounding=None, use_locale=False)
    contract_start = DateField(label='Fecha Inicio Contrato')
    contract_end = DateField(label='Fecha Finalizacion Contrato')
    address = StringField(label='Direccion de residencia')
    
    submit = SubmitField(label='Crear usuario')


class LoginForm(FlaskForm):
    email_address = StringField(label='Correo Electronico')
    password = PasswordField(label='Contrasena')

    login = SubmitField(label='Crear usuario')