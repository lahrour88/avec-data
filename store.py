
class Post:
    def __init__(self, id, photo_url, name, body, date):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body
        self.date = date

class PostStore:
    def __init__(self):
        self.posts = []

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return self.posts[::-1]