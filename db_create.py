from project import db
from project.models import BlogPosts

#Create DB and tables

#initialize the db based on the models which we created
db.create_all()

# INSERT
db.session.add(BlogPosts("Good", "I'm good man this is a test", 1))
db.session.add(BlogPosts("Well", "I'm well man this is a test", 1))
db.session.add(BlogPosts("Local Test", "Testing out some postsql", 1))


# commit the changes
db.session.commit()
