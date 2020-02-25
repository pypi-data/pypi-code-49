import requests
import time
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+'/..')
def ratelimit(response):
    if response==429 or response==403:
        print ("It seems you made too many requests, please try again in an hour")
        exit()

def getToken():
    with open(dir_path+'/../token.txt', 'r') as file:
	    return file.readline().strip()

def valideerStrInputs(args):
    errors = False
    for arg in vars(args):
        if type(getattr(args, arg)) is str and not getattr(args, arg).strip(): # als value van arg (die str is) leeg is
            errors = True
            print(arg + " mag niet leeg zijn")

    if errors:
        exit()

def create(repoOwner, repo, title, body, token, labels = []):
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }

    r = requests.post("https://api.github.com/repos/" + repoOwner + "/" + repo + "/issues", auth=("", token), json=data)
    ratelimit(r.status_code)
    if r.status_code != 201:
        print(r.status_code)
        print("Er was een fout bij het aanmaken van de issue, controleer de argumenten:")
        print("Repo owner: " + repoOwner)
        print("Repo: " + repo)
        print("Issue title: " + title)
        print("Issue body: " + body)
        print("Issue labels: " + str(labels))
        exit()
    return r

def update(repoOwner, repo, number, body, token):
    data = {
        "body": body,
        "state": "open"
    }
    r = requests.post("https://api.github.com/repos/" + repoOwner + "/" + repo + "/issues/" + str(number), auth=("", token), json=data)
    ratelimit(r.status_code)
    if r.status_code != 201 and r.status_code !=200:
        print(r.status_code)
        print("Er was een fout bij het editen van de issue, controleer de argumenten:")
        print("Repo owner: " + repoOwner)
        print("Repo: " + repo)
        print("Issue body: " + body)
        print("Issue nubmer: " + str(number))
        exit()
    print("issue nummer " + str(number) + " is aangepast, check voor aanpassingen aan de opgave")
    return r

def push(originRepoOwner, originRepo, organisation, prefix, issueIds, token):
    if prefix.strip() == "":
        print("geen prefix opgegeven")
        exit()
    if issueIds == []:
        print("geen issue IDs opgegeven")
        exit()    

    repos = requests.get("https://api.github.com/orgs/" + organisation + "/repos", auth=("", token))
    ratelimit(repos.status_code)
    if repos.status_code != 200:
        print("Er was een fout bij het ophalen van de repositories uit de organisation, controleer de argumenten")
        exit()

    destinationRepos = []
    for repo in repos.json():
        repo = repo["name"]
        if repo.startswith(prefix):
                destinationRepos.append(repo)

    originIssues = requests.get("https://api.github.com/repos/"+originRepoOwner+"/"+originRepo+"/issues?direction=asc&per_page=100", auth=("", token))
    ratelimit(originIssues.status_code)
    if originIssues.status_code != 200:
        print("Er was een fout bij het ophalen van de issues uit de origin repo, controleer de argumenten")
        exit()
    originJson = originIssues.json()
    while 'next' in originIssues.links.keys():
        originIssues=requests.get(originIssues.links['next']['url'],headers={"Authorization": token})
        ratelimit(originIssues.status_code)
        if originIssues.status_code != 200:
            print("Er was een fout bij het ophalen van de issues uit de origin repo, controleer de argumenten")
            exit()
        originJson.extend(originIssues.json())

    transferIssues = []
    for issue in originJson:
        if issue["number"] in issueIds and "pull_request" not in issue.keys():
            transferIssues.append(issue)
    returnValue=[]
    for repo in destinationRepos:
        returnValue.append(copyIssues(organisation,repo,transferIssues,token))
    return returnValue

def pull(originRepoOwner, originRepo, destinationRepoOwner, destinationRepo, token):
    originJson= getIssues(originRepoOwner,originRepo,token)
    return copyIssues(destinationRepoOwner,destinationRepo,originJson,token)
    
def copyIssues(destinationRepoOwner, destinationRepo, sourceIssues, token):
    destinationIssues = requests.get("https://api.github.com/repos/" + destinationRepoOwner + "/" + destinationRepo + "/issues?state=all&direction=asc&per_page=100", auth=("", token))
    ratelimit(destinationIssues.status_code)
    if destinationIssues.status_code != 200:
        print("Er was een fout bij het ophalen van de issues uit de destination repo, controleer de argumenten")
        exit()
    destinationJson=destinationIssues.json()
    while 'next' in destinationIssues.links.keys():
        destinationIssues=requests.get(destinationIssues.links['next']['url'],headers={"Authorization": token})
        ratelimit(destinationIssues.status_code)
        if destinationIssues.status_code != 200:
            print("Er was een fout bij het ophalen van de issues uit de destination repo, controleer de argumenten")
            exit()
        destinationJson.extend(destinationIssues.json())

    destinationTitles = {}
    for issue in destinationJson:
        destinationTitles[issue["title"]] = [issue["body"],issue["number"]]
    returnValue = [False]
    for issue in sourceIssues:
        if "pull_request" not in issue.keys() and issue["title"] not in destinationTitles:
            returnValue.append(create(destinationRepoOwner, destinationRepo, issue["title"], issue["body"], token, issue["labels"]))
            returnValue[0]=True
        if issue["title"] in destinationTitles:
            if issue["body"] !=destinationTitles[issue["title"]][0]:
                returnValue.append(update(destinationRepoOwner, destinationRepo, destinationTitles[issue["title"]][1],issue["body"], token))
                returnValue[0]=True
    return returnValue

def getIssues(originRepoOwner, originRepo, token):
    originIssues = requests.get("https://api.github.com/repos/" + originRepoOwner + "/" + originRepo + "/issues?direction=asc&per_page=100", auth=("", token))
    ratelimit(originIssues.status_code)
    if originIssues.status_code != 200:
        print("Er was een fout bij het ophalen van de issues uit de origin repo, controleer de argumenten")
        exit()
    originJson = originIssues.json()
    while 'next' in originIssues.links.keys():
        originIssues=requests.get(originIssues.links['next']['url'],headers={"Authorization": token})
        ratelimit(originIssues.status_code)
        if originIssues.status_code != 200:
            print("Er was een fout bij het ophalen van de issues uit de origin repo, controleer de argumenten")
            exit()
        originJson.extend(originIssues.json())

    return originJson