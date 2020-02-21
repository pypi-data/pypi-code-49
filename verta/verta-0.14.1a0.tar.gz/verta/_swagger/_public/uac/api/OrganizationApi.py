# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class OrganizationApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addUser(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/organization/addUser", __query, body)

  def deleteOrganization(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/organization/deleteOrganization", __query, body)

  def getOrganizationById(self, org_id=None):
    __query = {
      "org_id": client.to_query(org_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/organization/getOrganizationById", __query, body)

  def getOrganizationByName(self, org_name=None):
    __query = {
      "org_name": client.to_query(org_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/organization/getOrganizationByName", __query, body)

  def getOrganizationByShortName(self, short_name=None):
    __query = {
      "short_name": client.to_query(short_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/organization/getOrganizationByShortName", __query, body)

  def listMyOrganizations(self, ):
    __query = {
    }
    body = None
    return self.client.request("GET", self.base_path + s"/organization/listMyOrganizations", __query, body)

  def listTeams(self, org_id=None):
    __query = {
      "org_id": client.to_query(org_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/organization/listTeams", __query, body)

  def listUsers(self, org_id=None):
    __query = {
      "org_id": client.to_query(org_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/organization/listUsers", __query, body)

  def removeUser(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/organization/removeUser", __query, body)

  def setOrganization(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/organization/setOrganization", __query, body)
