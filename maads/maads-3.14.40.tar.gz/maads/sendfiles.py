#############################################################
#
#  Author: Sebastian Maurice, PhD
#  Copyright by Sebastian Maurice 2018
#  All rights reserved.
#  Email: Sebastian.maurice@gmail.com
#
#############################################################

import json, urllib
import requests
import csv
import os
import imp
import re
import urllib.request
import asyncio
import validators

    
async def tcp_echo_client(message, loop,host,port):
    reader, writer = await asyncio.open_connection(host, port,
                                                   loop=loop)

    mystr=str.encode(message)
    writer.write(mystr)
    data = await reader.read(2096)
    prediction=("%s" % (data.decode()))
    writer.close()
    
    return prediction

def hyperpredictions(host,port,username,password,company,email,pkey,theinputdata):
    theinputdata=theinputdata.replace(",",":")
    value="%s,%s,%s,%s,%s,[%s]" % (username,password,company,email,pkey,theinputdata)
    loop = asyncio.get_event_loop()
    val=loop.run_until_complete(tcp_echo_client(value, loop,host,port))
    return val

def returndata(buffer,label):
      #print("LABEL: %s" % (label))
      if label=='PKEY:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]
      elif label=='ALGO0:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         #print(listvalues)
         val=[s for s in listvalues if label in s]
         #print(val)
         rval=val[0].split(':')[1]
      elif label=='ACCURACY0:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]
      elif label=='SEASON0:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]         

      elif label=='ALGO1:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         #print(listvalues)
         val=[s for s in listvalues if label in s]
         #print(val)
         rval=val[0].split(':')[1]
      elif label=='ACCURACY1:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]
      elif label=='SEASON1:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]         
      elif label=='ALGO2:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         #print(listvalues)
         val=[s for s in listvalues if label in s]
         #print(val)
         rval=val[0].split(':')[1]
      elif label=='ACCURACY2:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]
      elif label=='SEASON2:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]         
      elif label=='ALGO3:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         #print(listvalues)
         val=[s for s in listvalues if label in s]
         #print(val)
         rval=val[0].split(':')[1]
      elif label=='ACCURACY3:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]
      elif label=='SEASON3:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]         
         
      elif label=='DATA:':
         val=""
         pattern = re.compile('\s*[:,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         #print(listvalues)
         fdate=listvalues[1]
         inp=listvalues[2]
         pred=float(listvalues[3])
         acc=float(listvalues[4])
         rval=[fdate,inp,pred,acc]
      else:
         return "%s not found" % (label)
          
      return rval

def retraining(pkey,thefile,username,passw,autofeature,removeoutliers,hasseasonality,dependentvariable,company,email,url,summer,winter,shoulder,trainingpercentage,retrainingdays,retraindeploy):

   rn=0
   tstr=''
   
   with open(thefile, 'r') as f:
     reader = csv.reader(f)
     for row in reader:
       row = ",".join(row)
       tstr = tstr + str(row) + '\n'
       rn=rn+1
       
   head, fname = os.path.split(thefile)
   print("Please wait...training can take several minutes.")
   
   files = {'file': tstr,
    'mode':-1,        
    'type':'CSV',
    'filename':fname,
    'username': username,
    'password': passw,
    'rowcount': rn,
    'autofeature': autofeature,
    'removeoutliers': removeoutliers,
    'hasseasonality': hasseasonality,
    'company': company,
    'email': email,            
    'dependentvariable': dependentvariable,
    'title':'File Upload for Training',
    'summer':summer,
    'winter':winter,
    'shoulder':shoulder,
    'trainingpercentage':trainingpercentage,
    'retrainingdays':retrainingdays,
    'retraindeploy':retraindeploy,
    'pkey':pkey
            
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg

def uploadcsvfortraining(thefile,username,passw,autofeature,removeoutliers,hasseasonality,dependentvariable,company,email,url,summer,winter,shoulder,trainingpercentage,retrainingdays,retraindeploy,shuffle):

   rn=0
   tstr=''
   
   with open(thefile, 'r') as f:
     reader = csv.reader(f)
     for row in reader:
       row = ",".join(row)
       tstr = tstr + str(row) + '\n'
       rn=rn+1
       
   head, fname = os.path.split(thefile)
   print("Please wait...training can take several minutes.")
   
   files = {'file': tstr,
    'mode':0,        
    'type':'CSV',
    'filename':fname,
    'username': username,
    'password': passw,
    'rowcount': rn,
    'autofeature': autofeature,
    'removeoutliers': removeoutliers,
    'hasseasonality': hasseasonality,
    'company': company,
    'email': email,            
    'dependentvariable': dependentvariable,
    'title':'File Upload for Training',
    'summer':summer,
    'winter':winter,
    'shoulder':shoulder,
    'trainingpercentage':trainingpercentage,
    'retrainingdays':retrainingdays,
    'retraindeploy':retraindeploy,
    'shuffle':shuffle
            
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg

def getpredictions(attr,pkey,thefile,username,passw,company,email,url):

   rn=0
   tstr=''

   
   if attr==0:
      tstr=thefile
         
      files = {'file': tstr,
        'mode':1,        
        'type':'CSV',
        'pkey':pkey,            
        'username': username,
        'password': passw,
    #'rowcount': rn,
    #'autofeature': autofeature,
    #'removeoutliers': removeoutliers,
    #'hasseasonality': hasseasonality,
       'company': company,
       'email': email,            
    #'dependentvariable': dependentvariable,
       'title':'Do Predictions'
      }

   #print(files)
      r = requests.post(url, files)
      msg = r.text
   #print ("Message %s" % (msg))
   
      return msg


def dolistkeys(username,passw,company,email,url):

   rn=0
   tstr=''

   
   files = {
      'mode':2,        
      'type':'CSV',        
      'username': username,
      'password': passw,
      'company': company,
      'email': email,              
     'title':'Do List keys'
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg

def dolistkeyswithkey(username,passw,company,email,pkey,url):

   rn=0
   tstr=''

   
   files = {
      'mode':3,
      'pkey':pkey,        
      'type':'CSV',        
      'username': username,
      'password': passw,
      'company': company,
      'email': email,              
     'title':'Do List keys with Key'
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg

def dodeletewithkey(username,passw,company,email,pkey,url):

   rn=0
   tstr=''

   
   files = {
      'mode':4,
      'pkey':pkey,        
      'type':'CSV',        
      'username': username,
      'password': passw,
      'company': company,
      'email': email,              
     'title':'Do Delete with Key'
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg



def getpicklezip(username,passw,company,email,pkey,url,localfolder):

    url = "%s/prodfiles/%s_DEPLOYTOPROD.zip" % (url,pkey)
    localname="%s/%s_DEPLOYTOPROD.zip" % (localfolder,pkey)
    urllib.request.urlretrieve(url, localname)
    #print(url)
    return "file retrieved"


def sendpicklezip(username,passw,company,email,pkey,url,localname):
    bn=os.path.basename(localname)
    data = {'mode':'uploads', 'username':username, 'password':passw,'company':company,'email':email,'pkey':pkey}
    
    files = {'file': open(localname, 'rb')}
    r = requests.post(url, data=data, files=files)
    return r.text
    
def deploytoprod(username,passw,company,email,pkey,url,localname='',ftpserver='',ftpuser='',ftppass=''):

    data = {'mode':'deploy', 'username':username, 'password':passw,'company':company,'email':email,'localname':localname,'pkey':pkey,'ftpserver':ftpserver,'ftpuser':ftpuser,'ftppass':ftppass}

    #print(prodserverurl)

    
    if len(localname)>0:
        bn=os.path.basename(localname)
        data = {'mode':'deploy', 'username':username, 'password':passw,'company':company,'email':email,'localname':bn,'pkey':pkey,'ftpserver':ftpserver,'ftpuser':ftpuser,'ftppass':ftppass}        
        files = {'file': open(localname, 'rb')}
        r = requests.post(url, data=data, files=files)
    else:
        bn="%s_DEPLOYTOPROD.zip" % (pkey)
        data = {'mode':'deploy', 'username':username, 'password':passw,'company':company,'email':email,'localname':localname,'pkey':pkey,'ftpserver':ftpserver,'ftpuser':ftpuser,'ftppass':ftppass}                
        r = requests.post(url, data=data)
 #   print(r.text)    
    return r.text

def nlp(username,passw,company,email,buffer,url,detail=20):
    isurl=0

    if validators.url(buffer):
        isurl=1
    else:
        isurl=0
        
    if os.path.isfile(buffer):  #pdf
        filename, file_extension = os.path.splitext(buffer)
        flower=file_extension.lower()
        bn=os.path.basename(buffer)
        if flower=='.pdf':         
           files = {'file': open(buffer, 'rb')}
        elif flower=='.txt':
           files = {'file': open(buffer, 'r')}               
        data = {'mode':'nlp1', 'username':username, 'password':passw,'company':company,'email':email,'localname':bn,'fvalue': detail}
        r = requests.post(url, data=data, files=files)
    elif isurl==1:  #url
        data = {'mode':'nlp2', 'username':username, 'password':passw,'company':company,'email':email,'localname':buffer,'fvalue': detail}
        r = requests.post(url, data=data)
    else: #paste text
        data = {'mode':'nlp3', 'username':username, 'password':passw,'company':company,'email':email,'localname':buffer,'fvalue': detail}
        r = requests.post(url, data=data)
    return r.text

#csvfile,iscategory,maads_rest_url,trainingpercentage,retrainingdays,retraindeploy
def nlpclassify(username,passw,company,email,thefile,iscategory,maads_rest_url,trainingpercentage=75,retrainingdays=0,retraindeploy=0):

    tstr=''
    rn=0
    with open(thefile, 'r') as f:
     reader = csv.reader(f)
     for row in reader:
       row = ",".join(row)
       tstr = tstr + str(row) + '\n'
       rn=rn+1
    base=os.path.basename(thefile)
    filename=os.path.splitext(base)[0]
    
    files = {'file': tstr,
        'mode':'nlpclassify',        
        'type':'CSV',
        'iscategory':iscategory,            
        'username': username,
        'password': passw,
        'trainingpercentage': trainingpercentage,
        'retrainingdays': retrainingdays,
        'retraindeploy': retraindeploy,
        'company': company,
        'email': email,
        'filename':filename,      
    #'dependentvariable': dependentvariable,
        'title':'Do NLP Classify'
      }

    r = requests.post(maads_rest_url, files)
    msg = r.text
   
    return msg

def genpdf(username,passw,company,email,maads_rest_url,pkey,urltomaadsserver,savetofolder):
    files = {'mode':'genpdf',        
        'username': username,
        'password': passw,
        'company': company,
        'email': email,
        'pkey':pkey     
      }

    r = requests.post(maads_rest_url, files)
    msg = r.text
# retrieve file
    try:
      url = "%s/maadsweb/pdfreports/%s.pdf" % (urltomaadsserver,pkey)
      localname="%s/%s.pdf" % (savetofolder,pkey)
      urllib.request.urlretrieve(url, savetofolder)
      return "PDF retrieved: %s" % localname
    except Exception as e:  
      return "ERROR: Retrieving PDF: %s" % e 

def algoinfo(username,passw,company,email,maads_rest_url,pkey):
    files = {'mode':'algoinfo',        
        'username': username,
        'password': passw,
        'company': company,
        'email': email,
        'pkey':pkey     
      }

    r = requests.post(maads_rest_url, files)
    msg = r.text
   
    return msg

def featureselectionjson(username,passw,company,email,maads_rest_url,pkey):
    files = {'mode':'featureselection',        
        'username': username,
        'password': passw,
        'company': company,
        'email': email,
        'pkey':pkey     
      }

    r = requests.post(maads_rest_url, files)
    msg = r.text
   
    return msg
    
#getpicklezip('demouser','demouser0828','OTICS','sebastian.maurice@otics.ml','demouser_acnstocksdatatest_csv','http://www.otics.ca/maadsweb','c:/maads')
