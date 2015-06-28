from app import db


class BlogPosts(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)

    def __init__(self, title, description):
        self.title = title
        self.description = description


    def __repr__(self):
        return ('<title {}, description {}'.format(self.title, self.description))
        # return (self.title + ": " + description)
