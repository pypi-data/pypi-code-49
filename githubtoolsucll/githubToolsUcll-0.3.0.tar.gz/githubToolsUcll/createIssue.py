import argparse
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"/..")
from githubToolsUcll import service


def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group("required arguments")

    required.add_argument('-O','--repoOwner', type=str, required=True, help="De eigenaar van de repo waar de issue in komt")
    required.add_argument('-R','--repo', type=str, required=True, help="De repo waar de issue in komt")
    required.add_argument('-T','--title', type=str, required=True, help="Titel van de issue")
    required.add_argument('-B','--body', type=str, required=True, help="Body van de issue")

    args = parser.parse_args()

    service.valideerStrInputs(args)

    token = service.getToken()
    service.create(args.repoOwner, args.repo, args.title, args.body, token)

if __name__ == '__main__':
    main()
