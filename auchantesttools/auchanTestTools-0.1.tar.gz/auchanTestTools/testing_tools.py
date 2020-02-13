import pysftp
import os
import fnmatch
import shutil
from subprocess import Popen,PIPE
ERROR_CODE=-1
class TestTools:
    def putToSFTP(self,host,port,remote,login,password,privateKey,mask,local):
        try:
            sftp = pysftp.Connection(host=host,port=port, username=login, password=password,private_key=privateKey)
        except Exception as ex:
            return ERROR_CODE,ex
        else:
            with sftp.cd(remote):  # temporarily cd to remote
                for file in os.listdir(local):
                    if(fnmatch.fnmatch(file,mask)):
                        sftp.put(remotepath=remote+"/"+file,localpath=local+"/"+file)  # upload to remote
            return 0, None

    def getFromSFTP(self,host,port,remote,login,password,privateKey,mask,local):
        try:
            sftp = pysftp.Connection(host=host,port=port, username=login, password=password,private_key=privateKey)
        except Exception as ex:
            return ERROR_CODE,ex
        else:
            for file in sftp.listdir(remote):
                if (fnmatch.fnmatch(file, mask)):
                    sftp.get(remotepath=remote + "/" + file, localpath=local + "/" + file)
            return 0,None


    def runTalendJob(self,scriptpath):
        if (shutil.which('java') is None): # check if java executable found in PATH
            print("Add path to java executable to PATH")
            return None
        my_env = os.environ.copy()
        p = Popen(scriptpath,env=my_env,stdout=PIPE,stderr=PIPE)
        stdout, stderr = p.communicate()
        if(stderr is b""):
            return 0,stdout.decode("utf-8"),None
        else:
            return ERROR_CODE, stdout.decode("utf-8"), stderr.decode("utf-8")