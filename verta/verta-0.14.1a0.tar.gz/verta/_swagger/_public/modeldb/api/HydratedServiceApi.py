# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class HydratedServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def findHydratedDatasetVersions(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedDatasetVersions", __query, body)

  def findHydratedDatasets(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedDatasets", __query, body)

  def findHydratedDatasetsByOrganization(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedDatasetsByOrganization", __query, body)

  def findHydratedDatasetsByTeam(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedDatasetsByTeam", __query, body)

  def findHydratedExperimentRuns(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedExperimentRuns", __query, body)

  def findHydratedExperiments(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedExperiments", __query, body)

  def findHydratedProjects(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedProjects", __query, body)

  def findHydratedProjectsByOrganization(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedProjectsByOrganization", __query, body)

  def findHydratedProjectsByTeam(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedProjectsByTeam", __query, body)

  def findHydratedProjectsByUser(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedProjectsByUser", __query, body)

  def findHydratedPublicDatasets(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedPublicDatasets", __query, body)

  def findHydratedPublicProjects(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/hydratedData/findHydratedPublicProjects", __query, body)

  def getHydratedDatasetByName(self, name=None, workspace_name=None):
    __query = {
      "name": client.to_query(name),
      "workspace_name": client.to_query(workspace_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getHydratedDatasetByName", __query, body)

  def getHydratedDatasetsByProjectId(self, project_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "project_id": client.to_query(project_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getHydratedDatasetsByProjectId", __query, body)

  def getHydratedExperimentRunById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getHydratedExperimentRunById", __query, body)

  def getHydratedExperimentRunsInProject(self, project_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "project_id": client.to_query(project_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getHydratedExperimentRunsInProject", __query, body)

  def getHydratedExperimentsByProjectId(self, project_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "project_id": client.to_query(project_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getHydratedExperimentsByProjectId", __query, body)

  def getHydratedProjectById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getHydratedProjectById", __query, body)

  def getHydratedProjects(self, page_number=None, page_limit=None, ascending=None, sort_key=None, workspace_name=None):
    __query = {
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key),
      "workspace_name": client.to_query(workspace_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getHydratedProjects", __query, body)

  def getHydratedPublicProjects(self, page_number=None, page_limit=None, ascending=None, sort_key=None, workspace_name=None):
    __query = {
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key),
      "workspace_name": client.to_query(workspace_name)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getHydratedPublicProjects", __query, body)

  def getTopHydratedExperimentRuns(self, project_id=None, experiment_id=None, experiment_run_ids=None, sort_key=None, ascending=None, top_k=None, ids_only=None):
    __query = {
      "project_id": client.to_query(project_id),
      "experiment_id": client.to_query(experiment_id),
      "experiment_run_ids": client.to_query(experiment_run_ids),
      "sort_key": client.to_query(sort_key),
      "ascending": client.to_query(ascending),
      "top_k": client.to_query(top_k),
      "ids_only": client.to_query(ids_only)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/getTopHydratedExperimentRuns", __query, body)

  def sortHydratedExperimentRuns(self, experiment_run_ids=None, sort_key=None, ascending=None, ids_only=None):
    __query = {
      "experiment_run_ids": client.to_query(experiment_run_ids),
      "sort_key": client.to_query(sort_key),
      "ascending": client.to_query(ascending),
      "ids_only": client.to_query(ids_only)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/hydratedData/sortHydratedExperimentRuns", __query, body)
