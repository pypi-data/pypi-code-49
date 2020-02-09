import base64
import json
from labelsync.util import map_to_dictionary
from labelsync.io import FileLoader

class ConflictResolver:

    def resolve(self, online, cache, authority, strat):
        """Figure out which labels should be created, deleted or updated based on where they came from.
            This method only cares about ids not the contents. Because of this, to_update ids might not nececarily need update,
            they are to be viewed as update candidates, and need to be checked further.

            :param list online: ids fetched from repo
            :param list cache: ids cached during the last synchronization
            :param list authority: ids from the master repo, they represent the desired state

            :return: triplet of sets to_add, to_update, to_remove in this order.
        """
        cache = set(cache)
        online = set(online)
        authority = set(authority)

        managed = cache.intersection(online)
        collisions = authority.intersection(online).difference(cache)
        print("col", collisions)
        if strat == "override":
            managed = managed.union(collisions)
        else:
            authority.difference_update(collisions)

        to_add = authority.difference(managed)
        to_remove = managed.difference(authority)
        to_update = authority.intersection(managed)
        print("add ", to_add)
        print("remove ", to_remove)
        print("update ", to_update)
        return [to_add, to_update, to_remove]

class RepoCache():
    """Lightweight helper for saving and retrieving repository info from the filesystem
    """
    def __init__(self, authority_client, loader):
        self.authority_client = authority_client
        self.loader = loader
        self.load_cache()

    def update_cache(self):
        remote = (self.authority_client.map_content_to_string(self.authority_client.get_file("repos.json")))
        self.repos = json.loads(remote)
        self.loader.save("repos.json", remote)

    def load_cache(self):
        self.repos = json.loads(self.loader.load("repos.json"))

    def read(self):
        return self.repos

class CredentialsManager():
    """Lightweight helper taking care of saving and retrieving credentials info from filesystem
    """
    def __init__(self, loader, repo_cache):
        self.loader = loader
        self.repo_cache = repo_cache
        self.load()

    def load(self):
        self.credentials = json.loads(self.loader.load("credentials.json", "{}"))

    def save_credentials(self, service, user, repo, token):
        repos = self.repo_cache.read()
        for service_name in repos.keys():
            if service_name == service:
                for repo_it in repos[service]:
                    if repo_it["owner"] == user and repo_it["repo"] == repo:
                        self.credentials[f"{service}_{user}_{repo}"] = token
                        break
        self.loader.save("credentials.json", json.dumps(self.credentials))

    def get_credentials_for(self, service, user, repo):
        return self.credentials.get(f"{service}_{user}_{repo}", None)


class SynchronizationService:
    """Handles the synchronization process
    """
    def __init__(self, authority_client, cache_manager):
        self.authority_client = authority_client
        self.cache_manager = cache_manager

    def fetch_and_map(self, client):
        result = []
        labels = client.read_labels()
        for label in labels:
            result.append(client.map_from_response(label))
        return result

    def process_repository(self, client, strat, key_property):
        """Orchestrate label update in one repository for which the client was provided

            :param client py:class:~UpdateClient: client to be used. It's implementation doesn't matter
            :param strat string: strategy to be used when new labels conflict (same name) with non-managed labels
        """
        resolver = ConflictResolver()

        online_labels = self.fetch_and_map(client)
        cached_labels = self.cache_manager.read()
        authority_labels = self.read_label_file(self.authority_client.map_content_to_string(self.authority_client.get_file("labels.json")))

        cached_labels_dict = map_to_dictionary(cached_labels, key_property)
        authority_labels_dict = map_to_dictionary(authority_labels, key_property)
        online_labels_dict = map_to_dictionary(online_labels, key_property)
        to_add, to_update, to_remove = resolver.resolve(list(online_labels_dict.keys()),
            list(cached_labels_dict.keys()),
            list(authority_labels_dict.keys()), strat)

        filtered = self.filter_to_update(to_update, cached_labels_dict, authority_labels_dict, online_labels_dict)
        errors = {}
        for label in to_add:
            self.attach_if_ok(client, client.add_label(client.map_to_create(authority_labels_dict[label])), errors, key_property)
        for label in to_remove:
            self.detach_if_ok(client.delete_label(label), errors, label)
        for label in filtered.keys():
            self.attach_if_ok(client, client.update_label(client.map_to_update(filtered[label]), label), errors, key_property)

        self.cache_manager.persist()
        return errors

    def filter_to_update(self, to_update_keys, cached_labels, authority_labels, online_labels):
        """Resolves which of the labels present both in cache and git repository have been actually updated
        """
        print("keys to update", to_update_keys)
        print("cached", cached_labels)
        print("authority", authority_labels)
        result = {}
        for key in to_update_keys:
            if cached_labels.get(key, None) != authority_labels[key] or online_labels[key] != authority_labels[key] :
                print(key + " will be updated")
                result[key] = authority_labels[key]
        return result

    def attach_if_ok(self, client, response, errors, id):
        if response.status_code < 300:
            self.cache_manager.attach(client.map_from_response(response.json()))
        else:
            errors[id] = {"status_code": response.status_code, "message": response.content}

    def detach_if_ok(self, response, errors, id):
        if response.status_code < 300:
            self.cache_manager.detach(id)
        else:
            errors[id] = {"status_code": response.status_code, "message": response.content}


    def read_label_file(self, file_content):
        return json.loads(file_content)

