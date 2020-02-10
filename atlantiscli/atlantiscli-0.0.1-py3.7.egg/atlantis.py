# -*- coding: utf-8 -*-
import tempfile
import os
import shutil
import socket
import logging
import logging.config
from pathlib import Path

from celery import Celery
from celery import signals
from celery.utils.log import get_task_logger

from kombu import Exchange, Queue

from wavescli.config import get_config
from wavescli.awsadapter import send_file
from wavescli.downloader import get_file
from wavescli.logger import WAVES_LOGGER_CONFIG


config = get_config()

app = Celery(config.WAVES_CLI_NAME)

# Atencao: pegar mais de 1 mensagem por vez pode ter perda
#          caso o container morra antes de processar todas
app.conf.broker_url = config.BROKER_URL
app.conf.result_backend = config.RESULT_BACKEND_URL

# Set the worker to fetch 1 message per time
app.conf.worker_prefetch_multiplier = 1
app.conf.task_acks_late = True

app.conf.worker_send_task_events = True
app.conf.task_track_started = True
app.conf.task_send_sent_event = True

app.conf.task_queues = (
    Queue(config.QUEUE_NAME,
          Exchange(config.QUEUE_NAME),
          routing_key=config.QUEUE_NAME),
)

BaseTask = app.create_task_cls()


def get_celery_app():
    signals.before_task_publish.connect(task_updated)
    signals.task_prerun.connect(task_started)
    signals.setup_logging.connect(worker_setup_logging)
    return app


class Values(object):
    pass


class WavesLogger(object):

    def __init__(self, logger, task):
        self._logger = logger
        self._task = task

    def info(self, message):
        identifier = self._task.identifier if self._task else 'no-identifier'
        self._logger.info(message, extra={'identifier': identifier})


def task_logger():
    celery_logger = get_task_logger
    return celery_logger


def worker_setup_logging(loglevel, logfile, format, colorize, **kwargs):
    logging.config.dictConfigClass(WAVES_LOGGER_CONFIG).configure()


def send_update_execution(
        identifier, task_id, task_name, task_root_id,
        task_parent_id, status=None, inputs=None, args=None, results=None, last_error=None, hostname=None):
    """
    Envia para fila default
    """

    params = (
        identifier,
        task_id,
        task_name,
        task_root_id,
        task_parent_id,
        status,
        inputs,
        args,
        results,
        last_error,
        hostname,
    )
    sig_status = app.signature(
        'awebrunner.update_execution',
        args=params,
        kwargs={},
        queue='celery',
    )
    sig_status.apply_async(countdown=60)


# @signals.before_task_publish.connect
def task_updated(sender=None, headers=None, body=None, **kwargs):
    """
    - Atualizacao de status de tasks existentes
    - Cria tasks em tempo de execucao
    """
    # logger.info("#Step-2(btask) Task published signal received by '{}'".format(sender))

    task_name = headers.get('task')
    task_id = headers.get('id')

    if task_name == 'awebrunner.update_execution':
        # logger.info("#Step-2(btask) Task published signal skipped")
        return True

    args_data, kwargs_data, signatures = body
    identifier = kwargs_data.get('identifier')
    task_root_id = headers.get('root_id')
    task_parent_id = headers.get('parent_id')

    # logger.info("[identifier:{}] #Step-2(btask) Publishing task: {} ({})".format(identifier, task_name, task_id))

    inputs = None
    if type(args_data) == tuple:
        results, inputs, *_ = args_data
        inputs = _handle_inputs(results, inputs['args'] if 'args' in inputs else inputs)

    send_update_execution(
        identifier=identifier,
        task_id=task_id,
        task_name=task_name,
        task_root_id=task_root_id,
        task_parent_id=task_parent_id,
        inputs=inputs if inputs else args_data,
        args=kwargs_data,)


# @signals.task_prerun.connect
def task_started(task_id, task, args, **kwargs):

    # logger.info("#Step-4(btask) Task pre run signal received: {} ".format(task_id))

    kw = kwargs.get('kwargs')
    identifier = kw.get('identifier')

    # logger.info("[identifier:{}] #Step-4(btask) Task pre run sending STARTED: {}".format(identifier, task_id))

    send_update_execution(
        identifier=identifier,
        task_id=task_id,
        task_name=None,
        task_root_id=None,
        task_parent_id=None,
        inputs=None,
        status='STARTED',
        args=kw)


