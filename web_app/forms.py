from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Give a username')
    email_address = StringField(label='E-Mail Address')
    password1 = PasswordField(label='Set a Password')
    password2 = PasswordField(label='Confirm your password')
    submit = SubmitField(label='Create new user')