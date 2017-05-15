import os
from peewee import *
from playhouse.db_url import connect
from flask_security import UserMixin, RoleMixin

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
	db = connect(DATABASE_URL)
else:
	DATABASE = 'Twibber'
	db = PostgresqlDatabase(DATABASE)

class User(Model, UserMixin):
	email = CharField(unique=True)
	username = CharField(unique=True)
	first_name = CharField()
	last_name = CharField()
	password = CharField()
	active = BooleanField(default=True)
	class Meta:
		database = db

class Role(Model, RoleMixin):
	name = CharField(unique=True)
	description = CharField(null=True)
	class Meta:
		database = db

class UserRoles(Model):
	user = ForeignKeyField(User, related_name="roles")
	role = ForeignKeyField(User, related_name="users")
	name = property(lambda self: self.role.name)
	description = property(lambda self: self.role.description)
	class Meta:
		database = db