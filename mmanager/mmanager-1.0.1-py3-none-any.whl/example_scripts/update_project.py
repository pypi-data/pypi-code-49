from mmanager.mmanager import Usecase

secret_key = "Secret-Key"

url = 'URL' #enter url
path =  'api_assets' #use assets path 
project_id = 'Project_id'

data = {
    "author": "sssdsadads",
    "description": "sss",
    "source": "ssssdsdsa",
    "contributor": "sdadssdssddass",
    "image": '%s/project_assets/thumbnail.jpg' % path,
    "banner": '%s/project_assets/banner.jpg' % path
}

try:
    Usecase(secret_key, url).patch_usecase(data, project_id)
except ConnectionResetError as e:
    print(str(e))

