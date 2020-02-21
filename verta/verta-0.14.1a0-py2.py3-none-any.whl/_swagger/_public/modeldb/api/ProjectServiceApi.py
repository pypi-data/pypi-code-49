# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ProjectServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addProjectAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/addProjectAttributes", __query, body)

  def addProjectTag(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/addProjectTag", __query, body)

  def addProjectTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/addProjectTags", __query, body)

  def createProject(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/createProject", __query, body)

  def deepCopyProject(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/deepCopyProject", __query, body)

  def deleteArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/project/deleteArtifact", __query, body)

  def deleteProject(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/project/deleteProject", __query, body)

  def deleteProjectAttributes(self, id=None, attribute_keys=None, delete_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "delete_all": client.to_query(delete_all)
    }
    body = None
    return self.client.request("DELETE", self.base_path + s"/project/deleteProjectAttributes", __query, body)

  def deleteProjectTag(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/project/deleteProjectTag", __query, body)

  def deleteProjectTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/project/deleteProjectTags", __query, body)

  def deleteProjects(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/project/deleteProjects", __query, body)

  def findProjects(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/findProjects", __query, body)

  def getArtifacts(self, id=None, key=None):
    __query = {
      "id": client.to_query(id),
      "key": client.to_query(key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getArtifacts", __query, body)

  def getProjectAttributes(self, id=None, attribute_keys=None, get_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "get_all": client.to_query(get_all)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getProjectAttributes", __query, body)

  def getProjectById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getProjectById", __query, body)

  def getProjectByName(self, name=None, workspace_name=None):
    __query = {
      "name": client.to_query(name),
      "workspace_name": client.to_query(workspace_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getProjectByName", __query, body)

  def getProjectCodeVersion(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getProjectCodeVersion", __query, body)

  def getProjectReadme(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getProjectReadme", __query, body)

  def getProjectShortName(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getProjectShortName", __query, body)

  def getProjectTags(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getProjectTags", __query, body)

  def getProjects(self, page_number=None, page_limit=None, ascending=None, sort_key=None, workspace_name=None):
    __query = {
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key),
      "workspace_name": client.to_query(workspace_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getProjects", __query, body)

  def getPublicProjects(self, user_id=None, workspace_name=None):
    __query = {
      "user_id": client.to_query(user_id),
      "workspace_name": client.to_query(workspace_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getPublicProjects", __query, body)

  def getSummary(self, entityId=None):
    __query = {
      "entityId": client.to_query(entityId)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/getSummary", __query, body)

  def getUrlForArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/getUrlForArtifact", __query, body)

  def logArtifacts(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/logArtifacts", __query, body)

  def logProjectCodeVersion(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/logProjectCodeVersion", __query, body)

  def setProjectReadme(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/setProjectReadme", __query, body)

  def setProjectShortName(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/setProjectShortName", __query, body)

  def setProjectVisibility(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/setProjectVisibility", __query, body)

  def setProjectWorkspace(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/setProjectWorkspace", __query, body)

  def updateProjectAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/updateProjectAttributes", __query, body)

  def updateProjectDescription(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/updateProjectDescription", __query, body)

  def updateProjectName(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/project/updateProjectName", __query, body)

  def verifyConnection(self, ):
    __query = {
    }
    body = None
    return self.client.request("GET", self.base_path + s"/project/verifyConnection", __query, body)
