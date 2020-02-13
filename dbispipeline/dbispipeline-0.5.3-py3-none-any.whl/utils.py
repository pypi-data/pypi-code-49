"""Utils used in the dbispipeline implementation."""
from email.mime.text import MIMEText
from os.path import basename
from os.path import splitext
import configparser
import datetime
import json
import logging
import numpy as np
import os
import pickle
import platform
import smtplib
import traceback
import warnings

from . import store

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)-16s %(message)s',
    level=logging.INFO,
)
LOGGER = logging.getLogger('dbispipeline')

SECTION_DATABASE = 'database'
SECTION_VARIABLES = 'variables'
SECTION_MAIL = 'mail'


def load_project_config():
    """Loads the project configuration."""
    config_files = ['/usr/local/etc/dbispipeline.ini']
    user_home = os.getenv('HOME')
    if user_home:
        config_files.append(user_home + '/.config/dbispipeline.ini')
    config_files.append('dbispipeline.ini')
    config = configparser.ConfigParser()

    if os.getenv("DBISPIPELINE_ENV") == "ci":
        # Sets default values if the environment is a ci
        config.read_dict({
            SECTION_DATABASE: {
                'host': 'postgres',
                'port': 5432,
                'user': 'runner',
                'password': 'runner_password',
                'database': 'pipelineresults',
            },
        })
        LOGGER.debug(f'detected CI environment')

    parsed_files = config.read(config_files)
    LOGGER.debug(f'loaded configuration from files: {parsed_files}')

    if not config.has_section(SECTION_DATABASE):
        raise KeyError('no database section found in the configuration')

    return config


def load_result_backup(path):
    """
    Loads results from a pickle backup.

    Args:
        path: to the backup file.
    """
    with open(path, 'rb') as f:
        return pickle.load(f)


def restore_backup(path, output_handlers):
    """
    Reads a backup file and handles it with the given handlers.

    Args:
        path: to the backup file.
        output_handlers: an iterable containing output handlers
    """
    backup = load_result_backup(path)

    for handler in output_handlers:
        handler.handle_result(backup)


def store_prediction(model, dataloader, file_name_prefix=None):
    if not file_name_prefix:
        file_name_prefix = type(model).__name__

    if store['plan_path']:
        if file_name_prefix[-1] != '_':
            file_name_prefix += '_'
        file_name_prefix += splitext(basename(store['plan_path']))[0]

    if file_name_prefix[-1] != '_':
        file_name_prefix += '_'

    x_test, _ = dataloader.load_test()

    try:
        y_pred = model.predict(x_test)
        np.save(file_name_prefix + 'predict.npy', y_pred)
    except AttributeError:
        LOGGER.warning('Model does not support predict.')

    try:
        y_pred = model.predict_proba(x_test)
        np.save(file_name_prefix + 'predict_proba.npy', y_pred)
    except AttributeError:
        LOGGER.warning('Model does not support predict_proba.')


def notify_success(plan_path,
                   times,
                   result=None,
                   run=None,
                   subject='DBIS Pipeline: successfully finished',
                   loader_config=None):
    run_string = ''
    if run is not None:
        run_string = f' run #{run}'

    result_string = 'The results are available in the database.'
    if result and isinstance(result, dict) or isinstance(result, str):
        try:
            pretty_printed_json = json.dumps(result, indent=2, sort_keys=True)
            result_string = f'Your results are:\n\n{pretty_printed_json}'
        except Exception:
            LOGGER.warn('could not write result as pretty json string')
            pass
    computer_name = platform.node()
    duration = datetime.timedelta(seconds=int(times['eval'] - times['start']))
    message = f'''\
Hello,
your configuration file {plan_path} running on {computer_name}\
        has finished{run_string}.
The calculation took {duration}.'''

    if loader_config:
        message += f'''
The configuration of the dataloader was:
    {loader_config}'''

    message += '\n' + result_string

    _notify(message, subject)


def notify_error(plan_path,
                 error_stage,
                 error_object,
                 subject='DBIS Pipeline: error',
                 run=None,
                 loader_config=None):
    run_string = ''
    if run is not None:
        run_string = f' on run #{run}'
    message = f'''Hello,
unfortunately, your configuration file {plan_path} caused an error on
the pipeline running on {platform.node()} during {error_stage}{run_string}.
'''
    if loader_config:
        message += f'''
The configuration of the dataloader was:
    {loader_config}'''

    if error_object:
        message += f'''
The error message is:
    {traceback.format_tb(error_object.__traceback__)}'''

    _notify(message, subject)


def _notify(message, subject):
    cfg = load_project_config()
    if SECTION_MAIL not in cfg:
        LOGGER.debug(f'missing section [{SECTION_MAIL}]: not sending success '
                     'message: {message}')
        return

    required_fields = ['recipient', 'sender', 'smtp_server']
    for field in required_fields:
        if field not in cfg[SECTION_MAIL]:
            LOGGER.error(f'missing option in mail configuration: {field}')
            return

    # required
    recipient = cfg[SECTION_MAIL]['recipient']
    sender = cfg[SECTION_MAIL]['sender']
    host = cfg[SECTION_MAIL]['smtp_server']

    LOGGER.info(f'sending mail to {recipient}')
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    if cfg[SECTION_MAIL].getboolean('authenticate', fallback=False):

        more_required_fields = ['username', 'password']
        for field in more_required_fields:
            if field not in cfg[SECTION_MAIL]:
                LOGGER.error(f'missing field in mail configuration: {field}')
                return

        # optional
        port = cfg.getint(SECTION_MAIL, 'port', fallback=465)
        s = smtplib.SMTP_SSL(host, port)
    else:
        s = smtplib.SMTP(host)

    s.sendmail(sender, [recipient], msg.as_string())


def prepare_slurm_job(dryrun, force, verbose, restore, mail, plan):
    config = load_project_config()
    jobname = config.get('project', 'name', fallback=None)
    if jobname is None:
        warnings.warn('no project name set, using configuration file name')
        jobname = os.path.basename(plan)
    log_directory = config.get('project', 'log_directory', fallback='logs')
    options = [
        '--partition=IFIgpu',
        f'--job-name={jobname}',
        '--account=dbis',
        '--nodes=1',
        '--tasks-per-node=1',
        f'-o {log_directory}/{jobname}.out',
        f'-e {log_directory}/{jobname}.err',
    ]

    if mail is not None:
        email = config.get('slurm', 'email', fallback=None)
        if email:
            options.append(f'--mail-type=ALL')
            options.append(f'--mail-user={email}')
        else:
            warnings.warn('No email address found in configuration, slurm will'
                          f'not send any emails')

    content = '#!/bin/bash -l\n'
    content += '\n'.join(['#SBATCH ' + x for x in options])
    content += f'\nsrun pipenv run python -m dbispipeline {planfile} '

    if dryrun:
        content += '--dryrun '
    if force:
        content += '--force '
    if restore:
        content += f'--restore {restore} '
    if verbose:
        content += '--verbose '

    if not os.path.isdir('slurmjobs'):
        os.makedirs('slurmjobs')
    timestamp = datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
    jobfile = os.path.join('slurmjobs', f'{timestamp}_{jobname}.job')
    with open(jobfile, 'w') as o_f:
        o_f.write(content)
    return jobfile
