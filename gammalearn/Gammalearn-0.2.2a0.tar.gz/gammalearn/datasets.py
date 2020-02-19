import os
import sys
import multiprocessing as mp
import copy

import tables
import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision.transforms import Compose

import gammalearn.utils as utils


class Subset(Dataset):
    """
    A subset of a dataset according to image indices
    """
    def __init__(self, dataset, indices):
        """
        Parameters
        ----------
        dataset (Dataset): the dataset
        indices (list of int): the indices to keep in the subset
        """
        self.dataset = dataset
        self.indices = indices

    def __getitem__(self, idx):
        return self.dataset[self.indices[idx]]

    def __len__(self):
        return len(self.indices)


class UCMCamDataset(Dataset):
    """camera simulation dataset for UCM hdf5 files. Data are loaded in memory """

    def __init__(self, hdf5_file_path, camera_type, group_by, targets, use_time=False, transform=None,
                 target_transform=None, telescope_transform=None, particle='gammaness'):
        """
        Parameters
        ----------
            hdf5_file_path (str): path to hdf5 file containing the data
            camera_type (str) : name of the camera used (e.g. camera_type='LST')
            group_by (str): the way to group images in the dataset (e.g. 'event_triggered_tels' :
            by event only for telescopes which triggered)
            targets (list): the targets to include in the sample
            use_time (bool, optional): whether or not include the time peak in the sample
            transform (callable, optional): Optional transform to be applied on a sample
            target_transform (callable, optional): Optional transform to be applied on a sample
            telescope_transform (callable, optional): Optional transform to be applied on a sample
        """
        self.hdf5_file_path = hdf5_file_path
        self.transform = transform
        self.target_transform = target_transform
        self.telescope_transform = telescope_transform
        self.camera_type = camera_type
        self.use_time = use_time
        self.targets = targets
        self.particle = particle

        group_by_options = ['image', 'event_all_tels', 'event_triggered_tels']

        assert group_by in group_by_options, '{} is not a suitable group option. Must be in {}'.format(group_by,
                                                                                            group_by_options)

        self.group_by = group_by

        with tables.File(hdf5_file_path, 'r') as hdf5_file:
            # Load images and peak times
            self.runs = len(hdf5_file.root._v_attrs.runlist)
            self.num_showers = hdf5_file.root._v_attrs.num_showers
            self.shower_reuse = hdf5_file.root._v_attrs.shower_reuse
            self.spectral_index = hdf5_file.root._v_attrs.spectral_index
            self.max_scatter_range = hdf5_file.root._v_attrs.max_scatter_range
            self.energy_range_max = hdf5_file.root._v_attrs.energy_range_max
            self.energy_range_min = hdf5_file.root._v_attrs.energy_range_min
            self.max_alt = hdf5_file.root._v_attrs.max_alt
            self.min_alt = hdf5_file.root._v_attrs.min_alt

            self.images = hdf5_file.root[self.camera_type][:]['charge'][()]
            self.times = hdf5_file.root[self.camera_type][:]['peakpos'][()]

            # Load event info
            self.multiplicity = hdf5_file.root.Events[:][self.camera_type + '_multiplicity'][()]
            indices_mask = self.multiplicity > 0
            self.image_indices = hdf5_file.root.Events[:][self.camera_type + '_indices'][()][indices_mask]
            self.multiplicity = self.multiplicity[indices_mask]

            self.altitudes = hdf5_file.root.Events[:]['alt'][()][indices_mask]
            self.azimuths = hdf5_file.root.Events[:]['az'][()][indices_mask]
            self.xCores = hdf5_file.root.Events[:]['core_x'][()][indices_mask]
            self.yCores = hdf5_file.root.Events[:]['core_y'][()][indices_mask]
            self.height_first = hdf5_file.root.Events[:]['h_first_int'][()][indices_mask]
            self.xmax = hdf5_file.root.Events[:]['x_max'][()][indices_mask]
            self.energies = hdf5_file.root.Events[:]['mc_energy'][()][indices_mask]
            self.particle_types = hdf5_file.root.Events[:]['shower_primary_id'][()][indices_mask]
            self.event_ids = hdf5_file.root.Events[:]['event_id'][()][indices_mask]
            self.run_ids = hdf5_file.root.Events[:]['obs_id'][()][indices_mask]

            # Load array info
            tel_info_mask = np.in1d(hdf5_file.root.Array_Information[:]['type'], self.camera_type.encode('ascii'))
            self.tel_ids = hdf5_file.root.Array_Information[tel_info_mask]['id'][()]
            self.tel_positions = np.column_stack((hdf5_file.root.Array_Information[tel_info_mask]['x'][()],
                                                 hdf5_file.root.Array_Information[tel_info_mask]['y'][()],
                                                 hdf5_file.root.Array_Information[tel_info_mask]['z'][()]))
            self.tel_altitudes = np.full(self.tel_ids.shape[0], hdf5_file.root._v_attrs.run_array_direction[1])
            self.tel_azimuths = np.full(self.tel_ids.shape[0], hdf5_file.root._v_attrs.run_array_direction[0])

        if self.group_by == 'image':
            altitudes = np.zeros(self.images.shape[0])
            azimuths = np.zeros(self.images.shape[0])
            xCores = np.zeros(self.images.shape[0])
            yCores = np.zeros(self.images.shape[0])
            height_first = np.zeros(self.images.shape[0])
            x_max = np.zeros(self.images.shape[0])
            energies = np.zeros(self.images.shape[0])
            particle_types = np.zeros(self.images.shape[0])
            event_ids = np.zeros(self.images.shape[0])
            run_ids = np.zeros(self.images.shape[0])
            telescope_ids = np.zeros(self.images.shape[0])
            multiplicity = np.zeros(self.images.shape[0])

            for event, indices in enumerate(self.image_indices):
                for tel_id, image_id in enumerate(indices):
                    if image_id != 0:
                        altitudes[image_id] = self.altitudes[event]
                        azimuths[image_id] = self.azimuths[event]
                        xCores[image_id] = self.xCores[event]
                        yCores[image_id] = self.yCores[event]
                        height_first[image_id] = self.height_first[event]
                        x_max[image_id] = self.xmax[event]
                        energies[image_id] = self.energies[event]
                        particle_types[image_id] = self.particle_types[event]
                        event_ids[image_id] = self.event_ids[event]
                        run_ids[image_id] = self.run_ids[event]
                        multiplicity[image_id] = self.multiplicity[event]
                        telescope_ids[image_id] = self.tel_ids[tel_id]

            self.altitudes = altitudes[1:]
            self.azimuths = azimuths[1:]
            self.xCores = xCores[1:]
            self.yCores = yCores[1:]
            self.height_first = height_first[1:]
            self.xmax = x_max[1:]
            self.energies = energies[1:]
            self.particle_types = particle_types[1:]
            self.event_ids = event_ids[1:]
            self.run_ids = run_ids[1:]
            self.multiplicity = multiplicity[1:]
            self.telescope_ids = telescope_ids[1:]
            self.images = self.images[1:]
            self.times = self.times[1:]

        if self.particle == 'gammaness':
            self.particle_types[self.particle_types == 0] = 1.
            self.particle_types[self.particle_types == 101] = 0.
        elif self.particle == 'hadroness':
            self.particle_types[self.particle_types == 101] = 1.
        else:
            raise ValueError('Unknown particleness')

    def __len__(self):
        if self.group_by == 'image':
            return len(self.images)
        else:
            return len(self.event_ids)

    def __getitem__(self, idx):
        if self.group_by == 'image':
            image = self.images[idx].reshape(1, -1)
            times = self.times[idx].reshape(1, -1)
            tel_id = self.telescope_ids[idx]

            if self.use_time:
                data = np.concatenate((image, times))
            else:
                data = image
            tel_altitude = self.tel_altitudes[self.tel_ids == tel_id]
            tel_azimuth = self.tel_azimuths[self.tel_ids == tel_id]
            tel_position = self.tel_positions[self.tel_ids == tel_id] / 1000
            telescopes = np.column_stack((tel_altitude, tel_azimuth, tel_position)).squeeze()
        else:
            if self.group_by == 'event_all_tels':
                # We want as many images as telescopes
                event_images = self.images[self.image_indices[idx]]
                event_times = self.times[self.image_indices[idx]]
                telescopes = np.column_stack((self.tel_altitudes, self.tel_azimuths, self.tel_positions))
            elif self.group_by == 'event_triggered_tels':
                indices = self.image_indices[idx][self.image_indices[idx] != 0]
                event_images = self.images[indices]
                event_times = self.times[indices]
                tel_altitudes = self.tel_altitudes[self.image_indices[idx] != 0]
                tel_azimuths = self.tel_azimuths[self.image_indices[idx] != 0]
                tel_positions = self.tel_positions[self.image_indices[idx] != 0]
                telescopes = np.column_stack((tel_altitudes, tel_azimuths, tel_positions))
            else:
                raise ValueError('group_by option has an incorrect value.')

            if self.use_time:
                data = np.zeros((event_images.shape[0] * 2, event_images.shape[1]), dtype=np.float32)
                data[0::2, :] = event_images
                data[1::2, :] = event_times
            else:
                data = event_images
        labels = []
        for t in self.targets:
            if t == 'energy':
                labels.append(np.log10(self.energies[idx]))
            elif t == 'impact':
                if self.group_by == 'image':
                    labels.append(self.xCores[idx]/1000 - tel_position[0, 0])
                    labels.append(self.yCores[idx]/1000 - tel_position[0, 1])
                else:
                    labels.append(self.xCores[idx] / 1000)
                    labels.append(self.yCores[idx] / 1000)
            elif t == 'direction':
                if self.group_by == 'image':
                    if self.targets[t]['unit'] == 'degrees':
                        labels.append((self.altitudes[idx] - tel_altitude.item()) / np.pi * 180)  # direction in degrees
                        labels.append((self.azimuths[idx] - tel_azimuth.item()) / np.pi * 180)  # direction in degrees
                    else:
                        labels.append(self.altitudes[idx] - tel_altitude.item())
                        labels.append(self.azimuths[idx] - tel_azimuth.item())
                else:
                    if self.targets[t]['unit'] == 'degrees':
                        labels.append((self.altitudes[idx] - tel_altitudes.item()) / np.pi * 180)  # direction in degrees
                        labels.append((self.azimuths[idx] - tel_azimuths.item()) / np.pi * 180)  # direction in degrees
                    else:
                        labels.append(self.altitudes[idx] - tel_altitudes.item())
                        labels.append(self.azimuths[idx] - tel_azimuths.item())
            elif t == 'xmax':
                labels.append(self.xmax[idx]/1000)
            elif t == 'class':
                labels.append(self.particle_types[idx])
            else:
                raise ValueError('Unknown target')

        sample = {'image': data, 'telescope': telescopes, 'label': np.array(labels, dtype=np.float32),
                  'mc_energy': np.log10(self.energies[idx])}

        if self.transform:
            sample['image'] = self.transform(sample['image'])
        if self.target_transform:
            sample['label'] = self.target_transform(sample['label'])
            sample['mc_energy'] = self.target_transform(sample['mc_energy'])
        if self.telescope_transform:
            sample['telescope'] = self.telescope_transform(sample['telescope'])

        return sample


