# THIS FILE IS AUTO-GENERATED. DO NOT EDIT

class VersioningServiceApi:
  def __init__(self, client, base_path = "/v1"):
    self.client = client
    self.base_path = base_path

  def ComputeRepositoryDiff(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, repository_id_repo_id=None, commit_a=None, commit_b=None, path_prefix=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id),
      "commit_a": client.to_query(commit_a),
      "commit_b": client.to_query(commit_b),
      "path_prefix": client.to_query(path_prefix)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/diff", __query, body)

  def ComputeRepositoryDiff2(self, repository_id_repo_id=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None, commit_a=None, commit_b=None, path_prefix=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name),
      "commit_a": client.to_query(commit_a),
      "commit_b": client.to_query(commit_b),
      "path_prefix": client.to_query(path_prefix)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$repository_id_repo_id/diff", __query, body)

  def CreateCommit(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, body=None):
    __query = {
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/commits", __query, body)

  def CreateCommit2(self, repository_id_repo_id=None, body=None):
    __query = {
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("PUT", self.base_path + s"/versioning/repositories/$repository_id_repo_id/commits", __query, body)

  def CreateRepository(self, id_named_id_workspace_name=None, body=None):
    __query = {
    }
    if id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"id_named_id_workspace_name\"")
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("POST", self.base_path + s"/versioning/workspaces/$id_named_id_workspace_name/repositories", __query, body)

  def DeleteCommit(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, commit_sha=None, repository_id_repo_id=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("DELETE", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/commits/$commit_sha", __query, body)

  def DeleteCommit2(self, repository_id_repo_id=None, commit_sha=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("DELETE", self.base_path + s"/versioning/repositories/$repository_id_repo_id/commits/$commit_sha", __query, body)

  def DeleteRepository(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, repository_id_repo_id=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    body = None
    return self.client.request("DELETE", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name", __query, body)

  def DeleteRepository2(self, repository_id_repo_id=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    body = None
    return self.client.request("DELETE", self.base_path + s"/versioning/repositories/$repository_id_repo_id", __query, body)

  def DeleteTag(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, tag=None, repository_id_repo_id=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if tag is None:
      raise Exception("Missing required parameter \"tag\"")
    body = None
    return self.client.request("DELETE", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/tags/$tag", __query, body)

  def DeleteTag2(self, repository_id_repo_id=None, tag=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if tag is None:
      raise Exception("Missing required parameter \"tag\"")
    body = None
    return self.client.request("DELETE", self.base_path + s"/versioning/repositories/$repository_id_repo_id/tags/$tag", __query, body)

  def GetCommit(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, commit_sha=None, repository_id_repo_id=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/commits/$commit_sha", __query, body)

  def GetCommit2(self, repository_id_repo_id=None, commit_sha=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$repository_id_repo_id/commits/$commit_sha", __query, body)

  def GetCommitBlob(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, commit_sha=None, repository_id_repo_id=None, path=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id),
      "path": client.to_query(path)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/commits/$commit_sha/blobs/path", __query, body)

  def GetCommitBlob2(self, repository_id_repo_id=None, commit_sha=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None, path=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name),
      "path": client.to_query(path)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$repository_id_repo_id/commits/$commit_sha/blobs/path", __query, body)

  def GetCommitFolder(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, commit_sha=None, repository_id_repo_id=None, path=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id),
      "path": client.to_query(path)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/commits/$commit_sha/folders/path", __query, body)

  def GetCommitFolder2(self, repository_id_repo_id=None, commit_sha=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None, path=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name),
      "path": client.to_query(path)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$repository_id_repo_id/commits/$commit_sha/folders/path", __query, body)

  def GetRepository(self, id_named_id_workspace_name=None, id_named_id_name=None, id_repo_id=None):
    __query = {
      "id.repo_id": client.to_query(id_repo_id)
    }
    if id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"id_named_id_workspace_name\"")
    if id_named_id_name is None:
      raise Exception("Missing required parameter \"id_named_id_name\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$id_named_id_workspace_name/repositories/$id_named_id_name", __query, body)

  def GetRepository2(self, id_repo_id=None, id_named_id_name=None, id_named_id_workspace_name=None):
    __query = {
      "id.named_id.name": client.to_query(id_named_id_name),
      "id.named_id.workspace_name": client.to_query(id_named_id_workspace_name)
    }
    if id_repo_id is None:
      raise Exception("Missing required parameter \"id_repo_id\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$id_repo_id", __query, body)

  def GetTag(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, tag=None, repository_id_repo_id=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if tag is None:
      raise Exception("Missing required parameter \"tag\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/tags/$tag", __query, body)

  def GetTag2(self, repository_id_repo_id=None, tag=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if tag is None:
      raise Exception("Missing required parameter \"tag\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$repository_id_repo_id/tags/$tag", __query, body)

  def ListCommitBlobs(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, commit_sha=None, repository_id_repo_id=None, pagination_page_number=None, pagination_page_limit=None, path_prefix=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id),
      "pagination.page_number": client.to_query(pagination_page_number),
      "pagination.page_limit": client.to_query(pagination_page_limit),
      "path_prefix": client.to_query(path_prefix)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/commits/$commit_sha/blobs", __query, body)

  def ListCommitBlobs2(self, repository_id_repo_id=None, commit_sha=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None, pagination_page_number=None, pagination_page_limit=None, path_prefix=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name),
      "pagination.page_number": client.to_query(pagination_page_number),
      "pagination.page_limit": client.to_query(pagination_page_limit),
      "path_prefix": client.to_query(path_prefix)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if commit_sha is None:
      raise Exception("Missing required parameter \"commit_sha\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$repository_id_repo_id/commits/$commit_sha/blobs", __query, body)

  def ListCommits(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, repository_id_repo_id=None, pagination_page_number=None, pagination_page_limit=None, commit_base=None, commit_head=None, path_prefix=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id),
      "pagination.page_number": client.to_query(pagination_page_number),
      "pagination.page_limit": client.to_query(pagination_page_limit),
      "commit_base": client.to_query(commit_base),
      "commit_head": client.to_query(commit_head),
      "path_prefix": client.to_query(path_prefix)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/commits", __query, body)

  def ListCommits2(self, repository_id_repo_id=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None, pagination_page_number=None, pagination_page_limit=None, commit_base=None, commit_head=None, path_prefix=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name),
      "pagination.page_number": client.to_query(pagination_page_number),
      "pagination.page_limit": client.to_query(pagination_page_limit),
      "commit_base": client.to_query(commit_base),
      "commit_head": client.to_query(commit_head),
      "path_prefix": client.to_query(path_prefix)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$repository_id_repo_id/commits", __query, body)

  def ListRepositories(self, workspace_name=None, pagination_page_number=None, pagination_page_limit=None):
    __query = {
      "pagination.page_number": client.to_query(pagination_page_number),
      "pagination.page_limit": client.to_query(pagination_page_limit)
    }
    if workspace_name is None:
      raise Exception("Missing required parameter \"workspace_name\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$workspace_name/repositories", __query, body)

  def ListRepositories2(self, workspace_name=None, pagination_page_number=None, pagination_page_limit=None):
    __query = {
      "workspace_name": client.to_query(workspace_name),
      "pagination.page_number": client.to_query(pagination_page_number),
      "pagination.page_limit": client.to_query(pagination_page_limit)
    }
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories", __query, body)

  def ListTags(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, repository_id_repo_id=None):
    __query = {
      "repository_id.repo_id": client.to_query(repository_id_repo_id)
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/tags", __query, body)

  def ListTags2(self, repository_id_repo_id=None, repository_id_named_id_name=None, repository_id_named_id_workspace_name=None):
    __query = {
      "repository_id.named_id.name": client.to_query(repository_id_named_id_name),
      "repository_id.named_id.workspace_name": client.to_query(repository_id_named_id_workspace_name)
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    body = None
    return self.client.request("GET", self.base_path + s"/versioning/repositories/$repository_id_repo_id/tags", __query, body)

  def SetTag(self, repository_id_named_id_workspace_name=None, repository_id_named_id_name=None, tag=None, body=None):
    __query = {
    }
    if repository_id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_workspace_name\"")
    if repository_id_named_id_name is None:
      raise Exception("Missing required parameter \"repository_id_named_id_name\"")
    if tag is None:
      raise Exception("Missing required parameter \"tag\"")
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("PUT", self.base_path + s"/versioning/workspaces/$repository_id_named_id_workspace_name/repositories/$repository_id_named_id_name/tags/$tag", __query, body)

  def SetTag2(self, repository_id_repo_id=None, tag=None, body=None):
    __query = {
    }
    if repository_id_repo_id is None:
      raise Exception("Missing required parameter \"repository_id_repo_id\"")
    if tag is None:
      raise Exception("Missing required parameter \"tag\"")
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("PUT", self.base_path + s"/versioning/repositories/$repository_id_repo_id/tags/$tag", __query, body)

  def UpdateRepository(self, id_named_id_workspace_name=None, id_named_id_name=None, body=None):
    __query = {
    }
    if id_named_id_workspace_name is None:
      raise Exception("Missing required parameter \"id_named_id_workspace_name\"")
    if id_named_id_name is None:
      raise Exception("Missing required parameter \"id_named_id_name\"")
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("PUT", self.base_path + s"/versioning/workspaces/$id_named_id_workspace_name/repositories/$id_named_id_name", __query, body)

  def UpdateRepository2(self, id_repo_id=None, body=None):
    __query = {
    }
    if id_repo_id is None:
      raise Exception("Missing required parameter \"id_repo_id\"")
    if body is None:
      raise Exception("Missing required parameter \"body\"")
    return self.client.request("PUT", self.base_path + s"/versioning/repositories/$id_repo_id", __query, body)
