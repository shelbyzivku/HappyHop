
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db



    def index(self):

        return self.load_view('hhprofile.html')


    def add_post(self):
        data = {
            'posts': request.form['posts']
        }
        self.models['User'].add_post(data)
        return redirect('/hhprofile')


    def add_comment(self):
        data = {
            'comments': request.form['comments']
        }
        self.models['User'].add_comment(data)
        return redirect('/hhprofile')

    # def show_all(self):
    #     squid = self.models['User'].display_post_by_id()
    #     octopus = self.models['User'].display_comment_by_id()
    #     return redirect('/hhprofile', squid=squid, octopus=octopus)
