#!/usr/bin/env python3

# Libraries
import collections
import colored
from dotenv import dotenv_values
import os
from pathlib import Path
import oyaml as yaml
import sys

# Components
from .main import NAME
from .menu import configurator

# Reader
def reader(options):

    # Variables
    environment = {
        'default': dict(),
        'files': [],
        'parameters': dict(),
    }

    # Parse environment options
    if options.env:
        for env in [env for env in options.env]:
            env_parsed = env.split('=', 1)

            # Parse VARIABLE=value
            if len(env_parsed) == 2:
                variable = env_parsed[0]
                value = env_parsed[1]
                os.environ[variable] = value
                environment['parameters'][variable] = value

            # Parse ENVIRONMENT_FILE
            elif os.path.isfile(Path(options.path) / env):
                environment['files'] += [Path(options.path) / env]

            # Parse VARIABLE
            else:
                variable = env
                if variable in os.environ:
                    environment['parameters'][variable] = os.environ[variable]
                else:
                    environment['parameters'][variable] = ''

    # Iterate through environment files
    environment['files'] += [Path(options.path) / '.env']
    for environment_file in environment['files']:
        if not environment_file.is_file():
            continue

        # Parse environment files
        environment_file_values = dotenv_values(dotenv_path=environment_file)
        for variable in environment_file_values:

            # Define default environment variable
            if variable in environment['default']:
                continue
            environment['default'][variable] = environment_file_values[variable]

    # Read GitLab CI YAML
    try:
        with open(options.configuration, 'r') as configuration_data:
            data = yaml.safe_load(configuration_data)
            return parser(options, data, environment)
    except yaml.YAMLError as exc:
        print(' ')
        print(' %s%s: %sERROR: %s%s%s' %
              (colored.fg('green') + colored.attr('bold'), NAME,
               colored.fg('red') + colored.attr('bold'),
               colored.attr('reset') + colored.attr('bold'), exc, colored.attr('reset')))
    except KeyboardInterrupt:
        pass
    except:
        print(' ')
        print(' %s%s: %sERROR: %s%s%s' %
              (colored.fg('green') + colored.attr('bold'), NAME, colored.fg('red') +
               colored.attr('bold'), colored.attr('reset') + colored.attr('bold'),
               str(sys.exc_info()[1]), colored.attr('reset')))

    # Failure
    return None

