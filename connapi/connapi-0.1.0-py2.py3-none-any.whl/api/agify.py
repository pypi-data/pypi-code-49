import requests
import json
from connapi.data import Linker

class Agify():
    def get_age(datadict,country_code=None,api_key=None):
        size = len(datadict)
        if(size == 1):
            url = Linker.url_agify + "name=" + str(datadict[0])
        else:
            temp_url = ""
            for i in range(0,size):
                if(i<(size-1)):
                    temp_url += "name[]=" + str(datadict[i]) + "&"
                else:
                    temp_url += "name[]=" + str(datadict[i])
            url = Linker.url_agify + temp_url
        if(country_code is not None):
            url += "&country_id=" + country_code
        if(api_key is not None):
            url += "&apikey=" + api_key
        resp = requests.get(url)
        return json.loads(resp.text)