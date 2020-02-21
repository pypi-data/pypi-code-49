# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbProject(dict):
  def __init__(self, id=None, name=None, description=None, date_created=None, date_updated=None, short_name=None, readme_text=None, project_visibility=None, workspace_id=None, workspace_type=None, attributes=None, tags=None, owner=None, code_version_snapshot=None, artifacts=None):
    self.id = id
    self.name = name
    self.description = description
    self.date_created = date_created
    self.date_updated = date_updated
    self.short_name = short_name
    self.readme_text = readme_text
    self.project_visibility = project_visibility
    self.workspace_id = workspace_id
    self.workspace_type = workspace_type
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
