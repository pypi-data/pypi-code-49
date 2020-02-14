# Argument parser
import argparse

def IMP_parser(args):
	parser = argparse.ArgumentParser(description='IMPRESSION')
	# Define command to perform
	parser.add_argument('Command', help='IMPRESSION command',
							choices=['setup_train', 'train', 'setup_predict', 'predict'])
	# Get preferences
	parser.add_argument('--prefs', help='How to obtain settings for command, leave blank to use command line input, specify json file, or <wizard> to run wizard',
							 default='')
	# Define training set, only needed for train and setup_train commands
	parser.add_argument('--training_set', help='Training dataset file(s), either single csv/pkl file or one/multiple nmredata files',
						 action="store", dest='training_set', default='')
	# Define output directory for non log files
	parser.add_argument('--output_dir', help='Output directory for non log files',
						action="store", dest='output_dir', default='')
	# Check whether to store prepared datasets or not
	parser.add_argument('--store_datasets', help='Option to store datasets as pickle files for later use',
						 action="store", dest='store_datasets', default='')

	# Define list of target parameters
	parser.add_argument('--target_list', help='Optional list of targets to go through',
						 action="store", dest='target_list', default=[])
	# Define single target (largely used internally)
	parser.add_argument('--targetflag', help='target NMR parameter',
							action="store", dest='targetflag', default='')

	# Optional arguments for train/test
	# Type of model to use
	parser.add_argument('--modelflag', help='type of model to use',
							action="store", dest='modelflag', default='',
							choices=['KRR', 'FCHL', 'NN', 'TFM'])
	# Type of features to user
	parser.add_argument('--featureflag', help='type of features to use',
							action="store", dest='featureflag', default='',
							choices=['CMAT', 'aSLATM', 'FCHL', 'ACSF', 'BCAI', ''])

	# Optional argments for train
	# Method for hyper-parameter search
	parser.add_argument('--searchflag', help='Method for hyper-parameter search',
							action="store", dest='searchflag', default='',
							choices=['grid', 'gaussian', 'random', ''])
	# Whether to optimise features in hyper-parameter optimisation (uses defaults for features otherwise)
	# This offers a pretty massive speed improvement especially for some features (aSLATM)
	parser.add_argument('--feature_optimisation', help='HPS includes feature parameters',
							action="store", dest='feature_optimisation', default='',
							choices=['True', 'False', ''])
	# Can supply pre-made features to use
	parser.add_argument('--feature_file', help='File containing pre-made feature dataset object',
							action="store", dest='feature_file', default='')
	# Define ranges for model parameters to optimise
	parser.add_argument('--param_ranges', help='Dictionary of parameter ranges for HPS',
							action="store", dest='param_ranges', default='{}')
	# Specify whether to treat paramater is linear of log scale (helps with optimisation)
	parser.add_argument('--param_logs', help='Dictionary (truth values only) for each parameter specifying whether parameter is on a log scale',
							action="store", dest='param_logs', default='{}')
	# Number of cross validation steps to perform
	parser.add_argument('--cv_steps', help='Number of cross validations to perform',
							 action="store", dest='cv_steps', default=-404)
	# How many HPS iterations to perform
	parser.add_argument('--epochs', help='Number of HPS iterations to perform',
							action="store", dest='epochs', default=-404)
	# Specify output logfile
	parser.add_argument('--logfile', help='Name of output log file',
							action="store", dest='logfile', default='')


	# Optional system arguments
	parser.add_argument('--python_env', help='Name of python environment to be used',
							action="store", dest='python_env', default='')
	# Define system (allows for HPC cluster specific submission)
	parser.add_argument('--system', help='System currently running',
							 action="store", dest='system', default='')
	# How much memory to allow in a HPC submission
	parser.add_argument('--memory', help='Memory needed in submission scripts',
							 action="store", dest='memory', default=-404)
	# How many processors to request in HPC submission
	parser.add_argument('--processors', help='Processors needed in submission scripts',
							 action="store", dest='processors', default=-404)
	# How much walltime to request in HPC submission
	parser.add_argument('--walltime', help='Walltime required for submission',
							 action="store", dest='walltime', default='')

	# Optional argments for predict
	# How many variance models to use
	parser.add_argument('--var', help='Number of pre-prediction variance models',
						action="store", dest='var', default=-404)
	# Define existing models to use for predictions
	parser.add_argument('--models', help='Existing model(s) to use, list',
						 action="store", dest='models', default=[])
	# Current prediction model, not sure if this is used
	parser.add_argument('--model', help='Current prediction model',
						action="store", dest='model', default='none')
	# Define set(s) of molecules to perform predictions on
	parser.add_argument('--test_sets', help='Testing dataset(s), either lists of file search patterns or individual files, list',
						 action="store", dest='test_sets', default=[])


	# Optional argments for grid search
	# Define density of points in grid
	parser.add_argument('--grid_density', help='Point density for grid search',
							 action="store", dest='grid_density', default=-404)

	# Optional arguments for gaussian search
	parser.add_argument('--kappa', help='Kappa value for gaussian process HPS',
							 action="store", dest='kappa', default=-404)
	parser.add_argument('--xi', help='Xi value for gaussian process HPS',
							action="store", dest='xi', default=-404)
	parser.add_argument('--random', help='Frequency of random selection in gaussian process search',
							action="store", dest='random', default=-404)
	parser.add_argument('--load', help='Load previous search from logfile before starting',
							action="store", dest='load', default=False)

	# Optional arguments for make features
	parser.add_argument('--input_files', help='Files to create features from',
							 action="store", dest='input_files', default='none')
	parser.add_argument('--output_files', help='Files to store features in',
							 action="store", dest='output_files', default='none')

	# Be very careful with this, having a different size between the training and
	# test sets screws up the predictions
	parser.add_argument('--max_size', help='Maximum molecule size',
							action="store", dest='max_size', default=-404)
	# Option to trace the code execution, for bug hunting
	parser.add_argument('--tracecode', help='Trace the code execution',
							action="store_true", dest='tracecode', default=False)
	# Option to trace memory usage, prints the biggest 10 memory blocks at the end of execution
	parser.add_argument('--tracemem', help='Trace the memory usage',
								action="store_true", dest='tracemem', default=False)
	# Option to trace code execution by time
	parser.add_argument('--tracetime', help='Trace the execution timings',
								action="store_true", dest='tracetime', default=False)


	return parser.parse_args(args)


