from rhythmic import rhythmicDB, faultReturnHandler;
from . import configuration, scanFolder;
from os import remove, rmdir as rmDir;
import requests;

@faultReturnHandler
def removeModel(data):
    """
    var data_for_helper =
    {
        "model_id": the_id,
        "model_path": model_path
    }
    """

    with rhythmicDB(configuration.db_name, configuration.db_file_name) as db:

        db.execute("PRAGMA foreign_keys = ON;");

        deploy_destination_request_result = \
        db.execute(
             """
             SELECT deploy_destination, deploy_id FROM models_table WHERE id = '{}'
             """.format(
                                data["model_id"]
                            )
 
                        );
        db.execute(
            """
            DELETE FROM models_table WHERE id = '{}';
            """.format(
                                data["model_id"]
                            )
            );

    model_storage_path = data["model_path"] + "/{}".format(configuration.storage_folder_name);

    versions_packages = scanFolder(model_storage_path, look_level_above = False);

    for version_package in versions_packages:
             remove(version_package);

    rmDir(model_storage_path);

    removal_operation_status = "Success";

    if deploy_destination_request_result:
        deploy_destination = deploy_destination_request_result[0][0];
        model_deploy_id = deploy_destination_request_result[0][1];
        print("{}/helpers/remove_deployment/{}".format(
                                                                                                                                                    deploy_destination,
                                                                                                                                                    model_deploy_id
                                                                                                                                                ));
        try:
            deploy_server_request_result = requests.post("{}/helpers/remove_deployment/{}".format(
                                                                                                                                                    deploy_destination,
                                                                                                                                                    model_deploy_id
                                                                                                                                                ));
            if deploy_server_request_result.status_code != 200:
                removal_operation_status = "Probably the deployment has to be removed manually from the server side: {}".\
                format(deploy_server_request_result.status_code);
        except Exception as what_is_wrong:
            removal_operation_status = "Probably the deployment has to be removed manually from the server side: {}".\
            format(what_is_wrong);
    print(removal_operation_status);
    return removal_operation_status;
