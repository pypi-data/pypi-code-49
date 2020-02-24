from flask import send_file, safe_join;
from .packer import packFiles;
from . import configuration;
import json;
import requests;
from rhythmic import rhythmicDB;

def deployModel(data):
    """
    var data = 
    {
        "deploy_url": window.actual_deploy_destination,
        "deploy_id": window.the_model_deploy_id,
        "model_path": window.model_path,
        "model_name": window.the_model_name,
        "model_id": window.the_model_id,
        "version_number": window.active_version_number,
        "files_data": window.active_version_files_data,
        "model_metadata": encodeURI(window.actual_metadata)
}
    """

    deploy_url = "{}/deploy".format(data["deploy_url"]);

    deploy_data = {};

    excluded_properties = \
    [
        "deploy_url",
        "model_path",
        "files_data"
    ];

    for the_property in data:
        if the_property not in excluded_properties:
            deploy_data[the_property] = data[the_property];

    deploy_data_json = json.dumps(deploy_data);

    deployed_files = {};

    for the_file in data["files_data"]:
        if data["files_data"][the_file]["is_deployed"]:
            deployed_files[the_file] = data["files_data"][the_file];

    package_name = "deploy_{}_{}.zip".format(data["model_id"], data["deploy_id"]);
    data_file_name = "deploy_{}_{}.json".format(data["model_id"], data["deploy_id"]);
    package_path = "{}/{}/{}".format(data["model_path"], configuration.storage_folder_name, package_name);
    data_file_path = "{}/{}/{}".format(data["model_path"], configuration.storage_folder_name, data_file_name);

    with open(data_file_path, "w+") as deploy_data_file:
        deploy_data_file.write(deploy_data_json);

    packFiles(data["model_path"], package_path, deployed_files);

    package_file = open(package_path, "rb");
    data_file = open(data_file_path, "rb");
    
    deploy_files = {data_file_name: data_file, package_name: package_file};

    try:
        files_deploy_result = requests.post(deploy_url, files = deploy_files);
    except Exception as e:
        return "Deploy failed: {}".format(e);

    package_file.close();
    data_file.close();



    deploy_execution_data_json = files_deploy_result.content;
    deploy_execution_data = json.loads(deploy_execution_data_json);

    # ***** deploy_result["model_deploy_id"] = model_deploy_id;
    # ***** deploy_result["status"] = "Success";

    deploy_id = deploy_execution_data["model_deploy_id"];
    deploy_status = deploy_execution_data["status"];

    if deploy_id != data["deploy_id"]:
        with rhythmicDB(configuration.db_name, configuration.db_file_name) as db:
            db.execute(
                """
                UPDATE models_table SET
                    deploy_id = '{}'
                WHERE id = '{}';
                """.format(
                                    deploy_id,
                                    data["model_id"]
                                )
            );


    return deploy_status;