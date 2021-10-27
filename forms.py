import datetime
from flask import flash
from flask_wtf.form import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,DateField,IntegerField, widgets
from wtforms.fields.core import DecimalField
from wtforms.validators import EqualTo, Length, Email, DataRequired
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets
from wtforms.widgets.core import TextArea

class LoginForm(FlaskForm):
    email = StringField('Usuario', validators=[DataRequired('El campo usuario no puede estar vacio')])
    password = PasswordField('Password', validators=[DataRequired('El campo de contraeña no puede estar vacio')])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Ingresar')
class UpdatePassForm(FlaskForm):
    password = PasswordField('Clave actual', validators=[DataRequired()])
    password1 = PasswordField('Nueva clave', validators=[DataRequired(),EqualTo("password2",message="La contraseña no coincide")])
    password2 = PasswordField('Confirmar clave', validators=[DataRequired()])
    submit = SubmitField()

class SignupForm(FlaskForm):
    name = StringField(label='Nombre',validators=[DataRequired('El campo de nombre no puede estar vacio'), Length(min=2)])
    lastname = StringField(label='Apellido',validators=[DataRequired('El campo de apellido no puede estar vacio'), Length(min=2)])
    email_address = StringField(label='Correo Electronico', validators=[Email('El valor ingresado en el campo de email no corresponde con una direccion de correo'), DataRequired('El campo de email no puede estar vacio')])
    employee_id = StringField(label='Numero de Identificacion', validators=[Length(min=6,message='La Longitud del texto ingresado no corresponde con un numero de identificacion'), DataRequired('El campo de identificacion es requerido')])
    address = StringField(label='Direccion de residencia', validators=[DataRequired('El campo de direccion no puede estar vacio'), Length(min=6)])
    gender = SelectField(label="Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')], validate_choice=True, validators=[DataRequired()])
    branch = SelectField(label="Dependencia",choices=['1','2'],validate_choice=True, validators=[DataRequired()])
    job_title = SelectField(label="Cargo",choices=['mesero'],validate_choice=True, validators=[DataRequired()])
    contract = StringField(label='Num. de Contrato', validators=[DataRequired(), Length(min=6, message='El Valor ingresado no corresponde a un numero de contrato valido')])
    
    salary = DecimalField(validators=[DataRequired()])
    contract_start = DateField('Fecha inicial',validators=[DataRequired()],    format='%Y-%m-%d', default=datetime.date.today) 
    contract_end = DateField('Fecha final',validators=[DataRequired()],    format='%Y-%m-%d', default=datetime.date.today) 
    
    password1 = PasswordField('password1',validators=[DataRequired(),EqualTo('password2',message="La contraseña de verificación no coincide")])  
    password2 = PasswordField('password2',validators=[DataRequired()])  
    submit = SubmitField('Crear usuario' )

class DeleteForm(FlaskForm):
    email = StringField()
    submit2 = SubmitField('OK' )

class PerformanceForm(FlaskForm):
    email = StringField(label='Correo Electronico', validators=[Email('El valor ingresado en el campo de email no corresponde con una direccion de correo'), DataRequired('El campo de email no puede estar vacio')])
    score = h5fields.IntegerField( "Number2", widget=h5widgets.NumberInput(min=0, max=100, step=5),validators=[DataRequired()])
    comment = StringField('Feedback',widget=TextArea())   
    date = DateField('Fecha',format='%Y-%m-%d' , default=datetime.date.today)
    submit3 = SubmitField('Enviar')


def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')


# def validate_contract_end(self, filed):
#         if filed.data <= self.contract_start.data:
#             raise ValidationError('Finish date must more or equal start date.')