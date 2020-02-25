#############################################################
#
#  Author: Sebastian Maurice, PhD
#  Copyright by Sebastian Maurice 2018
#  All rights reserved.
#  Email: Sebastian.maurice@otics.ca
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
from urllib.parse import urljoin
    
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
    if '_nlpclassify' not in pkey:
      theinputdata=theinputdata.replace(",",":")
    else:  
      buf2 = re.sub('[^a-zA-Z0-9 \n\.]', '', theinputdata)
      buf2=buf2.replace("\n", "").strip()
      buf2=buf2.replace("\r", "").strip()
      theinputdata=buf2
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

def uploadcsvfortraining(thefile,username,passw,autofeature,removeoutliers,hasseasonality,dependentvariable,company,email,url,summer,winter,shoulder,trainingpercentage,retrainingdays,retraindeploy,shuffle,theserverlocalname):

   rn=0
   tstr=''

   if len(thefile)>0:
       with open(thefile, 'r',encoding='utf-8') as f:
         reader = csv.reader(f)
         for row in reader:
           row = ",".join(row)
           tstr = tstr + str(row) + '\n'
           rn=rn+1
       head, fname = os.path.split(thefile)    
   elif len(theserverlocalname)>0:
       tstr=''
       fname=theserverlocalname
   else:
       return "ERROR: Must specify a local file, or a file in the server."
       
   
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

def nlp(username,passw,company,email,url,buffer,theserverfolder='',detail=20,maxkeywords=10):
    isurl=0
    print("Please wait..this could take several minutes")
    if len(buffer)>0:
        if validators.url(buffer):
            isurl=1
        else:
            isurl=0
        try:    
            if os.path.isfile(buffer):  #pdf
                filename, file_extension = os.path.splitext(buffer)
                flower=file_extension.lower()
                bn=os.path.basename(buffer)
                if flower=='.pdf':         
                   files = {'file': open(buffer, 'rb')}
                elif flower=='.txt':
                   files = {'file': open(buffer, 'r')}               
                data = {'mode':'nlp1', 'username':username, 'password':passw,'company':company,'email':email,'localname':bn,'theserverfolder':theserverfolder,'fvalue': detail,'maxkeywords': maxkeywords}
                r = requests.post(url, data=data, files=files)
            elif isurl==1:  #url
                data = {'mode':'nlp2', 'username':username, 'password':passw,'company':company,'email':email,'localname':buffer,'fvalue': detail,'maxkeywords': maxkeywords}
                r = requests.post(url, data=data)
            else: #paste text
                data = {'mode':'nlp3', 'username':username, 'password':passw,'company':company,'email':email,'localname':buffer,'fvalue': detail,'maxkeywords': maxkeywords}
                r = requests.post(url, data=data)
        except Exception as e:
            try:
              data = {'mode':'nlp3', 'username':username, 'password':passw,'company':company,'email':email,'localname':buffer,'fvalue': detail,'maxkeywords': maxkeywords}
              r = requests.post(url, data=data)
            except Exception as e:
              return r.text
    elif len(theserverfolder)>0:
           data = {'mode':'nlp1', 'username':username, 'password':passw,'company':company,'email':email,'localname':buffer,'theserverfolder':theserverfolder,'fvalue': detail,'maxkeywords': maxkeywords}
           r = requests.post(url, data=data)
        
    return r.text

def nlpaudiovideo(username,passw,company,email,maads_rest_url,thefile='',theserverfolder='',duration=-1,offset=0):   
    print("Please wait..this could take several minutes")
    if len(thefile)>0:
      files = {'file': open(thefile, 'rb')}
      data = {'mode':'nlpaudiovideo', 'username':username, 'password':passw,'company':company,'email':email,'localname':thefile,'thefolder': theserverfolder,'duration':duration,'offset':offset}
      r = requests.post(maads_rest_url, data=data, files=files)
    elif len(theserverfolder)>0:
      data = {'mode':'nlpaudiovideo', 'username':username, 'password':passw,'company':company,'email':email,'localname':thefile,'thefolder': theserverfolder,'duration':duration,'offset':offset}
      r = requests.post(maads_rest_url, data=data)
    else:
        return "ERROR: Please choose a file or server folder"
    return r.text

def nlpocr(username,passw,company,email,maads_rest_url,thefile='',theserverfolder=''):
    print("Please wait..this could take several minutes")
    if len(thefile)>0:
      files = {'file': open(thefile, 'rb')}
      data = {'mode':'nlpocr', 'username':username, 'password':passw,'company':company,'email':email,'localname':thefile,'thefolder': theserverfolder}
      r = requests.post(maads_rest_url, data=data, files=files)
    elif len(theserverfolder)>0:
      data = {'mode':'nlpocr', 'username':username, 'password':passw,'company':company,'email':email,'localname':thefile,'thefolder': theserverfolder}
      r = requests.post(maads_rest_url, data=data)
    else:
        return "ERROR: Please choose a file or server folder"
    return r.text
    
#csvfile,iscategory,maads_rest_url,trainingpercentage,retrainingdays,retraindeploy
def nlpclassify(username,passw,company,email,iscategory,maads_rest_url,thefile='',theserverlocalname='',csvonly=0,trainingpercentage=75,retrainingdays=0,retraindeploy=0):
    print("Please wait..this could take several minutes")
    tstr=''
    rn=0
    if len(thefile)>0:
        with open(thefile, 'r', encoding='utf8') as f:
         reader = csv.reader(f)
         for row in reader:
           #print(row)  
           rowstr = ",".join(row)
          # print(len(row))
           if len(row)>2:
               print("Ignored ROW %d: Improperly formatted CSV.  You have too many commas separating your data." % (rn+1))
           elif len(row)==2 and len(row[0])>1 and len(row[1])>1:
               buf=row[1]
               buf=buf.replace(","," ")
               buf2 = re.sub('[^a-zA-Z0-9 \n\.]', '', buf)
               buf2=buf2.replace("\n", "").strip()
               buf2=buf2.replace("\r", "").strip()
               row[1]=buf2

               buf=row[0]
               buf=buf.replace(","," ")
               buf2 = re.sub('[^a-zA-Z0-9 \n\.]', '', buf)
               buf2=buf2.replace("\n", "").strip()
               buf2=buf2.replace("\r", "").strip()

               row[0]=buf2
               rowstr = ",".join(row)
               tstr = tstr + str(rowstr) + '\n'
           else:
               print("Ignored ROW %d: Improperly formatted CSV." % (rn+1))
           rn=rn+1
        base=os.path.basename(thefile)
        filename=os.path.splitext(base)[0]
    elif len(theserverlocalname)>0:
        tstr=''
        filename=theserverlocalname
    else:
        return "ERROR: Must specify a local file, or a file in the server"
        
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
        'csvonly':csvonly,           
    #'dependentvariable': dependentvariable,
        'title':'Do NLP Classify'
      }

    r = requests.post(maads_rest_url, files)
    msg = r.text

    if csvonly:
      localname=username + '_' + filename + '_nlpclassify_' + str(iscategory) + '_.csv'
      baseurl=urljoin(maads_rest_url,'/')
      url = "%smaadsweb/csvtemps/%s" % (baseurl,localname)
      #localname="%s" % (localname)
      try:
        urllib.request.urlretrieve(url, localname)
        return msg
      except Exception as e:
        return "ERROR retrieving NLP CSV: %s" % e

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
      urllib.request.urlretrieve(url, localname)
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
