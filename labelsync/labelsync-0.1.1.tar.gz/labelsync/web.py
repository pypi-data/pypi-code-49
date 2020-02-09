import flask
import requests
import base64
import configparser
import io
import json
import copy
import hashlib
import hmac
from flask import render_template, url_for, request
from labelsync.clients import GithubClient
from labelsync.clients import GitlabClient, GithubMasterClient
from labelsync.io import LabelCacheManager, FileLoader
from labelsync.logic import ConflictResolver, SynchronizationService, RepoCache, CredentialsManager, LabelService, MasterService
from labelsync.util import hash_str

labelsync_blueprint = flask.Blueprint('labelsync', __name__)

# Frontend -----------------------------------------------------------------------------------------------------

@labelsync_blueprint.route('/')
def index():
    """Return html of the main info page
    """
    loader = FileLoader()
    repos_info = []
    labels = []
    errors = []
    if "master_client" not in flask.current_app.config:
        return render_template('create_master.html', services=flask.current_app.config["client_factory"].keys())
    else:
        master_client = flask.current_app.config["master_client"]
        master_response = master_client.ping_repo()
        master_info = {"url": master_client.url, "errors": [master_response.status_code] if master_response.status_code != 200 else [], "name": master_client.repo}
        if master_response.status_code != 200:
            return render_template("index.html",
                sync_url=url_for('.manual_sync'),
                master=master_info,
                repos="")
        try:
            repository_index = load_repos(master_client)
            flask.current_app.config['repositories'] = repository_index
            make_clients(repository_index, flask.current_app.config["client_factory"])
            ping_repos()
            repos_info = get_repos_info()
        except Exception:
            errors.append("INVALID_REPO_FILE")

        try:
            labels = json.loads(master_client.map_content_to_string(master_client.get_file('labels.json')))
        except Exception:
            errors.append("INVALID_LABEL_FILE")

        master_info["errors"] = errors

        return render_template("index.html",
            sync_url=url_for('.manual_sync'),
            master=master_info,
            labels=labels,
            repos=repos_info)

@labelsync_blueprint.route('/manual_sync', methods=['POST'])
def manual_sync():
    """Synchronize all the labels in connected repositories
    """
    on_update()
    return redirect()

@labelsync_blueprint.route('/update_login/<service>_<owner>_<name>')
def update_login_form(service, owner, name):
    """Show form for login info updating
    """
    return render_template("login_form.html", service=service, owner=owner, name=name)
    print(service, owner, name)


@labelsync_blueprint.route('/labels/add')
def create_label_form():
    """Show form for creating a new label
    """
    return render_template('label_form.html', label={"name": '', "color": 'ffffff', 'description': ''})


@labelsync_blueprint.route('/labels/edit/<name>')
def update_label_form(name):
    """Show form for updating an existing label

        :param string name: name (id) of the label to be updated
    """
    master_client = flask.current_app.config['master_client']
    response = master_client.get_file('labels.json')
    labels = json.loads(master_client.map_content_to_string(response))
    idx = 0
    for label in labels:
        if label["name"] == name:
            del labels[idx]
            break
        idx = idx + 1
    return render_template('label_form.html', label=label)

@labelsync_blueprint.route('/create_master')
def create_master_form():
    """Show form for creating / updating a master repository
    """
    return render_template('create_master.html', services=flask.current_app.config["client_factory"].keys())

# Backend -----------------------------------------------------------------------------------------------------

@labelsync_blueprint.route('/create_master', methods=['POST'])
def create_master_repo():
    """Trigger master repo create / update. Html form input must be in the body of request.
    """
    master_client = make_master_client(flask.request.form)
    service = MasterService(master_client)
    result = service.setup_master(flask.request.form["webhook_url"], flask.request.form["secret"])
    if result[0]:
        flask.current_app.config['master_client'] = master_client
    else:
        if 'master_client' in flask.current_app.config:
            del flask.current_app.config['master_client']
    return redirect()

@labelsync_blueprint.route('/update_login', methods=['POST'])
def update_login():
    """Update login credentials for repository. Html form must be in the body of request.
    """
    loader = FileLoader()
    credentials = json.loads(loader.load('credentials.json'))
    data = flask.request.form
    credentials[f"{data['service']}_{data['owner']}_{data['name']}"] = data['token']
    loader.save('credentials.json', json.dumps(credentials))
    return redirect()

@labelsync_blueprint.route('/labels/update', methods=['POST'])
def create_or_update_label():
    """Create or update label in master repository according to the contents of html form submitted.
    """
    service = LabelService(flask.current_app.config['master_client'])
    service.create_or_update_label(flask.request.form)
    return redirect()

@labelsync_blueprint.route('/labels/delete/<name>')
def delete_label(name):
    """Delete label from master repository

        :param string name: name of the label to be deleted
    """
    service = LabelService(flask.current_app.config['master_client'])
    service.delete_label(name)
    return redirect()

