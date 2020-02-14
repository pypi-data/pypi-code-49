#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


"""
=====
stats
=====

This module implements statistical related helper functions.
"""


def io_statistics(configuration, input_list=None, output_list=None):
    """Summarize current I/O statistics looking at data sources and sinks,
    inputs and outputs

    Parameters:

        configuration (dict): Executor configuration

        input_list (inputs.InputList): List of input to gather statistics from

        output_list (outputs.OutputList): List of outputs to gather statistics
            from


    Returns:

      dict: A dictionary summarizing current I/O statistics
    """

    network_time = 0.0

    # Data reading
    bytes_read = 0
    blocks_read = 0
    read_time = 0.0

    if input_list is not None:
        for input in input_list:
            size, duration = input.data_source.statistics()
            bytes_read += size
            read_time += duration
            blocks_read += input.nb_data_blocks_read

    # Data writing
    bytes_written = 0
    blocks_written = 0
    write_time = 0.0
    files = []

    if output_list is not None:
        for output in output_list:
            size, duration = output.data_sink.statistics()
            bytes_written += size
            write_time += duration
            blocks_written += output.nb_data_blocks_written

            if 'result' in configuration:
                hash = configuration['result']['path'].replace('/', '')
            else:
                hash = configuration['outputs'][output.name]['path'].replace(
                    '/', '')

            files.append(dict(
                hash=hash,
                size=size,
                blocks=output.nb_data_blocks_written,
            ))

    # Result
    return dict(
        volume=dict(read=bytes_read, write=bytes_written),
        blocks=dict(read=blocks_read, write=blocks_written),
        time=dict(read=read_time, write=write_time),
        network=dict(wait_time=network_time),
        files=files,
    )


# ----------------------------------------------------------


def update(statistics, additional_statistics):
    """Updates the content of statistics parameter with additional data. No new
    entries will be created. Only the values already available in statistics
    will be used.

    Parameters:

        statistics (dict): Original statistics

        additional_statistics (dict): Additional data to be added to the
            original statistics dict.
    """

    for k in statistics.keys():
        if k == 'files':
            continue

        for k2 in statistics[k].keys():
            statistics[k][k2] += additional_statistics[k][k2]

    if 'files' in statistics:
        statistics['files'].extend(additional_statistics.get('files', []))
    else:
        statistics['files'] = additional_statistics.get('files', [])
