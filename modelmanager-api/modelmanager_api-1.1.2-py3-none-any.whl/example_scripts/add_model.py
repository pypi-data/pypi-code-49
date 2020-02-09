from modelmanager_api import Model

secret_key = "cf52f46e85c61801a427bf4d1fa79d074072b273"

url = 'http://modelmanager.ai'
path =  'api_assets'
#for data
data = {
    "project":14,
    "transformerType": "logistic",
    "target_column": "id",
    "note": "api script Model",
    "model_area": "api script Model",
    "model_dependencies": "api script Model",
    "model_usage": "api script Model",
    "model_audjustment": "api script Model",
    "model_developer": "api script Model",
    "model_approver": "api script Model",
    "model_maintenance": "api script Model",
    "documentation_code": "api script Model",
    "implementation_plateform": "api script Model",
    "training_dataset": "%s/model_assets/train.csv" % path,
    "pred_dataset": "%s/model_assets/submissionsample.csv" % path,
    "actual_dataset": "%s/model_assets/truth.csv" % path,
    "test_dataset": "%s/model_assets/test.csv" % path,
    "model_file_path":"",
    "scoring_file_path":"",
    "production":"",
    "current_date":"",
}

try:
    Model(secret_key, url).post_model(data)
except ConnectionResetError as e:
    print(str(e))

        