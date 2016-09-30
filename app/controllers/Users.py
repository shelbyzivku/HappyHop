
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db



    def index(self):
        return self.load_view('hhprofile.html')

    def message(self):
        data = {
            'posts': request.form['posts']
        }
        self.models['User'].add_post(data)
        return redirect('/hhprofile')

    def comment(self):
        data = {
            'comments': request.form['comments']
        }
        self.models['User'].add_comment(data)
        return redirect('/hhprofile')

    def post_remove(self):
        self.models['User'].remove_post()
        return redirect('/happyhop')

    def comment_remove(self):
        self.models['User'].remove_comment()
        return redirect('/happyhop')
