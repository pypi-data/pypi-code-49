# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class UacAddTeamUser(dict):
  def __init__(self, team_id=None, share_with=None):
    self.team_id = team_id
    self.share_with = share_with

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]

  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError
