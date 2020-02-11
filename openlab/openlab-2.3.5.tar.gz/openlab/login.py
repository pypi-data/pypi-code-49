#Following imports are for the OpenlabApplicationClient
from __future__ import absolute_import, unicode_literals
from oauthlib.oauth2.rfc6749.parameters import (parse_authorization_code_response,
                          parse_token_response, prepare_grant_uri,
                          prepare_token_request)                          
from oauthlib.oauth2.rfc6749.clients.base import Client
from requests_oauthlib import OAuth2Session, OAuth1Session
from oauthlib.oauth2 import InvalidGrantError
from openlab import credentials
from openlab import account

import os
import validators
import json
import time
import inspect
import urllib
import keyring

#Get the location of the installed OpenLab Library
current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

#exec credentials to force compile so to recognize any changes to credentials
exec(open(current_directory+"/credentials.py").read())

token_file = "openlab_token.txt"
token_path = os.path.join(current_directory, token_file)

environments = {'prod': "https://live.openlab.app", 'dev' : "https://dev.openlab.app", 'build':"https://build.openlab.app", 'local':"http://localhost:8888"}
valid_environments = environments.keys()

reference_username = 'current_user' # For storing the active username account

class OpenlabApplicationClient(Client):
    """
    Custom ApplicationClient based on oauthlib's WebApplicationClient in order to pass in custom grant type
    """

    def __init__(self, client_id, code=None, **kwargs):
        super(OpenlabApplicationClient, self).__init__(client_id, **kwargs)
        self.code = code

    def prepare_request_uri(self, uri, redirect_uri=None, scope=None,
                            state=None, **kwargs):
            
        return prepare_grant_uri(uri, self.client_id, 'code', 
                                 redirect_uri=redirect_uri, scope=scope, state=state, **kwargs)

    def prepare_request_body(self, client_id=None, code=None, body='', redirect_uri=None, **kwargs):
        code = code or self.code
        return prepare_token_request('openlab_api_key', code=code, body=body,
                                     client_id=self.client_id, redirect_uri=redirect_uri, **kwargs)

    def parse_request_uri_response(self, uri, state=None):
        response = parse_authorization_code_response(uri, state=state)
        self._populate_attributes(response)
        return response

def token_saver(token):
    """
    Saves the token so it can be used next time
    """
    print("Saving token...")
    with open(token_path, 'w') as f:
        json.dump(token, f)

def get_expire_time():
    """
    Returns the expire time of a token if one exists
    """
    # check to see if a token exists
    has_token = os.path.isfile(token_path)
    if has_token:
         #open the token file and read it
        token = open(token_path,'r')
        token_text = token.read()
        #close the token file
        token.close()

        #convert the json data so that we can search key,value pairings
        j = json.loads(token_text)
        return j['expires_at']
    else:
        print("No token exits")
        return

def token_handler(token, auth_data):
    """
    Sets up and returns an Oauth Session that will automatically handle token refreshing
    """
    #validate the url and email
    valid_url=validators.url(auth_data['url'])
    valid_user= validators.email(auth_data['user'])
    if not valid_url:
        raise ValueError('Invalid url: ' + auth_data['url'])
    if not valid_user:
        raise ValueError('Invalid email: ' + auth_data['user'])

    extra = {'client_id' : auth_data['client_id'],
              'key' : auth_data['key'], 'proxies' : auth_data['proxies']}

    #attempt to create client session to pass back
    client = OpenlabApplicationClient(client_id=auth_data['client_id'])
    oauth = OAuth2Session(client = client, token = token, auto_refresh_url= auth_data['refresh_url'], auto_refresh_kwargs = extra, token_updater = token_saver)
    oauth.proxies = auth_data['proxies'] # probabily redundant
    
    return oauth

def check_for_proxies():
    """Checks for environmentally set HTTP_PROXY and HTTPS_PROXY which can be set from a command window.
        Alteranatively you can pass these in as a dictionary to the openlab http_client
        Returns an empty dictionary if none were found"""
    #execute all get proxy requests once or until proxies is not empty 
    proxies = {}
    while proxies == {}:
        try:
            proxies = urllib.request.getproxies()
            proxies = urllib.request.getproxies_environment()
            proxies = urllib.request.getproxies_registry() 
        except:
            pass
        
        break
    return proxies

