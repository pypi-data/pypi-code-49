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
=======
helpers
=======

This module implements various helper methods and classes
"""

import os
import errno
import logging

from .data import CachedDataSource
from .data import RemoteDataSource
from .data import CachedDataSink
from .data import getAllFilenames
from .data_loaders import DataLoaderList
from .data_loaders import DataLoader
from .inputs import InputList
from .inputs import Input
from .inputs import InputGroup
from .outputs import SynchronizationListener
from .outputs import OutputList
from .outputs import Output
from .outputs import RemotelySyncedOutput
from .algorithm import Algorithm

logger = logging.getLogger(__name__)


# ----------------------------------------------------------


def parse_inputs(inputs):
    data = {}
    for key, value in inputs.items():
        data[key] = dict(channel=value["channel"], path=value["path"])
        if "database" in value:
            db = dict(
                database=value["database"],
                protocol=value["protocol"],
                set=value["set"],
                output=value["output"],
            )
            data[key].update(db)
    return data


def parse_outputs(outputs):
    return dict(
        [(k, {"channel": v["channel"], "path": v["path"]}) for k, v in outputs.items()]
    )


def convert_loop_to_container(config):
    data = {
        "algorithm": config["algorithm"],
        "parameters": config["parameters"],
        "channel": config["channel"],
        "uid": os.getuid(),
    }

    data["inputs"] = parse_inputs(config["inputs"])
    data["outputs"] = parse_outputs(config["outputs"])
    return data


def convert_experiment_configuration_to_container(config):
    data = {
        "algorithm": config["algorithm"],
        "parameters": config["parameters"],
        "channel": config["channel"],
        "uid": os.getuid(),
    }

    if "range" in config:
        data["range"] = config["range"]

    data["inputs"] = parse_inputs(config["inputs"])

    if "outputs" in config:
        data["outputs"] = parse_outputs(config["outputs"])
    else:
        data["result"] = {
            "channel": config["channel"],
            "path": config["result"]["path"],
        }

    if "loop" in config:
        data["loop"] = convert_loop_to_container(config["loop"])

    return data


# ----------------------------------------------------------


class AccessMode:
    """Possible access modes"""

    NONE = 0
    LOCAL = 1
    REMOTE = 2


def create_inputs_from_configuration(
    config,
    algorithm,
    prefix,
    cache_root,
    cache_access=AccessMode.NONE,
    db_access=AccessMode.NONE,
    unpack=True,
    socket=None,
    databases=None,
    no_synchronisation_listeners=False,
):

    views = {}
    input_list = InputList()
    data_loader_list = DataLoaderList()

    # This is used for parallelization purposes
    start_index, end_index = config.get("range", (None, None))

    def _create_local_input(details):
        data_source = CachedDataSource()

        filename = os.path.join(cache_root, details["path"] + ".data")

        if details["channel"] == config["channel"]:  # synchronized
            status = data_source.setup(
                filename=filename,
                prefix=prefix,
                start_index=start_index,
                end_index=end_index,
                unpack=True,
            )
        else:
            status = data_source.setup(filename=filename, prefix=prefix, unpack=True)

        if not status:
            raise IOError("cannot load cache file `%s'" % details["path"])

        input = Input(name, algorithm.input_map[name], data_source)

        logger.debug(
            "Input '%s' created: group='%s', dataformat='%s', filename='%s'"
            % (name, details["channel"], algorithm.input_map[name], filename)
        )

        return input

    def _get_data_loader_for(details):
        data_loader = data_loader_list[details["channel"]]
        if data_loader is None:
            data_loader = DataLoader(details["channel"])
            data_loader_list.add(data_loader)

            logger.debug("Data loader created: group='%s'" % details["channel"])

        return data_loader

    def _create_data_source(details):
        data_loader = _get_data_loader_for(details)

        filename = os.path.join(cache_root, details["path"] + ".data")

        data_source = CachedDataSource()
        result = data_source.setup(
            filename=filename,
            prefix=prefix,
            start_index=start_index,
            end_index=end_index,
            unpack=True,
        )

        if not result:
            raise IOError("cannot load cache file `%s'" % filename)

        data_loader.add(name, data_source)

        logger.debug(
            "Input '%s' added to data loader: group='%s', dataformat='%s', filename='%s'"
            % (name, details["channel"], algorithm.input_map[name], filename)
        )

    for name, details in config["inputs"].items():

        input = None

        if details.get("database", None) is not None:
            if db_access == AccessMode.LOCAL:
                if databases is None:
                    raise IOError("No databases provided")

                # Retrieve the database
                try:
                    db = databases[details["database"]]
                except IndexError:
                    raise IOError("Database '%s' not found" % details["database"])

                # Create of retrieve the database view
                channel = details["channel"]

                if channel not in views:
                    view = db.view(details["protocol"], details["set"])
                    view.setup(
                        os.path.join(cache_root, details["path"]),
                        pack=False,
                        start_index=start_index,
                        end_index=end_index,
                    )

                    views[channel] = view

                    logger.debug(
                        "Database view '%s/%s/%s' created: group='%s'"
                        % (
                            details["database"],
                            details["protocol"],
                            details["set"],
                            channel,
                        )
                    )
                else:
                    view = views[channel]

                data_source = view.data_sources[details["output"]]

                if (algorithm.type == Algorithm.LEGACY) or (
                    (algorithm.is_sequential)
                    and (details["channel"] == config["channel"])
                ):
                    input = Input(name, algorithm.input_map[name], data_source)

                    logger.debug(
                        "Input '%s' created: group='%s', dataformat='%s', database-output='%s/%s/%s:%s'"
                        % (
                            name,
                            details["channel"],
                            algorithm.input_map[name],
                            details["database"],
                            details["protocol"],
                            details["set"],
                            details["output"],
                        )
                    )
                else:
                    data_loader = _get_data_loader_for(details)
                    data_loader.add(name, data_source)

                    logger.debug(
                        "DatabaseOutputDataSource '%s' created: group='%s', dataformat='%s', database-output='%s/%s/%s:%s'"
                        % (
                            name,
                            channel,
                            algorithm.input_map[name],
                            details["database"],
                            details["protocol"],
                            details["set"],
                            details["output"],
                        )
                    )

            elif db_access == AccessMode.REMOTE:
                if socket is None:
                    raise IOError("No socket provided for remote data sources")

                data_source = RemoteDataSource()
                result = data_source.setup(
                    socket=socket,
                    input_name=name,
                    dataformat_name=algorithm.input_map[name],
                    prefix=prefix,
                    unpack=True,
                )

                if not result:
                    raise IOError("cannot setup remote data source '%s'" % name)

                if (algorithm.type == Algorithm.LEGACY) or (
                    (algorithm.is_sequential)
                    and (details["channel"] == config["channel"])
                ):
                    input = Input(name, algorithm.input_map[name], data_source)

                    logger.debug(
                        "Input '%s' created: group='%s', dataformat='%s', database-file='%s'"
                        % (
                            name,
                            details["channel"],
                            algorithm.input_map[name],
                            details["path"],
                        )
                    )
                else:
                    data_loader = _get_data_loader_for(details)
                    data_loader.add(name, data_source)

                    logger.debug(
                        "RemoteDataSource '%s' created: group='%s', dataformat='%s', connected to a database"
                        % (name, details["channel"], algorithm.input_map[name])
                    )

        elif cache_access == AccessMode.LOCAL:

            if algorithm.type == Algorithm.LEGACY:
                input = _create_local_input(details)

            elif algorithm.is_sequential:
                if details["channel"] == config["channel"]:  # synchronized
                    input = _create_local_input(details)
                else:
                    _create_data_source(details)

            else:  # Algorithm autonomous types
                _create_data_source(details)

        else:
            continue

        # Synchronization bits
        if input is not None:
            group = input_list.group(details["channel"])
            if group is None:
                synchronization_listener = None
                if not no_synchronisation_listeners:
                    synchronization_listener = SynchronizationListener()

                group = InputGroup(
                    details["channel"],
                    synchronization_listener=synchronization_listener,
                    restricted_access=(details["channel"] == config["channel"]),
                )
                input_list.add(group)
                logger.debug("Group '%s' created" % details["channel"])

            group.add(input)

    return (input_list, data_loader_list)


# ----------------------------------------------------------


def create_outputs_from_configuration(
    config,
    algorithm,
    prefix,
    cache_root,
    input_list=None,
    data_loaders=None,
    loop_socket=None,
):

    data_sinks = []
    output_list = OutputList()

    # This is used for parallelization purposes
    start_index, end_index = config.get("range", (None, None))

    # If the algorithm is an analyser
    if "result" in config:
        output_config = {"result": config["result"]}
    else:
        output_config = config["outputs"]

    for name, details in output_config.items():

        synchronization_listener = None

        if "result" in config:
            dataformat_name = "analysis:" + algorithm.name
            dataformat = algorithm.result_dataformat()
        else:
            dataformat_name = algorithm.output_map[name]
            dataformat = algorithm.dataformats[dataformat_name]

        if input_list is not None:
            input_group = input_list.group(config["channel"])
            if input_group is not None:
                synchronization_listener = input_group.synchronization_listener

        path = os.path.join(cache_root, details["path"] + ".data")
        dirname = os.path.dirname(path)
        # Make sure that the directory exists while taking care of race
        # conditions. see: http://stackoverflow.com/questions/273192/check-if-a-directory-exists-and-create-it-if-necessary
        try:
            if len(dirname) > 0:
                os.makedirs(dirname)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        if start_index is None:
            input_path = None

            for k, v in config["inputs"].items():
                if v["channel"] != config["channel"]:
                    continue

                if "database" not in v:
                    input_path = os.path.join(cache_root, v["path"] + ".data")
                    break

            if input_path is not None:
                (
                    data_filenames,
                    indices_filenames,
                    data_checksum_filenames,
                    indices_checksum_filenames,
                ) = getAllFilenames(input_path)

                end_indices = [int(x.split(".")[-2]) for x in indices_filenames]
                end_indices.sort()

                start_index = 0
                end_index = end_indices[-1]

            else:
                for k, v in config["inputs"].items():
                    if v["channel"] != config["channel"]:
                        continue

                    start_index = 0

                    if (input_list is not None) and (input_list[k] is not None):
                        end_index = input_list[k].data_source.last_data_index()
                        break
                    elif data_loaders is not None:
                        end_index = data_loaders.main_loader.data_index_end
                        break

        data_sink = CachedDataSink()
        data_sinks.append(data_sink)

        status = data_sink.setup(
            filename=path,
            dataformat=dataformat,
            start_index=start_index,
            end_index=end_index,
            encoding="binary",
        )

        if not status:
            raise IOError("Cannot create cache sink '%s'" % details["path"])

        if loop_socket is not None:
            output_list.add(
                RemotelySyncedOutput(
                    name,
                    data_sink,
                    loop_socket,
                    synchronization_listener=synchronization_listener,
                    force_start_index=start_index,
                )
            )
        else:
            output_list.add(
                Output(
                    name,
                    data_sink,
                    synchronization_listener=synchronization_listener,
                    force_start_index=start_index,
                )
            )

        if "result" not in config:
            logger.debug(
                "Output '%s' created: group='%s', dataformat='%s', filename='%s'"
                % (name, details["channel"], dataformat_name, path)
            )
        else:
            logger.debug(
                "Output '%s' created: dataformat='%s', filename='%s'"
                % (name, dataformat_name, path)
            )

    return (output_list, data_sinks)
