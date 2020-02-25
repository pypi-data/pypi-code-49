import argparse
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"/..")
from githubToolsUcll import service
import xlwt
import xlrd
import requests
import git


def main():
    parser = argparse.ArgumentParser(description="Script voor het pullen van issues om opdrachten te krijgen")
    required = parser.add_argument_group("required arguments")

    required.add_argument('-O','--organisation', type=str, required=True, help="Organisation die de student repos bevat")
    required.add_argument('-P','--prefix', type=str, required=True, help="Prefix van de studenten repos")
    required.add_argument('-St','--students', type=str, required=True, help="path naar de excel file waar de studenten met hun github instaan")
    parser.add_argument('-Sh','--sheet', type=int, required=False, default=0, help="Sheet number, default 0")
    parser.add_argument('-D','--destination', type=str, required=False,default=".", help="path naar de gewenste directory waarin de structuur begint, default = .")

    args = parser.parse_args()
    
    token = service.getToken()
    
    wb = xlrd.open_workbook(args.students)
    sheet = wb.sheet_by_index(args.sheet)
    dictionary = {}
    for i in range(sheet.nrows):
        dictionary[sheet.cell_value(i,0)]=sheet.cell_value(i,1)

    repos = requests.get("https://api.github.com/orgs/" + args.organisation + "/repos?per_page=100", auth=("", token))
    service.ratelimit(repos.status_code)
    if repos.status_code != 200:
        print("Er was een fout bij het ophalen van de repositories uit de organisation, controleer de argumenten")
        exit()
    allRepos = repos.json()
    while 'next' in repos.links.keys():
        repos=requests.get(repos.links['next']['url'],headers={"Authorization": token})
        service.ratelimit(repos.status_code)
        if repos.status_code != 200:
            print("Er was een fout bij het ophalen van de repositories uit de organisation, controleer de argumenten")
            exit()
        allRepos.extend(repos.json())
    destinationRepos = []

    for repo in allRepos:
        repo = repo["name"]
        if repo.startswith(args.prefix):
                destinationRepos.append(repo)

    for repo in destinationRepos:
        try:
            name = dictionary[repo.replace(args.prefix+"-","")]
            path = args.destination+"\\"+name
            if os.path.isdir(path):
                if git.Git(path).pull() != "Already up to date.":
                    print(name+" has been updated.")
            else:
                os.mkdir(path)
                git.Git(".").clone("https://github.com/"+args.organisation+"/"+repo, name)
                print(name+" has been created")
        except KeyError as e:
            print(str(e) + " staat niet in de opgegeven excel sheet")
    
if __name__ == '__main__':
    main()
