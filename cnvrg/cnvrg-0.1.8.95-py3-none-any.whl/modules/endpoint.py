from cnvrg.modules.cnvrg_job import CnvrgJob
from cnvrg.modules.project import Project
import cnvrg.helpers.string_helper as string_helper
import cnvrg.helpers.param_build_helper as param_build_helper
from cnvrg.helpers.env_helper import CURRENT_JOB_TYPE, CURRENT_JOB_ID, ENDPOINT, POOL_SIZE
from cnvrg.modules.errors import UserError
from cnvrg.helpers.url_builder_helper import url_join
import cnvrg.helpers.parallel_helper as parallel_helper
import cnvrg.helpers.apis_helper as apis_helper
import json
import sys
import time
import os
import requests
import datetime
import traceback

class Endpoint(CnvrgJob):
    def __init__(self, endpoint=None):
        owner, project_slug, slug = param_build_helper.parse_params(endpoint, param_build_helper.ENDPOINT)
        if not slug:
            raise UserError("Cant create an endpoint without slug")
        slug = slug or CURRENT_JOB_ID
        self.model_name = os.environ.get("CNVRG_MODEL_NAME", "unknown")
        self.log_input = self.should_log_input()
        self.log_output = self.should_log_output()
        super(Endpoint, self).__init__(slug, ENDPOINT, Project(url_join(owner, project_slug)))
        self.__data = None


    def __base_log(self, **params):
        log = {
            "job_id": self.job_slug,
            "job_type": self.job_type,
            "owner": self.job_owner_slug,
            "project": self.job_project_slug,
            "model": self.model_name,
            "event_time": time.time(),
            **params
        }
        print(json.dumps(log))
        sys.stdout.flush()

    def log_request(self, input_params="", result="", start_time=None):
        hash = {}
        if self.log_input:
            hash["input"] = str(input_params)
        if self.log_output:
            hash["output"] = str(result)
        hash["start_time"] = str(datetime.datetime.utcfromtimestamp(int(start_time)))
        end_time = time.time()
        elapsed_time = int((end_time - start_time) * 1000)  # ms
        hash["elapsed_time"] = elapsed_time
        self.__base_log(**hash)

    def log_error(self, e, trace=False):
        hash = {}
        hash["error"] = str(e)
        if trace:
            hash["traceback"] = traceback.format_exc()
        self.__base_log(**hash)

    def log_param(self, tag_name=None, tag_value=None):
        hash = {}
        hash[tag_name] = tag_value
        hash["cnvrg_tag_name"] = tag_name
        self.__base_log(**hash)

    def log_metric(self, name=None, y:float=None, x=None):
        hash = {}
        try:
            hash[name] = float(y)
            hash["y"] = float(y)
        except Exception as e:
            print("ERROR {}".format(e), file=sys.stderr)
            return
        hash["x"] = x
        hash["cnvrg_metric_name"] = name
        self.__base_log(**hash)

    def log_prediction(self, input=None, output=None, elapsed_time=0):
        start_time = datetime.datetime.utcnow().strftime("%c")
        self.__base_log(input=input, output=output, elapsed_time=elapsed_time, start_time=start_time)

    @property
    def session(self):
        return self.__session()

    @property
    def data(self):
        if self.__data:
            return self.__data
        self.__data = self.__get_endpoint()
        return self.__data

    def __get_endpoint(self):
        return apis_helper.get(self.__base_url()).get("endpoint")

    def __base_url(self):
        return url_join(
            self.project.get_base_url(), string_helper.to_snake_case(self.job_type) + "s", self.job_slug
        )

    def __session(self):
        session = requests.session()
        session.headers = {
            **apis_helper.JSON_HEADERS,
            "Cnvrg-Api-Key": self.data.get("api_key")
        }
        return session

    def predict(self, o):
        return self.session.post(self.data.get("endpoint_url"), data=json.dumps({"input_params": o})).json()

    def single_batch_predict(self, o):
        prediction = self.predict(o)
        if isinstance(o, dict):
            return {**o, **prediction}
        else:
            return {"query": o, **prediction}

    def batch_predict(self, array: list, pool_size: int=POOL_SIZE):
        return parallel_helper.safe_parallel(self.single_batch_predict, array, pool_size=pool_size, progressbar={"total": len(array), "desc": "Predicting"})

    def disable_log_input(self):
        self.log_input = False
        os.environ["CNVRG_ENDPOINT_LOG_INPUT"] = "false"

    def should_log_input(self):
        return os.environ.get("CNVRG_ENDPOINT_LOG_INPUT", "").lower() != "false"

    def disable_log_output(self):
        self.log_output = False
        os.environ["CNVRG_ENDPOINT_LOG_OUTPUT"] = "false"

    def should_log_output(self):
        return os.environ.get("CNVRG_ENDPOINT_LOG_OUTPUT", "").lower() != "false"
