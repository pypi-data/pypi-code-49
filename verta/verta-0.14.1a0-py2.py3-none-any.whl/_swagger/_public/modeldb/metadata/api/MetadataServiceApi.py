# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class MetadataServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def AddLabels(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("PUT", self.base_path + s"/metadata/labels", __query, body)

  def DeleteLabels(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/metadata/delete", __query, body)

  def GetLabels(self, id_id_type=None, id_int_id=None, id_string_id=None):
    __query = {
      "id.id_type": client.to_query(id_id_type),
      "id.int_id": client.to_query(id_int_id),
      "id.string_id": client.to_query(id_string_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/metadata/labels", __query, body)