def create_signature(secret, data):
    return hmac.new(bytes(secret, "utf-8"), data, hashlib.sha1).hexdigest()

@labelsync_blueprint.route('/sync', methods=['POST'])
def sync():
    """Synchronize labels from all the connected repositories. Usually triggered by webhook.
    """
    if request.headers.get("X-GitHub-Event", None) == "ping":
        return "Hello there\n", 200
    if "master_client" not in flask.current_app.config:
        return "Master not configured", 200

    if "X-Hub-Signature" not in request.headers:
        return "Invalid signature", 401

    master = flask.current_app.config["master_client"]
    if create_signature(master.secret, request.data) != request.headers["X-Hub-Signature"].split("=", 2)[1]:
        return "Invalid signature", 401

    on_update()
    return "Synchronized", 200

def redirect():
    """Helper method to implement POST/REDIRECT/GET pattern. Used to generate redirect response for requests triggered by web browser
    """
    resp = flask.Response()
    resp.status_code = 303
    resp.headers["Location"] = url_for('.index')
    return resp

def get_repos_info():
    """Flatten information of all the repositories to list
    """
    result = []
    for repo in flask.current_app.config["repositories"].values():
        result.append(repo)
    return result

def make_master_client(data):
    """Create master client from html form data
    """
    return GithubMasterClient(data["owner"], data["name"], data["token"], data["url"], data["secret"], requests.Session())

def on_update():
    """Synchronize all the labels of repositories connected
    """
    master_client = flask.current_app.config['master_client']
    repos = flask.current_app.config['repositories']

    for repo in repos.values():
        if "client" in repo:
            try:
                service = SynchronizationService(master_client, LabelCacheManager(FileLoader(),
                    '.',
                    repo["owner"] + "_" + repo["repo"] + "_" + hash_str(repo["url"]) +
                         "_" + hash_str(master_client.url, master_client.owner, master_client.repo, master_client.service) + "_labels.json", "name"))
                service.process_repository(repo["client"], "ignore", "name")
                repo["errors"] = []
            except requests.exceptions.HTTPError as err:
                repo["errors"] = [err.response.status_code]

    return True



def load_repos(authority_client):
    """Fetch information about connected repositories and combine them with credentials stored locally

        :param authority_client: master repository client to be used for downloading repos information
    """
    repo_cache = RepoCache(authority_client, FileLoader())
    repo_cache.update_cache()
    credentials = CredentialsManager(FileLoader(), repo_cache)
    repos = repo_cache.read()

    repository_index = {}
    for service in repos:
        for repo in repos[service]:
            repo_id = f"{service}_{repo['owner']}_{repo['repo']}"
            repository = copy.deepcopy(repo)
            repository["service"] = service
            token = credentials.get_credentials_for(service, repo['owner'], repo['repo'])
            if token != None:
                repository["token"] = token
            repository_index[repo_id] = repository

    return repository_index

def ping_repos():
    """Test connectivity to all the connected repositories
    """
    print(flask.current_app.config["repositories"])
    for repo in flask.current_app.config["repositories"].values():
        if "client" in repo:
            response = repo["client"].ping_repo()

            if response.status_code != 200:
                repo["errors"].append("PING_STATUS_CODE=" + str(response.status_code))

def make_clients(repos, factory):
    """Construct connection clients for every service which is implemented, has at least one repo which uses it, and has
        credentials provided to it
    """
    for repo in repos.values():
        valid = True
        errors = []
        if not repo["service"] in factory:
            errors.append("UNSUPPORTED_SERVICE")
            valid = False
        if not "token" in repo:
            errors.append("MISSING_CREDENTIALS")
            valid = False
        if valid:
            repo["client"] = factory[repo["service"]](repo["owner"], repo["repo"], repo["token"], repo["url"], requests.Session())
        repo["errors"] = errors

def define_clients():
    """Serves for extending functionality by adding new service support.
        All the services provided by this method are supported.
    """
    clients = {
        'github': GithubClient,
        'gitlab': GitlabClient
    }
    return clients

def create_app(*args, **kwargs):
    """Construct labelsync web application"""
    app = flask.Flask(__name__)
    app.logger.info('Loading LABELSYNC configuration from files')
    app.config["client_factory"] = define_clients()
    loader = FileLoader()
    data = json.loads(loader.load('master_repo.json', '{}'))
    loader.load('repos.json', '{}')
    loader.load('labels.json', '[]')
    loader.load('credentials.json', '{}')
    if len(data) != 0:
        client = make_master_client(data)
        try:
            response = client.ping_repo()
            app.config["master_client"] = client
            if response.status_code == 200:
                app.config["repositories"] = load_repos(client)
                repo_cache = RepoCache(client, FileLoader())
                repo_cache.update_cache()
                make_clients(app.config["repositories"], app.config["client_factory"])

        except Exception:
            pass

    app.register_blueprint(labelsync_blueprint)

    return app

app = create_app()
