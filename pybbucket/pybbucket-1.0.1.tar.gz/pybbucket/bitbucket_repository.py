import json

from pybbucket.request import post, get


class BitbucketRepository:

    def __init__(self, bitbucket, repository_name):
        self.bitbucket = bitbucket
        self.repository_name = repository_name
        self.REQUEST_URL_BRANCHES = self.bitbucket.api_server_url + "2.0/repositories/" + \
                                    self.bitbucket.workspace_id + "/" + repository_name + "/refs/branches"
        self.REQUEST_URL_PULL_REQUESTS = self.bitbucket.api_server_url + "2.0/repositories/" + \
                                         self.bitbucket.workspace_id + "/" + repository_name + "/pullrequests"

    def create_branch(self, branch_name, from_branch_name_or_commit_hash):
        request_payload = {
            "name": branch_name,
            "target": {
                "hash": from_branch_name_or_commit_hash
            }
        }
        return post(url=self.REQUEST_URL_BRANCHES, data=json.dumps(request_payload),
                    headers=self.bitbucket.header_content_type_json,
                    description="Create branch '{}' from branch '{}' in Bitbucket repository '{}'"
                    .format(branch_name, from_branch_name_or_commit_hash, self.repository_name),
                    credentials=self.bitbucket.credentials)

    def get_branches(self):
        return get(url=self.REQUEST_URL_BRANCHES, headers=self.bitbucket.header_content_type_json,
                   description="Get branches in Bitbucket repository '{}'".format(self.repository_name),
                   credentials=self.bitbucket.credentials)

    def create_pull_request(self, title, source_branch_name, destination_branch_name, reviewers):
        request_payload = {
            "title": title,
            "source": {
                "branch": {
                    "name": source_branch_name
                }
            },
            "destination": {
                "branch": {
                    "name": destination_branch_name
                }
            },
            "reviewers": reviewers
        }
        return post(url=self.REQUEST_URL_PULL_REQUESTS, data=json.dumps(request_payload),
                    headers=self.bitbucket.header_content_type_json,
                    description="Create a pull request in repository '{}' with title '{}' from branch '{}' "
                                "to branch '{}'".format(self.repository_name, title, source_branch_name,
                                                        destination_branch_name),
                    credentials=self.bitbucket.credentials)

    def get_pull_request_details(self, pull_request_id):
        return get(url=self.REQUEST_URL_PULL_REQUESTS + "/" + str(pull_request_id),
                   headers=self.bitbucket.header_content_type_json, credentials=self.bitbucket.credentials,
                   description="Get details for the pull request with id {}".format(pull_request_id))
