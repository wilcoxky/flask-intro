from project import db
from project.models import User


#intialize

#INSERT
db.session.add(User("Kyle","wilcox32ahs@gmail.com", "hong0322"))
db.session.add(User("admin","admin@gmail.com", "admin"))

#commit
db.session.commit()
