
class User:
    def __init__(self, email, password, birthDate=None, topics=None, posts=None):
        self.email = email
        self.password = password
        self.birthDate = birthDate
        self.topics = topics
        self.posts = posts

    def set_id(self, id):
        self.id = id
        return self
