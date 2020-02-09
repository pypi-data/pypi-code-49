from modelmanager_api import Model

secret_key = "cf52f46e85c61801a427bf4d1fa79d074072b273"

url = 'http://modelmanager.ai'
model_id = 192 #use model id
#for data
try:
    Model(secret_key,url).delete_model(model_id)
except ConnectionResetError as e:
    print(str(e))

