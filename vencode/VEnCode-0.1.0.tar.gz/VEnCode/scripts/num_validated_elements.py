import os
import sys
from tqdm import tqdm

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals
from VEnCode.utils import dir_and_file_handling as d_f_handling
from VEnCode.utils import validation_utils as val
from VEnCode.common_variables import promoter_file_name, enhancer_file_name, primary_cell_list


class SetUp:
    """set up some variables: """
    cell_type = "hepatocellular carcinoma cell line: HepG2 ENCODE"
    type = "cell lines"
    data_type = "enhancers"

    celltypes = ["small cell lung carcinoma cell line"]  # primary_cell_list
    types = "primary cells"

    data_set = "both"  # default: None

    # Next ones you may not need to change:
    if data_type == "enhancers":
        file_name = enhancer_file_name
        target_celltype_activity = 0.1
    elif data_type == "promoters":
        file_name = promoter_file_name
        target_celltype_activity = 0.5
    else:
        raise AttributeError("data_type - {} - currently not supported".format(data_type))


# Now you don't need to change anything else

class ValidatedElements:
    def __init__(self, set_up):
        self.set_up = set_up
        self.validate_with = val.get_data_to_validate(set_up.cell_type, set_up.data_set)
        re_other_dataset = self.validate_with.data.shape[0]

        if val.status_parsed(set_up.cell_type):
            self._data_parsed_cleaner()
        else:
            self._data_raw_cleaner()
        re_not_val = self.data.data.shape[0]

        self.data.select_validated()

        re_val = self.data.data.shape[0]
        results = re_val / re_not_val * 100

        self.results = {"CAGE": re_not_val, "Other data set": re_other_dataset, "together": re_val,
                        "percentage": results}

    def _data_parsed_cleaner(self):
        self.data = internals.DataTpmValidated(self.validate_with, file="parsed", sample_types="cell lines",
                                               data_type=self.set_up.data_type)
        self.data.make_data_celltype_specific(self.set_up.cell_type)
        self.data.filter_by_target_celltype_activity(threshold=self.set_up.target_celltype_activity)

    def _data_raw_cleaner(self):
        data_to_add_ctp = internals.DataTpm(file=self.set_up.file_name, sample_types=self.set_up.type,
                                            data_type=self.set_up.data_type)

        self.data = internals.DataTpmValidated(self.validate_with, file=self.set_up.file_name,
                                               sample_types="primary cells",
                                               data_type=self.set_up.data_type)
        self.data.merge_donors_primary(exclude_target=False)
        self.data.add_celltype(self.set_up.cell_type, file=data_to_add_ctp, data_type=self.set_up.data_type)
        self.data.make_data_celltype_specific(self.set_up.cell_type)
        self.data.filter_by_target_celltype_activity(threshold=self.set_up.target_celltype_activity)

    def export(self):
        """
        Export the results to a file.
        """
        # create a directory to store results
        if self.set_up.data_set is not None:
            folder = os.path.join("Validations", self.set_up.data_set)
        else:
            folder = "Validations"
        results_directory = d_f_handling.file_directory_handler("{}.csv".format(self.set_up.cell_type),
                                                                folder=folder,
                                                                path_type="parent3")
        d_f_handling.write_one_value_dict_to_csv(results_directory, self.results)
        print("File saved in: {}".format(results_directory))

"""
validate_with = internals.BroadPeak("DennySK2016")
validate_with_2 = internals.ChristensenCL2014Data()
validate_with.join_data_sets(validate_with_2)
print(validate_with.data.shape)

results = {}
for celltype in tqdm(setup.celltypes, desc="Completed: "):
    data = internals.DataTpmValidated(validate_with, file="parsed", sample_types=setup.types,
                                      data_type=setup.data_type)
    data.make_data_celltype_specific(celltype)
    data.filter_by_target_celltype_activity(threshold=setup.target_celltype_activity)
    re = data.data.shape[0]
    data.select_validated()
    validated_re = data.data.shape[0]
    results[celltype] = validated_re  # / re * 100
"""
"""
# create a directory to store results
results_directory = d_f_handling.file_directory_handler("num SCLC Denny REs.csv", folder="Validations",
                                                        path_type="parent3")

# Set up the important information to include in the file
info_list = [attr for attr in dir(setup) if not callable(getattr(setup, attr)) and not attr.startswith("__")]
info_dict = {}
for item in info_list:
    info_dict[item] = getattr(setup, item)

# Write the results on a file
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, info_dict, deprecated=False)
VEnCode.utils.dir_and_file_handling.write_one_value_dict_to_csv(results_directory, results, method="a")
print("File saved in: {}".format(results_directory))
"""

if __name__ == "__main__":
    setup = SetUp()
    ven = ValidatedElements(setup)
    ven.export()