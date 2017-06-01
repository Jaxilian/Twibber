from database import db, User, Role, UserRoles, Contact,Tweeb

db.connect()
db.create_tables([User, Role, UserRoles, Contact, Tweeb], safe=True)