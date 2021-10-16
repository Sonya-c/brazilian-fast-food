import datetime

from flask_wtf.form import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,DateField,IntegerField, widgets
from wtforms import validators
from wtforms.fields.core import DecimalField
from wtforms.validators import EqualTo, Length, Email, DataRequired, NumberRange, ValidationError

class LoginForm(FlaskForm):
    email = StringField('Usuario', validators=[DataRequired('El campo usuario no puede estar vacio')])
    password = PasswordField('Password', validators=[DataRequired('El campo de contraeña no puede estar vacio')])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Ingresar')

class SignupForm(FlaskForm):
    name = StringField(label='Nombre',validators=[DataRequired('El campo de nombre no puede estar vacio'), Length(min=2)])
    lastname = StringField(label='Apellido',validators=[DataRequired('El campo de apellido no puede estar vacio'), Length(min=2)])
    email_address = StringField(label='Correo Electronico', validators=[Email('El valor ingresado en el campo de email no corresponde con una direccion de correo'), DataRequired('El campo de email no puede estar vacio')])
    employee_id = StringField(label='Numero de Identificacion', validators=[Length(min=6,message='La Longitud del texto ingresado no corresponde con un numero de identificacion'), DataRequired('El campo de identificacion es requerido')])
    address = StringField(label='Direccion de residencia', validators=[DataRequired('El campo de direccion no puede estar vacio'), Length(min=6)])
    gender = SelectField(label="Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')], validate_choice=True, validators=[DataRequired()])
    branch = SelectField(label="Dependencia",choices=['1'],validate_choice=True, validators=[DataRequired()])
    job_title = SelectField(label="Cargo",choices=['mesero'],validate_choice=True, validators=[DataRequired()])
    contract = StringField(label='Num. de Contrato', validators=[DataRequired(), Length(min=6, message='El Valor ingresado no corresponde a un numero de contrato valido')])
    
    salary = DecimalField(validators=[DataRequired()])
    contract_start = DateField('Fecha inicial',validators=[DataRequired()],    format='%Y-%m-%d', default=datetime.date.today) 
    contract_end = DateField('Fecha final',validators=[DataRequired()],    format='%Y-%m-%d', default=datetime.date.today) 
    
    password1 = PasswordField('password1',validators=[DataRequired()])  
    password2 = PasswordField('password2',validators=[DataRequired()])  
    submit = SubmitField('Crear usuario' )

def validate_contract_end(self, filed):
        if filed.data <= self.contract_start.data:
            raise ValidationError('Finish date must more or equal start date.')