import sys
import os
import logging

gammaLearn_path = os.path.abspath(os.path.join('../'))
if gammaLearn_path not in sys.path:
    sys.path.append(gammaLearn_path)

import gammalearn.data_handlers as data_handlers
import gammalearn.utils as utils


logging_level = logging.DEBUG
logger = logging.getLogger()
logger.setLevel(logging_level)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s - %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.info('logger created')

# files_folders = ['/home/mikael/projets_CTA/Prod3b/diffuse/']
files_folders = ['/uds_data/glearn/Data/HDF5-DL1/LaPalma/Gamma_diffuse/']

datafiles_list = utils.find_datafiles(files_folders)

camera_type = 'LSTCAM'
group_by = 'event_all_tels'
# group_by = 'image'
layout = '../share/Layouts/Layout_prod3b_LaPalma_N.layout'

layout_dic = utils.load_site_layout(layout)

energy_band = [0.1, 10]

logger.info('Create dataset')

dataset = data_handlers.create_datasets_memory(datafiles_list,
                                               camera_type,
                                               energy_band,
                                               None,
                                               layout_dic,
                                               group_by)
logger.debug('dataset size : {}'.format(len(dataset)))
num_errors = 0
for data in dataset:
    # logger.debug('labels shape : {}'.format(data['labels'].shape))
    # logger.debug('energy : {}'.format(data['labels'][0]))
    energy = data['labels'][0].numpy()
    if (energy > 1) | (energy < -1):
        logger.info('found error !')
        num_errors += 1
        logger.info('energy : {}'.format(energy))
        logger.info('file : {}'.format(data['file']))
        logger.info('run id {}, event id {}, shower id {}'.format(data['ids'][0],
                                                                  data['ids'][1],
                                                                  data['ids'][2]))

logger.info('number of out of energy bounds samples : {}'.format(num_errors))