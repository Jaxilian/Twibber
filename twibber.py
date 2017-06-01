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
@login_required
def index():
	session["Logged_In"] = 1 
	return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	else:
		register_form = RegisterUser()
		if register_form.validate_on_submit():
			user_datastore.create_user(
				email=register_form.email.data,
				username = register_form.username.data,
				password = register_form.password.data,
				first_name = register_form.first_name.data,
				last_name = register_form.last_name.data
				)
			return redirect(url_for('success'))
		print(register_form.errors)
		return render_template("register.html", register_form = register_form)

@app.route("/user/<username>", methods=["GET", "POST"])
def user_profile(username):
	user = User.select().where(User.username==username)[0]
	tweebs = Tweeb.select().order_by(-Tweeb.id)
	try:
		if current_user == user:
			tweeb_form = PostTweeb()
			if tweeb_form.validate_on_submit():
				Tweeb.create(
					author=current_user.id,
					content=tweeb_form.content.data
					)
			return render_template("user_template.html",tweeb_form=tweeb_form,tweebs=tweebs, user=user, editor=True)
		else:
			return render_template("user_template.html",tweebs=tweebs, user=user)
	except IndexError:
		return render_template("user_not_found.html")




if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)