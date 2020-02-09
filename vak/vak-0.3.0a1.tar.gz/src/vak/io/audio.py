import logging
import os

import numpy as np
import dask.bag as db
from dask.diagnostics import ProgressBar

from .annotation import source_annot_map
from ..config import validators
from ..config.spect_params import SpectParamsConfig
from ..util.audio import AUDIO_FORMAT_FUNC_MAP, files_from_dir
from ..util.spect import spectrogram


def to_spect(audio_format,
             spect_params,
             output_dir,
             audio_dir=None,
             audio_files=None,
             annot_list=None,
             audio_annot_map=None,
             labelset=None):
    """makes spectrograms from audio files and saves in array files

    Parameters
    ----------
    audio_format : str
        format of audio files. One of {'wav', 'cbin'}
    spect_params : dict or vak.config.spectrogram.SpectConfig
        parameters for computing spectrogram, from .ini file.
        To see all related parameters, run:
        >>> help(vak.config.spect_params.SpectParamConfig)
        To get a default configuration, create a SpectParamConfig
        with no arguments and then pass that to `to_spect`:
        >>> default_spect_params = vak.config.spect_params.SpectParamConfig()
        >>> to_spect(audio_format='wav', spect_params=default_spect_params, output_dir='.')
    audio_dir : str
        path to directory containing audio files from which to make spectrograms
    audio_files : list
        of str, full paths to audio files from which to make spectrograms
    annot_list : list
        of annotations for array files. Default is None.
    audio_annot_map : dict
        Where keys are paths to array files and value corresponding to each key is
        the annotation for that array file.
        Default is None.
    output_dir : str
        directory in which to save .spect.npz file generated for each audio file.
    labelset : set
        of str or int, set of unique labels for vocalizations. Default is None.
        If not None, then files will be skipped where the 'labels' array in the
        corresponding annotation contains labels that are not found in labelset

    Returns
    -------
    spect_files : list
        of str, full paths to .spect.npz files

    Notes
    -----
    For each audio file, a corresponding 'spect.npz' file will be created.
    Each '.spect.npz' file contains the following arrays:
        s : numpy.ndarray
            spectrogram, a 2-d array
        f : numpy.ndarray
            vector of centers of frequency bins from spectrogram
        t : numpy.ndarray
            vector of centers of tme bins from spectrogram
        audio_path : numpy.ndarray
            path to source audio file used to create spectrogram

    The names of the arrays are defaults, and will change if different values are specified
    in spect_params for 'spect_key', 'freqbins_key', 'timebins_key', or 'audio_path_key'.
    """
    if audio_format not in validators.VALID_AUDIO_FORMATS:
        raise ValueError(
            f"audio format must be one of '{validators.VALID_AUDIO_FORMATS}'; "
            f"format '{audio_format}' not recognized."
        )

    if all([arg is None for arg in (audio_dir, audio_files, audio_annot_map)]):
        raise ValueError('must specify one of: audio_dir, audio_files, audio_annot_map')

    if audio_dir and audio_files:
        raise ValueError('received values for audio_dir and audio_files, unclear which to use')

    if audio_dir and audio_annot_map:
        raise ValueError('received values for audio_dir and audio_annot_map, unclear which to use')

    if audio_files and audio_annot_map:
        raise ValueError('received values for audio_files and audio_annot_map, unclear which to use')

    if annot_list and audio_annot_map:
        raise ValueError(
            'received values for annot_list and array_annot_map, unclear which annotations to use'
        )

    if labelset is not None:
        if type(labelset) != set:
            raise TypeError(
                f'type of labelset must be set, but was: {type(labelset)}'
            )

    if type(spect_params) not in [dict, SpectParamsConfig]:
        raise TypeError(
            'type of spect_params must be an instance of vak.config.spect_params.SpectParamsConfig, '
            'or a dict that can be converted to a SpectParamsConfig instance, '
            f'but was {type(spect_params)}'
        )
    if type(spect_params) is dict:
        spect_params = SpectParamsConfig(**spect_params)

    # validate audio files if supplied by user
    if audio_files:
        # make sure audio files are all the same type, and the same as audio format specified
        exts = []
        for audio_file in audio_files:
            root, ext = os.path.splitext(audio_file)
            exts.append(ext)
        uniq_ext = set(exts)
        if len(uniq_ext) > 1:
            raise ValueError(
                'audio_files should all have the same extension, '
                f'but found more than one: {uniq_ext}'
                )
        else:
            ext_str = uniq_ext.pop()
            if audio_format not in ext_str:
                raise ValueError(
                    f"audio format. '{audio_format}', does not match extensions in audio_files, '{ext_str}''"
                )

        if annot_list:  # make map we can validate below
            audio_annot_map = source_annot_map(audio_files, annot_list)

    # otherwise get audio files using audio dir (won't need to validate audio files)
    if audio_dir:
        audio_files = files_from_dir(audio_dir, audio_format)
        if annot_list:
            audio_annot_map = source_annot_map(audio_files, annot_list)

    logger = logging.getLogger(__name__)
    logger.setLevel('INFO')
    logger.info('creating array files with spectrograms')

    # use mapping (if generated/supplied) with labelset, if supplied, to filter
    if audio_annot_map:
        if labelset:  # then remove annotations with labels not in labelset
            # note we do this here so it happens regardless of whether
            # user supplied audio_annot_map *or* we constructed it above
            for audio_file, annot in list(audio_annot_map.items()):
                # loop in a verbose way (i.e. not a comprehension)
                # so we can give user warning when we skip files
                annot_labelset = set(annot.seq.labels)
                # below, set(labels_mapping) is a set of that dict's keys
                if not annot_labelset.issubset(set(labelset)):
                    # because there's some label in labels that's not in labelset
                    audio_annot_map.pop(audio_file)
                    logger.info(
                        f'found labels in {annot.annot_file} not in labels_mapping, '
                        f'skipping audio file: {audio_file}'
                    )
        audio_files = sorted(list(audio_annot_map.keys()))

    # this is defined here so all other arguments to 'to_spect' are in scope
    def _spect_file(audio_file):
        """helper function that enables parallelized creation of array
        files containing spectrograms.
        Accepts path to audio file, saves .npz file with spectrogram"""
        fs, dat = AUDIO_FORMAT_FUNC_MAP[audio_format](audio_file)
        s, f, t = spectrogram(dat, fs,
                              spect_params.fft_size,
                              spect_params.step_size,
                              spect_params.thresh,
                              spect_params.transform_type,
                              spect_params.freq_cutoffs)
        spect_dict = {spect_params.spect_key: s,
                      spect_params.freqbins_key: f,
                      spect_params.timebins_key: t,
                      spect_params.audio_path_key: audio_file}
        basename = os.path.basename(audio_file)
        npz_fname = os.path.join(os.path.normpath(output_dir),
                                 basename + '.spect.npz')
        np.savez(npz_fname, **spect_dict)
        return npz_fname

    bag = db.from_sequence(audio_files)
    with ProgressBar():
        spect_files = list(bag.map(_spect_file))
    # sort because ordering from Dask not guaranteed
    spect_files = sorted(spect_files)
    return spect_files
