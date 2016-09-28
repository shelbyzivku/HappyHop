
from system.core.controller import *

class Admins(Controller):
    def __init__(self, action):
        super(Admins, self).__init__(action)

        self.load_model('Admin')
        self.db = self._app.db



    def index(self):
        return self.load_view('hhprofile.html')

    def post(self):
        data = {
            'posts': request.form['posts']
        }
        self.models['Admin'].add_post(data)
        return redirect('/hhprofile')

    def comment(self):
        data = {
            'comments': request.form['comments']
        }
        self.models['Admin'].add_comment(data)
        return redirect('/hhprofile')

    def post_remove(self):
        self.models['Admin'].remove_post()
        return redirect('/hhprofile')

    def comment_remove(self):
        self.models['Admin'].remove_comment()
        return redirect('/hhprofile')
