# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class DatasetServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addDatasetAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/addDatasetAttributes", __query, body)

  def addDatasetTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/addDatasetTags", __query, body)

  def createDataset(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/createDataset", __query, body)

  def deleteDataset(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/dataset/deleteDataset", __query, body)

  def deleteDatasetAttributes(self, id=None, attribute_keys=None, delete_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "delete_all": client.to_query(delete_all)
    }
    body = None
    return self.client.request("DELETE", self.base_path + s"/dataset/deleteDatasetAttributes", __query, body)

  def deleteDatasetTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/dataset/deleteDatasetTags", __query, body)

  def deleteDatasets(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/dataset/deleteDatasets", __query, body)

  def findDatasets(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/findDatasets", __query, body)

  def getAllDatasets(self, page_number=None, page_limit=None, ascending=None, sort_key=None, workspace_name=None):
    __query = {
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key),
      "workspace_name": client.to_query(workspace_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset/getAllDatasets", __query, body)

  def getDatasetAttributes(self, id=None, attribute_keys=None, get_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "get_all": client.to_query(get_all)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset/getDatasetAttributes", __query, body)

  def getDatasetById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset/getDatasetById", __query, body)

  def getDatasetByName(self, name=None, workspace_name=None):
    __query = {
      "name": client.to_query(name),
      "workspace_name": client.to_query(workspace_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset/getDatasetByName", __query, body)

  def getDatasetTags(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset/getDatasetTags", __query, body)

  def getExperimentRunByDataset(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/getExperimentRunByDataset", __query, body)

  def getLastExperimentByDatasetId(self, dataset_id=None):
    __query = {
      "dataset_id": client.to_query(dataset_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset/getLastExperimentByDatasetId", __query, body)

  def setDatasetVisibility(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/setDatasetVisibility", __query, body)

  def setDatasetWorkspace(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/setDatasetWorkspace", __query, body)

  def updateDatasetAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/updateDatasetAttributes", __query, body)

  def updateDatasetDescription(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/updateDatasetDescription", __query, body)

  def updateDatasetName(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset/updateDatasetName", __query, body)
