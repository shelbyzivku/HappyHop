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
        url = "https://maps.googleapis.com/maps/api/geocode/json?address="+str(95112)
        convertZIP = requests.request("GET",url)
        print(convertZIP.json())

        hhlocations = self.db.query_db('SELECT street_number,street_name,city,state,zip_code FROM hhprofiles join locations on locations_id = locations.id')
        print hhlocations
        print type(hhlocations)

        return self.load_view('/alvin/googleapiresult.html',hhlocations = hhlocations)

    def gethhlocations(self):
        hhlocations = self.db.query_db('SELECT street_number,street_name,city,state,zip_code FROM hhprofiles join locations on locations_id = locations.id')
        print hhlocations
        print type(hhlocations)

        return Response(json.dumps(hhlocations), mimetype='application/json')

    def dummy():pass
