import json
import requests
from requests.auth import HTTPBasicAuth
import time
import random
import string
import hashlib, binascii
import usaepay
from usaepay import mockhandler

api_user='test'
api_pass='test'
base_path='https://secure.usaepay.com/api/v2'
local_test=False;

def encrypt_string(hash_string):
    """
    Creates sha256 hash_string, not intended to be called directly
    """
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def set_authentication(key,pin):
    """
    Sets authentication for connecting to gateway
    Input: API Key and API pin generated on gateway account
    Output: True
    """
    seed = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    clear = key + seed + pin
    hashed = encrypt_string(clear)
    global api_user
    api_user = key
    global api_pass
    api_pass = 's2/' + seed + '/' + hashed
    return True
    

def run_call(type,end_path,data={},params={}):
    """
    Sends api calls to gateway, not intended to be called directly.
    """
    if api_user=='test' or api_pass=='test':
        raise Exception('Please run set_authentication before attempting to run api calls.')
    first=True
    for field,value in params.items():
        if first:
            end_path = end_path + '?' + field + '=' + value
            first=False
        else:
            end_path = end_path + '&' + field + '=' + value
    full_path = base_path+end_path
    
    if(local_test):
        return json.loads(mockhandler.mock_call(type,full_path,json.dumps(data)))
    
    if type=='get':
        response=requests.get(full_path,auth=HTTPBasicAuth(api_user,api_pass))
    elif type=='post':
        response=requests.post(full_path,auth=HTTPBasicAuth(api_user,api_pass),json=data)
    elif type=='put':
        response=requests.put(full_path,auth=HTTPBasicAuth(api_user,api_pass),json=data)
    elif type=='delete':
        response=requests.delete(full_path,auth=HTTPBasicAuth(api_user,api_pass))
    else:
        raise Exception('Unexpected call type, please contact support')
    if response:
        return response.json()
    else:
        raise Exception(f'Unexpected response {response}')
        