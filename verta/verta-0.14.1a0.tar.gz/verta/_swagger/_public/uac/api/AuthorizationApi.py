# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class AuthorizationApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def getAllowedEntities(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/authz/getAllowedEntities", __query, body)

  def getAllowedResources(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/authz/getAllowedResources", __query, body)

  def getDireclyAllowedResources(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/authz/getDirectlyAllowedResources", __query, body)

  def getSelfAllowedActionsBatch(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/authz/getSelfAllowedActionsBatch", __query, body)

  def getSelfAllowedResources(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/authz/getSelfAllowedResources", __query, body)

  def getSelfDirectlyAllowedResources(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/authz/getSelfDirectlyAllowedResources", __query, body)

  def isAllowed(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/authz/isAllowed", __query, body)

  def isSelfAllowed(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/authz/isSelfAllowed", __query, body)