def aE_parser(args):
	# Argparser
	parser = argparse.ArgumentParser(description='auto-ENRICH')
	# Define name of molecule (used for save/load of pickle file)
	parser.add_argument('Molecule', help='name of molecule')
	# Define command to perform
	parser.add_argument('Command', help='auto-ENRICH command', choices=['undo', 'init', 'conf_search', 'setup_opt', 'process_opt', 'setup_nmr', 'process_nmr', 'update', 'check_status'])
	# Optional arguments
	parser.add_argument('--xyz', help='xyz file to initialise molecule', action="store", dest='xyz_file', default='None')
	parser.add_argument('--path', help='path to molecule pickle file', action="store", dest='path', default='')
	parser.add_argument('--prefs', help='preferences file to use', action="store", dest='prefs', default='ENRICH.json')

	return parser.parse_args(args)

def util_parser(args):
	# Argparser
	parser = argparse.ArgumentParser(description='aE_utils')

	parser.add_argument('Command', help='aE_utils command',
							choices=['convert_to_nmredata', 'compare'])

	parser.add_argument('--files', help='Files to process',
							action="store", dest='files', default='')

	parser.add_argument('--type', help='File type',
							action="store", dest='type', default='g09')

	parser.add_argument('--out_dir', help='output directory',
							action="store", dest='out_dir', default='')

	parser.add_argument('--comp_targets', help='target parameters to compare',
							action="store", dest='comp_targets', default='HCS')

	parser.add_argument('--comp_sets', help='Datasets to compare',
							action="store", dest='comp_sets', default='')

	parser.add_argument('--comp_labels', help='Labels for datasets',
							action="store", dest="comp_labels", default='1 2')

	parser.add_argument('--match_criteria', help='Criteria by which to match molecules from different sets',
							action="store", dest="match_criteria", choices=['loose', 'strict', 'id'], default='id')

	return parser.parse_args(args)

def combine_args(user_args, file_args, wiz_args, default_args):
	args = {}
	for arg in user_args:
		user = False
		if type(user_args[arg]) is int:
			if user_args[arg] != -404:
				user = True
		elif type(user_args[arg]) is str:
			if user_args[arg] not in ['', 'none', '{}']:
				user = True
		elif type(user_args[arg]) is dict:
			if len(user_args[arg]) != 0:
				user = True
		elif type(user_args[arg]) is list:
			if len(user_args[arg]) != 0:
				user = True

		file = False
		if arg in file_args:
			if type(file_args[arg]) is int:
				if file_args[arg] != -404:
					file = True
			elif type(file_args[arg]) is str:
				if file_args[arg] not in ['', 'none', '{}']:
					file = True
			elif type(file_args[arg]) is dict:
				if len(file_args[arg]) != 0:
					file = True
			elif type(file_args[arg]) is list:
				if len(file_args[arg]) != 0:
					file = True


		if user:
			args[arg] = user_args[arg]
		elif file:
			args[arg] = file_args[arg]
		elif arg in wiz_args:
			args[arg] = wiz_args[arg]
		elif arg in default_args:
			args[arg] = default_args[arg]
		else:
			continue
	return args
