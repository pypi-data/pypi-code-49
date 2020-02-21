# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class TelemetryApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def collectTelemetry(self, body=None):
    __query = {
    }
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/telemetry/collectTelemetry", __query, body)