class UCMCamDatasetOld(Dataset):
    """camera simulation dataset for UCM hdf5 files. Data are loaded in memory """

    def __init__(self, hdf5_file_path, camera_type, group_by, targets, use_time=False, transform=None,
                 target_transform=None, telescope_transform=None, particle='gammaness'):
        """
        Parameters
        ----------
            hdf5_file_path (str): path to hdf5 file containing the data
            camera_type (str) : name of the camera used (e.g. camera_type='LST')
            group_by (str): the way to group images in the dataset (e.g. 'event_triggered_tels' :
            by event only for telescopes which triggered)
            targets (list): the targets to include in the sample
            use_time (bool, optional): whether or not include the time peak in the sample
            transform (callable, optional): Optional transform to be applied on a sample
            target_transform (callable, optional): Optional transform to be applied on a sample
            telescope_transform (callable, optional): Optional transform to be applied on a sample
        """
        self.hdf5_file_path = hdf5_file_path
        self.transform = transform
        self.target_transform = target_transform
        self.telescope_transform = telescope_transform
        self.camera_type = camera_type
        self.use_time = use_time
        self.targets = targets
        self.particle = particle

        group_by_options = ['image', 'event_all_tels', 'event_triggered_tels']

        assert group_by in group_by_options, '{} is not a suitable group option. Must be in {}'.format(group_by,
                                                                                            group_by_options)

        self.group_by = group_by

        with tables.File(hdf5_file_path, 'r') as hdf5_file:
            # Load images and peak times
            self.images = hdf5_file.root[self.camera_type][:]['image_charge'][()]
            self.times = hdf5_file.root[self.camera_type][:]['image_peak_times'][()]

            # Load event info
            self.image_indices = hdf5_file.root.Event_Info[:][self.camera_type + '_indices'][()]
            indices_mask = np.count_nonzero(self.image_indices, axis=1) > 0
            self.image_indices = self.image_indices[indices_mask]
            self.altitudes = hdf5_file.root.Event_Info[:]['alt'][()][indices_mask]
            self.azimuths = hdf5_file.root.Event_Info[:]['az'][()][indices_mask]
            self.xCores = hdf5_file.root.Event_Info[:]['core_x'][()][indices_mask]
            self.yCores = hdf5_file.root.Event_Info[:]['core_y'][()][indices_mask]
            self.height_first = hdf5_file.root.Event_Info[:]['h_first_int'][()][indices_mask]
            self.energies = hdf5_file.root.Event_Info[:]['mc_energy'][()][indices_mask]
            self.particle_types = hdf5_file.root.Event_Info[:]['particle_id'][()][indices_mask]
            self.event_ids = hdf5_file.root.Event_Info[:]['event_number'][()][indices_mask]
            self.run_ids = hdf5_file.root.Event_Info[:]['run_number'][()][indices_mask]

            # Load array info
            tel_info_mask = np.in1d(hdf5_file.root.Array_Info[:]['tel_type'], self.camera_type.encode('ascii'))
            self.tel_altitudes = hdf5_file.root.Array_Info[tel_info_mask]['run_array_direction'][:, 1][()]
            self.tel_azimuths = hdf5_file.root.Array_Info[tel_info_mask]['run_array_direction'][:, 0][()]
            self.tel_ids = hdf5_file.root.Array_Info[tel_info_mask]['tel_id'][()]
            self.tel_positions = np.column_stack((hdf5_file.root.Array_Info[tel_info_mask]['tel_x'][()],
                                                  hdf5_file.root.Array_Info[tel_info_mask]['tel_y'][()],
                                                  hdf5_file.root.Array_Info[tel_info_mask]['tel_z'][()]))

        if self.group_by == 'image':
            altitudes = np.zeros(self.images.shape[0])
            azimuths = np.zeros(self.images.shape[0])
            xCores = np.zeros(self.images.shape[0])
            yCores = np.zeros(self.images.shape[0])
            height_first = np.zeros(self.images.shape[0])
            energies = np.zeros(self.images.shape[0])
            particle_types = np.zeros(self.images.shape[0])
            event_ids = np.zeros(self.images.shape[0])
            run_ids = np.zeros(self.images.shape[0])
            telescope_ids = np.zeros(self.images.shape[0])

            for event, indices in enumerate(self.image_indices):
                for tel_id, image_id in enumerate(indices):
                    if image_id != 0:
                        altitudes[image_id] = self.altitudes[event]
                        azimuths[image_id] = self.azimuths[event]
                        xCores[image_id] = self.xCores[event]
                        yCores[image_id] = self.yCores[event]
                        height_first[image_id] = self.height_first[event]
                        energies[image_id] = self.energies[event]
                        particle_types[image_id] = self.particle_types[event]
                        event_ids[image_id] = self.event_ids[event]
                        run_ids[image_id] = self.run_ids[event]
                        telescope_ids[image_id] = self.tel_ids[tel_id]

            self.altitudes = altitudes[1:]
            self.azimuths = azimuths[1:]
            self.xCores = xCores[1:]
            self.yCores = yCores[1:]
            self.height_first = height_first[1:]
            self.energies = energies[1:]
            self.particle_types = particle_types[1:]
            self.event_ids = event_ids[1:]
            self.run_ids = run_ids[1:]
            self.telescope_ids = telescope_ids[1:]
            self.images = self.images[1:]
            self.times = self.times[1:]

        if self.particle == 'gammaness':
            self.particle_types[self.particle_types == 0] = 1.
            self.particle_types[self.particle_types == 101] = 0.
        elif self.particle == 'hadroness':
            self.particle_types[self.particle_types == 101] = 1.
        else:
            raise ValueError('Unknown particleness')

    def __len__(self):
        if self.group_by == 'image':
            return len(self.images)
        else:
            return len(self.event_ids)

    def __getitem__(self, idx):
        if self.group_by == 'image':
            image = self.images[idx].reshape(1, -1)
            times = self.times[idx].reshape(1, -1)
            tel_id = self.telescope_ids[idx]

            if self.use_time:
                data = np.concatenate((image, times))
            else:
                data = image
            tel_altitude = self.tel_altitudes[self.tel_ids == tel_id]
            tel_azimuth = self.tel_azimuths[self.tel_ids == tel_id]
            tel_position = self.tel_positions[self.tel_ids == tel_id]
            telescopes = np.column_stack((tel_altitude, tel_azimuth, tel_position)).squeeze()
        else:
            if self.group_by == 'event_all_tels':
                # We want as many images as telescopes
                event_images = self.images[self.image_indices[idx]]
                event_times = self.times[self.image_indices[idx]]
                telescopes = np.column_stack((self.tel_altitudes, self.tel_azimuths, self.tel_positions))
            elif self.group_by == 'event_triggered_tels':
                indices = self.image_indices[idx][self.image_indices[idx] != 0]
                event_images = self.images[indices]
                event_times = self.times[indices]
                tel_altitudes = self.tel_altitudes[self.image_indices[idx] != 0]
                tel_azimuths = self.tel_azimuths[self.image_indices[idx] != 0]
                tel_positions = self.tel_positions[self.image_indices[idx] != 0]
                telescopes = np.column_stack((tel_altitudes, tel_azimuths, tel_positions))
            else:
                raise ValueError('group_by option has an incorrect value.')

            if self.use_time:
                data = np.zeros((event_images.shape[0] * 2, event_images.shape[1]), dtype=np.float32)
                data[0::2, :] = event_images
                data[1::2, :] = event_times
            else:
                data = event_images
        labels = []
        for t in self.targets:
            if t == 'energy':
                labels.append(np.log10(self.energies[idx]))
            if t == 'impact':
                labels.append(self.xCores[idx]/1000)
                labels.append(self.yCores[idx]/1000)
            if t == 'direction':  #TODO update for stereo
                labels.append((self.altitudes[idx] - tel_altitude.item()) / np.pi * 180)  # direction in degrees
                labels.append((self.azimuths[idx] - tel_azimuth.item()) / np.pi * 180)
            if t == 'xmax':
                labels.append(self.xmax[idx]/1000)
            if t == 'class':
                labels.append(self.particle_types[idx])

        sample = {'image': data, 'telescope': telescopes, 'label': np.array(labels, dtype=np.float32),
                  'mc_energy': np.log10(self.energies[idx])}

        if self.transform:
            sample['image'] = self.transform(sample['image'])
        if self.target_transform:
            sample['label'] = self.target_transform(sample['label'])
            sample['mc_energy'] = self.target_transform(sample['mc_energy'])
        if self.telescope_transform:
            sample['telescope'] = self.telescope_transform(sample['telescope'])

        return sample


