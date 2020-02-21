# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class CollaboratorApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addOrUpdateDatasetCollaborator(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/collaborator/addOrUpdateDatasetCollaborator", __query, body)

  def addOrUpdateProjectCollaborator(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/collaborator/addOrUpdateProjectCollaborator", __query, body)

  def getDatasetCollaborators(self, entity_id=None):
    __query = {
      "entity_id": client.to_query(entity_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/collaborator/getDatasetCollaborators", __query, body)

  def getProjectCollaborators(self, entity_id=None):
    __query = {
      "entity_id": client.to_query(entity_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/collaborator/getProjectCollaborators", __query, body)

  def removeDatasetCollaborator(self, entity_id=None, share_with=None, date_deleted=None, authz_entity_type=None):
    __query = {
      "entity_id": client.to_query(entity_id),
      "share_with": client.to_query(share_with),
      "date_deleted": client.to_query(date_deleted),
      "authz_entity_type": client.to_query(authz_entity_type)
    }
    body = None
    return self.client.request("DELETE", self.base_path + s"/collaborator/removeDatasetCollaborator", __query, body)

  def removeProjectCollaborator(self, entity_id=None, share_with=None, date_deleted=None, authz_entity_type=None):
    __query = {
      "entity_id": client.to_query(entity_id),
      "share_with": client.to_query(share_with),
      "date_deleted": client.to_query(date_deleted),
      "authz_entity_type": client.to_query(authz_entity_type)
    }
    body = None
    return self.client.request("DELETE", self.base_path + s"/collaborator/removeProjectCollaborator", __query, body)
