import azure.mgmt.resource
from azure.keyvault.secrets import SecretClient


from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlockBlobService
from azure.storage.file import FileService
from azure.mgmt.compute import ComputeManagementClient
from datetime import datetime
import xlsxwriter
from string import Template

import requests
import random
import string
import time
import sys

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
## Send grid mail ##
import base64
import os
import os.path
from os import path
import filetype
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

headers = ['Url','Branch','Country','Domain 1','Domain 2','Application',\
           'Business','Criticity','Scan Profiles','Schedule','Timezone',\
           'Scanzone','Crawling Depth','Exclusions','Other comments']



def setKeyvaultSecret(credential,vaultUrl,secretName,secretValue):
    """Set a secret in a kleyvault i(create, update) """
    secret_client = SecretClient(vault_url=vaultUrl, credential=credential)
    try:
        secret = secret_client.set_secret(secretName, secretValue)
        print('We have updated secret '+secretName+' in '+vaultUrl)
    except Exception as e:
        print('WARNING:'+str(e))
        secret=''

    return secret

def getResource(credentials,subscription_id,resource_group_name, resource_type):
 """Get the resource object from resource group name, name and resource type """
 myResult = []
 client = ResourceManagementClient(credentials, subscription_id)
 for item in client.resources.list_by_resource_group(resource_group_name):
    if item.type == resource_type:
     myResult.append(item.name)
 return myResult


def checkUrl(url):
 """check the return code of url """
 try:
     r = requests.head(url)
     print(url+":"+str(r.status_code))
     return r.status_code
 except requests.ConnectionError:
     print(url+"failed to connect")
     return "Failed"

def generatePassword(stringLength=14):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + "!#$&()*+,-./:;<=>?@[\]^_{|}~"
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def generateXlsxFromList(headers, listUrls, fileName):
 """Generate xls file from a list"""
 workbook = xlsxwriter.Workbook(fileName)
 worksheet = workbook.add_worksheet()
 cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
 row = 0
 col = 0
 for col in range(0, len(headers)):
  worksheet.write(row, col,  headers[col], cell_format)
 row += 1
 for url in listUrls:
  for col in range(0, len(headers)):
   if headers[col] in url:
    worksheet.write(row, col,  url[headers[col]] )
   else:
    worksheet.write(row, col,  'Unknow' )
  row +=1
 workbook.close()
 return 0

def uploadFile2Blob(accountname, accountkey, container, \
                    targetFileName, localFileName):
 """upload file to a blob """
 block_blob_service = BlockBlobService(account_name=accountname, account_key=accountkey)
 block_blob_service.create_blob_from_path(container, targetFileName, localFileName)

def read_template(filename):
    """read template froma a  file """
    if sys.version_info.major > 2:
     with open(filename, 'r', encoding='utf-8') as template_file:
         template_file_content = template_file.read()
     return Template(template_file_content)
    else:
     with open(filename, 'r') as template_file:
         template_file_content = template_file.read()
     return Template(template_file_content)

def sendMail(SMTP_SERVER,SMTP_PORT,MY_ADDRESS,PASSWORD,Name,email,template,filename):
 """ function to send mail with attachment """
 s = smtplib.SMTP_SSL(host=SMTP_SERVER, port=SMTP_PORT)
 s.set_debuglevel(1)
 s.login(MY_ADDRESS, PASSWORD)
 message_template = read_template(template)
 msg = MIMEMultipart()
 message = message_template.substitute(PERSON_NAME=Name)
 msg['From']=MY_ADDRESS
 msg['To']=email
 msg['Subject']="This is TEST"
 msg.attach(MIMEText(message, 'plain'))
 if filename != 'NONE':
     with open(filename, "rb") as fil:
         part = MIMEApplication(
             fil.read(),
             Name=basename(filename)
            )
     part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
     msg.attach(part)
 s.send_message(msg)
 del msg

def sendMailSendGrid(FROM, TO, SUBJECT, CONTENT , LISTFILENAME, API_KEY):
    """Send Mail with send Grid """
    message = Mail(
     from_email=FROM,
     to_emails=TO,
     subject=SUBJECT,
     html_content=CONTENT)
    for FILENAME in LISTFILENAME:
     if (path.exists(FILENAME)):
      with open(FILENAME, 'rb') as f:
       data = f.read()
       f.close()
      kind = filetype.guess(FILENAME)
      if kind is None:
          FILETYPE = 'NONE'
      else:
          FILETYPE = kind.mime
      
      encoded = base64.b64encode(data).decode()
      attachment = Attachment()
      attachment.file_content = FileContent(encoded)
      attachment.file_type = FileType(FILETYPE)
      attachment.file_name = FileName(FILENAME)
      attachment.disposition = Disposition('attachment')
      attachment.content_id = ContentId('Example Content ID')
      message.attachment = attachment
    try:
     sg = SendGridAPIClient(API_KEY)
     response = sg.send(message)
     print(response.status_code)
     print(response.body)
     print(response.headers)
     return 0
    except Exception as e:
     print(e.message)
     return 2

