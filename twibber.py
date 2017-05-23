from flask import Flask, render_template, make_response, request, session, redirect, url_for
from flask_security import Security, PeeweeUserDatastore, login_required, current_user
from forms import *
from database import *
import psycopg2
import os

app = Flask("Twibber")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "insecure dev key")
app.config["WTF_CSRF_ENABLED"] = True
app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = "email"
app.config["SECURITY_PASSWORD_HASH"] = "pbkdf2_sha512"
app.config["SECURITY_PASSWORD_SALT"] = app.config["SECRET_KEY"]

user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
	register_form = RegisterUser()
	if register_form.validate_on_submit():
		user_datastore.create_user(email=register_form.email.data,username = register_form.username.data, password=register_form.password.data, first_name = register_form.first_name.data, last_name = register_form.last_name.data)
		return redirect(url_for('success'))
	return render_template("register.html", register_form = register_form)

@app.route("/login")
def login():
	session["Logged_In"] = 1 
	return render_template("/security/login_user.html")

@app.route("/success")
def success():
	return render_template("success.html")

@app.route("/home")
@login_required
def home():
	user = current_user()
	return render_template("home.html", user=user)






if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)