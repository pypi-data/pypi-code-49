# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class CommentApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addExperimentRunComment(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/comment/addExperimentRunComment", __query, body)

  def deleteExperimentRunComment(self, id=None, entity_id=None):
    __query = {
      "id": client.to_query(id),
      "entity_id": client.to_query(entity_id)
    }
    body = None
    return self.client.request("DELETE", self.base_path + s"/comment/deleteExperimentRunComment", __query, body)

  def getExperimentRunComments(self, entity_id=None):
    __query = {
      "entity_id": client.to_query(entity_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/comment/getExperimentRunComments", __query, body)

  def updateExperimentRunComment(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/comment/updateExperimentRunComment", __query, body)