class NumpyDataset(Dataset):

    def __init__(self, data, labels, transform=None, target_transform=None):
        self.images = data
        self.labels = labels
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, item):

        if self.transform:
            self.images[item] = self.transform(self.images[item])
        if self.target_transform:
            self.labels[item] = self.target_transform(self.labels[item])

        return self.images[item], self.labels[item]


class HDF5Dataset(Dataset):
    """Loads data in a Dataset from a HDF5 file.

    Args:
        path (str): The path to the HDF5 file.
        transform (callable, optional): A callable or a composition of callable to be applied to the data.
        target_transform (callable, optional): A callable or a composition of callable to be applied to the labels.
    """
    def __init__(self, path, camera_type, transform=None, target_transform=None, telescope_transform=None):
        with tables.File(path, 'r') as f:
            self.images = f.root['images'][:][()]
            self.labels = f.root['labels'][:][()]
        self.transform = transform
        self.target_transform = target_transform
        self.camera_type = camera_type

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, item):
        image, label = self.images[item], self.labels[item]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.transform(label)

        return {'image': image, 'label': label}


# Transforms classes

class Unsqueeze(object):
    """Unsqueeze a tensor"""
    def __call__(self, data):
        data.unsqueeze_(0)
        return data


class NumpyToTensor(object):
    """Convert a numpy array to a tensor"""

    def __call__(self, data):
        data = torch.tensor(data)
        return data


