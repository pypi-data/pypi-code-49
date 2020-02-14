from azure.graphrbac import GraphRbacManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.graphrbac.models import PasswordCredential
from datetime import datetime, timedelta

from az_k8s_operations import common as cn

import random
import string
import sys

if sys.version_info.major > 2:
  from datetime import timezone
else:
  import pytz


def checkKeys(listKeys, nbDays):
 """ check Keys"""
 if sys.version_info.major > 2:
   datenow = datetime.now(timezone.utc)
 else:
   datenow = pytz.utc.localize(datetime.utcnow())
 datethreshold = datenow + timedelta(days=nbDays)
 keys=[]
 for key in listKeys:
  # print("WARNING : Keys "+key.key_id+" will expired sooner ("+str(nbDays)+" days)!!!!!")
  if key.end_date < datethreshold:
    if key.end_date < datenow:
     state = 'true'
    else:
     state = 'SOON'
  else:
   state = 'false'

  keys.append({'KeyId':key.key_id,
               'EndDate':key.end_date.replace(tzinfo=None),
			   'ToLate':state})
 return keys

def getObjectIdFromAppId(TENANT_ID,credential,app_id):
 """Get object id from application client id """
 graphrbac_client = GraphRbacManagementClient(credential, TENANT_ID)
 for app in graphrbac_client.applications.list():
  if app.app_id == app_id :
   return app.object_id
 return 'null'

def getSpnFromClientId(CLIENT, KEY, TENANT_ID,client_id):
 """Get Spn from application client id """
 graph_credentials = ServicePrincipalCredentials(client_id = CLIENT,secret = KEY,tenant = TENANT_ID,resource = 'https://graph.windows.net')
 graphrbac_client = GraphRbacManagementClient(graph_credentials, TENANT_ID)
 for item in graphrbac_client.service_principals.list():
  if item.app_id == client_id:
   result=item  
 if result:
  return result
 else:
  return 'NOT FIND'

def getSpnListWithNoClientSecrets(graph_credentials, TENANT_ID):
  """Get Spn list with no client secrets (without expiration date). 
  Required READALL on diectory on API graph Admin consent.
  Return a list dict(SpnId: ,Name:)"""
  listSpn = []
  graphrbac_client = GraphRbacManagementClient(graph_credentials, TENANT_ID)
 # Required READALL on diectory on API graph Admin consent.
  for app in graphrbac_client.applications.list():
   listKeys = graphrbac_client.applications.list_password_credentials(app.object_id)
   Ok=  False
   for key in listKeys :
       Ok= True
 #Add only the spns that do not have a key
   if not Ok:
    listSpn.append({'SpnId':app.object_id,'Name':app.display_name,'KeyId':'-', 'EndDate':'-','ToLate':'-'})
    print((' '.join((app.display_name, app.object_id))))
  return listSpn

def CreateKeyForSpnList(graph_credentials, TENANT_ID,nbDays,listSpn):
  """Create Key (client secrets with expiration date). 
  Return a list dict(SpnId: ,Name:,Secret:,EndDate:)"""
  newlistSpn=[]
  if sys.version_info.major > 2:
   dateNow = datetime.now(timezone.utc)
  else:
   dateNow = pytz.utc.localize(datetime.utcnow())
  dateEnd = dateNow + timedelta(days=nbDays)
  for spn in listSpn:
   keyName='automatickey'
   result = update_password_key(graph_credentials,TENANT_ID, spn.get("SpnId"), nbDays,keyName,'create')
   newlistSpn.append({'SpnId':spn.get('SpnId'),'Name':spn.get('Name'),'Secret':result['value'],'EndDate':dateEnd.replace(tzinfo=None)})
  return newlistSpn

