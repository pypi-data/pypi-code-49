import argparse
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"/..")
from githubToolsUcll import service


# de student pullt alle issues van de hoofd-repo na het clonen van de start-code
def main():
    parser = argparse.ArgumentParser(description="Script voor het pullen van issues om opdrachten te krijgen")
    required = parser.add_argument_group("required arguments")

    required.add_argument('-Oo','--originRepoOwner', type=str, required=True, help="De GitHub naam van de lector")
    required.add_argument('-Or','--originRepo', type=str, required=True, help="De repo waar de opdracht staat")
    required.add_argument('-Do','--destinationRepoOwner', type=str, required=True, help="Uw GitHub naam")
    required.add_argument('-Dr','--destinationRepo', type=str, required=True, help="Uw repository naam test")

    args = parser.parse_args()

    service.valideerStrInputs(args)

    token = service.getToken()
    service.pull(args.originRepoOwner, args.originRepo, args.destinationRepoOwner, args.destinationRepo, token)

if __name__ == '__main__':
    main()
