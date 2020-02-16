from mmanager.mmanager import Model

secret_key = "Secret-Key"
url = 'URL' #enter url
path = 'api_assets'
model_id = 'Model_id'

data = {
    "transformerType": "logistic",
    "target_column": "id",
    "note": "api script Model Updated",
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
    "model_file_path":"", #not required
    "scoring_file_path":"", #not required
    "production":"", #not required
    "current_date":"", #not required
}

try:
    Model(secret_key, url).patch_model(data, model_id)
except ConnectionResetError as e:
    print(str(e))