def get_proxies(**kwargs):
    proxies = {}
    
    # give 1st priority to kwargs passed in
    if 'proxies' in kwargs:
        # use proxies that were passed in
        proxies = kwargs.get('proxies')
            
        # check type
        if type(proxies) is not dict:
            raise TypeError("proxies must be a dictionary")

    # give 2nd priority to kwargs in credentials
    elif len(credentials.network_proxies) > 0:
        proxies = credentials.network_proxies

    else:
        # check for environemntal proxies if none were passed in
        proxies = check_for_proxies()
    
    return proxies

def request_user_credentials(environment='prod'):
    """
    Asks user for email and api_key
    """
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))

    service = "_".join(["openlab",environment])

    # make a list of safe functions/variables for exec
    safe_list = ['username', 'apikey', 'licenseguid']
    safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])

    input_text = input("Enter the python generated login script:\n")
    
    #format the string
    input_text.strip() #get rid of whitespace
    text = input_text.split() #split at spaces
    
    #assign each assignment
    for assignment in text:
        exec(assignment, {'__builtins__' : None} , safe_dict)

    name = safe_dict['username']
    api_key = safe_dict['apikey']
    license_id = safe_dict['licenseguid']

    # Again, we set an arbritary account's (i.e reference_username) password to the username inputted
    # This way we can keep track of the active account
    if name is not None and api_key is not None:
        try:
            keyring.set_password(service, reference_username, name)
            keyring.set_password(service, name + "_key", api_key)
            keyring.set_password(service, name +"_license", license_id)
        except:
            print("Problems setting credentials in keyring")
    else:
        return request_individual_credentials(environment)
    return {'email' : name, 'api_key' : api_key, 'licenseguid' : license_id}

def request_individual_credentials(environment='prod'):
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))

    service = "_".join(["openlab",environment])

    email = input("Username: ")
    if email is not None:
        try:
            keyring.set_password(service, reference_username, email)
        except:
            pass

    api_key = input("Api key: ")
    if api_key is not None and email is not None:
        try:
            keyring.set_password(service, email + "_key", api_key)
        except:
            pass


    license_id = input("License Guid: ")
    if license_id is not None and email is not None:
        try:
            keyring.set_password(service, email + "_license", license_id )
        except:
            pass

    return {'email' : email, 'api_key' : api_key, 'licenseguid' : license_id}

def get_keyring_username(environment='prod'):
    """
    Gets the active openlab python account
    If one does not exist, it will prompt the user for one
    """
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))
    
    service = "_".join(["openlab",environment])

    #Treating username like a password
    email = None
    try:
        email = keyring.get_password(service, reference_username) #service ="openlab_prod" ; reference_username = "current_user"
    except:
        print("Problem getting email from keyring")
        email = None

    if email == None:
        exec(open(current_directory+"/account.py").read())
        if account.username is not None:
            try:
                keyring.set_password(service, reference_username, account.username)
                print("Using email from accounts.py")
                email = account.username
            except:
                email = None

    if email is None:
        print("No OpenLab username exists yet for this environment...")
        email = request_user_credentials(environment)['email']

    return email

def get_keyring_password(username, environment = 'prod'):
    """
    Returns the openlab key associated with a username.
    If one does not exist, it will prompt the user for one
    """
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))
    
    service = "_".join(["openlab",environment])
    username += "_key"

    #get actual password
    password = None
    try:
        password = keyring.get_password(service, username)
    except:
        print("Problem getting api key from keychain")
        password = None

    if password is None:
        exec(open(current_directory+"/account.py").read())
        if account.apikey is not None:
            try:
                keyring.set_password(service, username, account.apikey)
                print("Using password from accounts.py")
                return account.apikey
            except:
                password = None
    if password is None:
        print("No api_key associated with {}...\nInput Api Key: ".format(username))
        # FIXME
        api_key = request_user_credentials(environment)['api_key']
        try:
            keyring.set_password(service, username, api_key)
            return api_key
        except:
            password = api_key
  
    return password

def get_keyring_license(username, environment = 'prod'):
    """
    Returns the openlab license associated with a username.
    If one does not exist, it will prompt the user for one
    """
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))
    
    service = "_".join(["openlab",environment])
    
    username += "_license"

    license_id = None
    try:
        license_id = keyring.get_password(service, username)
    except:
        license_id = None
    if license_id is None:
        exec(open(current_directory+"/account.py").read())
        if account.licenseguid is not None:
            try:
                keyring.set_password(service, username, account.licenseguid)
                print("Using license from accounts.py")
                return account.licenseguid
            except:
                license_id = account.licenseguid

    if license_id is None:
        print("No license exists yet for this environment. Default will be personal limits")
        answer = input(
            """
            No license exists yet for this environment.\n
            Default is personal license\n
            Would you like to add one? (y/n)
            """
            )
            
        if answer == 'y':
            return request_user_credentials(environment)['license_id']

    return license_id

