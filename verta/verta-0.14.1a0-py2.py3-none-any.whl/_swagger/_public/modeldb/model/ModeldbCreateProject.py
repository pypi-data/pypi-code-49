# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class ModeldbCreateProject(dict):
  def __init__(self, name=None, description=None, attributes=None, tags=None, readme_text=None, project_visibility=None, artifacts=None, workspace_name=None, date_created=None):
    self.name = name
    self.description = description
    self.attributes = attributes
    self.tags = tags
    self.readme_text = readme_text
    self.project_visibility = project_visibility
    self.artifacts = artifacts
    self.workspace_name = workspace_name
    self.date_created = date_created

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