class LabelService:
    """Handles label state changes on master repository
    """

    def __init__(self, master_client):
        self.master_client = master_client

    def delete_label(self, name):
        """Delete label specified from master repository

            :param string name: name of the label to delete
        """
        response = self.master_client.get_file('labels.json')
        labels = map_to_dictionary(json.loads(self.master_client.map_content_to_string(response)), "name")
        del labels[name]
        self.master_client.update_file('labels.json',
                str(base64.b64encode(bytes(json.dumps(list(labels.values())), 'utf-8')), encoding='utf-8'),
                response.json()["sha"],
                "Delete label " + name)

    def create_or_update_label(self, form):
        """Create or update label on master repository

            :param dict form: values of label to be updated, it's obtained through html form
        """
        response = self.master_client.get_file('labels.json')
        labels = map_to_dictionary(json.loads(self.master_client.map_content_to_string(response)), "name")
        update = form["original_name"] != ""
        label = {"name": form["name"], "color": form["color"].split('#')[1], "description": form["description"]}
        labels[form["original_name"] if update else form["name"]] = label
        self.master_client.update_file('labels.json',
            str(base64.b64encode(bytes(json.dumps(list(labels.values())), 'utf-8')), encoding='utf-8'),
            response.json()["sha"],
            ("Update" if update else "Create") + " label " + form["name"])

class MasterService:
    """Handles  master repository creating
    """

    def __init__(self, client):
        self.master_client = client

    def setup_master(self, webhook_url, secret):
        repo_data = {"url": self.master_client.url,
                "name": self.master_client.repo,
                "owner": self.master_client.owner,
                "token": self.master_client.token,
                "webhook_url": webhook_url,
                "secret": secret,
                "errors": []}
        try:
            response = self.master_client.ping_repo()
            if response.status_code == 404 and response.headers.get('Server', None) == 'GitHub.com':
                create_response = self.create_master_repo(webhook_url,  secret)
            elif response.status_code != 200:
                return self.append_error(repo_data, response.status_code, '')
            FileLoader().save("master_repo.json", json.dumps(repo_data))
            return (True, '')
        except Exception as e:
            return self.append_error(repo_data, 'CONNECTION_ERROR', e)

    def append_error(self, repo_data, data, exception):
        repo_data["errors"].append(data)
        FileLoader().save("master_repo.json", json.dumps(repo_data))
        return (False, exception)


    def create_master_repo(self, webhook_url, secret):
        response = self.master_client.create_repo()
        self.master_client.set_webhook(webhook_url, secret)
        repos_response = self.master_client.upload_file("repos.json", str(base64.b64encode(bytes('{}', encoding='utf-8')), 'utf-8'), "Add repo file.")
        repos_response = self.master_client.upload_file("labels.json", str(base64.b64encode(bytes('[]', encoding='utf-8')), 'utf-8'), "Add label file.")



