#!/usr/bin/env python2.7
#coding:utf-8

import sbrowser
import subprocess
import os
import hjson
import codecs
import shutil

class Publisher:

  def __init__(self, path):
    self.path = path
    self.__fullPath = self._fullPath(path)
    self.__name = self._repositoryName(path)
    self.__repositoryName = self._repositoryName(path)
    self.__username = self._userName()
    self.__properties = self._properties()

  def _properties (self):
    result = None
    path = os.path.join(self.__fullPath, "project.properties")
    if os.path.isfile(path):
      fp = codecs.open(path, mode='r', encoding='utf-8')
      result = hjson.load(fp)
    return result

  def _saveProperties (self):
    if self.__properties is not None:
      path = os.path.join(self.__fullPath, "project.properties")
      fp = codecs.open(path, mode='w', encoding='utf-8')
      hjson.dump(self.__properties, fp)

  def _fullPath (self, path):
    result = None
    if path.endswith(os.path.sep):
      path = path[0:-1]
    result = os.path.join(os.getcwd(), path) if not path.startswith(os.path.sep) else path
    return result

  def _repositoryName (self, path):
    result = None
    if path.endswith(os.path.sep):
      path = path[0:-1]
    result = path.split(os.path.sep)[-1]
    return result
  
  def _userName (self):
    result = None
    result = self._userName_file()
    if result is None or len(result) <= 0:
      result = self._userName_github()
    return result
  
  def _userName_file (self):
    result = None
    path = os.path.join(self.__fullPath, "project.properties")
    if os.path.isfile(path):
      fp = codecs.open(path, mode='r', encoding='utf-8')
      data = hjson.load(fp)
      result = data['username']
    return result

  def _userName_github (self):
    result = None

    b = sbrowser.Browser()
    b.openUrl("https://github.com/").maximize()
    b.click("//summary[@aria-label='View profile and more']")
    username = b.attr("//a[@role='menuitem'][contains(text(), 'Your profile')]", "href")
    username = username[username.rindex("/")+1:]
    result = username
    print("user = " + username)
    b.close()

    return result
  
  def createRepository (self):
    print("Creating repository " + self.__repositoryName + " ...")
    b = sbrowser.Browser()
    #b.openUrl("https://github.com/tuaplicacionpropia").maximize()
    b.openUrl("https://github.com/new").maximize()
    b.setInput("//input[@name='repository[name]']", self.__repositoryName)
    b.click("//button[contains(text(), 'Create repository')]")
    b.close()
    #b.screenshot()

  def deleteRepository (self):
    url = "https://github.com/" + self.__username + "/" + self.__repositoryName + "/settings"
    b.openUrl(url).maximize()
    #b.click("//summary[@aria-label='View profile and more']")
    b.click("//summary[contains(text(), 'Delete this repository')]")
    b.setInput("//input[@name='verify'][contains(@aria-label, 'to delete this repository')]", self.__username + "/" + self.__repositoryName)
    b.click("//button[contains(text(), 'I understand the consequences, delete this repository')]")
    b.wait()
    b.close()

  def createProject (self):
    self.cfgGit()
    self.createBaseProject()
    self.createRepository()
    if os.path.isdir(os.path.join(self.__fullPath, ".git")):
      self.commit()
    else:
      self.firstCommit()

  def createBaseProject (self):
    print("Creating project ...")
    if not os.path.isdir(self.__fullPath):
      os.mkdir(self.__fullPath)
  
    self.createBaseProject_Readme()
    self.createBaseProject_Properties()
    self.createBaseProject_Src()

  def createBaseProject_Readme (self):
    path = os.path.join(self.__fullPath, "README.md")
    if not os.path.isfile(path):
      f = open(path, "w+")
      f.write("# " + self.__repositoryName)
      f.close()

  def createBaseProject_Src (self):
    path = os.path.join(self.__fullPath, "src")
    if not os.path.isdir(path):
      os.mkdir(path)

  def saveObj (self, path, obj):
    fp = codecs.open(path, mode='w', encoding='utf-8')
    hjson.dump(obj, fp)

  def loadObj (self, path):
    result = None
    fp = codecs.open(path, mode='r', encoding='utf-8')
    result = hjson.load(fp)
    return result

  def createBaseProject_Properties (self):
    path = os.path.join(self.__fullPath, "project.properties")
    if not os.path.isfile(path):
      properties = hjson.OrderedDict()
      properties['name'] = self.__repositoryName
      properties['version'] = "0.0.1"
      properties['repository'] = self.__repositoryName
      properties['username'] = self.__username
      fp = codecs.open(path, mode='w', encoding='utf-8')
      hjson.dump(properties, fp)

  def _cmd (self, cmdArr):
    result = None
    log = True
    cmdStr = ""
    for itemCmd in cmdArr:
      cmdStr += (" " if len(cmdStr) > 0 else "") + itemCmd
    print("Executing command ... " + cmdStr)
    cmdOut = ""
    try:
      #cmdOut = subprocess.check_output(cmdArr, shell=True)                       
      cmdOut = subprocess.check_output(cmdArr)
    except subprocess.CalledProcessError as grepexc:                                                                                                   
      print "error code", grepexc.returncode, grepexc.output    
    #cmdOut = subprocess.check_output(cmdArr)
    if log:
      print cmdOut
    result = cmdOut
    return result

  def cfgGit (self):
    print("Configuring git...")
    #git config --global --unset user.email
    #git config --global --unset user.name
    userName = self._cmd(["git", "config", "--global", "user.name"])
    userEmail = self._cmd(["git", "config", "--global", "user.email"])
    userName = userName.strip() if userName is not None else ""
    userEmail = userEmail.strip() if userEmail is not None else ""
    if len(userName) <= 0 or len(userEmail) <= 0:
      self._cmd(["git", "config", "--global", "user.name", u"\"Jesús María Ramos Saky\""])
      self._cmd(["git", "config", "--global", "user.email", "\"tuaplicacionpropia@gmail.com\""])

  def firstCommit (self):
    print("First commit repository " + self.__repositoryName + " ...")
    os.chdir(self.__fullPath)
  
    self._cmd(["git", "init"])
    self._cmd(["git", "add", "."])
    self._cmd(["git", "commit", "-m", "first commit"])
    self._cmd(["git", "remote", "add", "origin", "https://github.com/" + self.__username + "/" + self.__repositoryName + ".git"])
    self._cmd(["git", "push", "-u", "origin", "master"])
  
  '''
  
git status -s | grep "^D"
  
  
  '''
  def commit (self):
    print("Commit repository " + self.__repositoryName + " ...")
    os.chdir(self.__fullPath)
    
    msgCommit = "" + self.__properties["version"]
    
    self._cmd(["git", "status"])
    self._cmd(["git", "add", "."])
    self._cmd(["git", "commit", "-m", msgCommit])
    self._cmd(["git", "remote", "add", "origin", "https://github.com/" + self.__username + "/" + self.__repositoryName + ".git"])
    self._cmd(["git", "push", "-u", "origin", "master"])
  
  def update (self):
    print("Updating project ...")
    self.updateVersion()
    self.commit()
  
  #1.4.99
  #1.04.99
  def updateVersion (self):
    print("Updating version ...")
    version = self.__properties["version"]
    
    array = version.split(".")
    for i in range(len(array) - 1, -1, -1):
      num = int(array[i]) + 1
      nNext = (num >= 100)
      
      num = num if not nNext else 0

      numTxt = str(num)
      if i > 0:
        numTxt = ("0" if num < 10 else "") + numTxt
      array[i] = numTxt

      if not nNext:
        break
    
    version = ""
    for item in array:
      version += ("." if len(version) > 0 else "") + item
    
    print("Version: " + version)
    self.__properties["version"] = version
    self._saveProperties()

  def updatePyPi (self):
	#rm -v dist/*
    distDir = os.path.join(self.__fullPath, dist)
    if os.path.isdir(distDir):
      shutil.rmtree(distDir)
    
    os.chdir(self.__fullPath)

    #python2.7 setup.py sdist bdist_wheel
    self._cmd(['python', 'setup.py', 'sdist', 'bdist_wheel'])
    
    #twine upload dist/*
    self._cmd(['twine', 'upload', 'dist/*'])

  #sudo pip2.7 install --upgrade findfaces
  def installOnSystem (self):
    cmd = subprocess.Popen(['sudo','pip', 'install', '--upgrade', self.__repositoryName])
    output = cmd2.stdout.read().decode()
    print(output)

  def publish (self):
    pass


if True and __name__ == '__main__':
  #b = sbrowser.Browser()
  #b.openUrl("https://github.com/").maximize()
  github = Publisher("/home/jmramoss/Descargas/jopetas11")
  #github.createProject()

  #github.update()
  #for i in range(150):
  #  github.updateVersion()
  github.update()

  #createRepository(repository)
  #firstCommit(repository)
  #deleteRepository(repository)
