# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class LineageApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addLineage(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/lineage/addLineage", __query, body)

  def deleteLineage(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/lineage/deleteLineage", __query, body)

  def findAllInputs(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/lineage/findAllInputs", __query, body)

  def findAllInputsOutputs(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/lineage/findAllInputsOutputs", __query, body)

  def findAllOutputs(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/lineage/findAllOutputs", __query, body)