class EnergyToLog(object):
    """Convert energy to log(energy)"""

    def __call__(self, label):
        label[0] = np.log10(label[0])
        return label


class ImpactToKm(object):
    """Transform impact coordinates from m to km"""

    def __call__(self, label):
        label[1] /= 1000
        label[2] /= 1000
        return label


class TelescopePositionToKm(object):
    """Transform impact coordinates from m to km"""

    def __call__(self, telescope):
        if len(telescope.shape) == 1:
            telescope[2] /= 1000
            telescope[3] /= 1000
            telescope[4] /= 1000
        elif len(telescope.shape) == 2:
            telescope[:, 2] /= 1000
            telescope[:, 3] /= 1000
            telescope[:, 4] /= 1000
        return telescope


class RotateImage(object):
    """Rotate telescope image based on rotated indices"""

    def __init__(self, rotated_indices):
        self.rotated_indices = rotated_indices

    def __call__(self, data):
        assert data.shape[-1] == self.rotated_indices.shape[0], 'The length of rotated indices must match the size of the image to rotate. '
        return data[..., self.rotated_indices]


class NormalizePixel(object):

    def __init__(self, max):
        self.max = max

    def __call__(self, data):
        return data / self.max

# Deprecated
# class NormalizePixels(object):
#     """Normalize pixels intensity based on global data stats"""
#
#     def __init__(self, stats_file, norm_type='standard', scaling_range=[0, 1]):
#         self.norm_type = norm_type
#         self.scaling_range = scaling_range
#         with h5py.File(stats_file, 'r') as f:
#             self.min_pixel = f['min_pixel'].value
#             self.max_pixel = f['max_pixel'].value
#             self.pixel_mean = f['pixel_mean'].value
#             self.pixel_var = f['pixel_var'].value
#
#     def __call__(self, sample):
#         if self.norm_type == 'standard':
#             # Works well for normally distributed population
#             sample['images'] -= self.pixel_mean
#             sample['images'] /= torch.sqrt(torch.tensor(self.pixel_var))
#         elif self.norm_type == 'scaling':
#             # Rescaling into the range in parameters
#             sample['images'] -= self.min_pixel
#             sample['images'] /= (self.max_pixel - self.min_pixel) * (self.scaling_range[1] - self.scaling_range[0])
#             sample['images'] += self.scaling_range[0]
#         elif self.norm_type == 'log':
#             sample['images'] -= self.min_pixel - 1
#             sample['images'] = torch.log(sample['images'])
#         else:
#             self.logger.warning('Unknown normalization type : {}, no normalization applied'.format(self.norm_type))
#
#         return sample

