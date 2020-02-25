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

    required.add_argument('-O','--repoOwner', type=str, required=True, help="De eigenaar van de repo waar de issues in komen")
    required.add_argument('-R','--repo', type=str, required=True, help="De repo waar de issues in komen")
    parser.add_argument('-F','--file', type=str, required=False, default="input.yaml", help="De file waar de issues in staan")

    args = parser.parse_args()

    service.valideerStrInputs(args)

    token = service.getToken()
    with open(args.file) as file:
        issues = yaml.full_load(file)

        for issue in issues:
            print(issue)
            service.create(args.repoOwner, args.repo, issue["title"], issue["body"], token, labels=issue["labels"])

if __name__ == '__main__':
    main()
