from flask_wtf.form import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,DecimalField,DateField
from wtforms.validators import DataRequired, Email, length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Ingresar')

class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), length(max=64)])
    lastname = StringField('Apellido', validators=[DataRequired(), length(max=64)])
    address = StringField('Direccion')
    gender = SelectField('Sexo', choices=['M','F'])
    employee_id = StringField('Numero de Identificacion')
    branch = SelectField('Dependencia')
    job_title = SelectField('Cargo')
    contract = StringField('Num. de Contrato')
    salary = DecimalField('Salario')
    contract_start = DateField('Fecha Inicio Contrato')
    contract_end = DateField('Fecha Inicio Contrato')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password confirmation', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')