def getTagsFromRg(credentials, subscription_id, rgName):
 """get Tags from resource group """
 resource_client = ResourceManagementClient(credentials, subscription_id)
 rg = resource_client.resource_groups.get(rgName)
 return rg.tags


def getAllUrlAppServ(credentials, subscription, checkUrl):
 """get  All url from AppServ """
 listUrl=[]
 branch = 'Unknown'
 appname = 'Unknown'
 env = 'Unknown'
 hostname = 'No'
 app_serv_client = WebSiteManagementClient(credentials, subscription['id'])
 for webapp in  app_serv_client.web_apps.list():
  for hostname in webapp.host_names:
   rgTags = getTagsFromRg(credentials, subscription['id'], webapp.resource_group)
   if rgTags :
    if 'Branch' in rgTags:
     branch = rgTags['Branch']
    if 'AppName' in rgTags:
     appname = rgTags['AppName']
    if 'Appname' in rgTags:
     appname = rgTags['Appname']
    if 'Env' in rgTags:
     env = rgTags['Env']
   url = "https://"+hostname
   if checkUrl:
    rc = checkUrl(url)
   else:
    rc = 'No test'
   listUrl.append({'Url':url,'Branch':branch,'Country':webapp.location,\
                   'Domain 1':subscription['name'],'Domain 2':webapp.resource_group,'Application':appname,\
                   'Criticity':env,'Other comments':"WEB APP :"+webapp.name,\
                   'Scanzone':'internet','rc':rc} )
 return listUrl

def getAllUrlAppGw(credentials, subscription, checkUrl ):
 """get  All url from AppGw """
 listUrl=[]
 branch = 'Unknown'
 appname = 'Unknown'
 env = 'Unknown'
 hostname = 'No'
 network_client = NetworkManagementClient(credentials, subscription['id'])
 apgwList = network_client.application_gateways.list_all()
 for apgw in apgwList:
  rgName = str(apgw.id).split('/')[4]
  for frontEndIp in apgw.frontend_ip_configurations:
   if frontEndIp.public_ip_address:
    ip = network_client.public_ip_addresses.get(rgName, str(frontEndIp.public_ip_address.id).split('/')[8])
    if ip.dns_settings:
     hostname = ip.dns_settings.fqdn
    else:
     hostname = ip.ip_address
  rgTags = getTagsFromRg(credentials, subscription['id'], rgName)
  if rgTags :
   if 'Branch' in rgTags:
    branch = rgTags['Branch']
   if 'AppName' in rgTags:
    appname = rgTags['AppName']
   if 'Appname' in rgTags:
    appname = rgTags['Appname']
   if 'Env' in rgTags:
    env = rgTags['Env']
  for httpListener in apgw.http_listeners:
   if str(httpListener.host_name) != 'None':
    hostname = str(httpListener.host_name)
   for frontend in apgw.frontend_ports:
    if frontend.id == httpListener.frontend_port.id:
     port = frontend.port
     break
   if len(apgw.url_path_maps) == 0:
    url=str(httpListener.protocol).lower()+"://"+hostname+":"+str(port)
    if checkUrl:
     rc = checkUrl(url)
    else:
     rc = 'No test'
    listUrl.append({'Url':url,'Branch':branch,'Country':apgw.location,\
                    'Domain 1':subscription['name'],'Domain 2':rgName,'Application':appname,\
                    'Criticity':env,'Other comments':"App Gw :"+apgw.name,\
                    'Scanzone':'internet','rc':rc} )
  for maps in apgw.url_path_maps:
   for pathRule in maps.path_rules:
    url=str(httpListener.protocol).lower()+"://"+hostname\
        +":"+str(port)+str(pathRule.paths[0])
   if checkUrl:
    rc = checkUrl(url)
   else:
    rc = 'No test'
    listUrl.append({'Url':url,'Branch':branch,'Country':apgw.location,\
                    'Domain 1':subscription['name'],'Domain 2':rgName,'Application':appname,\
                    'Criticity':env,'Other comments':"App Gw:"+apgw.name,\
                    'Scanzone':'internet','rc':rc} )
 return listUrl

