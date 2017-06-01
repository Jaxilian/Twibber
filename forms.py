from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import Form, StringField, validators, PasswordField, TextField, TextAreaField
from wtforms.fields.html5 import EmailField

class RegisterUser(FlaskForm):
	username = StringField('Username', [validators.InputRequired(), validators.Length(min=2, max=15)])
	first_name = StringField('First Name', [validators.InputRequired(), validators.Length(min=2, max=20)])
	last_name = StringField('Last Name', [validators.InputRequired(), validators.Length(min=2, max=20)])
	email = EmailField('Email address', [validators.InputRequired(), validators.Email()])
	password = PasswordField('Password',[
		validators.InputRequired(),
		validators.Length(min=2, max=800),
		validators.EqualTo('confirm', message = 'Password must match')
		])
	confirm = PasswordField('Repeat Password')

class ContactForm(FlaskForm):
	first_name = StringField('First Name', [validators.InputRequired(), validators.Length(min=2, max=20)])
	last_name = StringField('Last Name', [validators.InputRequired(), validators.Length(min=2, max=20)])
	email = EmailField('Email address', [validators.InputRequired(), validators.Email()])
	message = TextAreaField('Message', [validators.InputRequired(), validators.Length(min=2, max=800)])

class PostTweeb(FlaskForm):
	content = TextAreaField('Content', [validators.InputRequired(), validators.Length(min=3, max=400)])

