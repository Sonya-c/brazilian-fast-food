from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, DecimalField
from wtforms.fields.core import IntegerField

class RegisterForm(FlaskForm):
    name = StringField(label='Nombre')
    lastname = StringField(label='Apellido')
    email_address = StringField(label='Correo Electronico')
    employee_id = StringField(label='Numero de Identificacion')
    address = StringField(label='Direccion de residencia')
    gender = SelectField(label="Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')], validate_choice=True)
    branch = SelectField(label="Dependencia",validate_choice=True)
    job_title = SelectField(label="Cargo",validate_choice=True)
    contract = StringField(label='Num. de Contrato')
    salary = IntegerField(label='Salario')
    contract_start = DateField(label='Fecha Inicio Contrato')
    contract_end = DateField(label='Fecha Finalizacion Contrato')
    password1 = PasswordField(label='Contrasena')
    password2 = PasswordField(label='Confirme la contrasena')
    
    submit = SubmitField(label='Crear usuario')

class EditForm(FlaskForm):
    email_address = StringField(label='Correo Electronico')
    address = StringField(label='Direccion de residencia')
    branch = SelectField(label="Dependencia",validate_choice=True)
    job_title = SelectField(label="Cargo",validate_choice=True)
    contract = StringField(label='Num. de Contrato')
    salary = IntegerField(label='Salario')
    contract_start = DateField(label='Fecha Inicio Contrato')
    contract_end = DateField(label='Fecha Finalizacion Contrato')
    address = StringField(label='Direccion de residencia')
    
    submit = SubmitField(label='Guardar Cambios')


class LoginForm(FlaskForm):
    email_address = StringField(label='Correo Electronico')
    password = PasswordField(label='Contrasena')

    login = SubmitField(label='Crear usuario')