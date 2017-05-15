from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, TextField, TextAreaField
from wtforms.fields.html5 import EmailField

class RegisterUser(FlaskForm):
	username = StringField('Username', [validators.InputRequired(), validators.Length(min=2, max=15)])
	first_name = StringField('First Name', [validators.InputRequired(), validators.Length(min=2, max=20)])
	last_name = StringField('Last Name', [validators.InputRequired(), validators.Length(min=2, max=20)])
	email = EmailField('Email address', [validators.InputRequired(), validators.Email()])
	password = PasswordField('Password', [validators.InputRequired(), validators.Length(min=2, max=800)])
