import argparse
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"/..")
from githubToolsUcll import service

def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group("required arguments")

    required.add_argument('-Oo','--originRepoOwner', type=str, required=True, help="De eigenaar van de repo van waar de issues komen")
    required.add_argument('-Or','--originRepo', type=str, required=True, help="De repo van waar de issues komen")
    required.add_argument('-Og','--organisation', type=str, required=True, help="Organisation die de student repos bevat")
    required.add_argument('-P','--prefix', type=str, required=True, help="Prefix van de studenten repos")
    # '+' == 1 or more.
    parser.add_argument('-I','--issueIds', nargs='+', type=int, required=True, help="Een lijst van issue ids die gekopierd moeten worden (--issueIds 1 2 5)")

    args = parser.parse_args()

    service.valideerStrInputs(args)
    
    token = service.getToken()
    service.push(args.originRepoOwner, args.originRepo, args.organisation, args.prefix, args.issueIds, token)

if __name__ == '__main__':
    main()
