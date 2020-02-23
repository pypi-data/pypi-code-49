"""Functions to manage pandas and hdf5 databases.

Intended to be used within a Python 3 environment.
Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

# Flexibility for python 2.x
try:
    from pathlib import Path
except ImportError:
    pass

import shutil

import h5py
import numpy as np
import pandas as pd

from . import strings_tools as st
from . import filesystem_tools as ft


class H5(h5py._hl.files.File):
    """A class to add functionally to h5py objects.

    The following thermnilogy is used in this class:

    - "Root level" is defined as the root of hdf5 file. Therefore, the
        "root level groups" correspond to those located in the root of
        the file.

    - "First level" nodes (groups or datasets) are those inside a root
        level group.

    Attributes
    ----------
    fl_attrs : list of str
        List of attributes names of all first level datasets.
    """

    @staticmethod
    def get_fl_unique_attrs(db_path):
        """Extract a list of hdf5 first level datasets attributes.

        Returns
        -------
        List of str
            Attributes names of all first level datasets.
        """
        get_uniques = st.get_uniques_in_list_of_lists
        m_attrs = get_uniques([list(b.attrs) for v in db_path.values()
                               for b in v.values()])
        return m_attrs

    @staticmethod
    def save_npz_in_hdf5(npz_files_list, hdf5_path=None,
                         add_attributes=None, verbose=False):
        """Save content of multiple npz numpy arrays to hdf5 file.

        Parameters
        ----------
        npz_files_list : List of Paths
            Npz saved compressed numpy arrays.
        hdf5_path : Path, optional
            Output database hdf5 file. If not given, the function takes
            the first path in `npz_files_list` as hdf5 file name.
        add_attributes : dict of dicts, optional
            Npz identifier : {parameters names : float } pairs. If
            given, add attributes to each npz group.
        verbose : bool, optional
            If True, print output hdf5 structure. Default is False.
        """
        # Set default output hdf5 path.
        if hdf5_path is None:
            hdf5_path = Path(npz_files_list[0]).with_suffix('.hdf5')

        # Create output hdf5 file
        #
        # Iterate over npz files list. Create a group  for each npz file,
        # using relative orders as groups keys.
        output = H5(hdf5_path, 'w')
        for model_pos, npz_path in enumerate(npz_files_list):
            model_no = model_pos + 1
            grp = output.create_group(str(model_no))

            # Set values of interest as group attributes.
            if add_attributes:
                for k, value in add_attributes[int(model_no)].items():
                    grp.attrs[k] = value

            # Load npz arrays and save them as groups data-sets. Keys
            # will be whatever keys were present in each npz file.
            arrays = np.load(npz_path)
            for k, value in arrays.items():
                grp.create_dataset(k, data=value)

        # Print output file structure
        if verbose:
            output.show_hdf5_structure()
        return output

    @property
    def fl_unique_attrs(self):
        """Get list of first level dataset attributes."""
        return H5.get_fl_unique_attrs(self)

    def restructure_fl(self, common_dsets_keys=None):
        """Reorder hdf5 using first level datasets as root groups.

        This function reorganizes hdf5 internal structure, using common
        first level datasets keys as root level groups keys. This
        allows to have outputs from different models under one group
        for each physic output variable.

        If there are M root groups (corresponding to M models, from M
        npz files) and V output variables, input hdf5 should have M
        root level groups, each of them containing V first level
        datasets. This algorithm swaps those categories. Therefore,
        restructured hdf5 should have V root level groups with M
        datasets each.

        Attributes are copied from each original group to corresponding
        restructured datasets.

        Parameters
        ----------
        common_dsets_keys : list of str, optional
            Keys of first level datasets to use as root groups. If not
            provided, the function find and uses all common keys.

        Returns
        -------
        None

        Examples
        --------
        Original hdf5 structure as follows:

        root groups = 1, 2, 3, ...
        first level datasets from 1 =
        {out_a: array_1}, {out_b: array_2}, {out_c: array_3}, ...
        first level datasets in 2 =
        {out_a: array_4}, {out_b: array_5}, {out_c: array_6}, ...
        first level datasets in 3 =
        {out_a: array_7}, {out_b: array_8}, {out_c: array_9}, ...

        New structure as follows:

        new root gropus = out_a, out_b, out_3, ...
        first level datasets in out_a =
        {1: array_1}, {2: array_4}, {3: array_7}, ...
        first level datasets in out_b =
        {1: array_2}, {2: array_5}, {3: array_8}, ...
        first level datasets in out_c =
        {1: array_3}, {2: array_6}, {3: array_9}, ...

        Attributes are copied from 1 to {1 : array_1}, {1: array_2},
        {1: array_3}, ...; and from {out_a: array_1}, {out_a: array_4},
        {out_a: array_7}, ... to out_a root group.

        """
        # Set a temporal file path.
        origin_path = Path(self.filename)
        temp_path = Path(origin_path.parent, 'temp')

        # Set all datasets keys as default root groups keys.
        if not common_dsets_keys:
            get_unique = st.get_uniques_in_list_of_lists
            common_dsets_keys = get_unique([v.keys() for v
                                            in self.values()])

        # Open temp hdf5 file and iterate trough original datasets,
        # swapping groups names with datasets, including attributes.
        out = H5(temp_path, 'w')
        datasets_attrs = {}
        for groups in self.values():
            for dts_key, dts in groups.items():
                datasets_attrs[dts_key] = dts.attrs.items()
        for key in common_dsets_keys:
            out_grp = out.create_group(key)
            out_grp.attrs.update(datasets_attrs[key])
            for group_n, group in self.items():
                dts = out_grp.create_dataset(group_n, data=group[key])
                dts.attrs.update(group.attrs)

        # Close both original hdf5 and temp files. Copy temporal hdf5
        # as original, delete it and redefine H5 object.
        self.close()
        out.close()
        shutil.copy(temp_path, origin_path)
        Path.unlink(temp_path)
        self.__init__(origin_path, 'r')

    def show_structure(self):
        """Print main structure of a hdf5 file."""
        def print_attrs(name, _):
            print(name)
        self.visititems(print_attrs)


def reformat_peer_data_csv(csv_file_path, time_step=0.005):
    """Reformat PEER motion records to column-wise, and save to csv.

    Typically, PEER data is given in a plane text file, with data
    disposed in horizontal consecutive arrays. This function serializes
    it in a single column and returns the new data frame in a csv file.

    Parameters
    ----------
    csv_file_path : Path
        Csv file to load data from.
    time_step : float
        Time step of record. Needs to be set to create time column.

    Returns
    -------
    Path
        Path of corrected cdv file.
    """
    # Normalize input as Path object and read csv file.
    csv_file_path = Path(csv_file_path).with_suffix('.csv')
    data_frame = pd.read_csv(csv_file_path, header=None)

    # Transpose data for handling. Extract it column-wise in new df.
    df_trans = data_frame.transpose()
    column = [df_trans[i] for i in df_trans]
    combined = pd.concat(column, ignore_index=True)

    # Create new data-frame and add time column.
    df_out = pd.DataFrame()
    df_out['T'] = np.arange(0, time_step * (len(combined) - 2), time_step)
    df_out['DATA'] = combined

    # Save corrected csv file in new csv file.
    output_path = ft.modify_filename_in_path(csv_file_path,
                                             added='_corrected', prefix=False)
    df_out.to_csv(output_path, index=False)
    return output_path


def save_dataframe_safely(data_frame, output_csv, overwrite=False):
    """Save pandas dataframe as csv, avoiding accidental overwriting.

    Parameters
    ----------
    data_frame : pandas DataFrame
        To be saved as csv.
    output_csv : Path
        Path of output csv file.
    overwrite : bool, optional
        If True, allow overwrite of output file.
    """
    # Normalize csv file path.
    output_csv = Path(output_csv).with_suffix('.csv')

    # Check output file existence.
    if output_csv.exists():
        print('WARNING: CSV FILE EXISTS')

        # Overwrite if it is allowed.
        if overwrite:
            data_frame.to_csv(output_csv, index=False, mode='w+')
            print(Path(output_csv).stem, 'CSV FILE OVERWRITTEN')

        # Do not save file is overwrite is not allowed.
        else:
            print(Path(output_csv).stem, 'CSV FILE NOT SAVED')

    # If output file does not exist yet, create it.
    else:
        data_frame.to_csv(output_csv, index=False, mode='w')
        print(Path(output_csv).stem, '*** CSV FILE SAVED ***')