def checkAllSpn(graph_credentials, TENANT_ID, nbDays):
 """Get Spn key validity (which expires in x days. 
 Required READALL on diectory on API graph Admin consent.
 Return a list dict(SpnId: ,KeyId: , EndDate: ,  ToLate:true|false|SOON )"""
 listSpn=[]
 if sys.version_info.major > 2:
   datenow = datetime.now(timezone.utc)
 else:
   datenow = pytz.utc.localize(datetime.utcnow())
 datethreshold = datenow + timedelta(days=nbDays)
 print((str(datethreshold)))
 graphrbac_client = GraphRbacManagementClient(graph_credentials, TENANT_ID)
 # Required READALL on diectory on API graph Admin consent.
 for app in graphrbac_client.applications.list():
  listKeys= graphrbac_client.applications.list_password_credentials(app.object_id)
  keys = checkKeys(listKeys, nbDays)
  if keys:
   for key in keys :
    listSpn.append({'SpnId':app.object_id,'Name':app.display_name,
                    'KeyId':key.get('KeyId'), 
					'EndDate':key.get('EndDate'), 'ToLate':key.get('ToLate')})
    print((' '.join((app.display_name, app.object_id,key.get('KeyId'),str(key.get('EndDate')),key.get('ToLate') )).encode('utf-8')))
 return listSpn
   
def update_password_key(credentials,TENANT_ID, app_id, nbDays,keyName,action):
 """ Update password key of client ID which expires in x days (action : create|delete) """
 myvalue=''
 s = keyName 
 b = bytearray()
 b.extend(list(map(ord, s)))
 graphrbac_client = GraphRbacManagementClient(credentials, TENANT_ID)
 if sys.version_info.major > 2:
   dateNow = datetime.now(timezone.utc)
 else:
   dateNow = pytz.utc.localize(datetime.utcnow())
 dateEnd = dateNow + timedelta(days=nbDays)
 listPasswordKeys = [] 
 currentListPasswordKeys = graphrbac_client.applications.list_password_credentials(app_id)
 for key in currentListPasswordKeys:
  if action == 'delete' and key.custom_key_identifier == b:
   print(("we delete "+keyName))
  else:
   listPasswordKeys.append(key)
 if action == 'create':
  if sys.version_info.major > 2:
    datenow = datetime.now(timezone.utc)
  else:
    datenow = pytz.utc.localize(datetime.utcnow())
  s += datenow.strftime("%Y%m%d%H%M%S")
  b = bytearray()
  b.extend(list(map(ord, s)))
  print(("we create "+s))
  myvalue = cn.generatePassword(32)
  newPasswordKey = PasswordCredential(start_date=dateNow, end_date=dateEnd, value=myvalue, custom_key_identifier=b)   
  listPasswordKeys.append(newPasswordKey)
 if action == 'create' or action == 'delete':
  result = graphrbac_client.applications.update_password_credentials(app_id,listPasswordKeys )
 else:
  print('Error: Unknow action')
 return {'key_custom_name':s ,'value':myvalue}
    #{'type': 'AsymmetricX509Cert', 'value': None, 'custom_key_identifier': '4E7C31D2BE0FF71BDE73E69B0F4DA0CF8C46029B', 'end_date': datetime.datetime(2020, 1, 15, 10, 14, tzinfo=<isodate.tzinfo.Utc object at 0x7fc29e5e7dd8>), 'usage': 'Verify', 'key_id': '0238b2e2-e4a3-4de2-9fa1-b004aad204ed', 'start_date': datetime.datetime(2019, 10, 17, 10, 14, tzinfo=<isodate.tzinfo.Utc object at 0x7fc29e5e7dd8>), 'additional_properties': None}

def checkKeyCreation(graph_credential, TENANT_ID,client_id, key_custom_name):
 """iCheck if key_custom_name exist"""
 result = False 
 graphrbac_client = GraphRbacManagementClient(graph_credential, TENANT_ID)
 print(key_custom_name)
 listKeys = graphrbac_client.applications.list_password_credentials(getObjectIdFromAppId(TENANT_ID,graph_credential,client_id))
 for key in listKeys:
     if key.custom_key_identifier:
         if str(key.custom_key_identifier.decode("utf8")) == key_custom_name :
          result = True
          break
 return result