@app.task(name='waves.ping')
def task_ping(seconds=10):
    import time
    time.sleep(seconds)
    return "pong"


def _handle_inputs(results, inputs):

    if type(inputs) == dict and inputs.get('inputs'):
        inputs = inputs.get('inputs')

    if results is not None:   # and type(inputs) == dict:
        if type(results) == dict:
            # inputs.update(results)
            inputs = results
        elif type(results) == list:
            # inputs['items'] = results
            inputs = {
                'items': results
            }
    return inputs


class WavesBaseTask(BaseTask):
    """Abstract base class for all tasks in my app."""

    abstract = True

    def _initialize(self):
        self._clean_attrs()
        self.inputs = Values()
        self.outputs = Values()

    def _clean_attrs(self):
        for attr in ['call_updated', 'downloaded', 'uploaded', 'on_success_updated']:
            try:
                delattr(self, attr)
            except Exception:
                pass

    def _generate_task_attributes(self, args, kwargs):
        results, inputs = args
        inputs = _handle_inputs(results, inputs)

        self.inputs_values = inputs
        self.outputs_values = kwargs.get('outputs', {})
        self.auto_download = kwargs.get('auto_download', [])
        self.auto_upload = kwargs.get('auto_upload', [])
        self.make_public = kwargs.get('make_public', [])
        self.identifier = kwargs.get('identifier')
        self.bucket = kwargs.get('bucket')

        self.task_id = self.request.id
        self.task_dir = os.path.join(tempfile.gettempdir(), self.task_id)
        self.inputs_dir = os.path.join(self.task_dir, 'inputs')
        self.outputs_dir = os.path.join(self.task_dir, 'outputs')

    def _download_inputs(self):
        if type(self.inputs_values) != dict:
            return

        for item in self.inputs_values.keys():
            self.inputs.__setattr__(item, self.inputs_values.get(item))
            if item not in self.auto_download:
                continue
            try:
                local_file = get_file(
                    self.inputs_values[item], self.inputs_dir)
                self.inputs.__setattr__(item, local_file)

            except Exception as error:
                raise RuntimeError('Error downloading: {}'.format(self.inputs_values.get(item)), error)
        self.downloaded = True

    def _upload_outputs(self, outputs, target):
        for item in self.auto_upload:
            try:

                if item.startswith('items.') and 'items' in outputs:
                    for subitem_dict in outputs['items']:
                        subitem = item.replace('items.', '')
                        local_file_path = self._replace_vars(subitem_dict[subitem])
                        filename = os.path.basename(local_file_path)
                        remote_path = '{}/{}'.format(target, filename)
                        remote_file = send_file(
                            local_file_path, self.bucket, remote_path)
                        subitem_dict[subitem] = remote_file
                else:
                    local_file_path = self._replace_vars(outputs[item])
                    filename = os.path.basename(local_file_path)
                    remote_path = '{}/{}'.format(target, filename)
                    remote_file = send_file(
                        local_file_path, self.bucket, remote_path)
                    outputs[item] = remote_file

            except Exception as error:
                raise RuntimeError('Error uploading: {}'.format(local_file_path), error)
        self.uploaded = True
        return outputs

    def _get_task_state(self):
        if self.request.id:
            return str(app.AsyncResult(self.request.id).state)

    def _update_execution(self, identifier, task_id,
                          inputs=None, params=None, result=None, status=None, last_error=None):
        if not status:
            status = self._get_task_state()

        if status in ['SUCCESS', 'FAILURE']:
            # private_ip = socket.gethostbyname(socket.gethostname())
            private_ip = os.getenv('WORKER_PRIVATE_IP')
            hostname = '{}@{}'.format(self.request.task, private_ip)
            self.info("----> status:{} hostname:{}".format(status, hostname))

        send_update_execution(
            identifier=identifier,
            task_id=task_id,
            task_name=self.request.task,
            task_root_id=self.request.root_id,
            task_parent_id=self.request.parent_id,
            status=status,
            inputs=inputs,
            args=params,
            results=result,
            last_error=last_error,
            hostname=hostname)

    def _create_temp_task_folders(self):
        os.makedirs(self.inputs_dir)
        os.makedirs(self.outputs_dir)

    def _delete_temp_task_folders(self):
        shutil.rmtree(self.task_dir)

    def _get_env_variables(self, kwargs):
        env = kwargs.get('env', {})
        env['TASK_ID'] = self.request.id
        env['INPUTS_DIR'] = self.inputs_dir
        env['OUTPUTS_DIR'] = self.outputs_dir
        env['IDENTIFIER'] = self.identifier
        env['BUCKET'] = self.bucket
        return env

    def __call__(self, *args, **kwargs):
        self._initialize()
        self._generate_task_attributes(args, kwargs)

        if not hasattr(self, 'downloaded'):
            self._create_temp_task_folders()
            self._download_inputs()
        self.info("WAVES CALL")
        return super(WavesBaseTask, self).__call__(*args, **kwargs)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        super(WavesBaseTask, self).on_retry(exc, task_id, args, kwargs, einfo)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        error = self.get_task_error_details(exc, task_id, args, kwargs, einfo)
        self._update_execution(
            kwargs['identifier'], task_id, status='FAILURE', last_error=error)
        self.info("WAVES ON FAILURE")
        super(WavesBaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)

    def send_auto_upload_outputs(self, delete_temp_folders=True):
        if hasattr(self, 'uploaded'):
            return self.results

        target = '{}/{}/{}'.format(config.WAVES_RESULTS_PATH, self.identifier, self.task_id)
        self.results = self._upload_outputs(self.results, target)

        if delete_temp_folders:
            self._delete_temp_task_folders()
        self.info("WAVES SEND AUTO UPLOAD")
        return self.results

    def folder_to_zip(self, source_folder, compress_format='zip'):
        """
        Zip the source folder and returns the zip file path

        Usage:
          self.folder_to_zip('/tmp/EXEC1/task1/outputs/MYFOLDER')
          returns '/tmp/EXEC1/task1/outputs/MYFOLDER.zip'
        """
        source_folder = Path(source_folder)
        self.info("WAVES FOLDER TO ZIP")
        return shutil.make_archive(
            str(source_folder),
            compress_format,
            root_dir=str(source_folder.parent),
            base_dir=source_folder.name)

    def on_success(self, retval, task_id, args, kwargs):
        if not hasattr(self, 'results'):
            self.results = retval

        results = self.results
        if not hasattr(self, 'on_success_updated'):
            self._update_execution(
                kwargs['identifier'], self.request.id, result=results)
        self.info("WAVES ON SUCCESS")
        super(WavesBaseTask, self).on_success(results, task_id, args, kwargs)

    def _replace_vars(self, text):
        self.info("WAVES REPLACE VARS")
        if type(self.inputs_values) == dict:
            for item in self.inputs_values.keys():
                in_value = self.inputs_values[item]

                if type(in_value) == dict or type(in_value) == list:
                    continue
                if in_value:
                    original = '${{ ' + 'inputs.{}'.format(item) + ' }}'
                    text = text.replace(original, str(self.inputs.__getattribute__(item)))

        if type(self.outputs_values) == dict:
            for item in self.outputs_values.keys():
                out_value = self.outputs_values[item]
                if type(out_value) == dict or type(out_value) == list:
                    continue
                if out_value:
                    original = '${{ ' + 'outputs.{}'.format(item) + ' }}'
                    text = text.replace(original, str(out_value))
        return text

    def get_task_error_details(self, exc, task_id, args, kwargs, traceback):
        """
        Return the task error based on the exception
        """
        error = '''{}\n{}'''.format(str(exc).strip(), str(traceback).strip())
        return error

    def get_logger(self, logger):
        self._logger = WavesLogger(logger, self)
        return self._logger

    def info(self, message):
        try:
            l = self._logger
            if not l:
                l = logger
            l.info(message)
        except Exception:
            pass
