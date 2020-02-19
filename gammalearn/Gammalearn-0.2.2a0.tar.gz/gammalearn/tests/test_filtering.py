from __future__ import division, print_function
import os
import sys
import argparse
import importlib.util
import logging
import faulthandler

import numpy as np
from torch.utils.data import ConcatDataset


gammaLearn_path = os.path.abspath(os.path.join('../'))
if gammaLearn_path not in sys.path:
    sys.path.append(gammaLearn_path)
import gammalearn.utils as utils
import gammalearn.data_handlers as data_handlers
from gammalearn.experiment_runner import Experiment

faulthandler.enable()


if __name__ == '__main__':

    logging_level = logging.INFO
    # Parse script arguments
    print('parse arguments')
    parser = argparse.ArgumentParser()
    parser.add_argument("configuration_file", help="path to configuration file")
    parser.add_argument("--debug", help="log useful information for debug purpose",
                        action="store_true")
    parser.add_argument("--logfile", help="whether to write the log on disk", action="store_true")
    args = parser.parse_args()
    configuration_file = args.configuration_file
    debug = args.debug
    logfile = args.logfile

    # Load logging config
    if debug:
        logging_level = logging.DEBUG
    logger = logging.getLogger()
    logger.setLevel(logging_level)
    # create formatter
    if debug:
        formatter = logging.Formatter('[%(levelname)s] %(name)s - %(message)s')
    else:
        formatter = logging.Formatter('[%(levelname)s] - %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.debug('logger created')

    # load settings file
    logger.info('load settings')
    spec = importlib.util.spec_from_file_location("settings", configuration_file)
    settings = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(settings)

    # check config and prepare experiment
    experiment = Experiment(settings)

    # print config
    utils.log_config(experiment)

    # look for data and create datasets and dataloaders
    logger.info('look for data files')
    datafiles_list = utils.find_datafiles(experiment.files_folders, experiment.files_max_number)
    logger.debug(datafiles_list)
    datafiles_list = list(datafiles_list)
    datafiles_list.sort()
    for file in datafiles_list:
        logger.info('found : {}'.format(file))
    dataset = data_handlers.create_datasets_memory(datafiles_list,
                                                   experiment)
    data = ConcatDataset(dataset)
    distances = []
    emission_cones = []
    energies = []
    for sample in data:
        energies.append(sample['label'][0])
        impact = sample['label'][1:3]
        if len(sample['telescope'].shape) > 1:
            tels_position = sample['telescope'][:, 2:4].numpy()
            tel_altitudes = sample['telescope'][:, 0].numpy()
            tel_azimuths = sample['telescope'][:, 1].numpy()
            distances.append(np.sqrt((tels_position[:, 0] - impact[0]) ** 2 + (tels_position[:, 1] - impact[1]) ** 2))
        else:
            tels_position = sample['telescope'][2:4].numpy()
            tel_altitudes = sample['telescope'][0].numpy()
            tel_azimuths = sample['telescope'][1].numpy()
            distances.append(np.sqrt((tels_position[0] - impact[0]) ** 2 + (tels_position[1] - impact[1]) ** 2))

        shower_direction = sample['label'][3:5]

        # emission_cones.append(utils.angular_separation_altaz(tel_altitudes, tel_azimuths,
        #                                          shower_direction[0], shower_direction[1]))

    logger.info('max distance : {}'.format(np.max(distances)))
    # logger.info('max cone : {}'.format(np.max(emission_cones)))
    logger.info('max energy : {}'.format(np.max(energies)))
    logger.info('min distance : {}'.format(np.min(distances)))
    # logger.info('min cone : {}'.format(np.min(emission_cones)))
    logger.info('min energy : {}'.format(np.min(energies)))