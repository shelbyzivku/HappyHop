#Tests.py

from system.core.controller import *
import requests
import ast

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
        return self.load_view('/alvin/googlemapsapi.html', data=response.json())

    def showresults(self,zip):
        url = "https://api.yelp.com/v3/businesses/search"
        querystring = {"term":"happy hour","location":zip}
        headers = {
            'authorization': "Bearer C8K-8SczRtkkty_VmzqvtAKVTicHQW9D9qf8dBBG85KZn6ycLTGCUW6TCD-VKBjNoJ12x4BFLZ16Mmfb82Cy07f9okDAaM-VIV9qf2sqpbQDE1i0ANX625CJ_BfsV3Yx",
            'cache-control': "no-cache",
            'postman-token': "cb65d0da-ecee-7b91-346d-f1766bc3ce2a"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return self.load_view('/alvin/googlemapsapi.html', data=response.json())
