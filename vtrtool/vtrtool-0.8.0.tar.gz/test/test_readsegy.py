from vtrtool.aux_funcs import segymodel_to_vtrfile


sgy_file = "/Users/timlin/Projects/SubSalt/WebClient/vtrplot/tests/test_files/segy_vtr_equal/from_seisspace_3D.sgy"
vtr_file = "test_vtr.vtr"

segymodel_to_vtrfile(sgy_file, vtr_file, dims=(1041, 113, 161))
