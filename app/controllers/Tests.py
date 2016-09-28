#Tests.py

from system.core.controller import *

class Tests(Controller):
    def __init__(self, action):
        super(Tests, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db


    def index(self):
        return self.load_view('/alvin/yelpapitest.html')
