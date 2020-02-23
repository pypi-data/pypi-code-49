#!/usr/bin/env python3

# Libraries
import colored
import docker
import os
from pathlib import Path
import signal
import stat
import tempfile
import time

# Components
from .main import NAME
from .puller import pull

# Launcher
def launcher(options, jobs):

    # Variables
    result = None

    # Run selected jobs
    for job in jobs:

        # Filter jobs list
        if not options.pipeline and job not in options.names:
            continue

        # Filter stages list
        if options.pipeline and options.names and jobs[job]['stage'] not in options.names:
            continue

        # Filter manual jobs
        job_manual = (jobs[job]['when'] == 'manual')
        if job_manual and not options.manual and job not in options.names:
            continue

        # Raise initial result
        if result == None:
            result = True

        # Run job
        attempt = 0
        expected = result
        result = runner(options, jobs[job], result)

        # Retry job if allowed
        if expected and not result and jobs[job]['retry'] > 0:
            while not result and attempt < jobs[job]['retry']:
                attempt += 1
                result = runner(options, jobs[job], expected)

    # Result
    return True if result else False

# Runner
def runner(options, job_data, last_result):

    # Variables
    result = False

    # Filter when
    if last_result and job_data['when'] not in ['on_success', 'manual', 'always']:
        return last_result
    if not last_result and job_data['when'] not in ['on_failure']:
        return last_result

    # Prepare image
    image = job_data['image']

    # Prepare network
    network = 'bridge'
    if options.network:
        network = options.network

    # Header
    if not options.quiet:
        print(' %s===[ %s%s: %s%s %s(%s) %s]===%s' %
              (colored.fg('green') + colored.attr('bold'),
               colored.fg('yellow') + colored.attr('bold'), job_data['stage'],
               colored.fg('yellow') + colored.attr('bold'), job_data['name'],
               colored.fg('cyan') + colored.attr('bold'), image,
               colored.fg('green') + colored.attr('bold'), colored.attr('reset')))
        print(' ', flush=True)

    # Create Docker client
    client = docker.from_env()

    # Acquire project path
    pathProject = options.path
    pathParent = str(Path(pathProject).parent)

    # Prepare working directory
    if options.workdir:
        pathWorkDir = os.path.abspath(options.workdir)
    else:
        pathWorkDir = pathProject

    # Prepare entrypoint and scripts
    entrypoint = job_data['entrypoint']
    scripts = []

    # Append before_scripts, scripts, after_scripts
    if options.before:
        scripts += job_data['before_script']
    scripts += job_data['script']
    if options.after:
        scripts += job_data['after_script']

    # Prepare commands
    scriptFile = tempfile.NamedTemporaryFile(delete=True)
    with open(scriptFile.name, mode='w') as scriptStream:

        # Prepare script context
        scriptStream.write('#!/bin/sh\n')
        scriptStream.write('set -ex\n')

        # Prepare script commands
        scriptStream.write('\n'.join(scripts))
        scriptStream.flush()

    # Prepare script execution
    script_stat = os.stat(scriptStream.name)
    os.chmod(scriptStream.name, script_stat.st_mode | stat.S_IEXEC)
    scriptFile.file.close()

    # Prepare mounts
    temp_dir = tempfile.gettempdir()
    volumes = {
        pathParent: {
            'bind': pathParent,
            'mode': 'rw'
        },
        temp_dir: {
            'bind': temp_dir,
            'mode': 'rw'
        },
        '/var/run/docker.sock': {
            'bind': '/var/run/docker.sock',
            'mode': 'rw'
        }
    }

    # Extend mounts
    if options.volume:
        for volume in options.volume:
            volume_nodes = volume.split(':')

            # Parse HOST:TARGET:MODE
            if len(volume_nodes) == 3:
                volume_host = os.path.abspath(os.path.expandvars(volume_nodes[0]))
                volume_target = os.path.expandvars(volume_nodes[1])
                volume_mode = volume_nodes[2]

            # Parse HOST:TARGET
            elif len(volume_nodes) == 2:
                volume_host = os.path.abspath(os.path.expandvars(volume_nodes[0]))
                volume_target = os.path.expandvars(volume_nodes[1])
                volume_mode = 'rw'

            # Parse VOLUME
            else:
                volume_host = os.path.abspath(os.path.expandvars(volume))
                volume_target = os.path.abspath(os.path.expandvars(volume))
                volume_mode = 'rw'

            # Clear volume overrides
            for volume in list(volumes.keys()):
                if volume_target == volumes[volume]['bind']:
                    volumes.pop(volume)

            # Append volume mounts
            volumes[volume_host] = {'bind': volume_target, 'mode': volume_mode}

    # Prepare variables
    variables = dict()
    for variable in job_data['variables']:
        variables[variable] = os.path.expandvars(str(job_data['variables'][variable]))

    # Container execution
    if image not in ['local']:

        # Image validation
        try:
            client.images.get(image)
        except docker.errors.ImageNotFound:
            pull(image)

        # Launch container
        container = client.containers.run(
            image, command=scriptFile.name, detach=True, entrypoint=entrypoint,
            environment=variables, network_mode=network, remove=False, stdout=True,
            stderr=True, stream=True, volumes=volumes, working_dir=pathWorkDir)

        # Create interruption handler
        def interruptHandler(signal, frame):
            print(' ')
            print(' ')
            print(
                ' %s> WARNING: %sUser interruption detected, stopping the container...%s'
                % (colored.fg('yellow') + colored.attr('bold'),
                   colored.attr('reset') + colored.attr('bold'), colored.attr('reset')))
            print(' ', flush=True)
            container.stop(timeout=0)

        # Register interruption handler
        originalInterruptionHandler = signal.getsignal(signal.SIGINT)
        signal.signal(signal.SIGINT, interruptHandler)

        # Execution wrapper
        success = False

        # Show container logs
        try:
            for line in container.logs(stream=True):
                print(line.decode('utf-8'), end='', flush=True)
        except:
            pass

        # Check container status
        wait = container.wait()
        success = (wait['StatusCode'] == 0)

        # Stop container
        container.stop(timeout=0)
        time.sleep(0.1)

        # Remove container
        container.remove(force=True)

        # Unregister interruption handler
        signal.signal(signal.SIGINT, originalInterruptionHandler)

        # Result evaluation
        if job_data['when'] in ['on_failure', 'always']:
            result = last_result
        elif success:
            result = True

    # Native execution
    else:

        # Prepare environment
        _environ = dict(os.environ) # or os.environ.copy()
        os.environ.update(variables)

        # Native execution
        scripts = []
        if entrypoint:
            scripts += entrypoint
        scripts += [scriptFile.name]
        success = (os.system(' '.join(scripts)) == 0)

        # Result evaluation
        if job_data['when'] in ['on_failure', 'always']:
            result = last_result
        elif success:
            result = True

        # Restore environment
        os.environ.clear()
        os.environ.update(_environ)

    # Prepare when details
    when_details = ''
    if job_data['when'] not in ['on_success']:
        when_details = ' (when: %s)' % (job_data['when'])

    # Footer
    print(' ', flush=True)
    if not options.quiet:
        print(' %s> Result: %s%s%s' %
              (colored.fg('yellow') + colored.attr('bold'), colored.fg('green') +
               colored.attr('bold') + 'Success' if result else colored.fg('red') +
               colored.attr('bold') + 'Failure', colored.fg('cyan') +
               colored.attr('bold') + when_details, colored.attr('reset')))
        print(' ')
        print(' ', flush=True)

    # Result
    return result
