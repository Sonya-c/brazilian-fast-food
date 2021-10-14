from flask_wtf.form import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,DateField,IntegerField
from wtforms.validators import EqualTo, Length, Email, DataRequired, NumberRange


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
    salary = IntegerField(label='Salario', validators=[DataRequired('El campo de salario no puede estar vacio'), NumberRange(min=1,message='El salario especificado debe ser superior a $1')])
    contract_start = DateField(label='Fecha Inicio Contrato', validators=[DataRequired('Debe especificar una fecha de inicio de contrato')])
    contract_end = DateField(label='Fecha Finalizacion Contrato', validators=[DataRequired('Debe especificar una fecha de inicio de contrato'), NumberRange(min=contract_start,message='La fecha de inicio de contrato no puede ser posterior a la fecha final')])
    password1 = PasswordField(label='Contrasena', validators=[DataRequired('La contrasena no puede ser vacia')])
    password2 = PasswordField(label='Confirme la contrasena', validators=[DataRequired('La confirmacion de contrasena no puede ser vacia'), EqualTo(fieldname='password1',message='Las contrasenas provistas no coinciden')])
    
    submit = SubmitField(label='Crear usuario')