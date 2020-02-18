#!/usr/bin/env python

import subprocess
from decimal import Decimal

import collectd

CPU_COUNT = 5
MEMORY_COUNT = 5


def configure(config):
    for node in config.children:
        key = node.key.lower()
        value = node.values[0]

        if key == 'cpu_count':
            global CPU_COUNT
            CPU_COUNT = value
        elif key == 'memory_count':
            global MEMORY_COUNT
            MEMORY_COUNT = value
        else:
            collectd.info('cpu_temp plugin: Unknown config key "%s"' % key)


def top():
    out = subprocess.Popen(['ps', '--no-headers', '-eo', 'pmem,pcpu,comm'],
                           stdout=subprocess.PIPE).communicate()[0].splitlines()
    out = [i.split() for i in out]
    processes = {}

    for i in out:
        old = processes.get(i[2], [0, 0])
        processes[i[2]] = (old[0] + Decimal(i[0].decode()),
                           old[1] + Decimal(i[1].decode()))

    processes = [(value[0], value[1], key) for key, value in processes.items()]
    memory = sorted([(i[0], i[2]) for i in processes], reverse=True)
    cpu = sorted([(i[1], i[2]) for i in processes], reverse=True)
    return memory[0:MEMORY_COUNT], cpu[0:CPU_COUNT]


def read(data=None):
    val = collectd.Values(type='gauge')
    val.plugin = 'top'
    memory, cpu = top()

    val.type_instance = 'memory'
    for i in memory:
        val.dispatch(type='percent', plugin_instance=i[1], values=[i[0]])

    val.type_instance = 'cpu'
    for i in cpu:
        val.dispatch(type='percent', plugin_instance=i[1], values=[i[0]])


collectd.register_config(configure)
collectd.register_read(read)
