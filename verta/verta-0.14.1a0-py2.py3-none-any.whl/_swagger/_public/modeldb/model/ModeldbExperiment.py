# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbExperiment(dict):
  def __init__(self, id=None, project_id=None, name=None, description=None, date_created=None, date_updated=None, attributes=None, tags=None, owner=None, code_version_snapshot=None, artifacts=None):
    self.id = id
    self.project_id = project_id
    self.name = name
    self.description = description
    self.date_created = date_created
    self.date_updated = date_updated
    self.attributes = attributes
    self.tags = tags
    self.owner = owner
    self.code_version_snapshot = code_version_snapshot
    self.artifacts = artifacts

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
