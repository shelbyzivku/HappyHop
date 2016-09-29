
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()


    def save_user(self, name, email, facebook_id):
        user_exist = False

        query = "SELECT * FROM users WHERE email =:email"
        data = {'email':email}
        user = self.db.query_db(query, data)

        if len(user) > 0:
            user_exist = True
        else:
            insert_query = "INSERT INTO users(email, user_name, facebook_id, created_at, updated_at) values(:email, :name, :facebook_id, NOW(), NOW())"
            data = {'email':email,
                    'name':name,
                    'facebook_id':facebook_id}
            self.db.query_db(insert_query, data)

        query = "SELECT * FROM users where email=:email"
        data = {'email':email}
        user = self.db.query_db(query, data)
        return user[0]

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
        query = "DELETE FROM posts WHERE id = :posts_id"
        data = {'posts_id': id}
        return mysql.query_db(query, data)

    def remove_comment(self, info):
        query = "DELETE FROM comments WHERE id = :comments_id"
        data = {'comments_id': id}
        return mysql.query_db(query, data)
