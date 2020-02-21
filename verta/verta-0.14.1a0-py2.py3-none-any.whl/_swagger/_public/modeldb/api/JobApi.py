# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class JobApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def createJob(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/job/createJob", __query, body)

  def deleteJob(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/job/deleteJob", __query, body)

  def getJob(self, id=None):
    __query = {
      "id": client.to_query(id)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/job/getJob", __query, body)

  def updateJob(self, id=None, end_time=None, job_status=None):
    __query = {
      "id": client.to_query(id),
      "end_time": client.to_query(end_time),
      "job_status": client.to_query(job_status)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/job/updateJob", __query, body)
