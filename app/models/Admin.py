
from system.core.model import Model

class Admin(Model):
    def __init__(self):
        super(Admin, self).__init__()


    def add_post(self, info):
        query = "INSERT INTO posts (content, updated_at, users_id) VALUES (:content, NOW(), :users_id)"
        data = { 'posts': info['posts'], 'users_id': info['id'] }
        return self.db.query_db(query, data)

    def add_comment(self, info):
        query = "INSERT INTO comments (content, updated_at, users_id) VALUES (:content, NOW(), :users_id)"
        data = { 'comments': info['comments'], 'users_id': info['id'] }
        return self.db.query_db(query, data)

    def display_post_by_id(self, info):
        query = "SELECT users.first_name, posts.content, posts.users_id, posts.created_at, posts.id FROM posts JOIN users ON posts.users_id ORDER BY posts.created_at DESC"
        posts = mysql.query_db(query)

    def display_comment_by_id(self, info):
        query = "SELECT users.first_name, comments.content, comments.users_id, comments.created_at, comments.id, comments.posts FROM comments JOIN users ON comments.users_id ORDER BY comments.created_at DESC"
        comments = mysql.query_db(query)

    def remove_post(self, info):
        query = "DELETE FROM posts WHERE id = :posts_id AND users.id = '1'"
        data = {'posts_id': id}
        return mysql.query_db(query, data)

    def remove_comment(self, info):
        query = "DELETE FROM comments WHERE id = :comments_id AND users.id = 1"
        data = {'comments_id': id}
        return mysql.query_db(query, data)
