import argparse
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"/..")
from githubToolsUcll import service
import yaml


def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group("required arguments")

    required.add_argument('-O','--repoOwner', type=str, required=True, help="De eigenaar van de repo waar de issues in staan")
    required.add_argument('-R','--repo', type=str, required=True, help="De repo waar de issues in staan")
    parser.add_argument('-F','--file', type=str, required=False, default="output.yaml", help="De file waar de issues in komen")

    args = parser.parse_args()

    service.valideerStrInputs(args)

    token = service.getToken()
    issuesJson=service.getIssues(args.repoOwner,args.repo,token)
    dict=[]
    for issue in issuesJson:
        dict.append({
            "title": issue["title"],
            "body": issue["body"],
            "lables": issue["labels"]
            })
    with open(args.file,"w+") as file:
        yaml.dump(dict,file)

if __name__ == '__main__':
    main()
