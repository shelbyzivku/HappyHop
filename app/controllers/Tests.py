#Tests.py

from system.core.controller import *
from flask import Response
import requests
import ast
import json

class Tests(Controller):
    def __init__(self, action):
        super(Tests, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        url = "https://api.yelp.com/v3/businesses/search"
        querystring = {"term":"happy hour","location":"95112"}
        headers = {
            'authorization': "Bearer C8K-8SczRtkkty_VmzqvtAKVTicHQW9D9qf8dBBG85KZn6ycLTGCUW6TCD-VKBjNoJ12x4BFLZ16Mmfb82Cy07f9okDAaM-VIV9qf2sqpbQDE1i0ANX625CJ_BfsV3Yx",
            'cache-control': "no-cache",
            'postman-token': "cb65d0da-ecee-7b91-346d-f1766bc3ce2a"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.json()['businesses'][1]['coordinates'])
        #print(ast.literal_eval(response.text[14:]))
        #print(response.text[14:])
        #print type(response.text)
        return self.load_view('/alvin/googlemapsapi.html')

    def showresults(self):
        hhlocations = self.db.query_db('select * from hhprofiles left join hhtime on hhtime.hhprofiles_id = hhprofiles.id left join (select locations.* from locations left join hhprofiles on locations.id = hhprofiles.locations_id) as locations on locations.id = hhprofiles.locations_id')
        #print hhlocations
        #print type(hhlocations)

        return self.load_view('/alvin/googleapiresult.html',hhlocations = hhlocations)

    def insertlocations(self):
        url = "https://api.yelp.com/v3/businesses/search"
        querystring = {"term":"happy hour","location":"95112"}
        headers = {
            'authorization': "Bearer C8K-8SczRtkkty_VmzqvtAKVTicHQW9D9qf8dBBG85KZn6ycLTGCUW6TCD-VKBjNoJ12x4BFLZ16Mmfb82Cy07f9okDAaM-VIV9qf2sqpbQDE1i0ANX625CJ_BfsV3Yx",
            'cache-control': "no-cache",
            'postman-token': "cb65d0da-ecee-7b91-346d-f1766bc3ce2a"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        for x in response.json()['businesses']:
            print x['name'],x['location']['address1'],'\n',x['coordinates'],'\n\n'
            query = 'INSERT INTO locations (address1,city,state,zip_code,latitude,longitude)\
                     VALUES (:address1,:city,:state,:zip_code,:latitude,:longitude)'
            data = {'address1':x['location']['address1'],
            'city':x['location']['city'],
            'state':x['location']['state'],
            'zip_code':x['location']['zip_code'],
            'latitude':x['coordinates']['latitude'],
            'longitude':x['coordinates']['longitude']}
            self.db.query_db(query,data)

            query = 'SELECT id from locations WHERE address1 = :address1 LIMIT 1'
            data = {'address1':x['location']['address1']}
            id = self.db.query_db(query,data)[0]['id']

            query = 'INSERT INTO hhprofiles (name,description,locations_id) VALUES(:name,:description,:id)'
            data = {'name':x['name'],'description':x['url'],'id':id}
            self.db.query_db(query,data)
        return self.load_view('alvin/data.html', data = response.json())









    def dummy():pass
