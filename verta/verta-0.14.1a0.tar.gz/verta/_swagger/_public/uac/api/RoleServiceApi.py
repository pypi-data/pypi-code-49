# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class RoleServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def deleteRole(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/role/deleteRole", __query, body)

  def deleteRoleBinding(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/role/deleteRoleBinding", __query, body)

  def getBindingRoleById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/role/getRoleBindingById", __query, body)

  def getRoleBindingByName(self, name=None, scope_org_id=None, scope_team_id=None):
    __query = {
      "name": client.to_query(name),
      "scope.org_id": client.to_query(scope_org_id),
      "scope.team_id": client.to_query(scope_team_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/role/getRoleBindingByName", __query, body)

  def getRoleById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/role/getRoleById", __query, body)

  def getRoleByName(self, name=None, scope_org_id=None, scope_team_id=None):
    __query = {
      "name": client.to_query(name),
      "scope.org_id": client.to_query(scope_org_id),
      "scope.team_id": client.to_query(scope_team_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/role/getRoleByName", __query, body)

  def listRoleBindings(self, entity_id=None, scope_org_id=None, scope_team_id=None):
    __query = {
      "entity_id": client.to_query(entity_id),
      "scope.org_id": client.to_query(scope_org_id),
      "scope.team_id": client.to_query(scope_team_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/role/listRoleBindings", __query, body)

  def listRoles(self, scope_org_id=None, scope_team_id=None):
    __query = {
      "scope.org_id": client.to_query(scope_org_id),
      "scope.team_id": client.to_query(scope_team_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/role/listRoles", __query, body)

  def setRole(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/role/setRole", __query, body)

  def setRoleBinding(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/role/setRoleBinding", __query, body)
