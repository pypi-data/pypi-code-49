# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class DatasetVersionServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addDatasetVersionAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset-version/addDatasetVersionAttributes", __query, body)

  def addDatasetVersionTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset-version/addDatasetVersionTags", __query, body)

  def createDatasetVersion(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset-version/createDatasetVersion", __query, body)

  def deleteDatasetVersion(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/dataset-version/deleteDatasetVersion", __query, body)

  def deleteDatasetVersionAttributes(self, id=None, attribute_keys=None, delete_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "delete_all": client.to_query(delete_all)
    }
    body = None
    return self.client.request("DELETE", self.base_path + s"/dataset-version/deleteDatasetVersionAttributes", __query, body)

  def deleteDatasetVersionTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/dataset-version/deleteDatasetVersionTags", __query, body)

  def deleteDatasetVersions(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/dataset-version/deleteDatasetVersions", __query, body)

  def findDatasetVersions(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset-version/findDatasetVersions", __query, body)

  def getAllDatasetVersionsByDatasetId(self, dataset_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "dataset_id": client.to_query(dataset_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset-version/getAllDatasetVersionsByDatasetId", __query, body)

  def getDatasetVersionAttributes(self, id=None, attribute_keys=None, get_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "get_all": client.to_query(get_all)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset-version/getDatasetVersionAttributes", __query, body)

  def getDatasetVersionById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset-version/getDatasetVersionById", __query, body)

  def getDatasetVersionTags(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset-version/getDatasetVersionTags", __query, body)

  def getLatestDatasetVersionByDatasetId(self, dataset_id=None, ascending=None, sort_key=None):
    __query = {
      "dataset_id": client.to_query(dataset_id),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/dataset-version/getLatestDatasetVersionByDatasetId", __query, body)

  def setDatasetVersionVisibility(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset-version/setDatasetVersionVisibility", __query, body)

  def updateDatasetVersionAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset-version/updateDatasetVersionAttributes", __query, body)

  def updateDatasetVersionDescription(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/dataset-version/updateDatasetVersionDescription", __query, body)