def switch_license(environment ='prod'):
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))
    
    request_user_credentials(environment)
    
def switch_user(new_user, new_key, environment='prod'):
    """
    Deletes old openlab account/key combination and sets a new one
    """
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))
    
    service = "_".join(["openlab",environment])
    
    new_user += "_key"

    try:
        keyring.delete_password(service, reference_username)
    except:
        print("No previous Openlab account detected")
    try:
        keyring.delete_password(service, new_user)
    except:
        print("New user deteced. Creating a new username/key keychain")

    #set the username so we can find the email later without having to know it
    keyring.set_password(service, reference_username, new_user)
    keyring.set_password(service, new_user , new_key)

def clear_password(environment ='prod'):
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))
    
    service = "_".join(["openlab",environment])

    try:
        keyring.delete_password(service, reference_username)
    except:
        print("Problem clearing password")

def get_credentials(location = 'keyring', environment = 'prod', **kwargs):
    #get the credials/login info needed for logging in/getting token
    if environment not in valid_environments:
        raise Exception("Invalid environment: {}\nValid environments: {}".format(environment, valid_environments))
    username = None
    apikey = None
    licensguid = None
    c = dict()

    if 'url' in kwargs:
        c['url'] = kwargs['url']    
    else:
        c['url'] = environments.get(environment) #FIXME
        
    c['refresh_url'] = c['url'] + "/connect/token"

    # Give highest priority to passed-in Variables
    if 'username' in kwargs.keys():
        username = kwargs.get('username')
    if 'apikey' in kwargs.keys():
        apikey = kwargs.get('apikey')
    if 'licenseguid' in kwargs.keys():
        licensguid = kwargs.get('licenseguid')

    # Give second priority if location = "account"
    if location == 'account':
        try:
            exec(open(current_directory+"/account.py").read())
            c['user'] = username or account.username
            c['key'] = apikey or account.apikey
            c['license_id'] = licensguid or account.licenseguid
        except:
            print("Problem loading from accont")
            
    # Give last priority to default keyring
    elif location == 'keyring':
        c['user'] = username or get_keyring_username(environment)
        c['key'] = apikey or get_keyring_password(c['user'], environment)
        c['license_id'] = licensguid or get_keyring_license(c['user'], environment)

    c['client_id'] = 'OpenLab'

    c['proxies'] = get_proxies(**kwargs)

    c['verify'] = credentials.verify
    return c
    
def create_token(**kwargs):
    kwargs.setdefault('environment', "prod")
    kwargs.setdefault('location', "keyring")
    kwargs.setdefault('proxies', {})

    environment = kwargs.pop('environment')
    location = kwargs.pop('location')

    auth_data = get_credentials(location, environment, **kwargs)
    
    token = None

    client = OpenlabApplicationClient(client_id=auth_data['client_id'])
    oauth = OAuth2Session(client=client)  # this session will be be overwritten with one containing token details for refreshing, but we need it to fetch an initial token
    oauth.proxies = auth_data['proxies']
    oauth.verify = auth_data['verify']
    # create an initial token
    try:
        token = oauth.fetch_token(token_url = auth_data['url'] + "/connect/token",
            key = auth_data['key'], username = auth_data['user'], client_id=auth_data['client_id'],
            proxies = auth_data['proxies'], include_client_id=True)
    except InvalidGrantError:
        print("Invalid Grant Error. Ensure the following account information is correct:\n"
              "email = {}\n"
              "key = {}\n"
              "url = {}\n".format(auth_data['user'], auth_data['key'], auth_data['url']))
        print("Would you like to change any of the above? (y/n)")
        answer = input()
        if answer is 'y':
            request_user_credentials(environment)
            print("User credentials were reset. Trying again...")

            #reload the auth_data
            auth_data = get_credentials(location, environment, **kwargs['proxies'])

            #Try once more
            try:
                token = oauth.fetch_token(token_url = auth_data['url'] +"/connect/token",
                key = auth_data['key'], username = auth_data['user'], client_id = auth_data['client_id'],
                proxies = auth_data['proxies'], include_client_id=True)
            except InvalidGrantError:
                print("""Failed to login again. Ensure that {} is exactly how it appears in the web client 
                and that the api_key is current and then try again.""".format(auth_data))
                exit()
        
    if token is not None:
        #save the token
        token_saver(token)
        return token_handler(token, auth_data) #overwrite the oauth so that we can refresh on the first time
    else:
        raise Exception("Problem creating a token. Check your credentials")