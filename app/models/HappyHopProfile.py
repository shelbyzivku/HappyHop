"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class HappyHopProfile(Model):
    def __init__(self):
        super(HappyHopProfile, self).__init__()

    def get_all_hhlocations(self):
        query = "SELECT * FROM hhprofiles"
        hhlocations = self.db.query_db(query)
        return hhlocations

    def get_hhname_by_id(self, id):
        query = 'SELECT * FROM hhprofiles WHERE id = :hhprofiles_id'
        data = { 'hhprofiles_id': id }
        hhname = self.db.query_db(query, data)
        return hhname[0]

    def get_hhlocation_by_id(self, id):
        query = 'SELECT l.id as locationId,l.address1 FROM locations l INNER JOIN hhprofiles p WHERE l.id = p.locations_id AND p.id = :hhprofiles_id'
        data = { 'hhprofiles_id': id }
        hhlocation = self.db.query_db(query, data)
        return hhlocation[0]

    def display_all_messages_hhname_by_id(self, id):
        query = "SELECT p.content, date_format(p.created_at,'%D-%M-%Y') as created_at, u.user_name  from posts p inner join hhprofiles hp on p.hhprofiles_id = hp.id inner join users u on u.id =p.users_id and hp.id = :hhprofiles_id"
        data = { 'hhprofiles_id': id }
        return self.db.query_db(query, data)

    def get_all_locations(self):
        return self.db.query_db('select * from hhprofiles left join hhtime on hhtime.hhprofiles_id = hhprofiles.id left join (select locations.* from locations left join hhprofiles on locations.id = hhprofiles.locations_id) as locations on locations.id = hhprofiles.locations_id')

    def get_location_by_id(self,id):
        query = 'select * from hhprofiles left join hhtime on hhtime.hhprofiles_id = hhprofiles.id left join (select locations.* from locations left join hhprofiles on locations.id = hhprofiles.locations_id) as locations on locations.id = hhprofiles.locations_id where locations.id = :id'
        data = {'id':id}
        return self.db.query_db(query,data)
