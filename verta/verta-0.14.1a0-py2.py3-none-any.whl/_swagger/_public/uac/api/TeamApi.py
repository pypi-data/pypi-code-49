# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class TeamApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addUser(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/team/addUser", __query, body)

  def deleteTeam(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/team/deleteTeam", __query, body)

  def getTeamById(self, team_id=None):
    __query = {
      "team_id": client.to_query(team_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/team/getTeamById", __query, body)

  def getTeamByName(self, org_id=None, team_name=None):
    __query = {
      "org_id": client.to_query(org_id),
      "team_name": client.to_query(team_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/team/getTeamByName", __query, body)

  def getTeamByShortName(self, org_id=None, short_name=None):
    __query = {
      "org_id": client.to_query(org_id),
      "short_name": client.to_query(short_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/team/getTeamByShortName", __query, body)

  def listMyTeams(self, ):
    __query = {
    }
    body = None
    return self.client.request("GET", self.base_path + s"/team/listMyTeams", __query, body)

  def listUsers(self, team_id=None):
    __query = {
      "team_id": client.to_query(team_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/team/listUsers", __query, body)

  def removeUser(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/team/removeUser", __query, body)

  def setTeam(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/team/setTeam", __query, body)
