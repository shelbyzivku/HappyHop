
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db



    def index(self):

        return self.load_view('hhprofile.html')


    def add(self):
        data = {
            'posts': request.form['posts'],
            'comments': request.form['comments']
        }