# Parser
def parser(options, data, environment):

    # Variables
    global_values = dict({
        'after_script': [],
        'before_script': [],
        'image': '',
        'entrypoint': None,
        'variables': dict()
    })
    jobs = dict()
    names_local = False
    stages = dict()

    # Parse nested include
    if 'include' in data and data['include']:
        for include_node in data['include']:

            # Parse local nodes
            if 'local' in include_node:
                file_path = include_node['local'].lstrip('/')
                if os.path.isfile(Path(options.path) / file_path):
                    with open(Path(options.path) / file_path, 'r') as include_data:
                        include_additions = yaml.safe_load(include_data)
                        data.update(include_additions)

    # Prepare parameters variables
    if environment['parameters']:
        global_values['variables'].update(environment['parameters'])

    # Filter .local node
    if '.local' in data and data['.local']:
        local = data['.local']

        # Parse local after
        if 'after' in local:
            if options.after:
                options.after = local['after']

        # Parse local all
        if 'all' in local:
            if not options.all:
                options.all = local['all']

        # Parse local before
        if 'before' in local:
            if options.before:
                options.before = local['before']

        # Parse local defaults
        if 'defaults' in local:
            if not options.defaults:
                options.defaults = local['defaults']

        # Parse local env
        if 'env' in local:
            for env in local['env']:
                env_parsed = env.split('=', 1)

                # Parse VARIABLE=value
                if len(env_parsed) == 2:
                    variable = env_parsed[0]
                    value = env_parsed[1]
                    if variable not in global_values['variables']:
                        os.environ[variable] = value
                        global_values['variables'][variable] = value

                # Parse ENVIRONMENT_FILE
                elif os.path.isfile(Path(options.path) / env):
                    environment_file = Path(options.path) / env
                    if not environment_file.is_file():
                        continue

                    # Parse environment files
                    environment_file_values = dotenv_values(dotenv_path=environment_file)
                    for variable in environment_file_values:

                        # Define default environment variable
                        if variable not in global_values['variables']:
                            global_values['variables'][variable] = environment_file_values[variable]

                # Parse VARIABLE
                else:
                    variable = env
                    if variable not in global_values['variables']:
                        if variable in os.environ:
                            global_values['variables'][variable] = os.environ[variable]
                        else:
                            global_values['variables'][variable] = ''

        # Parse local image
        if 'image' in local:
            if not options.image:
                options.image = local['image']

        # Parse local manual
        if 'manual' in local:
            if not options.manual:
                options.manual = local['manual']

        # Parse local names
        if 'names' in local:
            if not options.names and not options.pipeline:
                names_local = True
                options.names = local['names']

        # Parse local network
        if 'network' in local:
            if not options.network:
                options.network = local['network']

        # Parse local pipeline
        if 'pipeline' in local:
            if not options.pipeline and (not options.names or names_local):
                options.pipeline = local['pipeline']

        # Parse local quiet
        if 'quiet' in local:
            if not options.quiet:
                options.quiet = local['quiet']

        # Parse local tags
        if 'tags' in local:
            if options.tags_default:
                options.tags = local['tags'][:]
                options.tags_default = False

        # Parse local volumes
        if 'volumes' in local:
            if not options.volume:
                options.volume = []
            options.volume = local['volumes'] + options.volume

        # Parse local workdir
        if 'workdir' in local:
            if not options.workdir:
                options.workdir = local['workdir']

        # Parse local configurations
        if 'configurations' in local:
            configuredVariables = configurator(options, local['configurations'])
            global_values['variables'].update(configuredVariables)

    # Prepare default variables
    if environment['default']:
        for variable in environment['default']:
            if variable in global_values['variables']:
                pass
            elif variable in os.environ:
                global_values['variables'][variable] = os.environ[variable]
            else:
                global_values['variables'][variable] = environment['default'][variable]
            if variable not in os.environ:
                os.environ[variable] = global_values['variables'][variable]

    # Prepare global values
    if options.image:
        if isinstance(options.image, dict):
            global_values['image'] = os.path.expandvars(options.image['name'])
            if 'entrypoint' in options.image and len(options.image['entrypoint']) > 0:
                global_values['entrypoint'] = options.image['entrypoint'][:]
            else:
                global_values['entrypoint'] = None
        else:
            global_values['image'] = os.path.expandvars(options.image)
            global_values['entrypoint'] = None

    # Iterate through nodes
    for node in data:

        # Filter services node
        if node == 'services':
            continue

        # Filter image node
        if node == 'image':
            if not global_values['image']:
                image_data = data[node]
                if isinstance(image_data, dict):
                    global_values['image'] = os.path.expandvars(image_data['name'])
                    if 'entrypoint' in image_data and len(image_data['entrypoint']) > 0:
                        global_values['entrypoint'] = image_data['entrypoint'][:]
                    else:
                        global_values['entrypoint'] = None
                else:
                    global_values['image'] = os.path.expandvars(image_data)
                    global_values['entrypoint'] = None
            continue

        # Filter before_script node
        if node == 'before_script':
            global_values['before_script'] = data[node]
            continue

        # Filter after_script node
        if node == 'after_script':
            global_values['after_script'] = data[node]
            continue

        # Filter stages node
        if node == 'stages':
            for i, stage in enumerate(data['stages']):
                stages[stage] = i
            continue

        # Filter variables node
        if node == 'variables':
            for variable in data['variables']:
                if variable not in global_values['variables']:
                    global_values['variables'][variable] = data['variables'][variable]
            continue

    # Iterate through stages
    for node in data:

        # Validate job node
        if 'stage' not in data[node]:
            continue

        # Ignore template stage
        if node[0:1] == '.':
            continue

        # Register job
        jobs[node] = stager(options, node, data[node], global_values)

    # Sort jobs based on stages
    jobs = collections.OrderedDict(
        sorted(jobs.items(), key=lambda x: stages[x[1]['stage']]))

    # Result
    return jobs

# Stager
def stager(options, job_name, job_data, global_values):

    # Variables
    job = dict()

    # Prepare stage
    job['name'] = job_name
    job['stage'] = job_data['stage']
    job['image'] = global_values['image']
    job['entrypoint'] = global_values['entrypoint'][:] if global_values[
        'entrypoint'] else None
    job['variables'] = dict(global_values['variables'])
    job['before_script'] = global_values['before_script'][:]
    job['script'] = []
    job['after_script'] = global_values['after_script'][:]
    job['retry'] = 0
    job['when'] = 'on_success'
    job['tags'] = []

    # Extract job image
    if 'image' in job_data and job_data['image']:
        image_data = job_data['image']
        if isinstance(image_data, dict):
            job['image'] = os.path.expandvars(image_data['name'])
            if 'entrypoint' in image_data and len(image_data['entrypoint']) > 0:
                job['entrypoint'] = image_data['entrypoint'][:]
            else:
                job['entrypoint'] = None
        else:
            job['image'] = os.path.expandvars(image_data)
            job['entrypoint'] = None

    # Extract job variables
    if 'variables' in job_data and job_data['variables']:
        job['variables'].update(job_data['variables'])

    # Extract job before_script
    if 'before_script' in job_data and job_data['before_script']:
        job['before_script'] = job_data['before_script'][:]

    # Extract job script
    if 'script' in job_data and job_data['script']:
        job['script'] = job_data['script'][:]

    # Extract job after_script
    if 'after_script' in job_data and job_data['after_script']:
        job['after_script'] = job_data['after_script'][:]

    # Extract job retry
    if 'retry' in job_data:
        retry_data = job_data['retry']
        if isinstance(retry_data, dict):
            job['retry'] = int(retry_data['max'])
        else:
            job['retry'] = int(retry_data)

    # Extract job when
    if 'when' in job_data and job_data['when'] in [
            'on_success', 'on_failure', 'always', 'manual'
    ]:
        job['when'] = job_data['when']

    # Extract job tags
    if 'tags' in job_data and job_data['tags']:
        job['tags'] = job_data['tags'][:]

    # Configure job tags
    if (set(job['tags']) & set(options.tags)):
        job['when'] = 'manual'

    # Result
    return job
