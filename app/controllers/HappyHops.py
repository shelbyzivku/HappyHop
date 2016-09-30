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
        self.load_model('HappyHopProfile')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        hhlocations = self.models['HappyHopProfile'].get_all_hhlocations()
        locations = self.models['HappyHopProfile'].get_all_locations()

        return self.load_view('/happyhop/happyhop.html', hhlocations=hhlocations,locations=locations)

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


    def message(self, id):
        print id
        print session['userId']
        self.models['User'].add_message(request.form['message'], session['userId'], id, request.form['happyhop_profile_location_id'])
        happyhopname = self.models['HappyHopProfile'].get_hhname_by_id(id)
        happyhoplocation = self.models['HappyHopProfile'].get_hhlocation_by_id(id)
        happyhopname_message = self.models['HappyHopProfile'].display_all_messages_hhname_by_id(id)
        location = self.models['HappyHopProfile'].get_location_by_id(id)

        return self.load_view('/happyhopprofiles/profile.html', happyhopname = happyhopname, happyhoplocation = happyhoplocation, happyhopname_message = happyhopname_message,location = location[0])

    def happyhopdetail(self, id):
        happyhopname,happyhoplocation,happyhopname_message = [[1],[2],[3]]
        happyhopname = self.models['HappyHopProfile'].get_hhname_by_id(id)
        happyhoplocation = self.models['HappyHopProfile'].get_hhlocation_by_id(id)
        happyhopname_message = self.models['HappyHopProfile'].display_all_messages_hhname_by_id(id)
        location = self.models['HappyHopProfile'].get_location_by_id(id)
        return self.load_view('/happyhopprofiles/profile.html', happyhopname = happyhopname, happyhoplocation = happyhoplocation, happyhopname_message = happyhopname_message,location = location[0])



    # def comment(self):
    #      data = {
    #          'comments': request.form['comments']
    #      }
    #      self.models['User'].add_comment(data)
    #      return redirect('/hhprofile')
    #
    # def post_remove(self):
    #      self.models['User'].remove_post()
    #      return redirect('/happyhop')
    #
    # def comment_remove(self):
    #      self.models['User'].remove_comment()
    #      return redirect('/happyhop')
