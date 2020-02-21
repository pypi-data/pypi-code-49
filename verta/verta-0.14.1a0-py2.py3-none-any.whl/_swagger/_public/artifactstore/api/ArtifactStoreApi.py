# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ArtifactStoreApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def deleteArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/artifact/deleteArtifact", __query, body)

  def getArtifact(self, key=None):
    __query = {
      "key": client.to_query(key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/artifact/getArtifact", __query, body)

  def storeArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/artifact/storeArtifact", __query, body)

  def storeArtifactWithStream(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/artifact/storeArtifactWithStream", __query, body)
