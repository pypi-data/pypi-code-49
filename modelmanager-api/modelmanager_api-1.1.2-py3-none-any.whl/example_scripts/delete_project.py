from modelmanager_api import Usecase

secret_key = "cf52f46e85c61801a427bf4d1fa79d074072b273"

url = 'http://modelmanager.ai'
project_id =15
#for data
try:
    Usecase(secret_key,url).delete_usecase(project_id)
except ConnectionResetError as e:
    print(str(e))
