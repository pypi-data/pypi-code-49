# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbQueryDatasetVersionInfo(dict):
  def __init__(self, query=None, query_template=None, query_parameters=None, data_source_uri=None, execution_timestamp=None, num_records=None):
    self.query = query
    self.query_template = query_template
    self.query_parameters = query_parameters
    self.data_source_uri = data_source_uri
    self.execution_timestamp = execution_timestamp
    self.num_records = num_records

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
