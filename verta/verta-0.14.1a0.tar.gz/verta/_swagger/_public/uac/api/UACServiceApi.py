# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UACServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def createUser(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/uac/createUser", __query, body)

  def deleteUser(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/uac/deleteUser", __query, body)

  def getCurrentUser(self, ):
    __query = {
    }
    body = None
    return self.client.request("GET", self.base_path + s"/uac/getCurrentUser", __query, body)

  def getUser(self, user_id=None, email=None, username=None):
    __query = {
      "user_id": client.to_query(user_id),
      "email": client.to_query(email),
      "username": client.to_query(username)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/uac/getUser", __query, body)

  def getUsers(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/uac/getUsers", __query, body)

  def updateUser(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/uac/updateUser", __query, body)
