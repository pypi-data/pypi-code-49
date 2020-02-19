import gammalearn.data_handlers as data_h
import gammalearn.utils as utils
import numpy as np
import gammalearn.datasets as datasets

file = ['/home/mikael/projets_CTA/Prod3b/diffuse/LaPalma_gamma_diffuse_20deg_0deg_prod3b_training_0020.hdf5']
file2 = ['/home/mikael/projets_CTA/CMU/diffuse/gamma_20deg_180deg_srun4068-23744___cta-prod3_desert-2150m-Paranal-HB9_cone10.h5']


class DummyExperimentLapp(object):

    def __init__(self):
        self.data_filter = {'filter': [utils.amplitude_filter],
                            'parameter': [{'amplitude': [43.3, 1000]}]}
        self.data_transform = None
        self.dataset_parameters = {'group_by': 'image',
                                  'camera_type': 'LSTCAM'
                                   }
        self.dataloader_workers = 2
        self.dataset_class = datasets.LappCamDataset


exp = DummyExperimentLapp()
dset = data_h.create_datasets_memory(file, exp)[0]

amps = []
for id in dset.indices:
    sample = dset.dataset[id]
    amps.append(sample['image'].sum(axis=-1))
amps = np.array(amps)
print(amps)
print(amps.min())
print(amps.max())