# Augment data functions

def augment_via_rotation(datasets, thetas, num_workers):
    """
    Function to augment dataset via image rotation
    Parameters
    ----------
    datasets (list): list of Subsets
    thetas (list): list of thetas (in rad)
    num_workers (int): number of processes to use

    Returns
    -------

    """
    def process_subset():
        torch.set_num_threads(1)
        while True:
            if input_queue.empty():
                break
            else:
                sub = input_queue.get()
            for theta in thetas:
                pixels_position = utils.load_camera_parameters(sub.dataset.camera_type)['pixelsPosition']
                rot_indices = utils.rotated_indices(pixels_position, theta)
                new_subset = copy.copy(sub)
                new_subset.dataset.transform = Compose([RotateImage(rot_indices)] + sub.dataset.transform.transforms)
                new_datasets.append(new_subset)

    input_queue = mp.Queue()
    for subset in datasets:
        input_queue.put(subset)
    manager = mp.Manager()
    new_datasets = manager.list()
    workers = [mp.Process(target=process_subset) for _ in range(num_workers)]
    for w in workers:
        w.start()
    input_queue.close()
    for w in workers:
        w.join()

    datasets += list(new_datasets)

    return datasets


def augment_via_duplication(datasets, scale, num_workers):
    """
    Augment data by duplicating events based on the inverse detected energies distribution
    Parameters
    ----------
    datasets (list): list of Subsets
    scale (float): the scale to constrain the maximum duplication factor
    num_workers (int): number of processes to use

    Returns
    -------

    """
    def get_factor(energy, scale):
        fitlog = 1.19 * (2.59 - energy) * (1 - np.exp(-2.91 - energy))
        p = 1/(10**fitlog) * 1/(1/(10**fitlog)).min()
        return np.floor(1 + scale * np.log10(p)).astype(np.int)

    def process_subset():
        torch.set_num_threads(1)
        while True:
            if input_queue.empty():
                break
            else:
                sub = input_queue.get()
                factors = get_factor(np.log10(sub.dataset.energies), scale)
                augmented_ids = np.repeat(np.arange(len(sub.dataset)), factors)
                sub.indices = augmented_ids[np.in1d(augmented_ids, sub.indices)]
                new_datasets.append(sub)

    input_queue = mp.Queue()
    for subset in datasets:
        input_queue.put(subset)
    manager = mp.Manager()
    new_datasets = manager.list()
    workers = [mp.Process(target=process_subset) for _ in range(num_workers)]
    for w in workers:
        w.start()
    input_queue.close()
    for w in workers:
        w.join()
    return list(new_datasets)
