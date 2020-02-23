#!/usr/bin/env python3

# Libraries
import oyaml as yaml

# Dumper
def dumper(options, jobs):

    # Variables
    configuration = dict()
    result = False

    # Prepare configuration results
    if options.names:
        for job in options.names:
            if job in jobs:
                configuration[job] = jobs[job]
                result = True
    else:
        configuration = jobs
        result = True

    # Dump configuration results
    print(yaml.dump(configuration, indent=2))
    print(' ', flush=True)

    # Result
    return result