def getAllUrlNginx(credentials, subscription, rgName, vmName, SUBSCRIPTION_ID, rgname, accountname,sharename, checkUrl):
 """get  All url from Nginx vm (we use a tempory share to do run command and get result)="""
 print("=="+subscription['name']+"=="+rgName+"=="+vmName+"===")
 listUrl=[]
 branch = 'Unknown'
 appname = 'Unknown'
 env = 'Unknown'
 location = rgName.split('-')[3]
 env = rgName.split('-')[2]

 storage_client = StorageManagementClient(credentials,SUBSCRIPTION_ID)
 storage_keys = storage_client.storage_accounts.list_keys(rgname, accountname)
 storage_keys = {v.key_name: v.value for v in storage_keys.keys}
 accountkey = storage_keys['key1']
 client = ComputeManagementClient(credentials, subscription['id'])
 run_command_parameters = {
      'command_id': 'RunShellScript',
      'script': [
 'grep -v \'#\' /etc/nginx/conf.d/*/*.conf | grep server_name | grep -v return | uniq | awk -F\'/\' \'{print $5"/"$6}\' | awk \'{ print $1 $3}\'| sed \'s/\.conf//g\' | sed \'s/;//g\' >extracts; echo "username=$arg2">$PWD/cred;echo "password=$arg1" >>$PWD/cred; chmod 600 cred;sudo mkdir -p /mnt/$arg3 ; sudo mount -t cifs //$arg2.file.core.windows.net/$arg3 /mnt/$arg3 -o vers=3.0,credentials=$PWD/cred,dir_mode=0777,file_mode=0777,serverino;cp extracts /mnt/$arg3/; sudo umount /mnt/$arg3;sudo rm -rf $PWD/cred /mnt/$arg3'
       ],
       'parameters':[
         {'name':"arg1", 'value':accountkey },
         {'name':"arg2", 'value':accountname },
         {'name':"arg3", 'value':sharename }
       ]
  }
 try:
  poller = client.virtual_machines.run_command(
        rgName,
        vmName,
        run_command_parameters
   )
 except:
  print('We will wait 2 minutes before retry')
  time.sleep(120)
  try:
   poller = client.virtual_machines.run_command(
         rgName,
         vmName,
         run_command_parameters
    )
  except: 
   print('Still lock: we quit...')
   return 99
 result = poller.result()
 file_service = FileService(account_name=accountname, account_key=accountkey)
 file_service.get_file_to_path(sharename, None, 'extracts','extracts')
 myFile = open("extracts","r")
 for line in myFile:
  if "." in line.split(':')[1]:
   url = "https://"+(line.split(':')[1]).rstrip()
   if checkUrl:
    rc = checkUrl(url)
   else:
    rc = 'No test'
   print(url) 
   listUrl.append({'Url':url,'Branch':branch,'Country':location,\
                    'Domain 1':subscription['name'],'Domain 2':line.split(':')[0],'Application':'Unknown',\
                    'Criticity':env,'Other comments':"NGINX:"+vmName,\
                    'Scanzone':'internet','rc':rc} )
 myFile.close()
 return listUrl

def scanAthena(listSub,nginxList,azure_credential,SUBSCRIPTION_ID_pub,rgname_pub, accountname_pub,container_pub,SUBSCRIPTION_ID_temp,rgname_temp, accountname_temp, sharename_temp, checkUrl):
 """get  All url from Nginx vm, appserv, appgw , generate excel file and push it on blob container"""
 fileName=(datetime.now()).strftime("%Y%m%d%H%M%S")+"athena.xlsx"
 targetFileName="athena/"+fileName
 allSub=[]


 for nginx in nginxList:
     #getAllUrlNginx(credentials, subscription, rgName, vmName, SUBSCRIPTION_ID, rgname, accountname):
    listUrls=getAllUrlNginx(azure_credential, \
        next(subscription for subscription in \
        listSub if subscription['id'] == nginx['subscription_id']),\
             nginx['rgName'], nginx['vmName'],SUBSCRIPTION_ID_temp,rgname_temp, accountname_temp,sharename_temp,checkUrl)
    allSub+=listUrls

 storage_client = StorageManagementClient(azure_credential,SUBSCRIPTION_ID_pub)
 storage_keys = storage_client.storage_accounts.list_keys(rgname_pub, accountname_pub)
 storage_keys = {v.key_name: v.value for v in storage_keys.keys}
 accountkey = storage_keys['key1']
 for subscription in listSub:
  print("==="+subscription['name']+"===")
  print("===WEB APP===")
  listUrls = getAllUrlAppServ(azure_credential, subscription,checkUrl)
  allSub+=listUrls
  print("===APP GW===")
  listUrls = getAllUrlAppGw(azure_credential, subscription, checkUrl )
  allSub+=listUrls
 generateXlsxFromList(headers, allSub, fileName)
 uploadFile2Blob(accountname_pub, accountkey, container_pub,targetFileName,fileName)

def listDictToHtmlTable(listDict):
 """return string containing html code for table"""
 result='<table>'
 if len(listDict) > 0:
  result += '<thead><tr>'
  for key in listDict[0]:
   result += '<th>'+str(key)+'</th>'
  result += '</tr></thead><tbody>'
  for item in listDict:
   result += '<tr>'
   for key  in item:
    result += '<td>'+str(item[key])+'</td>'
   result += '</tr>'
  result += '</tbody>'
 result += '</table>'
 return result
