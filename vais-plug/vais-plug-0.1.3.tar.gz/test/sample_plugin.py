import json
import logging
from rq import get_current_job
from vais_plugin import plugin_skeleton
from vais_plugin.plugin_config import *


def handle_job(doc_index, doc_id, input_data=None, depended_jobs=None, config_json=None):
    """
    :param depended_jobs:
    :param doc_index:
    :param doc_id:
    :param input_data:
    {
        "plugin_code":{
            "data": {},
            "version_code": {}
        },
        "plugin_code":{
            "data": {},
            "version_code": {}
        },
        ...
    }
    :param config_json:

    {
        "global_config": {},
        "user_config": {}
    }
    :return: {
        "plugin_code":{
            "data": {},
            "version_code": {}
        }
    """
    current_job = get_current_job()
    config = Config.load_from_object(config_json) if config_json else None
    print(config)
    input_data = SamplePlugin.get_depended_jobs_output(current_job, input_data, depended_jobs)

    try:
        audio_id = input_data['audio_info']['data'].get('audio_id', None)
        if audio_id:
            output = {
                "status": 'success'
            }

            return plugin_skeleton.PluginSkeleton.push_result(current_job,
                                                              doc_index,
                                                              doc_id,
                                                              output,
                                                              SamplePlugin.VERSION_CODE)
        else:
            SamplePlugin.push_job_status(current_job.get_id(), doc_index,
                                         SamplePlugin.FAILED,
                                         description="handle job error")
    except:
        SamplePlugin.push_job_status(current_job.get_id(), doc_index,
                                     SamplePlugin.FAILED,
                                     description="handle job error")


class SamplePlugin(plugin_skeleton.PluginSkeleton):
    VERSION_CODE = 2

    # def __init__(self):
    #     config = Config()
    #     config.add_user_config(
    #         EditText(config_code='key_ignore', title="Keyword ignored", description="List of words will be ignored"))
    #     super().__init__(config=config)

    def preload(self):
        logging.info("Model loaded")
