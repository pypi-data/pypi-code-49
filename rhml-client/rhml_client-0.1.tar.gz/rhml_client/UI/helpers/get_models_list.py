from . import configuration;
from rhythmic import rhythmicDB, faultReturnHandler;
from .db_record_to_dictionary import modelPropertiesDictionary;
import requests;

@faultReturnHandler
def getModelDeployStatus(model_data_dict):
    """
    the model_data_dictionary has only two compulsory fields: "deploy_id" and "deploy_destination".
    others are unnecessary in this method.
    """

    if model_data_dict["deploy_id"] != 0:
        status_request_url = "{}/status/{}".format(model_data_dict["deploy_destination"], model_data_dict["deploy_id"]);
        try:
            the_response = requests.post(status_request_url);
            if the_response.status_code == 200:
                the_model_status = the_response.text;
            else:
                the_model_status = "Error: returned code {}".format(the_response.status_code);
        except Exception as e:
            the_model_status = "Error: {}".format(e);
    else:
        the_model_status = "Not deployed";

    return the_model_status;

@faultReturnHandler
def getModelsList():

    with rhythmicDB(configuration.db_name, configuration.db_file_name) as db:
        models_table = db.execute(
            """
            SELECT * FROM models_table WHERE 1 ORDER BY last_version_timestamp DESC;
            """);

    models = [];

    for stored_model in models_table:

        the_model = modelPropertiesDictionary(stored_model);
        the_model["deploy_status"] = getModelDeployStatus(the_model);
        models.append(the_model);

    return models;