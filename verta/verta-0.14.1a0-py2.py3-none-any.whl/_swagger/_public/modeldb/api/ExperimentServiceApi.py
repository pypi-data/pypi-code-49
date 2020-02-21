# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ExperimentServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addAttribute(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/addAttribute", __query, body)

  def addExperimentAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/addExperimentAttributes", __query, body)

  def addExperimentTag(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/addExperimentTag", __query, body)

  def addExperimentTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/addExperimentTags", __query, body)

  def createExperiment(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/createExperiment", __query, body)

  def deleteArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment/deleteArtifact", __query, body)

  def deleteExperiment(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment/deleteExperiment", __query, body)

  def deleteExperimentAttributes(self, id=None, attribute_keys=None, delete_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "delete_all": client.to_query(delete_all)
    }
    body = None
    return self.client.request("DELETE", self.base_path + s"/experiment/deleteExperimentAttributes", __query, body)

  def deleteExperimentTag(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment/deleteExperimentTag", __query, body)

  def deleteExperimentTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment/deleteExperimentTags", __query, body)

  def deleteExperiments(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment/deleteExperiments", __query, body)

  def findExperiments(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/findExperiments", __query, body)

  def getArtifacts(self, id=None, key=None):
    __query = {
      "id": client.to_query(id),
      "key": client.to_query(key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment/getArtifacts", __query, body)

  def getExperimentAttributes(self, id=None, attribute_keys=None, get_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "get_all": client.to_query(get_all)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment/getExperimentAttributes", __query, body)

  def getExperimentById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment/getExperimentById", __query, body)

  def getExperimentByName(self, name=None, project_id=None):
    __query = {
      "name": client.to_query(name),
      "project_id": client.to_query(project_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment/getExperimentByName", __query, body)

  def getExperimentCodeVersion(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment/getExperimentCodeVersion", __query, body)

  def getExperimentTags(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment/getExperimentTags", __query, body)

  def getExperimentsInProject(self, project_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "project_id": client.to_query(project_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment/getExperimentsInProject", __query, body)

  def getUrlForArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/getUrlForArtifact", __query, body)

  def logArtifacts(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/logArtifacts", __query, body)

  def logExperimentCodeVersion(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/logExperimentCodeVersion", __query, body)

  def updateExperimentDescription(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/updateExperimentDescription", __query, body)

  def updateExperimentName(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/updateExperimentName", __query, body)

  def updateExperimentNameOrDescription(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment/updateExperimentNameOrDescription", __query, body)
