#!/usr/bin/env python3

# Libraries
import docker
import os
import sys

# Puller
def puller(options, jobs):

    # Variables
    images = []
    result = False

    # List Docker images
    for job in jobs:
        image = jobs[job]['image']
        if image and image != 'local' and image not in images:
            images += [image]
            result = True

    # Pull Docker images
    if images:
        images.sort()
        for image in images:
            pull(image)

    # Result
    return result

# Pull
def pull(image):

    # Create Docker client
    client = docker.from_env()

    # Pull image with logs stream
    for data in client.api.pull(image, stream=True, decode=True):

        # Layer progress logs
        if 'progress' in data:
            if sys.stdout.isatty():
                print(
                    '\r\033[K%s: %s %s' % (data['id'], data['status'], data['progress']),
                    end='', flush=True)

        # Layer event logs
        elif 'progressDetail' in data:
            if sys.stdout.isatty():
                print('\r\033[K%s: %s' % (data['id'], data['status']), end='', flush=True)

        # Layer completion logs
        elif 'id' in data:
            print('\r\033[K%s: %s' % (data['id'], data['status']), flush=True)

        # Image logs
        else:
            print('\r\033[K%s' % (data['status']), flush=True)

    # Footer
    print(' ', flush=True)
