from flask import Flask, render_template, make_response, request, session, redirect, url_for
from forms import *
from database import *
from flask_security import Security, PeeweeUserDatastore, login_required
import psycopg2
import os

app = Flask("Twibber")


@app.route("/")
def index():

	return render_template("index.html")

