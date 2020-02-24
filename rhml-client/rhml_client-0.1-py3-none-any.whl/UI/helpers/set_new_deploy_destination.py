from rhythmic import rhythmicDB, faultReturnHandler;
from . import configuration;

@faultReturnHandler
def setNewModelDeployDestination(model_id, new_deploy_destionation):
    with rhythmicDB(configuration.db_name, configuration.db_file_name) as db:
        db.execute("UPDATE models_table SET deploy_destination = '{}' WHERE id = '{}';".format(new_deploy_destionation, model_id));

    return "Success";