"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class HappyHops(Controller):
    def __init__(self, action):
        super(HappyHops, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('/happyhop/happyhop.html')

    def login(self):    
       name = request.form['name']
       email = request.form['email']
       facebookId = request.form['facebookId'] 
       
       user = self.models['User'].save_user(name, email, facebookId)
       session['userId'] = user['id']
       session['email'] = user['email']
       session['user_name'] = user['user_name']
       print session['userId']


       return "ok"