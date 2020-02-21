# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ExperimentRunServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def addExperimentRunAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/addExperimentRunAttributes", __query, body)

  def addExperimentRunTag(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/addExperimentRunTag", __query, body)

  def addExperimentRunTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/addExperimentRunTags", __query, body)

  def createExperimentRun(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/createExperimentRun", __query, body)

  def deleteArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment-run/deleteArtifact", __query, body)

  def deleteExperimentRun(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment-run/deleteExperimentRun", __query, body)

  def deleteExperimentRunAttributes(self, id=None, attribute_keys=None, delete_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "delete_all": client.to_query(delete_all)
    }
    body = None
    return self.client.request("DELETE", self.base_path + s"/experiment-run/deleteExperimentRunAttributes", __query, body)

  def deleteExperimentRunTag(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment-run/deleteExperimentRunTag", __query, body)

  def deleteExperimentRunTags(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment-run/deleteExperimentRunTags", __query, body)

  def deleteExperimentRuns(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("DELETE", self.base_path + s"/experiment-run/deleteExperimentRuns", __query, body)

  def findExperimentRuns(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/findExperimentRuns", __query, body)

  def getArtifacts(self, id=None, key=None):
    __query = {
      "id": client.to_query(id),
      "key": client.to_query(key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getArtifacts", __query, body)

  def getChildrenExperimentRuns(self, experiment_run_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "experiment_run_id": client.to_query(experiment_run_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getChildrenExperimentRuns", __query, body)

  def getDatasets(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getDatasets", __query, body)

  def getExperimentRunAttributes(self, id=None, attribute_keys=None, get_all=None):
    __query = {
      "id": client.to_query(id),
      "attribute_keys": client.to_query(attribute_keys),
      "get_all": client.to_query(get_all)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getAttributes", __query, body)

  def getExperimentRunById(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getExperimentRunById", __query, body)

  def getExperimentRunByName(self, name=None, experiment_id=None):
    __query = {
      "name": client.to_query(name),
      "experiment_id": client.to_query(experiment_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getExperimentRunByName", __query, body)

  def getExperimentRunCodeVersion(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getExperimentRunCodeVersion", __query, body)

  def getExperimentRunTags(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getExperimentRunTags", __query, body)

  def getExperimentRunsByDatasetVersionId(self, datset_version_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "datset_version_id": client.to_query(datset_version_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getExperimentRunsByDatasetVersionId", __query, body)

  def getExperimentRunsInExperiment(self, experiment_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "experiment_id": client.to_query(experiment_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getExperimentRunsInExperiment", __query, body)

  def getExperimentRunsInProject(self, project_id=None, page_number=None, page_limit=None, ascending=None, sort_key=None):
    __query = {
      "project_id": client.to_query(project_id),
      "page_number": client.to_query(page_number),
      "page_limit": client.to_query(page_limit),
      "ascending": client.to_query(ascending),
      "sort_key": client.to_query(sort_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getExperimentRunsInProject", __query, body)

  def getHyperparameters(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getHyperparameters", __query, body)

  def getJobId(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getJobId", __query, body)

  def getMetrics(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getMetrics", __query, body)

  def getObservations(self, id=None, observation_key=None):
    __query = {
      "id": client.to_query(id),
      "observation_key": client.to_query(observation_key)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/getObservations", __query, body)

  def getTopExperimentRuns(self, project_id=None, experiment_id=None, experiment_run_ids=None, sort_key=None, ascending=None, top_k=None, ids_only=None):
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
    return self.client.request("GET", self.base_path + s"/experiment-run/getTopExperimentRuns", __query, body)

  def getUrlForArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/getUrlForArtifact", __query, body)

  def logArtifact(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logArtifact", __query, body)

  def logArtifacts(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logArtifacts", __query, body)

  def logAttribute(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logAttribute", __query, body)

  def logAttributes(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logAttributes", __query, body)

  def logDataset(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logDataset", __query, body)

  def logDatasets(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logDatasets", __query, body)

  def logExperimentRunCodeVersion(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logExperimentRunCodeVersion", __query, body)

  def logHyperparameter(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logHyperparameter", __query, body)

  def logHyperparameters(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logHyperparameters", __query, body)

  def logJobId(self, id=None, job_id=None):
    __query = {
      "id": client.to_query(id),
      "job_id": client.to_query(job_id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/logJobId", __query, body)

  def logMetric(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logMetric", __query, body)

  def logMetrics(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logMetrics", __query, body)

  def logObservation(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logObservation", __query, body)

  def logObservations(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/logObservations", __query, body)

  def setParentExperimentRunId(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/setParentExperimentRunId", __query, body)

  def sortExperimentRuns(self, experiment_run_ids=None, sort_key=None, ascending=None, ids_only=None):
    __query = {
      "experiment_run_ids": client.to_query(experiment_run_ids),
      "sort_key": client.to_query(sort_key),
      "ascending": client.to_query(ascending),
      "ids_only": client.to_query(ids_only)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/experiment-run/sortExperimentRuns", __query, body)

  def updateExperimentRunDescription(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/updateExperimentRunDescription", __query, body)

  def updateExperimentRunName(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/experiment-run/updateExperimentRunName", __query, body)
