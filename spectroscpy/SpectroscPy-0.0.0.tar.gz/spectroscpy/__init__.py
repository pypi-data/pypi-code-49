# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from .cauchy import get_interquartile_range, get_gamma, cauchy_lincomb, get_weighted_averages, \
                    get_set_of_weighted_averages, get_simple_averages
from .get_spectroscopy import which_spectroscopies_to_be_calculated, get_spectroscopy_indices, \
                              get_energy_derivatives, get_vibrational_frequencies_and_intensities, \
                              reduced_dims, getting_the_subblocks
from .openrsp_tensor_reader import read_openrsp_tensor_file, remove_whitespaces, get_redundant_indices, \
                                   rspProperty
from .parameters import *
from .plotting_module import get_sorted, get_zero_padded_intensities, get_x_fit, get_plot_values, \
                             visualize_spectrum
from .SpectroscPy_tools import check_spectroscopy_specifications_input, check_spectroscopy_types_input, \
                               check_command_input, check_cauchy_type, check_run_specification, \
                               get_mode_captions, get_ir_captions, get_raman_captions, \
                               get_cauchy_prefactor
from .SpectroscPy_wrapper import SpectroscPy_run
from .transform_nc_to_nm import list_product_int, transform_cartesian_to_normal_one_rank, \
                                transform_cartesian_to_normal
from .vib_analysis import mol_is_linear, read_mol, project_out_transl_and_rot, \
                          get_vib_harm_freqs_and_eigvecs, get_vibrational_w
from .ir import summed_dip_grad_sq, qi_prefactor2, get_ir_intensities
from .raman import combined_polarizabilites, raman_scattering_cross_section, get_exp_denominator, \
                   get_b2_term, get_a2_term, get_raman_headers, get_raman_intensities, \
                   requested_unit_incident_mode
from .hyperraman import get_hyperraman_intensities, get_average_beta_aaa2, get_average_beta_baa2, \
                        get_hyperraman_SI_scs, get_hyperraman_intensities
