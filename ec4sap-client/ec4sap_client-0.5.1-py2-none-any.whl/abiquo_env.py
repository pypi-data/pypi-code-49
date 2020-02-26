# --------------------------------------------------------------------
# Abiquo REST-API - Configuration
# --------------------------------------------------------------------

import os
import json
import requests
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
from ec4sap import config


# --------------------------------------------------------------------
class ABIQUO_ENV:

    # general
    key = ""
    name = ""
    scope = ""
    
    # api endpoint
    api_url = ""
    api_version = ""
    
    # credentials (oauth)
    hasAuth = False 
    bearer = ""
    app_name = ""
    app_key = ""
    app_secret = ""
    access_token = ""
    access_secret = ""

    #error
    error_msg = None

    # ssl verification
    verify_ssl = config.CFG_VERIFY_SSL

    def __init__(self, key, token=None):
        data = ABIQUO_ENV_DATA().getEnv(key)

        self.bearer = 'Bearer %s' % token
        self.key = key
        try:
            self.name = data["name"]
            self.scope = data["scope"]
            self.api_url = data["api_url"]
            self.api_version = data["api_version"]
            self.app_key = data["app_key"]
            self.app_secret = data["app_secret"]
            self.access_token = data["access_token"]
            self.access_secret = data["access_secret"]
        except:
            pass


    def authenticate(self, bt):
        try:
            if bt != None: self.bearer = 'Bearer %s' % bt
            oauth = OAuth1Session(self.app_key, client_secret=self.app_secret, callback_uri='oob')
            tokens = oauth.fetch_request_token("%s/oauth/request_token" % self.api_url, verify=self.verify_ssl)
            r = requests.get("%s/oauth/authorize?oauth_token=%s" % (self.api_url, tokens['oauth_token']),
                    headers={'Authorization': self.bearer},
                    allow_redirects=False,
                    verify=self.verify_ssl)
            if r.status_code == 401: raise ValueError("401 - Invalid OAuth Token")
            location = r.headers['location']
            verifier_index = location.index('oauth_verifier=')
            verifier = location[verifier_index+15:]
            oauth = OAuth1Session(self.app_key, client_secret=self.app_secret,
                    resource_owner_key=tokens['oauth_token'],
                    resource_owner_secret=tokens['oauth_token_secret'],
                    verifier=verifier)
            access_tokens = oauth.fetch_access_token("%s/oauth/access_token" % self.api_url, verify=self.verify_ssl)
            self.access_token = access_tokens['oauth_token']
            self.access_secret = access_tokens['oauth_token_secret']

            #save data
            data = dict()
            data["name"] = self.name
            data["scope"] = self.scope
            data["api_url"] = self.api_url
            data["api_version"] = self.api_version
            data["app_key"] = self.app_key
            data["app_secret"] = self.app_secret
            data["access_token"] = self.access_token
            data["access_secret"] = self.access_secret
            ABIQUO_ENV_DATA().saveData(self.key,data)

            return True
        except ValueError as e:
            self.error_msg = e
            return False
        

    def register_app(self, app_name, bt):
        try:
            if bt != None: self.bearer = 'Bearer %s' % bt
            user_info = requests.get("%s/login" % self.api_url, verify=self.verify_ssl,
                    headers={'Accept': 'application/vnd.abiquo.user+json',
                             'Authorization': self.bearer})
            if user_info.status_code == 401: raise ValueError("401 - Invalid OAuth Token")
            app_link = filter(lambda l: l['rel'] == 'applications', user_info.json()['links'])[0]
            app = requests.post(app_link['href'], verify=self.verify_ssl,
                    headers={'Content-type': 'application/vnd.abiquo.application+json',
                             'Authorization': self.bearer},
                    data=json.dumps({'name': app_name})).json()
            self.app_key = app['apiKey']
            self.app_secret = app['apiSecret']
            self.app_name = app_name

            return True
        except ValueError as e:
            self.error_msg = e
            return False       
    
    
    def getOAuth(self):
        return OAuth1(self.app_key, 
                      client_secret=self.app_secret, 
                      resource_owner_key=self.access_token, 
                      resource_owner_secret=self.access_secret)
    

# --------------------------------------------------------------------
class ABIQUO_ENV_DATA:

    env = {}

    def __init__(self):
        try:
            f = open(os.path.dirname(__file__)+'/ec4sap.env','r')
            data = f.read()
            f.close()
            self.env = eval(data)
        except:
            self.env["int"] = dict(
                name = "EC4SAP INT",
                scope = "tenant",
                api_url = config.CFG_ABQ_URL_INT,
                api_version = config.CFG_ABQ_VERSION_INT
            )
            self.env["prd"] = dict(
                name = "EC4SAP PRD",
                scope = "tenant",
                api_url = config.CFG_ABQ_URL_PRD,
                api_version = config.CFG_ABQ_VERSION_PRD
            )

    def getEnv(self, key="int"):
        if key not in self.env:
            self.env[key] = dict(
                name = "EC4SAP %s" % key,
                scope = "tenant",
                api_url = config.CFG_ABQ_URL_PRD,
                api_version = config.CFG_ABQ_VERSION_PRD
            )
        return self.env[key]

    def saveData(self, key, data):
        self.getEnv(key)
        self.env[key] = data
        f = open(os.path.dirname(__file__)+'/ec4sap.env','w')
        f.write(str(self.env))
        f.close()
