from modelmanager_api import Usecase

secret_key = "cf52f46e85c61801a427bf4d1fa79d074072b273"

url = 'http://modelmanager.ai'
path =  'api_assets'
project_id = 14
#for data
data = {
    # "name": "test usecase",
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

