from abc import abstractmethod
import os
import requests
import json
import logging
from rq import Worker, Queue
from redis import Redis
import traceback
from rq.job import Job, JobStatus
import time
from prometheus_client import make_wsgi_app, Histogram
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import threading
from werkzeug.serving import run_simple


class PluginSkeleton(object):
    redis = None
    FAILED = "failed"
    SUCCESS = "success"
    PROMETHEUS_PORT = 8000

    #

    def __init__(self):
        os.environ['PLUGIN_CODE'] = "{}/{}".format(os.environ.get('PLUGIN_CODE'), self.plugin_version_name())
        os.environ['JOB_QUEUE'] = "{}/{}".format(os.environ.get('JOB_QUEUE'), self.plugin_version_name())
        logging.info("Init connection to redis {}:{}".format(os.environ.get('REDIS_HOST'),
                                                             os.environ.get('REDIS_PORT')))
        PluginSkeleton.redis = Redis(host=os.environ.get('REDIS_HOST'),
                                     port=os.environ.get('REDIS_PORT'))
        logging.info("Redis info: {}".format(PluginSkeleton.redis.info()))

    @abstractmethod
    def preload(self):
        pass

    @abstractmethod
    def plugin_version_name(self):
        return "normal"

    @abstractmethod
    def check_plugin_live(self):
        try:
            if PluginSkeleton.redis.ping():
                return "OK", 200
            else:
                return "FAILURE", 500
        except:
            return "FAILURE", 500

    @abstractmethod
    def check_plugin_ready(self):
        return "OK", 200

    def start_prometheus(self, port):
        """Starts a WSGI server for prometheus metrics as a daemon thread."""
        # Create my app
        app = Flask(__name__)

        # Add prometheus wsgi middleware to route /metrics requests
        app_dispatch = DispatcherMiddleware(app, {
            '/metrics': make_wsgi_app()
        })
        plugin_handle_time = Histogram('handle_process_time', 'Handle time')

        @app.route("/histogram/<float:handle_time>", methods=['GET'])
        def histogram_handle_time(handle_time):
            plugin_handle_time.observe(handle_time)
            return str(handle_time)

        @app.route("/health/live", methods=['GET'])
        def check_plugin_live():
            return self.check_plugin_live()

        @app.route("/health/ready", methods=['GET'])
        def check_plugin_ready():
            return self.check_plugin_ready()

        def run_app():
            run_simple('localhost', port, app_dispatch)

        t = threading.Thread(target=run_app)
        t.daemon = True
        t.start()

    @staticmethod
    def registry_plugin(file_exec, func_exec, version_code, version_name):
        assert version_name is not None, "version_name none is not accepted"
        try:
            payload = {
                "description": os.environ.get('PLUGIN_DESCRIPTION'),
                "job_queue_name": os.environ.get('JOB_QUEUE'),
                "function_name": "{}.{}".format(file_exec[file_exec.rindex(os.sep) + 1:file_exec.rindex('.')],
                                                func_exec.__name__),
                "plugin_name": os.environ.get('PLUGIN_NAME'),
                "plugin_code": os.environ.get('PLUGIN_CODE'),
                "depended_plugin_code": os.environ.get('DEPENDED_PLUGIN_CODE'),
                "plugin_version_code": version_code,
            }
            headers = {
                'Content-Type': "application/json"
            }
            logging.info("Resister worker: {}".format(json.dumps(payload)))
            response = requests.request("POST", os.environ.get('BACKEND_ENDPOINT'), data=json.dumps(payload),
                                        headers=headers, timeout=10)

            return response.status_code
        except:
            return 500

    @staticmethod
    def handler_error(job, exc_type, exc_value, traceback_):
        job_id = job.id
        job_index = job.args[0]
        description_error = " ".join(traceback.format_exception(exc_type, exc_value, traceback_))
        logging.info(job, traceback)
        PluginSkeleton.push_job_status(job_id, job_index, PluginSkeleton.FAILED, description=description_error)

    def run(self, file_exec, func_exec, version_code, ignore_register=False):
        # register plugin
        register_status = self.registry_plugin(file_exec, func_exec, version_code, self.plugin_version_name())
        if register_status == 201 or ignore_register:
            logging.info('Plugin {} Resisted'.format(os.environ.get('PLUGIN_NAME')))
            self.preload()
            # Start up the server to expose the metrics.
            # logging.info('Start Prometheus service on port {}'.format(8000))
            # start_http_server(8000)
            self.start_prometheus(PluginSkeleton.PROMETHEUS_PORT)
            queue = Queue(name=os.environ.get('JOB_QUEUE'), connection=PluginSkeleton.redis)
            # Start a worker with a custom name
            worker = Worker([queue], connection=PluginSkeleton.redis, exception_handlers=[PluginSkeleton.handler_error])
            worker.work(logging_level="INFO")
        else:
            logging.error('Plugin {} register failed'.format(os.environ.get('PLUGIN_NAME')))

    @staticmethod
    def push_job_status(doc_id, doc_index, result, description=None):
        global START_PROCESS_TIME
        if "START_PROCESS_TIME" not in globals():
            START_PROCESS_TIME = -1
        handle_process_time = time.time() - START_PROCESS_TIME if START_PROCESS_TIME > 0 else None
        output = {
            "id": doc_id,
            "index": doc_index + "_log",
            "status": result,
            "end_process_time": time.time(),
            "handle_process_time": handle_process_time,
            "traceback": description
        }
        if handle_process_time:
            r = requests.get(url='http://localhost:{}/histogram/{}'.format(PluginSkeleton.PROMETHEUS_PORT,
                                                                           handle_process_time))
            logging.info("Handle time {}".format(r.text))
        START_PROCESS_TIME = -1
        return PluginSkeleton.redis.lpush('result', json.dumps(output))

    @staticmethod
    def push_start_time_process(doc_id, doc_index):
        global START_PROCESS_TIME
        START_PROCESS_TIME = time.time()
        output = {
            "id": doc_id,
            "index": doc_index + "_log",
            "start_process_time": START_PROCESS_TIME
        }
        return PluginSkeleton.redis.lpush('result', json.dumps(output))

    @staticmethod
    def push_result(current_job, doc_index, doc_id, result, version_code):
        output = {
            "id": doc_id,
            "index": doc_index,
            "plugin_code": os.environ.get('PLUGIN_CODE'),
            os.environ.get('PLUGIN_CODE'): {
                "version_code": version_code,
                "update_time": time.time(),
                "data": result
            }
        }

        push_result = PluginSkeleton.redis.lpush('result', json.dumps(output))

        if push_result > 0:
            logging.info("Push success {}".format(json.dumps(output)))
            PluginSkeleton.push_job_status(current_job.get_id(), doc_index, PluginSkeleton.SUCCESS)
        else:
            PluginSkeleton.push_job_status(current_job.get_id(),
                                           doc_index,
                                           PluginSkeleton.FAILED,
                                           description="Push result error")

        return PluginSkeleton.get_output_result(result, version_code)

    @staticmethod
    def get_output_result(result, version_code):
        output = {
            os.environ.get('PLUGIN_CODE'): {
                "version_code": version_code,
                "data": result
            }
        }
        return output

    @staticmethod
    def get_depended_jobs_output(current_job, input_data, depended_jobs=None):
        """
        :param input_data:
        :param current_job:
        :param depended_jobs: {
            "plugin_code": "job_id",
            "plugin_code": "job_id",
                ...
        }
        :return:
        """
        previous_job = current_job.dependency
        if previous_job:
            results = {}
            # append input_data with depended on job result
            for item in previous_job.result.items():
                results[item[0][:item[0].index('/')]] = item[1]
            PluginSkeleton.push_start_time_process(current_job.get_id(), current_job.args[0])
            return results
        elif depended_jobs:
            jobs = {item[0]: Job.fetch(item[1], connection=PluginSkeleton.redis) for item in depended_jobs.items()}
            while True:
                jobs_status = [item.get_status() for item in jobs.values()]
                count_jobs_failed = jobs_status.count(JobStatus.FAILED)
                if count_jobs_failed > 0:
                    PluginSkeleton.push_start_time_process(current_job.get_id(), current_job.args[0])
                    return None
                count_jobs_finish = jobs_status.count(JobStatus.FINISHED)
                if count_jobs_finish == len(jobs):
                    results = {item[0][:item[0].index('/')]: item[1].result[item[0]] for item in jobs.items()}
                    if input_data:
                        # append input_data with depended on job result
                        for item in input_data.items():
                            if not results.get(item[0]):
                                results[item[0][:item[0].index('/')]] = item[1]
                    PluginSkeleton.push_start_time_process(current_job.get_id(), current_job.args[0])
                    return results
                time.sleep(0.1)
        else:
            results = {}
            # append input_data with depended on job result
            for item in input_data.items():
                results[item[0][:item[0].index('/')]] = item[1]

            PluginSkeleton.push_start_time_process(current_job.get_id(), current_job.args[0])
            return results
