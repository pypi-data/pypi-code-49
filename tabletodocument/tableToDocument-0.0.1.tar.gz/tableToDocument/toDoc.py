import os
import word
import excel
import pdf
import tex
import googleDoc
import dropboxDoc
import locale

supportedEncodings = ['ascii','utf-8','latin-1']

def getDefaultEncoding():
    return locale.getpreferredencoding()
def docExists(path):
    return os.path.exists(path)
def isDocAccessible(path):
    return os.access(path,os.W_OK)
def isDocFile(path):
    return os.path.isfile(path)
def validFlag(flag):
    if type(flag)==type(0) and flag>=0:
        return True
    if type(flag)==type('a') and (flag=='a' or flag=='b'):
        return True
    return False
def overflowError(table):
    return -1
def errorHandler(type_of_possible_error,path):
    if type_of_possible_error == 0:
        return
    if type_of_possible_error == 1:
        print("Access denied for writing to the file ".join(str(path)))
    if type_of_possible_error == 2:
        print("Document "+str(path)+" does not exist.You should provide -c flag to create it")
    if type_of_possible_error == 3:
        print("The document to be written is not a valid document")
    if type_of_possible_error == 4:
        print("Unknown flag")

class toWord:
    def __init__(self,path,flag,dataType):
        self.path = path
        self.flag = flag
        self.dataType = dataType
        errorHandler(word.write(self),path)

class toExcel:
    def __init__(self,path,flag,dataType):
        self.path = path
        self.flag = flag
        self.dataType = dataType

class toTex:
    def __init__(self,path,flag,dataType):
        self.path = path
        self.flag = flag
        self.dataType = dataType
        errorHandler(tex.write(self),path)

class toPdf:
    def __init__(self,path,flag,to_word_and_then_to_pdf,dataType):
        self.path = path
        self.flag = flag
        self.dataType = dataType
        pdf.write(self)

class toGoogleDoc:
    def __init__(self,url,flag,dataType,credentials):
        self.url = url
        self.flag = flag
        self.dataType = dataType
        self.credentials = credentials

class toDropboxDoc:
    def __init__(self,url,flag,dataType,credentials):
        self.url = url
        self.flag = flag
        self.dataType = dataType
        self.credentials = credentials
