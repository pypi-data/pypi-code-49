#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import range
from builtins import bytes, str

import sys
import os
import configparser
import copy
import shutil
from Bio.PDB import *
import itertools
import multiprocessing
import subprocess
import time
import LibSLIDER
import SELSLIB2
import SystemUtility
import ALEPH
import alixe_library
import string
import random
import traceback
import math
import Grid
import Data

import logging

from io import StringIO
from optparse import OptionParser
from operator import itemgetter, attrgetter, methodcaller
from collections import defaultdict
from termcolor import colored
import numpy
from natsort import natsorted
import re

def startSLIDER(Config, input_bor):

	##INITIAL CONFIGURATIONS
	
	amino_acid_list=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','M']
	frequencyresbySS={}
	frequencyresbySS['ah']  ='D'*18+'E'*29+'R'*19+'K'*22+'H'*7+ 'L'*37+'M'*9+'I'*19+'V'*20+'F'*13+'W'*5+'Y'*12+'S'*16+'T'*15+'N'*12+'Q'*16+'C'*4+'G'*13+'A'*39+'P'*8
	frequencyresbySS['bs']  ='D'*6+ 'E'*10+'R'*9+ 'K'*10+'H'*5+ 'L'*21+'M'*5+'I'*21+'V'*28+'F'*12+'W'*4+'Y'*11+'S'*11+'T'*16+'N'*6+ 'Q'*6+ 'C'*4+'G'*11+'A'*14+'P'*4
	frequencyresbySS['coil']='D'*35+'E'*23+'R'*19+'K'*26+'H'*11+'L'*26+'M'*7+'I'*15+'V'*21+'F'*14+'W'*6+'Y'*14+'S'*33+'T'*28+'N'*29+'Q'*15+'C'*7+'G'*55+'A'*30+'P'*34
	frequencyresbySS['H']=frequencyresbySS['ah']
	frequencyresbySS['E']=frequencyresbySS['bs']
	frequencyresbySS['C']=frequencyresbySS['coil']
	buster_parametersRfactorRSCC='-M MapOnly UsePdbchk="no" -B None'
	listrefines=['1']
	RemHomIndependMode=False


	print('\n Reading the bor configuration file for SLIDER at ',input_bor)

	Config.readfp(StringIO(str(Data.defaults_bor)))
	Config.read(input_bor)

	###GENERAL INPUT
	current_directory = Config.get("GENERAL", "working_directory")
	if not os.path.isdir(current_directory):
		os.mkdir(current_directory)

	output_folder = os.path.join(current_directory, "SLIDER")
	if not os.path.isdir(output_folder):
		os.mkdir(output_folder)

	os.chdir(output_folder)

	if os.path.exists(os.path.join(output_folder,'temp_transfer')):
		shutil.rmtree(os.path.join(output_folder,'temp_transfer'))
	if os.path.exists(os.path.join(output_folder,'grid_jobs')):
		shutil.rmtree(os.path.join(output_folder,'grid_jobs'))
	if os.path.exists(os.path.join(output_folder,'temp')):
		shutil.rmtree(os.path.join(output_folder,'temp'))

	hkl = Config.get("GENERAL", "hkl_path")
	hkl = os.path.abspath(hkl)
	LibSLIDER.checkFile(hkl)

	mtz = Config.get("GENERAL", "mtz_path")
	mtz = os.path.abspath(mtz)
	LibSLIDER.checkFile(mtz)

	pdbcl = Config.get("GENERAL", "pdb_path")
	LibSLIDER.checkFile(pdbcl)

	HighRes=LibSLIDER.extract_resolution_from_mtz(mtz)[1]
	LibSLIDER.CheckHeaderPDB (pdbcl)

	try:
		ent = Config.get("GENERAL", "ent_path")
		if ent == "":
			raise Exception
		LibSLIDER.checkFile(ent)
		post_mortem=True
	except:
		ent = False
		post_mortem=False

	###ARCIMBOLDO INPUT
	Config2 = configparser.ConfigParser()
	Config2.read(input_bor)
	if Config2.has_section("ARCIMBOLDO"):
		string_arci = "ARCIMBOLDO"
	elif Config2.has_section("ARCIMBOLDO-BORGES"):
		string_arci = "ARCIMBOLDO-BORGES"
	elif Config2.has_section("ARCIMBOLDO-SHREDDER"):
		string_arci = "ARCIMBOLDO-SHREDDER"
	else:
		string_arci = "SLIDER"

	try:
		nameJob = Config.get(string_arci, "name_job")
		nameJob = "_".join(nameJob.split())
		if len(nameJob.strip()) == 0:
			print('\nKeyword name_job is empty, setting a default name for the job...')
			nameJob = (os.path.basename(mtz))[:-4] + '_slider'
	except:
		nameJob = (os.path.basename(mtz))[:-4] + '_slider'


	F = Config.get(string_arci, "f_label")
	SIGF = Config.get(string_arci, "sigf_label")

	try:
		coiled_coil = Config.getboolean(string_arci, "coiled_coil")
	except:
		coiled_coil = False

	try:
		MW = Config.get(string_arci, 'molecular_weight')
	except:
		print('molecular_weight variable not set, use protparam and sequence to obtain protein molecular weight, exiting.')
		sys.exit(1)

	try:
		NC = Config.get(string_arci, 'number_of_component')
	except:
		print("number_of_component variable not set, use Matthew's Coefficient to obtain most probable number of molecules per Asymmetric Unit, exiting.")
		sys.exit(1)

###SLIDER INPUT
	try:
		secstr_file = Config.get("SLIDER", "secstr_path")
		LibSLIDER.checkFile(secstr_file)
		sliding_by_ss = True
	except:
		secstr_file   = False
		sliding_by_ss = False

	try:
		seq_file = Config.get("SLIDER", "seq_path")
		LibSLIDER.checkFile(seq_file)
	except:
		seq_file = False

	try:
		align_file = Config.get("SLIDER", "align_path")
		LibSLIDER.checkFile(align_file)
		RemoteHomologous = True
	except:
		align_file = False
		RemoteHomologous = False

	try:    
		sspdb_file = Config.get("SLIDER", "sspdb_path")
		LibSLIDER.checkFile(sspdb_file)
	except: 
		sspdb_file = False

	if not RemoteHomologous and not sliding_by_ss:
		print('Either alignment (pir format) or secondary structure prediction file (PSIPRED) should be provided.')
		sys.exit(1)
	elif RemoteHomologous == True and sliding_by_ss == True:
		print('Choose one prior information only, either alignment (PIR format) or secondary structure prediction file (PSIPRED).')

	try:
		refmac_ins_file = Config.get("SLIDER", "refmac_parameters_path")
		LibSLIDER.checkFile(refmac_ins_file)
	except:
		refmac_ins_file = ''

	try:
		use_coot = Config.get("SLIDER", "use_coot")
		if use_coot.lower() == 'true' or int(use_coot) == 1:
			use_coot = True
		else:
			use_coot = False
	except:
		use_coot = False

	try:
		I_SLIDER = Config.get("SLIDER", 'i_label')
		SIGI_SLIDER = Config.get("SLIDER", 'sigi_label')
	except:
		I_SLIDER = False
		SIGI_SLIDER = False

	mtz_free = Config.get("SLIDER", 'rfree_label')

	try:
		pp_conf = Config.getint("SLIDER", "psipred_confidence_level")
	except:
		pp_conf = 0

	try:
		pp_frag_size = Config.getint("SLIDER", "psipred_min_frag_size")
	except:
		pp_frag_size = 4

	try:
		ss_method = Config.get("SLIDER", "ss_eval_pdb_method")
	except:
		ss_method = 'borgesmatrix'

	try:
		minimum_ss_frag = Config.getint("SLIDER", "minimum_ss_frag")
	except:
		minimum_ss_frag = 5

	try:
		sliding_tolerance = Config.getint("SLIDER", "sliding_tolerance")
	except:
		sliding_tolerance = 3

	try:
		models_by_chain = Config.getint("SLIDER", "models_by_chain")
		if models_by_chain > 3000:
			print('models_by_chain given exceeds limit, value setting to 1000.')
			models_by_chain = 3000
	except:
		models_by_chain = 100

	try:
		seq_pushed_refinement = Config.getint("SLIDER", "seq_pushed_refinement")
		if seq_pushed_refinement > 1000:
			print('seq_pushed_refinement given exceeds limit, value setting to 1000.')
			seq_pushed_refinement = 1000
	except:
		seq_pushed_refinement = models_by_chain

	try:
		Config.get("SLIDER", "chosen_chains_independent")
		print('Obsolete variable "chosen_chains_independent" was used in borfile, please use "chosen_chains" and separate by , dependent chains and ; independent chains.')
		exitt = True
	except:
		exitt = False

	if exitt == True: 
		sys.exit(1)

	try:
		Config.get("SLIDER", "chosen_chains_dependent")
		print('Obsolete variable "chosen_chains_dependent" was used in borfile, please use "chosen_chains" and separate by , dependent chains and ; independent chains.')
		exitt = True
	except:
		exitt = False

	if exitt == True:
		sys.exit(1)

	chosen_chains = []
	try:
		for i in Config.get("SLIDER", "chosen_chains").replace(' ', '').split(';'):
			chosen_chains.append(i.split(','))
	except:
		pass

	try:
		fixed_residues_modelled = Config.get("SLIDER", "fixed_residues_modelled")  # should be given as chain:residueN1-residueN2,residueN3-residueN4 such as: A:1-10,20-30 B:1-5,30-35
		# DicFixResMod={}
		DicFixResMod = defaultdict(list)
		FixRes2 = fixed_residues_modelled.split()
		for s in FixRes2:
			# DicFixRes[s[0]]=[]
			for ss in s[2:].split(','):
				resn1 = int(ss.split('-')[0])
				resn2 = int(ss.split('-')[1])
				for i in range(resn1, resn2 + 1):
					DicFixResMod[s[0]].append(i)
	except:
		DicFixResMod = defaultdict(list)

	try:
		fixed_residues_notmodelled = Config.get("SLIDER", "fixed_residues_notmodelled")  # should be given as chain:residueN1-residueN2,residueN3-residueN4 such as: A:1-10,20-30 B:1-5,30-35
		# DicFixResNotMod={}
		DicFixResNotMod = defaultdict(list)
		FixRes3 = fixed_residues_notmodelled.split()
		for s in FixRes3:
			# DicFixRes[s[0]]=[]
			for ss in s[2:].split(','):
				resn1 = int(ss.split('-')[0])
				resn2 = int(ss.split('-')[1])
				for i in range(resn1, resn2 + 1):
					DicFixResNotMod[s[0]].append(i)
	except:
		DicFixResNotMod = defaultdict(list)

	for ch in DicFixResMod:
		for i in DicFixResMod:
			if i in DicFixResNotMod[ch]:
				print('Chosen fixed_residues_modelled and fixed_residues_notmodelled cannot have overlap. They have same residue', i, 'in chain', ch, '.')
				sys.exit(1)

	try:
		ncschains = Config.get("SLIDER", "ncschains")
		if 'true' == ncschains.lower() or '1' == ncschains:
			ncschains = True
		else:
			ncschains = False
	except:                                                 
		ncschains = False

	# try:
	# 	merge_chosen_chains = Config.get("SLIDER", "merge_chosen_chains")
	# 	merge_chosen_chains = merge_chosen_chains.replace(' ', '').split(',')
	# except:
	# 	merge_chosen_chains = []
	# try:
	# 	models_by_merge_chain = Config.getint("SLIDER", 'models_by_merge_chain')
	# except:
	# 	models_by_merge_chain = int(models_by_chain)
	# models_by_merge_chain = int(math.sqrt(models_by_merge_chain))

	try:
		number_shelxe_trials = Config.getint("SLIDER", 'number_shelxe_trials')
	except:
		number_shelxe_trials = 15

	try:
		trust_loop = Config.get("SLIDER", "trust_loop")
		if trust_loop == '1' or trust_loop.lower() == 'true':
			trust_loop = True
		elif trust_loop == '-1' or trust_loop == '0' or trust_loop.lower() == 'false':
			trust_loop = False
	except:
		trust_loop = False

	try:
		ModelEdge = Config.get("SLIDER", "ModelEdge")
		if ModelEdge == '1' or ModelEdge.lower() == 'true':
			ModelEdge = True
		elif ModelEdge == '0' or ModelEdge.lower() == 'false':
			ModelEdge = False
		else:
			print('Invalid option given for ModelEdge', ModelEdge)
			sys.exit(1)
	except:
		ModelEdge = False

	try:
		buster_parameters = Config.get("SLIDER", "buster_parameters")
	except:
		buster_parameters = '-noWAT -nbig 10 -RB -nthread 1 UsePdbchk="no"'

	try:
		PhenixRefineParameters = Config.get("SLIDER", "PhenixRefineParameters")
	except:
		PhenixRefineParameters = False

	# try:
	# 	merge_FOM = Config.get("SLIDER", "merge_FOM")
	# except:
	# 	merge_FOM = 'refine1_LLG'

	try:
		LLG_testing = Config.get("SLIDER", "LLG_testing")
		if LLG_testing == '1' or LLG_testing.lower() == 'true':
			LLG_testing = True
		elif LLG_testing == '0' or LLG_testing.lower() == 'false':
			LLG_testing = False
	except:
		LLG_testing = False

	try:
		RandomModels = Config.getint("SLIDER", "RandomModels")
	except:
		RandomModels = 0
	if RandomModels != 0:
		if RandomModels > 1000:
			print('Random models given exceeds limit, value setting to 1000.')
			RandomModels = 1000
		try:
			RandomOnlyEvalSequence = Config.get("SLIDER", "RandomOnlyEvalSequence")
			if RandomOnlyEvalSequence == '1' or RandomOnlyEvalSequence.lower() == 'true':
				RandomOnlyEvalSequence = True
			else:
				RandomOnlyEvalSequence = False
		except:
			RandomOnlyEvalSequence = False
	else:
		RandomOnlyEvalSequence = None

	try:
		ReduceComplexity = Config.get("SLIDER", "ReduceComplexity").lower()
		if ReduceComplexity == '1' or ReduceComplexity == 'true': ReduceComplexity = True
	except:
		ReduceComplexity = False

	try:
		Recover0occup = Config.get("SLIDER", "Recover0occup")
		if Recover0occup == '1' or Recover0occup.lower() == 'true': 
			Recover0occup = True
	except:
		Recover0occup = False

	try:
		refinement_program = Config.get("SLIDER", "refinement_program")  # should be buster / phenix.refine / refmac
	except:
		print('refinement_program not given in bor file')
		sys.exit(1)

	try:
		expand_from_map = Config.get("SLIDER", "expand_from_map")
		if 'true' == expand_from_map.lower() or '1' == expand_from_map:
			expand_from_map = True
		else:
			expand_from_map = False
	except:
		if refinement_program == 'buster':
			expand_from_map = True
		else:
			expand_from_map = False

	if I_SLIDER == False:
		I_SLIDER = F
		SIGI_SLIDER = SIGF
		Amplitudes=True
	else:
		Amplitudes=False


	try:
		sprout_path = Config.get("LOCAL", "path_local_sprout")
		LibSLIDER.checkFile(sprout_path)
	except:
		if sys.platform == "darwin":
			sprout_path = os.path.join(os.path.dirname(__file__),"executables/sprout_mac")
		else:
			sprout_path = os.path.join(os.path.dirname(__file__),"executables/sprout_linux")
	try:
		edstats_path = Config.get("LOCAL", "path_local_edstats")
		LibSLIDER.checkFile(edstats_path)
	except:
		edstats_path = False


	distribute_computing = Config.get("CONNECTION", "distribute_computing")

	if refinement_program == 'buster':
		try:
			buster_path = Config.get("LOCAL", "path_local_buster")
			LibSLIDER.checkFile(buster_path)
			listrefines.append('2')
			refmac_path = False
			phenixrefine_path = False
		except:
			print('buster path not given in bor file')
			sys.exit(1)

		try:
			ccp4_config_path = Config.get("LOCAL", "path_config_ccp4")
		except:
			if not distribute_computing=='multiprocessing':
				print('CCP4 configuration path not given in bor file. Required by buster')
				sys.exit(1)
			pass
			
		try:
			buster_config_path = Config.get("LOCAL", "path_config_buster")
		except:
			buster_config_path = buster_path.replace("/autoBUSTER/bin/linux64/refine", "/setup.sh")

	elif refinement_program == 'phenix.refine':
		try:
			phenixrefine_path = Config.get("LOCAL", "path_local_phenix.refine")
			LibSLIDER.checkFile(phenixrefine_path)
			refmac_path = False
			buster_path = False
		except:
			print('phenix.refine path not given in bor file')
			sys.exit(1)
		try:
			phenixrefine_config_path = Config.get("LOCAL", "path_config_phenix")
		except:
			phenixrefine_config_path = phenixrefine_path.replace("/build/bin/phenix.refine", "/phenix_env.sh")

	elif refinement_program == 'refmac':
		try:
			refmac_path = Config.get("LOCAL", "path_local_refmac")
			LibSLIDER.checkFile(refmac_path)
			phenixrefine_path = False
			buster_path = False
		except:
			print('refmac path not given in bor file')
			sys.exit(1)
		try:
			ccp4_config_path = Config.get("LOCAL", "path_config_ccp4")
		except:
			ccp4_config_path = refmac_path.replace("bin/refmac5", "include/ccp4.setup-sh.in")

	else:
		print('refinement_program should be either buster / phenix.refine / refmac.')
		sys.exit(1)

	if use_coot == True:
		coot_path = Config.get("LOCAL", "path_local_coot")
		LibSLIDER.checkFile(coot_path)
	else:
		coot_path = False

	DicGridConn={}
	DicParameters={}

	DicParameters["nameExecution"] = nameJob

	if distribute_computing in ["multiprocessing","supercomputer"]:
		shelxe_path = Config.get("LOCAL", "path_local_shelxe")
		phaser_path = Config.get("LOCAL", "path_local_phaser")
		SELSLIB2.PATH_NEW_PHASER = phaser_path
		SELSLIB2.PATH_NEW_SHELXE = shelxe_path
	
	if distribute_computing == "remote_grid":
			path_bor = Config.get("CONNECTION", "setup_bor_path")
			if path_bor is None or path_bor == "" or not os.path.exists(path_bor):
				print(colored("ATTENTION: the path given for the setup.bor does not exist.\n Please contact your administrator","red"))
				sys.exit(1)
			try:
				setupbor = configparser.ConfigParser()
				setupbor.readfp(open(path_bor))
				DicGridConn["username"] = setupbor.get("GRID", "remote_frontend_username")
				DicGridConn["host"] = setupbor.get("GRID", "remote_frontend_host")
				DicGridConn["port"] = setupbor.getint("GRID", "remote_frontend_port")
				DicGridConn["passkey"] = Config.get("CONNECTION", "remote_frontend_passkey")
				DicGridConn["promptA"] = (setupbor.get("GRID", "remote_frontend_prompt")).strip()+" "
				DicGridConn["isnfs"] = setupbor.getboolean("GRID", "remote_fylesystem_isnfs")
				try:
					DicGridConn["remote_submitter_username"] = setupbor.get("GRID", "remote_submitter_username")
					DicGridConn["remote_submitter_host"] = setupbor.get("GRID", "remote_submitter_host")
					DicGridConn["remote_submitter_port"] = setupbor.getint("GRID", "remote_submitter_port")
					DicGridConn["promptB"] = (setupbor.get("GRID", "remote_submitter_prompt")).strip()+" "
				except:
					pass
				DicGridConn["home_frontend_directory"] = setupbor.get("GRID", "home_frontend_directory")
			except:
				print(colored("ATTENTION: Some keyword in your configuration files are missing. Contact your administrator","red"))
				print("Path bor given: ",path_bor)
				print(traceback.print_exc(file=sys.stdout))
				sys.exit(1)

	setupbor = None
	if distribute_computing == "remote_grid":
		path_bor = Config.get("CONNECTION", "setup_bor_path")
		if path_bor is None or path_bor == "" or not os.path.exists(path_bor):
			print(colored( "ATTENTION: the path given for the setup.bor does not exist.\n Please contact your administrator", "red"))
			sys.exit(1)
		try:
			setupbor = configparser.ConfigParser()
			setupbor.readfp(open(path_bor))
			DicGridConn["username"] = setupbor.get("GRID", "remote_frontend_username")
			DicGridConn["host"] = setupbor.get("GRID", "remote_frontend_host")
			DicGridConn["port"] = setupbor.getint("GRID", "remote_frontend_port")
			DicGridConn["passkey"] = Config.get("CONNECTION", "remote_frontend_passkey")
			DicGridConn["promptA"] = (setupbor.get("GRID", "remote_frontend_prompt")).strip() + " "
			DicGridConn["isnfs"] = setupbor.getboolean("GRID", "remote_fylesystem_isnfs")
			try:
				DicGridConn["remote_submitter_username"] = setupbor.get("GRID", "remote_submitter_username")
				DicGridConn["remote_submitter_host"] = setupbor.get("GRID", "remote_submitter_host")
				DicGridConn["remote_submitter_port"] = setupbor.getint("GRID", "remote_submitter_port")
				DicGridConn["promptB"] = (setupbor.get("GRID", "remote_submitter_prompt")).strip() + " "
			except:
				pass
			DicGridConn["home_frontend_directory"] = setupbor.get("GRID", "home_frontend_directory")
			SELSLIB2.PATH_NEW_PHASER = setupbor.get("GRID", "path_remote_phaser")
			SELSLIB2.PATH_NEW_SHELXE = setupbor.get("GRID", "path_remote_shelxe")
			shelxe_path = Config.get("LOCAL", "path_local_shelxe")
			phaser_path = Config.get("LOCAL", "path_local_phaser")
			SELSLIB2.GRID_TYPE_R = setupbor.get("GRID", "type_remote")
			if SELSLIB2.GRID_TYPE_R == "Condor":
				SELSLIB2.SHELXE_REQUIREMENTS = setupbor.get("CONDOR", "requirements_shelxe")
				SELSLIB2.PHASER_REQUIREMENTS = setupbor.get("CONDOR", "requirements_phaser")
				SELSLIB2.BORGES_REQUIREMENTS = setupbor.get("CONDOR", "requirements_borges")
			SELSLIB2.LOCAL = False
		except:
			print(colored("ATTENTION: Some keywords in the configuration file are missing. Contact your administrator",
						  "red"))
			print("Path bor given: ", path_bor)
			print(traceback.print_exc(file=sys.stdout))
			sys.exit(1)
	elif distribute_computing == "local_grid":
		path_bor = Config.get("CONNECTION", "setup_bor_path")
		if path_bor is None or path_bor == "" or not os.path.exists(path_bor):
			print(colored(
				"ATTENTION: the path given for the setup.bor does not exist.\n Please contact your administrator",
				"red"))
			sys.exit(1)
		try:
			setupbor = configparser.ConfigParser()
			setupbor.readfp(open(path_bor))
			SELSLIB2.PATH_NEW_PHASER = setupbor.get("LOCAL", "path_local_phaser")
			SELSLIB2.PATH_NEW_SHELXE = setupbor.get("LOCAL", "path_local_shelxe")
			shelxe_path = Config.get("LOCAL", "path_local_shelxe")
			phaser_path = Config.get("LOCAL", "path_local_phaser")
			SELSLIB2.GRID_TYPE_L = setupbor.get("GRID", "type_local")
			if SELSLIB2.GRID_TYPE_L == "Condor":
				SELSLIB2.SHELXE_REQUIREMENTS = setupbor.get("CONDOR", "requirements_shelxe")
				SELSLIB2.PHASER_REQUIREMENTS = setupbor.get("CONDOR", "requirements_phaser")
				SELSLIB2.BORGES_REQUIREMENTS = setupbor.get("CONDOR", "requirements_borges")
		except:
			print(colored("ATTENTION: Some keyword in your configuration files are missing. Contact your administrator",
						  "red"))
			print("Path bor given: ", path_bor)
			print(traceback.print_exc(file=sys.stdout))
			sys.exit(1)

	if distribute_computing == "supercomputer":
		# TODO: Read the list of available nodes
		path_nodes = Config.get("CONNECTION", "nodefile_path")
		if path_nodes is None or path_nodes == "" or not os.path.exists(path_nodes):
			print(colored(
				"ATTENTION: the path given for the node file does not exist.\n Please contact your administrator",
				"red"))
			sys.exit(1)
		f = open(path_nodes, "r")
		nodes_list = f.readlines()
		f.close()
		for i in range(len(nodes_list)):
			nodes_list[i] = nodes_list[i][:-1] + "***" + str(i)
		SystemUtility.NODES = nodes_list

	 #STARTING THE GRID MANAGER
	cm = None
	GRID_TYPE = ""
	if distribute_computing == "remote_grid":
		GRID_TYPE = setupbor.get("GRID","type_remote")
	elif distribute_computing == "local_grid":
		path_bor = Config.get("CONNECTION", "setup_bor_path")
		if path_bor is None or path_bor == "" or not os.path.exists(path_bor):
			print(colored("ATTENTION: the path given for the setup.bor does not exist.\n Please contact your administrator","red"))
			sys.exit(1)
		setupbor = configparser.ConfigParser()
		setupbor.readfp(open(path_bor))
		GRID_TYPE = setupbor.get("GRID","type_local")

	if cm == None:
		if GRID_TYPE == "Condor":
			cm = Grid.condorManager( should_transfer_files='TRUE' )
		elif GRID_TYPE == "SGE":
			QNAME = setupbor.get("SGE","qname")
			FRACTION = setupbor.getfloat("SGE","fraction")
			cm = Grid.SGEManager(qname=QNAME,fraction=FRACTION)
		elif GRID_TYPE == "MOAB":
			PARTITION = setupbor.get("MOAB","partition")
			#FRACTION = setupbor.getfloat("MOAB","partition")
			cm = Grid.MOABManager(partition=PARTITION)
		elif GRID_TYPE == "SLURM":
			PARTITION = setupbor.get("SLURM","partition")
			if PARTITION != None and PARTITION != '':
				cm = Grid.SLURMManager(partition=PARTITION)
			else:
				cm = Grid.SLURMManager()
		elif GRID_TYPE == "TORQUE":
			QNAME = setupbor.get("TORQUE","qname")
			FRACTION = setupbor.getint("TORQUE","cores_per_node")
			PARALLEL_JOBS = setupbor.getint("TORQUE","number_of_parallel_jobs")
			MAUI = setupbor.getboolean("TORQUE","maui")
			cm = Grid.TORQUEManager(qname=QNAME,cores_per_node=FRACTION,parallel_jobs=PARALLEL_JOBS,maui=MAUI)

	if cm is not None:
		cm.setRank("kflops")
		cm.nice_user = "true"
		#TODO: Eliminate the SGE.py
		PATH_REMOTE_SGEPY = setupbor.get("GRID", "path_remote_sgepy")
		PATH_REMOTE_PYTHON_INTERPRETER = setupbor.get("GRID", "python_remote_interpreter")
		PATH_LOCAL_PYTHON_INTERPRETER = setupbor.get("LOCAL", "python_local_interpreter")

		if PATH_REMOTE_PYTHON_INTERPRETER.strip() in ["", None]:
			PATH_REMOTE_PYTHON_INTERPRETER = "/usr/bin/python"

		if PATH_LOCAL_PYTHON_INTERPRETER.strip() in ["", None]:
			PATH_LOCAL_PYTHON_INTERPRETER = "/usr/bin/python"


	if len(chosen_chains)==0:
		protein_chain_list = LibSLIDER.return_chainlist_seqlist_numbres(pdbcl)
		chosen_chains=protein_chain_list[0]

	formfactors = 'FORMFACTORS XRAY'

	######################
	###PROGRAM STARTS HERE
	######################
	print('\nStarting slider\n')

	sym = SystemUtility.SystemUtility()

	try:
		nproc = [ Config.getint("SLIDER", "nproc") ]
	except:
		if 'grid' in distribute_computing:
			nproc = [1, 20000]
		else:
			nproc=[ sym.REALPROCESSES+1 ]


	shelxe_line_initial = '-a0 -m1 -s0.5'
	if not ent:
		entt = ''
	else:
		entt = ent
		shelxe_line_initial += ' -x'
	Aniso = True
	# if Amplitudes: Intensities=False
	# else:          Intensities=True

	anismtz,normfactors,tncsfactors,trashF,trashSIGF,spaceGroup,cell_dim,resolution,unique_refl,aniout,anierr,\
	fneed, shelxe_new, tNCS_bool = SELSLIB2.anisotropyCorrection_and_test(cm=cm, sym=sym, DicGridConn=DicGridConn,
			DicParameters=DicParameters, current_dir=output_folder, mtz=mtz, F=I_SLIDER, SIGF=SIGI_SLIDER, Intensities=not Amplitudes, Aniso=Aniso,
			formfactors=formfactors, nice=-20, pda=pdbcl, hkl=hkl, ent=entt, shelxe_line=shelxe_line_initial, tncsVector=[0, 0, 0])
	
	SpaceGroup=spaceGroup
	HighRes=resolution


	try:
		shelxe_line = Config.get(string_arci, 'shelxe_line')
	except:
		if resolution <= 1.0:
			shelxe_line = "-m200 -a8 -s0.25 -v0.5 -t10 -q -y" + str('%.2f' % (resolution))
			if shelxe_new and coiled_coil:
				shelxe_line = "-m200 -a8 -s0.25 -v0.5 -t10 -Q -I200 -y" + str('%.2f' % (resolution)) + " -e1.0"
		elif resolution <= 1.3:  # and resolution > 1.0:
			shelxe_line = "-m100 -a8 -s0.35 -v0.25 -t10 -q -y" + str('%.2f' % (resolution))
			if shelxe_new and coiled_coil:
				shelxe_line = "-m100 -a8 -s0.35 -v0.5 -t10 -Q -I100 -y" + str('%.2f' % (resolution)) + " -e1.0"
		elif resolution <= 1.5:  # and resolution > 1.3:
			shelxe_line = "-m50 -a8 -s0.45 -v0.1 -t10 -q -y" + str('%.2f' % (resolution))
			if shelxe_new and coiled_coil:
				shelxe_line = "-m50 -a8 -s0.45 -v0.1 -t10 -Q -I50 -y" + str('%.2f' % (resolution)) + " -e" + \
						str('%.2f' % (resolution-0.3))
		elif resolution <= 2.0:  # and resolution > 1.5:
			shelxe_line = "-m15 -a8 -s0.5 -v0 -t10 -q -y" + str('%.2f' % (resolution))
			if shelxe_new and coiled_coil:
				shelxe_line = "-m15 -a8 -s0.5 -v0 -t10 -Q -I15 -y" + str('%.2f' % (resolution)) + " -e" + \
						str('%.2f' % (resolution-0.3))
		else:  # resolution > 2.0:
			shelxe_line = "-m10 -a8 -s0.6 -v0 -t10 -q -y" + str('%.2f' % (resolution))

			if shelxe_new and coiled_coil and resolution <= 2.5:
				shelxe_line = "-m10 -a8 -s0.6 -v0 -t10 -Q -I10 -y" + str('%.2f' % (resolution)) + " -e" + \
						str('%.2f' % (resolution - 0.3))
			elif shelxe_new and coiled_coil and resolution <= 3.0:
				shelxe_line = "-m5 -a8 -s0.6 -v0 -t10 -Q -I5 -y" + str('%.2f' % (resolution)) + " -e" + \
						str('%.2f' % (resolution - 0.3))
		if fneed:
			shelxe_line += " -f"
			
	if ent != False and '-x' not in shelxe_line: 
		shelxe_line+=' -x'

	spacegroup_aux = alixe_library.get_space_group_number_from_symbol(SpaceGroup)
	if expand_from_map:
		shelxe_ins_path=os.path.join(output_folder, 'symmetry.ins')
		alixe_library.generate_fake_ins_for_shelxe(shelxe_ins_path , [float(cell) for cell in cell_dim] , spacegroup_aux)


	# script_file = os.path.join(output_folder, 'anis_tNCS_correction.sh')
	# log_file = os.path.join(output_folder, 'anis_tNCS_correction.log')
	# if not os.path.isfile( script_file ):
	# 	LibSLIDER.phaser_Ani_tNCS_correction (input_mtz=mtz,F=I_SLIDER,SigF=SIGI_SLIDER,Amplitudes=Amplitudes,sh_file=script_file,log_file=log_file, output_folder=output_folder)
	# filevar=open(log_file)
	# filevar2=filevar.read()
	# filevar.close()
	# SpaceGroup=SELSLIB2.readSpaceGroupFromOut(filevar2)

	###########################################################

	if refmac_ins_file == '' and 'refmac' in refinement_program:
		refmac_ins_file=output_folder+'/refmacTMP.tmp'
		LibSLIDER.write_refmac_TMP_default_file ( refmac_ins_file , '100' , '' , mtz_f=F , mtz_sf=SIGF , mtz_free=mtz_free )

	output_pdb_name = os.path.join(output_folder, os.path.basename(pdbcl))[:-4]
	#Removing possible incomplete residues (edges) from shelxe_trace
	correction=LibSLIDER.remove_partial_res_from_PDB_BioPython ( pdbcl, output_pdb_name+'_corrected.pdb' )
	if correction: 
		pdbcl=output_pdb_name+'_corrected.pdb'
	LibSLIDER.add_Bfactors_occup_to_pdb ( pdb_input_file=pdbcl , pdb_output_file=output_pdb_name+'_corrected.pdb' , Bf_number_in_string_6characters=' 20.00' , occ_number_in_string_3characters='1.00')
	pdbcl=output_pdb_name+'_corrected.pdb'

	#Post Mortem sequence reference
	if post_mortem:
		list_CA_trace_related_ent,i1,i2=LibSLIDER.given_2_superposed_pdbs_return_list_res_match    (pdbcl,ent,1.0)
		true_seq_string                =LibSLIDER.GivenListMatchCA2PDBsReturnCorrespondentResString(list_CA_trace_related_ent)
		true_seq_dic_string            =LibSLIDER.GivenListListMatchCA2PDBsReturnDicSequenceByChain(list_CA_trace_related_ent)
		TrueSeqDicChResNResT           =LibSLIDER.GivenListListMatchCA2PDBsReturnDicChResNResT     (list_CA_trace_related_ent)
		TrueSeqDicChResNRangeSeq       =LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(TrueSeqDicChResNResT)


	protein_chain_list,protein_seq_list,count_zzz,DicChResNResType,listChResNCA=LibSLIDER.extract_protein_chainID_res_number (pdbcl)
	DicChResNRangeSeq=LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(DicChResNResType)
	protein_seq_list = LibSLIDER.return_restype_list(pdbcl)
	listChResNRangeCA=LibSLIDER.GivenPDBlistChResNCAReturnlistChResNRangeCA (listChResNCA)


	# Generate dictionary for Initial model
	if not os.path.isdir(os.path.join(output_folder, 'initial')):
		os.mkdir(os.path.join(output_folder, 'initial'))

	DicRefInitial = {}
	DicRefInitial['PATH'] = output_folder + '/initial'
	DicRefInitial['file']='initial'
	DicRefInitial['HypSeq']=DicRefInitial['file']
	DicRefInitial['seq'] = ''.join(protein_seq_list).lower()
	DicRefInitial['EvalChResn']=''
	DicRefInitial['assigned_res_int']=0
	DicRefInitial['energy']='n/a'
	if post_mortem:
		DicChImpartialRes = LibSLIDER.return_impartial_res(pdbcl)
		seqvar = DicRefInitial['seq']
		ident = 0
		for i, l in enumerate(list_CA_trace_related_ent):  # list_CA_trace_related_ent[0]=[('A', 3, 'T', <Atom CA>), ('A', 3, 'K', <Atom CA>), 1.2654423]
			if len(l) > 1:
				AAtrue = l[1][2]
				AAVar = seqvar[i]
				ChModel = l[0][0]
				ResnModel = l[0][1]
				# print i
				if AAtrue == AAVar or (AAtrue.lower() == AAVar and ResnModel not in DicChImpartialRes[ChModel]): ident += 1
		DicRefInitial['#IdRes'] = ident

	DicRefInitial['initial_pdbfile'] = pdbcl
	filevarr=pdbcl[pdbcl.rindex('/'):]
	if Recover0occup == True: filevarr=filevarr.replace('Bf20','Bf20_0occ')
	if   refinement_program == 'refmac': DicRefInitial['refine_file1'] = DicRefInitial['PATH'] + filevarr[:-4] + '_refmac.pdb'
	if   refinement_program == 'phenix.refine': DicRefInitial['refine_file1'] = DicRefInitial['PATH'] + filevarr[:-4] + '_phenixrefine.pdb'
	elif refinement_program == 'buster':
		DicRefInitial['refine_file1'] = DicRefInitial['PATH'] + filevarr[:-4] + '_BUSTER.pdb'
		DicRefInitial['refine_file2'] = DicRefInitial['PATH'] + filevarr[:-4] + '_BUSTER2.pdb'
		#DicRefInitial['refine_file2_map_lst'] = DicRefInitial['refine_file2'][:-4] + '_map.lst'
		DicRefInitial['refine_file2_map_lst'] = DicRefInitial['PATH'] + '/initial-ref2_map.lst'
		if edstats_path!=False: DicRefInitial['edstats_file2'] = DicRefInitial['refine_file2'][:-4] + '_rss2.out'
	if expand_from_map: DicRefInitial['refine_file1_map_lst'] = DicRefInitial['PATH'] + '/initial-ref1_map.lst'
	if edstats_path!=False: DicRefInitial['edstats_file1'] = DicRefInitial['refine_file1'][:-4] + '_rss.out'
	#if refinement_program=='phenix.refine': DicRefInitial['phenixRSCC_file1']=DicRefInitial['refine_file1'][:-4] + '_ref1_phenixRSCC.log'
	if use_coot: DicRefInitial['coot_file'] = DicRefInitial['refine_file1'][:-4] + '_coot.pdb'
	#DicRefInitial['refine_file1_lst']     = DicRefInitial['refine_file1'][:-4] + '_pda.lst'
	DicRefInitial['refine_file1_lst']     = DicRefInitial['PATH'] + '/initial-ref1_pda.lst'


	##############SECONDARY STRUCTURE EVALUATION BY PHENIX PROGRAMS AND ALEPH

	print('According to secondary structure evaluations on pdb:', pdbcl)

	pdbborgesmatrix = ALEPH.annotate_pdb_model_with_aleph(pdb_model=pdbcl, write_pdb=False, strictness_ah=0.5, strictness_bs=0.30, peptide_length=3)[0] #, min_diff_ah=0.5, min_diff_bs=0.4,peptide_length=3)[0]

	pdbborgesmatrix = ALEPH.get_all_fragments(pdbborgesmatrix)
	listSSpdb = LibSLIDER.convertALEPHfrags2listSSpdb(pdbcl, pdbborgesmatrix)
	#[('A', 5, 'L', 'coil'), ('A', 6, 'I', 'coil'), ('A', 7, 'L', 'bs'), ('A', 8, 'G', 'bs'), ('A', 9, 'D', 'bs'), ('A', 21, 'G', 'ah'), ('A', 22, 'W', 'ah'), ('A', 23, 'V', 'ah')]
	# print listSSpdb
	# exit()

	pdb_dic_seq_ss = {}
	DicChResnSecStr={}
	SSpdbSEQ = ''
	for tpaa in listSSpdb:
		ch = tpaa[0]
		resn=tpaa[1]
		if tpaa[-1] == 'ah':   ss = 'H'
		elif tpaa[-1] == 'bs': ss = 'E'
		else:                  ss = 'C'
		if ch not in pdb_dic_seq_ss:   pdb_dic_seq_ss[ch] = ss
		else:                          pdb_dic_seq_ss[ch] += ss
		if ch not in DicChResnSecStr:  DicChResnSecStr[ch] = {}
		DicChResnSecStr[ch][resn]=ss
		SSpdbSEQ += ss

	DicChResnRangeSecStr = LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(DicChResnSecStr)

	if sliding_by_ss:
		DicChResnRangeSeqbySecStr = LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(DicChResNResType,DicChResnSecStr)
		DicChResnRangeSecStrbySecStr = LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(DicChResnSecStr, DicChResnSecStr)
		# print DicChResnRangeSeqbySecStr
		if post_mortem: TrueSeqDicChResNRangeSeqbySecStr = LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(TrueSeqDicChResNResT, DicChResnSecStr)


	##############DESCRIPTION OF MODEL TO BE SHOWN IN SCREEN


	logger = logging.getLogger()

	if os.path.exists('SLIDER.log'):
		os.remove('SLIDER.log')

	ch = logging.StreamHandler()
	ch.setLevel(logging.INFO) # or any other level
	logger.addHandler(ch)	

	fh = logging.FileHandler('SLIDER.log')
	fh.setLevel(logging.INFO)
	logger.addHandler(fh)

	logger.info('\n\n\nFollowing to ALEPH Secondary Structure assignment, model has:\n')

	for ch in sorted(DicChResNRangeSeq):
		DicResNRangeSeq = DicChResNRangeSeq[ch]
		logger.info('CHAIN ' + ch + ' HAS IN CONTINUOUS RESIDUES:')
		for ResNRange in natsorted(DicResNRangeSeq):
			logger.info('\tInitialModel\t' + ResNRange + '\t' + DicResNRangeSeq[ResNRange])
			if post_mortem:
				logger.info('\tTrueSequence\t' + len(ResNRange)*' ' + '\t' + TrueSeqDicChResNRangeSeq[ch][ResNRange])
			logger.info('\tSecStructPDB\t' + len(ResNRange)*' ' + '\t' + DicChResnRangeSecStr[ch][ResNRange])
			logger.info('\n')


	if sspdb_file != False:
		logger.info('User gave its owns SECONDARY STRUCTURE assignment through file '+sspdb_file)
		ChainChangeSS=[]
		with open(sspdb_file) as f:
			f2 = f.readlines()
			for l in f2:
				if len(l)>1 and l.split()[-1]!=pdb_dic_seq_ss[l[0]]:
					pdb_dic_seq_ss[l[0]] = l.split()[-1]
					ChainChangeSS.append(l[0])
				else: 
					logger.info('Given SECONDARY STRUCTURE of chain '+l.split()[0]+' '+l.split()[-1]+' is identical to assigned by ALEPH.')
		#print pdb_dic_seq_ss
		iCh=listChResNCA[0]
		count=0
		for chvar in ChainChangeSS:
			for Ch,ResN in listChResNCA:
				if chvar==Ch:
					if Ch!=iCh: count=0
					DicChResnSecStr[Ch][ResN]=pdb_dic_seq_ss[Ch][count]
					count+=1
					iCh=Ch

		DicChResnRangeSecStr = LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(DicChResnSecStr)
		DicChResnRangeSecStrbySecStr = LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(DicChResnSecStr, DicChResnSecStr)
		DicChResnRangeSeqbySecStr = LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(DicChResNResType, DicChResnSecStr)
		if post_mortem: TrueSeqDicChResNRangeSeqbySecStr = LibSLIDER.GivenDicChResNResTReturnDicChResNRangeSeq(TrueSeqDicChResNResT, DicChResnSecStr)

		##############DESCRIPTION OF MODEL TO BE SHOWN IN SCREEN
		logger.info(ChainChangeSS)
		if len(ChainChangeSS)==1: 
			logger.info('Chains '+ChainChangeSS[0]+' had its SECONDARY STRUCTURE changed to:\n')
		else:
			logger.info('Chains '+' '.join(ChainChangeSS)+' had their SECONDARY STRUCTURE changed to:\n')
		for ch in sorted(ChainChangeSS):
			DicResNRangeSeq = DicChResNRangeSeq[ch]
			logger.info('CHAIN '+ch+' HAS IN CONTINUOUS RESIDUES:')
			for ResNRange in natsorted(DicResNRangeSeq):
				logger.info('\tInitialModel\t' + ResNRange + '\t' + DicResNRangeSeq[ResNRange])
				if post_mortem:
					logger.info('\tTrueSequence\t' + len(ResNRange)*' ' + '\t' + TrueSeqDicChResNRangeSeq[ch][ResNRange])
				logger.info('\tSecStructPDB\t' + len(ResNRange)*' ' + '\t' + DicChResnRangeSecStr[ch][ResNRange])
				logger.info('\n')

	if sliding_by_ss:
		listChResNRangeBySecStrCA=[]
		for ch,resn in listChResNCA:
			for Ch in DicChResnRangeSeqbySecStr:
				for ResNRange in DicChResnRangeSeqbySecStr[Ch]:
					if Ch==ch and resn==int(ResNRange.split('-')[0]): listChResNRangeBySecStrCA.append([Ch,ResNRange])
		listChResNRangeCA=listChResNRangeBySecStrCA
		if post_mortem: TrueSeqDicChResNRangeSeq = TrueSeqDicChResNRangeSeqbySecStr
		DicChResnRangeSecStr=DicChResnRangeSecStrbySecStr
		# print listChResNRangeBySecStrCA


	#Check if NCS chains are identical
	if ncschains:
		# for lch in chosen_chains:
		# it may require correction
		for lch in chosen_chains:
			if len(lch) > 1:
				for i, ch in enumerate(lch):
					for ch2 in lch[i + 1:]:
						if (DicChResnSecStr[ch] != DicChResnSecStr[ch2] and sliding_by_ss) or (len(DicChResnSecStr[ch]) != len(DicChResnSecStr[ch2]) and RemoteHomologous):
							logger.info('NCS mode chosen for chains: '+lch)
							logger.info('Chain '+ch+' has SecStr '+DicChResnSecStr[ch])
							logger.info('Chain '+ch2+' has SecStr '+DicChResnSecStr[ch2])
							logger.info('Their SecStr are different and should be corrected in the PDB to be identical coordinates or at least give same SecStr from ALEPH.')
							sys.exit(1)
	#                    else: print 'All selected and NCS-related chains have same SS assignement given by ALEPH'



	#SECONDARY STRUCTURE MODE reading sequence from PSIPRED prediction
	if sliding_by_ss:
		dic_secstr_pred_psipred = LibSLIDER.read_secstr_pred_psipred(secstr_file)
		seq_string = dic_secstr_pred_psipred['sequence']

	#Evaluating SEQUENCE file
	if seq_file!=False:
		with open(seq_file) as f: seq_string = f.read().strip()

	#TARGET SEQUENCE
	logger.info('\n TARGET SEQUENCE HAS '+str(len(seq_string))+' RESIDUES:')
	logger.info(seq_string)
	logger.info('\n\n')

	# # Evaluating sequence from PDB file separated by chain
	# for ch in DicChResNResType:
	#     seqvar=''
	#     for resn in sorted(DicChResNResType[ch]): seqvar+=DicChResNResType[ch][resn]
	#     print 'CHAIN',ch,'IN MODEL HAS', str(len(seqvar)), 'RESIDUES:'
	#     print seqvar
	#     print '\n'
	#
	# exit()


	###### SECTION TO OBTAIN REFERENCES OF INFORMATION FROM SEQUENCE (ALIGNMENT OR SS PREDICTION)

	if RemoteHomologous:
		#Obtaining ALIGNMENT file
		#LibSLIDER.AlignTwoSequences (seq1=seq_string,seq2=seqq)
		# LibSLIDER.AlignTwoSequences(seq1=seq_string, seq2='MDNTILILGDALSAAYGLQQEEGWVKLLQDKYDAEQSDIVLINASISGETSGGALRRLDALLEQYEPTHVLIELGANDGLRGFPVKKMQTNLTALVKKSQAANAMTALMEIYIPPNYGPRYSKMFTSSFTQISEDTNAHLMNFFMLDIAGKSDLMQNDSLHPNKKAQPLIRDEMYDSIKKWLNNV')
		dicalign=LibSLIDER.readPIRalignment (align_file)
		if len(dicalign)!=2:
			for vId, vSeq in dicalign.items():
				logger.info(vId, vSeq)
			logger.info('Alignment file contains number of sequences different than 2, please change file to restrict sequences to target and remote homologous sequence only.')
			sys.exit(1)
		#getting overall alignment given by user  TARGET sequence / remote homologous
		for vId,vSeq in dicalign.items():
			vSeq=str(vSeq)
			if vSeq.replace('-','') in seq_string or seq_string in vSeq.replace('-',''):
				targetSeqalign=vSeq
				logger.info('Target SEQ: '+targetSeqalign+' '+vId)
			else:
				remotehSeqAlign=vSeq
				logger.info('RemHom SEQ: '+remotehSeqAlign+' '+vId)

		if '-' in remotehSeqAlign:
			logger.info('\nGaps found in RemHom SEQ in respect to Target SEQ, therefore - being removed.\n')
			seq1=''
			seq2=''
			for i,s in enumerate(remotehSeqAlign):
				if s!='-':
					seq1+=remotehSeqAlign[i]
					seq2+=targetSeqalign[i]
			remotehSeqAlign=seq1
			targetSeqalign =seq2
			logger.info('Target SEQ: '+ targetSeqalign)
			logger.info('RemHom SEQ: '+ remotehSeqAlign)

		logger.info('\n\n')

	else:
		logger.info('\n\nThe given sequence has the following secondary structure based on psipred prediction:\n')

		logger.info('sequence   is '+ dic_secstr_pred_psipred['sequence'])
		logger.info('secstr_prd is '+ dic_secstr_pred_psipred['sec_str_pred'])
		logger.info('confidence is '+ dic_secstr_pred_psipred['confidence'])
		logger.info('\n\n')

		list_dics_sspred_conf = LibSLIDER.from_secstr_pred_psipred_generate_trusted_fragments(dic_secstr_pred_psipred,pp_conf, pp_frag_size,trust_loop)
		for i in range(len(list_dics_sspred_conf)):
			logger.info('Fragment '+ str(i+1) +' of '+str(list_dics_sspred_conf[i]['sec_str_pred'][0])+' with length '+str(len(list_dics_sspred_conf[i]['sequence'])))
			logger.info(str(list_dics_sspred_conf[i]['initial_res'])+' '+str(list_dics_sspred_conf[i]['sequence'])+' '+str(list_dics_sspred_conf[i]['final_res'])+'\n')
		# LibSLIDER.print_list_dics_sspred_conf_in_nice_way(list_dics_sspred_conf)


	###### Section to calculate LLG contribution by SecStr Fragment in trace

	if RemoteHomologous: 
		DicChResNRangeS=copy.deepcopy(DicChResNRangeSeq)
	if sliding_by_ss:    
		DicChResNRangeS=copy.deepcopy(DicChResnRangeSecStrbySecStr)

	countFrags=0
	for ch in DicChResNRangeS: countFrags+=len(DicChResNRangeS[ch])

	folderLLG = output_folder + '/initial/LLG'
	if not os.path.isdir(folderLLG): 
		os.mkdir(folderLLG)

	if not os.path.isfile(folderLLG+'/initial_phaser.log'): 
		LibSLIDER.calculate_LLG (
		output_folder, pdbcl, mtz, SpaceGroup, I_SLIDER, SIGI_SLIDER, Amplitudes, HighRes, MW, NC,
		'1.0', folderLLG+'/initial_phaser.sh', folderLLG+'/initial_phaser.log')
	vrmsi = LibSLIDER.return_VRMS(folderLLG + '/initial_phaser.log')
	LLG0 = LibSLIDER.return_LLG  (folderLLG + '/initial_phaser.log')
	if countFrags>1:
		with open(pdbcl) as fr:
			frl=fr.readlines()
			for ch in DicChResNRangeS:
				for resrange in DicChResNRangeS[ch]:
					idash=resrange.index('-')
					ires=resrange[:idash]
					fres=resrange[idash+1:]
					lresrange = list ( range(int(ires),int(fres)+1) )

					ff=folderLLG+'/initial_no'+ch+resrange+'.pdb'
					fw=open(ff,'w')

					for l in frl:
						if l.startswith('CRYST') or l.startswith('SCALE') or l.startswith('END'):                      fw.write(l)
						elif l.startswith('ATOM') and (l[21]!=ch or (l[21]==ch and int(l[22:26]) not in lresrange )):  fw.write(l)

					fw.close()
					# print ch,ires,fres
					# print ff

					PDB_input_file=ff
					PDB_sh_file_log=PDB_input_file[:-4]+'fix_phaser.log'
					PDB_sh_file=PDB_sh_file_log[:-3]+'sh'

					if not os.path.isfile(PDB_sh_file_log):
						if nproc[0] > -1:  # NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
							#                    print "I found ", sym.REALPROCESSES, "CPUs." #NOTE: REALPROCESSES es el numero de cores de tu ordenador
							while 1:
								time.sleep(0.1)
								if len(multiprocessing.active_children()) < nproc[0]:
									process_phaser = multiprocessing.Process(target=LibSLIDER.calculate_LLG, args=(
									output_folder, PDB_input_file, mtz, SpaceGroup, I_SLIDER, SIGI_SLIDER, Amplitudes, HighRes, MW, NC,
									vrmsi, PDB_sh_file, PDB_sh_file_log,False))
									process_phaser.start()
									time.sleep(0.1)
									break
						else:
							print("FATAL ERROR: I cannot load correctly information of CPUs.")
							sys.exit(1)

		# CONDITION TO WAIT ALL PROCESSES TO BE FINISHED
		while 1:
			if len(multiprocessing.active_children()) == 0:
				break
			else:
				time.sleep(0.1)

		logger.info('LLG0 '+str(LLG0)+'\n')

		for ch in DicChResNRangeS:
			for resrange in DicChResNRangeS[ch]:
				DicChResNRangeS[ch][resrange]={}
				DicChResNRangeS[ch][resrange]['LLG0fix']=LibSLIDER.return_LLG (folderLLG+'/initial_no'+ch+resrange+'fix_phaser.log')
				DicChResNRangeS[ch][resrange]['LLG+fix']=LLG0-DicChResNRangeS[ch][resrange]['LLG0fix']
				#print ch, resrange, 'LLG0', DicChResNRangeS[ch][resrange]['LLG0'], 'fix' , DicChResNRangeS[ch][resrange]['LLG0fix']
				logger.info(ch+' '+resrange+' LLG+ '+str(DicChResNRangeS[ch][resrange]['LLG+fix']))


	###### Section to obtain target sequence in REMOTE HOMOLOG and SECONDARY STRUCTURE MODE
	###### Section to generate DicChResNRangeSeqTarget which will have a dictionary of chain as key which will have range-residues and the target sequence (1). {Chain1: {ResNRange1:[seqposs1,seqposs2]} seqposs1 usually is larger than fragment in model, more possibilities will be generated afterward
	#DicChResNRangeAlignmentseq = {}
	#DicChResNRangeAlignmentss = {}
	DicChResNRangeSeqTarget={}
	for l_ch in chosen_chains:
		# if len(l_ch)>1:
		#     if not ncschains:
		#         print 'SLIDER IN HOMOLOG MODE ONLY WORKS IF NCS IS GIVEN. CORRECT BOR FILE AND RERUN ALGORITHM.'
		#         exit()
		for ch in l_ch:
			DicChResNRangeSeqTarget[ch] = {}
			if RemoteHomologous: DicVar=DicChResNRangeSeq[ch]
			if sliding_by_ss:    DicVar=DicChResnRangeSecStrbySecStr[ch]

			for ResNRange,FragModel in DicVar.items():
				# print ResNRange,FragModel
				ResNRangeList= list ( range (int(ResNRange.split('-')[0]) , int(ResNRange.split('-')[1])+1) )
				# print ResNRangeList
				# print DicFixRes[ch]
				# print set(ResNRangeList)<=set(DicFixRes[ch])
				if len(FragModel) > minimum_ss_frag and not set(ResNRangeList)<=set(DicFixResMod[ch]) and not set(ResNRangeList)<=set(DicFixResNotMod[ch]):
					listpossibvar=[]
					###### This part will obtain pieces of sequence that will be slided (their size will be the size of the fragment in model + 2*sliding_tolerance)
					###### Section to obtain target sequence in REMOTE HOMOLOG MODE
					if RemoteHomologous:
						try:indexvar=remotehSeqAlign.index(FragModel)
						except:
							logger.info('Sequence found in model chain '+ch+' and residues '+str(ResNRange)+': '+str(FragModel)+' not found in sequence given in alignment:')
							logger.info(str(remotehSeqAlign))
							logger.info('Please correct the correspondence between partial model contiguous sequence and given sequence in alignment.')
							sys.exit(1)
							#condition to add A if sliding window get outside sequence in the beginning
						if indexvar-sliding_tolerance<0:  seqwindow='A'*((indexvar-sliding_tolerance)*-1)+targetSeqalign[ : indexvar+sliding_tolerance+len(FragModel) ]
						#if targetSeqalign.index(targetseq)-sliding_tolerance<0:  seqwindow='A'*((targetSeqalign.index(targetseq)-sliding_tolerance)*-1)+targetSeqalign[ : targetSeqalign.index( targetseq)+sliding_tolerance+len(targetseq) ]
						#below line works even sliding window surpass the end, as no problem happens if a higher index is given then its last index in variable
						else:                             seqwindow=targetSeqalign[ indexvar-sliding_tolerance : indexvar+sliding_tolerance+len(FragModel) ]
						# else:                                                    seqwindow=targetSeqalign[ targetSeqalign.index( targetseq)-sliding_tolerance : targetSeqalign.index( targetseq)+sliding_tolerance+len(targetseq) ]
						#add A if sliding window got outside sequence in the end
						seqwindow+='A'*(len(FragModel)+sliding_tolerance*2-len(seqwindow))
						#This below line changes the residues of the Remote Homolog sequence that have no correspondence to the residues of the Target Sequence (-) to 'A'
						seqwindow=seqwindow.replace('-','A')
						listpossibvar.append(seqwindow)
						#listpossibvar = [targetSeqalign[indexvar:indexvar + len(FragModel)].replace('-','A')]
					#DicChResNRangeSeqTarget[ch][ResNRange]= targetSeqalign[indexvar:indexvar+len(FragModel)]
					###### Section to obtain target sequence in REMOTE HOMOLOG MODE
					if sliding_by_ss:
						for frag in list_dics_sspred_conf: #example of list_dics_sspred_conf=[{'confidence': '76688999888776569999999974', 'sec_str_pred': 'HHHHHHHHHHHHHHHHHHHHHHHHHH', 'initial_res': 5, 'final_res': 30, 'sequence': 'PEDKKRILTRVRRIRGQVEALERALE'}]
							if len(frag['sequence'])+sliding_tolerance>=len(FragModel): #Check if size of sequence is within expected size of fragment in model
								if frag['sec_str_pred'][0]==FragModel[0]: #FragModel in this case is Secondary Structure of the model and frag['sec_str_pred'] is Secondary Structure of predicted fragment ('sequence')
									listpossibvar.append(sliding_tolerance*'A'+frag['sequence']+sliding_tolerance*'A')

					#DicChResNRangeSeqTarget[ch][ResNRange] = listpossibvar
					DicChResNRangeSeqTarget[ch][ResNRange]=[]
					CounterFrag1=0# Counter to generate pretty name in output
					for possib1 in listpossibvar:
						CounterFrag1+=1
						for i in range( len(possib1)-len(FragModel)+1 ):
							DicChResNRangeSeqTarget[ch][ResNRange].append( [ possib1[i:len(FragModel)+i] , str(CounterFrag1)+'-'+str(i+1) ])


	if RemoteHomologous: 
		logger.info('\n\nSLIDER generate from partial contiguous residues and given alignment, the following hypotheses per fragment:')
	if sliding_by_ss:
		logger.info('\n\nSLIDER generate from partial contiguous residues and given secondary structure elements in PSIPRED prediction, the following hypotheses per fragment:')

	#    print DicFixRes
	#    exit()

	# for ch in DicChResNRangeSeqTarget:
	#     for Res in DicChResNRangeSeqTarget[ch]:
	#         print ch,Res,DicChResNRangeSeqTarget[ch][Res]
	# exit()

	DicListPossib=defaultdict(list)

	#Here I will create:a dictionary of dictionary of list {Chain1: {ResNRange1:[seqposs1,score]}
	for igroupeval, l_ch in enumerate(chosen_chains):
		logger.info('\nEvaluation on group of chains '+str(igroupeval+1)+'('+'+'.join(l_ch)+')')
		#ListPossib = []
		for ch,resnrange in listChResNRangeCA:
			resi=int(resnrange.split('-')[0])
			resf=int(resnrange.split('-')[-1])
			ListResNRangeInt= list ( range(resi,resf+1) )                                                                        #list of residues numbers to be evaluated within this chosen fragment
			ListResNRangeIntModeled=sorted(list(set(ListResNRangeInt)-set(DicFixResMod[ch])-set(DicFixResNotMod[ch]))) #list of residues numbers to be modeled within this chosen fragment
			if RemoteHomologous: SeqOrigFrag=DicChResNRangeSeq[ch][resnrange]
			if sliding_by_ss:    SeqOrigFrag=DicChResnRangeSeqbySecStr[ch][resnrange]
			if ch in l_ch and ch in DicChResNRangeSeqTarget and resnrange in DicChResNRangeSeqTarget[ch] and len(DicChResNRangeSeqTarget[ch][resnrange])>0 and len(ListResNRangeIntModeled)>minimum_ss_frag: #Conditions that fragment in model need to fulfill for SLIDER WINDOW be applied.
				ListPossib = []
				logger.info('\nEvaluation '+ch+' '+resnrange)

				slidingwindow = list ( range(len(DicChResNRangeSeqTarget[ch][resnrange])) )

				if RemoteHomologous:
					targetSeq=targetSeqalign
					logger.info('REM HOMOLOG SEQ (ALIGN) '+'-'*sliding_tolerance+remotehSeqAlign+'-'*sliding_tolerance)
					logger.info('TARGET SEQUENCE (ALIGN) '+'-'*sliding_tolerance+targetSeqalign +'-'*sliding_tolerance)

					#range of Remote Homolog Mode will be different to facilitate its description through prints, but sequence order will be sorted based on scoring afterward
					# this range would slide by its edge to the middle, i.e., 1st extreme left, 2nd extreme right, until middle is reached
					# slidingwindow2 = []
					# for ii in range(len(slidingwindow) / 2 + 1):
					#     slidingwindow2.append(slidingwindow[ii])
					#     if slidingwindow[ii] != slidingwindow[-ii-1]: slidingwindow2.append(slidingwindow[-ii-1])
					# slidingwindow=slidingwindow2

				if sliding_by_ss:
					targetSeq=dic_secstr_pred_psipred['sequence']
					logger.info('TARGET SEQUENCE        '+'-'*sliding_tolerance+targetSeq+'-'*sliding_tolerance)
					logger.info('Predicted SecStructure '+'-'*sliding_tolerance+dic_secstr_pred_psipred['sec_str_pred']+'-'*sliding_tolerance)

				for ipossib in slidingwindow:
					possib=DicChResNRangeSeqTarget[ch][resnrange][ipossib][0]

					if sliding_by_ss: FragName=DicChResNRangeSeqTarget[ch][resnrange][ipossib][1]
					possibvar = ''
					for iaa,i in enumerate(ListResNRangeInt):
						if   i in DicFixResNotMod[ch]:  possibvar += DicChResNResType[ch][i].lower() #add residues not modeled
						elif i in DicFixResMod[ch]   :  possibvar += DicChResNResType[ch][i].upper() #add fixed residues to be modeled through ModelFixedResidues/DicFixRes
						else:                           possibvar += possib[iaa]                     #add residues being assigned

					# replace res in edge for A
					# replace res in edge for A if there is no previous residue
					if ModelEdge==False and resi - 1 not in DicChResNResType[ch]: possibvar = 'A' + possibvar[1:]
					if ModelEdge==False and resf + 1 not in DicChResNResType[ch]: possibvar =       possibvar[:-1] + 'A'

					if RemoteHomologous:
						score = abs (ipossib - (max(slidingwindow) / 2) ) #OLD
						score = score * -4 + (len(possibvar) - 2) * 6  # Score is = number (residues being modelled) * 6 - number of slides applied * -4
						if ModelEdge: score += 6*2
						if ReduceComplexity:
							counterr=0
							for aa in 'DEKNQRST': counterr+=possibvar.count(aa)
							score+= counterr*-6


						#OBSOLETE before different scoring function #score=ipossib-(max(slidingwindow)/2) # abs(i-(len(possib)-len(SeqOrigFrag))/2)*-1 this formula makes the given score mean the number of slides done in alignment
						#print (possibvar,{ch: ListResNRangeInt},slidingwindow,score) #checking what is it doing
					if sliding_by_ss:    score=0                              # score in sliding_by_ss here is 0 and it will calculated afterward when each sequence is generated.

					#ListPossib.append([possibvar, {ch: ListResNRangeInt}, abs(score)*-1]) #OBSOLETE before different scoring function
					ListPossib.append([possibvar, {ch: ListResNRangeInt}, score ])
					#print possibvar

					indextargetSEQ=LibSLIDER.BestAlignment2StringsReturnIndex(targetSeq, possib)
					idres=''
					if post_mortem:
						idres1=LibSLIDER.GivenTwoSequencesIdenticalRes(possibvar,TrueSeqDicChResNRangeSeq[ch][resnrange])
						idres='#IdRes:'+str(idres1)
					if RemoteHomologous:
						logger.info('SEQ slide ' +str(score)       + ' ' * (len('REM HOMOLOG SEQ (ALIGN)') - len('SEQ slide ' +str(score)))+     '-' * (sliding_tolerance+indextargetSEQ) + possibvar + '-'*(len('-'*(sliding_tolerance)+targetSeq)-len(possibvar)-indextargetSEQ)+' '+ idres)
					if sliding_by_ss:
						logger.info('Frag ' + FragName + ' ' * (len('REM HOMOLOG SEQ (ALIGN)') - len('Frag ' + FragName))+ '-' * (sliding_tolerance + indextargetSEQ) + possibvar + '-'*(len('-'*(sliding_tolerance)+targetSeq)-len(possibvar)-indextargetSEQ)+' '+idres)
				if post_mortem:
					indextrueSEQ = LibSLIDER.BestAlignment2StringsReturnIndex(targetSeq, TrueSeqDicChResNRangeSeq[ch][resnrange])
					logger.info('\nTrueSEQ'                      + ' ' * (len('REM HOMOLOG SEQ (ALIGN)') - len('TrueSEQ'))+                    '-' * (sliding_tolerance+indextrueSEQ)   + TrueSeqDicChResNRangeSeq[ch][resnrange] + '-'*(len('-'*(sliding_tolerance)+targetSeq)-len(possibvar)-indextrueSEQ))
					if RemoteHomologous: 
						logger.info('SS ' + ch + '/' + resnrange   + ' ' * (len('REM HOMOLOG SEQ (ALIGN)') - len('SS ' + ch + '/' + resnrange))+ '-' * (sliding_tolerance+indextrueSEQ)   + DicChResnRangeSecStr[ch][resnrange]     + '-'*(len('-'*(sliding_tolerance)+targetSeq)-len(possibvar)-indextrueSEQ))
				else:
					if RemoteHomologous: 
						logger.info('SS ' + ch + '/' + resnrange + ' ' * (len('REM HOMOLOG SEQ (ALIGN)') - len('SS ' + ch + '/' + resnrange))+ '-' * (sliding_tolerance+indextargetSEQ) + DicChResnRangeSecStr[ch][resnrange]     + '-'*(len('-'*(sliding_tolerance)+targetSeq)-len(possibvar)-indextargetSEQ))

				if not ncschains or l_ch.index(ch)==0: DicListPossib[','.join(l_ch)].append(ListPossib)

			# else:
			#     if RemoteHomologous: print 'Fragment in model did not fulfill one or more of the conditions selected by SLIDER and SLIDING WINDOW will not be applied to its residues.'
			#
			#     possibvar = ''
			#     for i in ListResNRangeInt:
			#         if ModelFixedResidues and i in DicFixRes[ch]: possibvar += DicChResNResType[ch][i].upper()
			#         else:                                         possibvar += DicChResNResType[ch][i].lower()
			#     ListPossib.append([possibvar, {ch: ListResNRangeInt}, 0])
			#

	# Section to see if number of combinations is greater than models_by_chain
	# if IndependentMode!=True:

	# #### DEBUGING DicListPossib
	# for ch in DicListPossib:
	#     print ch
	#     for listi in DicListPossib[ch]:
	#         # for listii in listi:
	#             print listi
	# exit()

	#exit()

	logger.info('\n\n\n\nAccording to the previous sequences being generated for each fragment:')

	for l_ch,ListPossib in sorted(DicListPossib.items()):
		numbcomb = 1
		for ListPoss in ListPossib:
			numbcomb = numbcomb*len(ListPoss)
		if numbcomb > models_by_chain:
			if RemoteHomologous:
				logger.info('\nFor chain(s) '+l_ch+' -> '+str(numbcomb)+' hypotheses exceed the allowed maximum ('+ str(models_by_chain)+ '). Evaluation of "fragments" will be done independently and selected based on LLG.')
				IndependentMode = True
			if sliding_by_ss:
				logger.info('\nFor chain(s) '+l_ch+' -> '+str(numbcomb)+' hypotheses exceed the allowed maximum ('+str(models_by_chain)+ '). Exceding hypotheses will be excluded by alignment scoring matrix as the order of fragments will be applied in this following step.')
		else:   
			logger.info('\nFor chain(s) '+l_ch+' -> '+str(numbcomb)+' hypotheses will be generated.')



	try:    IndependentMode
	except: IndependentMode=False
	#except: IndependentMode=True

	#Generating all possibilities of slided fragments into a list SeqPushRefCrude

	SeqPushRefCrude=[]

	for l_ch,ListPossib in sorted(DicListPossib.items()):
		if IndependentMode==False:
			for EachPossib in itertools.product(*ListPossib):
				SeqPushRefCrude.append(EachPossib)
		else:
			for ListPoss in ListPossib:
				for EachPossib in ListPoss:
					SeqPushRefCrude.append( [EachPossib] )

	#Converting SeqPushRefCrude to SeqPushRef
	#Adding other fragments that are fixed
	SeqPushRef=[]
	for poss in SeqPushRefCrude:
		DicOrgChResNRangeEval = {}
		seq=''
		score=0

		for Ch,ResNRange in listChResNRangeCA:
			#Constructing whole sequence and DicChResNRangeEval (evaluated residues numbers) in each Hypothesis to be pushed through Refinement
			# print Ch,ResNRange
			ListResNRange = list ( range ( int(ResNRange.split('-')[0]) , int(ResNRange.split('-')[1])+1 ) ) #List of residues in model
			Check=False
			for Frag in poss:
				seqvar = Frag[0]
				DicChResNRangeEval = Frag[1]
				if ncschains and Ch in chosen_chains[0]: Ch2=chosen_chains[0][0]
				else:                                    Ch2=Ch
				if RemoteHomologous: scoreVar = Frag[2]
				if Ch2 in DicChResNRangeEval and DicChResNRangeEval[Ch2]==ListResNRange: #Checking if residue in partial model is within slided residues and adding info
					if Ch not in DicOrgChResNRangeEval: DicOrgChResNRangeEval[Ch]=[]
					DicOrgChResNRangeEval[Ch]=DicOrgChResNRangeEval[Ch]+ListResNRange
					seq+=seqvar
					if RemoteHomologous: score+=scoreVar                               #In the case of Remote Homolog Mode, score is already in this list
					Check=True                                                         #No need to retrieve residues from original model
					# print 'seqvar',seqvar

			if Check==False:                                                           #Residues not being assigned, therefore retrieving them from original model
				seqvar=''
				for i in ListResNRange:
					if   i in DicFixResMod[Ch]   :  seqvar += DicChResNResType[Ch][i].upper()
					elif i in DicFixResNotMod[Ch]:  seqvar += DicChResNResType[Ch][i].lower()
					else:                           seqvar += 'A'
					#else:                                         seqvar += DicChResNResType[Ch][i].lower()
				seq+=seqvar
				# print 'seqvar2', seqvar

		#Obtaining scoring from alignment scoring matrix
		if sliding_by_ss:
			#print '\nScoring hypotheses using SLIDER alignment scoring matrix\n'
			matrix_align=LibSLIDER.generate_matrix_SLIDER_alignment(includeX=True)
			DicChResNSeqs = {}
			for Frag in poss:
				seqvar=Frag[0]
				DicChResNRangeEval = Frag[1]
				for Ch,ListResN in DicChResNRangeEval.items():
					if Ch not in DicChResNSeqs: DicChResNSeqs[Ch]={}
					for i,ResN in enumerate(ListResN):
						DicChResNSeqs[Ch][ResN]=seqvar[i]
			DicChSeqs={}
			for Ch in DicChResNSeqs:
				DicChSeqs[Ch]=''
				for ResN in sorted(DicChResNSeqs[Ch]): DicChSeqs[Ch]+= DicChResNSeqs[Ch][ResN]
			score=0
			for Ch,seqchain in DicChSeqs.items():
				pairwise,scorevar=LibSLIDER.AlignTwoSequences (dic_secstr_pred_psipred['sequence'],seqchain,matrix_align)
				score+=scorevar

		#SeqPushRef.append( ( seq , DicOrgChResNRangeEval , score ) )
		SeqPushRef.append([seq, DicOrgChResNRangeEval, score])

	logger.info('\nFor chain(s) '+l_ch+' -> '+str(numbcomb)+' hypotheses will be generated.')

	# Calculating number of identical residues by sequence
	if post_mortem:
		for ii, s in enumerate(SeqPushRef):
			seqvar = s[0]
			ident = 0
			# countt = 0
			# print s
			for i, l in enumerate(list_CA_trace_related_ent):  # list_CA_trace_related_ent[0]=[('A', 3, 'T', <Atom CA>), ('A', 3, 'K', <Atom CA>), 1.2654423]
				if len(l) > 1:
					AAtrue = l[1][2]
					AAVar = seqvar[i]
					ChModel = l[0][0]
					ResnModel = l[0][1]
					# print i
					if AAtrue == AAVar or (AAtrue.lower() == AAVar and ResnModel not in DicChImpartialRes[ChModel]): ident += 1
			# if seqvar[i] == seqvar[i].upper():
			#         countt += 1
			#         if len(l) > 1 and l[1][-2] == seqvar[i]: ident += 1
			# identt = (ident * 100) / countt
			# seq_pushed_refinement[ii] = seq_pushed_refinement[ii] + (identt,)
			#SeqPushRef[ii] = SeqPushRef[ii] + (ident,)
			SeqPushRef[ii].append(ident)
			# seq=(seq,list_chain, ll_score , alig_score , list_seq_chain , id ) id only in post_mortem

	#Sorting list to be pushed by alignment score
	if not IndependentMode: SeqPushRef=sorted(SeqPushRef, key=lambda x: x[2], reverse=True)

	# list of different evaluations
	ListCategoriesRun = []
	for s in SeqPushRef:
		if s[1] not in ListCategoriesRun:
			ListCategoriesRun.append(s[1])

	SeqPushRef2 = []
	for eval in ListCategoriesRun:
		count=0
		for s in SeqPushRef:
			if (count<seq_pushed_refinement or s[2]==scoreprev) and eval==s[1]:
				SeqPushRef2.append(s)
				scoreprev=s[2]
				count+=1
		trash1,TextDescriptionChResRange=LibSLIDER.convertDicChResNStr(eval)
		print ('\nFor',TextDescriptionChResRange+';',str(count),'hypotheses will be tried by SLIDER.')

	SeqPushRef=SeqPushRef2

	# # obtaining dictionary of chain and list of residues numbers having SC modeled
	# for s in seq_pushed_refinement:
	#     for i, aa in enumerate(s[0]):
	#         Ch = listChResNCA[i][0]
	#         ResN = listChResNCA[i][1]
	#         if aa == aa.upper(): s[1][Ch].append(ResN)


	for DicChResNEval in ListCategoriesRun:
		strfolder,_=LibSLIDER.convertDicChResNStr (DicChResNEval)
		folder = output_folder + '/' + strfolder + '/'
		if not os.path.isdir(folder): 
			os.mkdir(folder)
		table_name=folder+'Table_eval_'+strfolder
		output_table=open(table_name,'w')
		ms = ''
		if post_mortem: ts=''
			# for ch in l_chain_resrange:
			#     ts+=true_seq_dic_string[ch]+'\t'
		for ch in sorted(DicChResNResType):
			for resn in sorted(DicChResNResType[ch]):
				ms+=DicChResNResType  [ch][resn]
				if post_mortem: ts+=TrueSeqDicChResNResT[ch][resn]
		output_table.write    (ms + ' "INIT  SEQUENCE"\n')
		if post_mortem:
			output_table.write(ts + ' "TRUE MATCH SEQ"\n')
			output_table.write  ('\nSeq\tAlignScore\t#IdRes\n')
		else: output_table.write('\nSeq\tAlignScore\n')

		print('\n\n')

		for t in SeqPushRef:
			if t[1]== DicChResNEval:
			#t=s(seq,list_chain, ll_score , alig_score , list_seq_chain , id ) id only in post_mortem
				alsc='%.2f' % (t[2])
				output_table.write(t[0] + '\t' + str(alsc))
				if post_mortem:
					output_table.write('\t'+str(t[-1]) )
				output_table.write('\n')
		output_table.close()
		print('\n\n',table_name)
		with open(table_name) as f: print(f.read())


	##############_
	##############CREATING DICTIONARIES OF FILES

	for DicChResNEval in ListCategoriesRun:
		strfolder,_=LibSLIDER.convertDicChResNStr (DicChResNEval)
		folder = output_folder + '/' + strfolder + '/'
		lfolder=['','0_Scwrl4','1_ref','3_shelxe']
		if edstats_path != False: lfolder.append('2_edstats')
		for f in lfolder:
			if not os.path.isdir(folder+f): 
				os.mkdir(folder+f)

	list_dics_all_files = []
	#dic_index_by_chain={}
	prevdic=''

	for seq in SeqPushRef: #[(seqvar, defaultdict(list) , alig_score , ResId# )]    #OBSOLETE seq=(seq,list_chain, ll_score , alig_score , list_seq_chain , id ) id only in post_mortem
		if seq[1]==prevdic: count+=1
		else:               count=0
		prevdic = seq[1]
		dic={}

		strfolder,_ = LibSLIDER.convertDicChResNStr(seq[1])
		dic['PATH']=output_folder+'/'+strfolder+'/'
		dic['file']='seq'+str(count)+strfolder[3:]
		dic['HypSeq'] = LibSLIDER.GivenSeqListChResNCASeqReturnStringRef(seqSeqPushRef=seq, listChResNCA=listChResNCA, Sequence=seq_string)

		dic['seq']=seq[0]
		dic['EvalChResn']=seq[1]
		dic['align_score']=seq[2]
		# dic['seq_eval']=seq[4]

		if post_mortem:
			dic['#IdRes']=seq[-1]
		#dic['assigned_res_int']=len(filter(lambda x: x in string.uppercase, dic['seq']))
		dic['assigned_res_int'] =len(re.findall(r'[A-Z]', dic['seq']))

		dic['seq_file']=dic['PATH']+'0_Scwrl4/'+dic['file']+'.seq'
		dic['seq_log']=dic['seq_file'][:-4]+'.log'
		dic['initial_pdbfile']=dic['seq_file'][:-3]+'pdb'
		dic['refine_file1']=dic['PATH']+'1_ref/'+dic['file']+'_ref1.pdb'
		#if expand_from_map: dic['refine_file1_map_lst'] = dic['PATH'] + '3_shelxe/'+dic['file']+ '_ref1_map.lst'
		if expand_from_map: dic['refine_file1_map_lst'] = dic['PATH'] + '3_shelxe/seq'+str(count)+'_ref1_map.lst'
		if refinement_program=='buster':
			dic['refine_file2']=dic['PATH']+'1_ref/'+dic['file']+'_ref2.pdb'
			#dic['refine_file2_map_lst'] = dic['PATH'] + '3_shelxe/'+dic['file']+ '_ref2_map.lst'
			dic['refine_file2_map_lst'] = dic['PATH'] + '3_shelxe/seq'+str(count)+'_ref2_map.lst'
		#dic['refine_file1_lst']=dic['PATH']+'3_shelxe/'+dic['file']+'_ref1.lst'
		#large names are impossible to allow shelxe run
		dic['refine_file1_lst']=dic['PATH']+'3_shelxe/seq'+str(count)+'_ref1.lst'
		if edstats_path != False: dic['edstats_file1']=dic['PATH']+'2_edstats/'+dic['file']+'_ref1_rss.out'
		#if refinement_program=='phenix.refine': dic['phenixRSCC_file1']=dic['PATH']+'1_ref/'+dic['file']+'_ref1_phenixRSCC.log'
		if use_coot: dic['coot_file']=dic['initial_pdbfile'][:-4]+'_coot.pdb'
		dic['refine_file2']=dic['PATH']+'1_ref/'+dic['file']+'_ref2.pdb'
		#dic['refine_file2_lst']=dic['refine_file2'][:-3]+'lst'
		if edstats_path != False: dic['edstats_file2']=dic['PATH']+'2_edstats/'+dic['file']+'_ref2_rss.out'
		list_dics_all_files.append(dic)





	##############RANDOM SEQUENCE GENERATION BY CHOSEN CHAIN(S)

	for DicChResNEval in ListCategoriesRun:
		#print DicChResNEval
		strfolder,_ = LibSLIDER.convertDicChResNStr(DicChResNEval)

		# If postmortem on, then hydpho and lowrot will be automatically generated for the most correct sequence
		if post_mortem:
			iii = -3
			bestpossibID = 0
			for dic in list_dics_all_files:
				if dic['EvalChResn'] == DicChResNEval and dic['#IdRes'] > bestpossibID:
					bestpossibID  = dic['#IdRes']
					bestpossibseq = dic['seq']
					#print 'here'
		else:
			iii = -1
			bestpossibseq=''
			for dic in list_dics_all_files:
				if bestpossibseq=='' and dic['EvalChResn'] == DicChResNEval: bestpossibseq=dic['seq']


		for ccount in range(iii, RandomModels + 1):
			dic = {}
			if ccount == -3:   dic['file'] = 'hydpho_'  + strfolder[4:]
			elif ccount == -2: dic['file'] = 'lowrot_' + strfolder[4:]
			elif ccount == -1: dic['file'] = 'polyA_'  + strfolder[4:]
			elif ccount == 0 : dic['file'] = 'polyS_'  + strfolder[4:]
			else:              dic['file'] = 'rdm'+str(ccount)+ '_' +strfolder[4:]

			dic['HypSeq']=dic['file'].split('_')[0]
			dic['PATH'] = output_folder + '/' + strfolder + '/'
			dic['EvalChResn'] = DicChResNEval
			dic['align_score'] = 0
			dic['seq']=bestpossibseq
			dic['seq_file'] = dic['PATH'] + '0_Scwrl4/' + dic['file'] + '.seq'

			if not dic['file'].startswith('rdm'):
				dic['seq']=bestpossibseq
				#if dic['file'].startswith('hydpho_')   : replacestring = 'CDEHKNQRSTY' # Hydrophobic HPH: AFGILMPVW   #EXCLUDED: CDEHKNQRSTY
				if dic['file'].startswith('hydpho_'):    replacestring = 'DEKNQRST'  # !!!NEW!!! Hydrophobic HPH: ACFGHILMPVWY   #EXCLUDED: DEKNQRST
				elif dic['file'].startswith('lowrot_'): replacestring = 'DEHKMNQRW'    # LOWROT:          ACFGILPSTVY #EXCLUDED: DEHKMNQRW
				else                                  : replacestring = 'ACDEFGHILKMNPQRSTVWY' #ALL RESIDUES
				for char in replacestring:
					if not dic['file'].startswith('polyS_') : dic['seq']=dic['seq'].replace(char,'A')
					else                                    : dic['seq']=dic['seq'].replace(char,'S')

			else:
				#check if rdm was already generated, if so, get that sequence
				if os.path.isfile(dic['seq_file']):
					with open    (dic['seq_file']) as f:  dic['seq']=f.read().replace('\n', '')
					print('File',dic['seq_file'],'exists and SLIDER will use its sequence:',dic['seq'],'.')
				else:

					# Before, it was like happening when RandomOnlyEvalSequence is False
					if not RandomOnlyEvalSequence:  variter=str(bestpossibseq)
					else:                           variter=listChResNCA
					dic['seq'] = str(bestpossibseq)
					for i,s in enumerate(variter):
						if RandomOnlyEvalSequence: chvar,resnvar=s
						if (not RandomOnlyEvalSequence and s.upper()==s) or (RandomOnlyEvalSequence and chvar in DicChResNEval and resnvar in DicChResNEval[chvar]):
							randomstring = frequencyresbySS[SSpdbSEQ[i]]
							newaa = randomstring[random.randint(0, len(randomstring) - 1)]
							dic['seq']=dic['seq'][:i]+newaa+dic['seq'][i+1:]

			#Calculating number of identical residues by sequence
			if post_mortem:
				DicChImpartialRes = LibSLIDER.return_impartial_res(pdbcl)
				seqvar=dic['seq']
				ident = 0
				for i, l in enumerate(list_CA_trace_related_ent): #list_CA_trace_related_ent[0]=[('A', 3, 'T', <Atom CA>), ('A', 3, 'K', <Atom CA>), 1.2654423]
					if len(l) > 1:
						AAtrue=    l[1][2]
						AAVar=     seqvar[i]
						ChModel=   l[0][0]
						ResnModel= l[0][1]
						#print i
						if AAtrue == AAVar or (AAtrue.lower() == AAVar and ResnModel not in DicChImpartialRes[ChModel]) : ident += 1
				dic['#IdRes']=ident

			#Assigning values dictionary
			#dic['assigned_res_int'] = len(filter(lambda x: x in string.uppercase, dic['seq']))
			dic['assigned_res_int'] = len(re.findall(r'[A-Z]', dic['seq']))
			dic['seq_log'] = dic['seq_file'][:-4] + '.log'
			dic['initial_pdbfile'] = dic['seq_file'][:-3] + 'pdb'
			dic['refine_file1'] = dic['PATH'] + '1_ref/' + dic['file'] + '_ref1.pdb'

			#if expand_from_map: dic['refine_file1_map_lst'] = dic['PATH'] + '3_shelxe/' + dic['file'] + '_ref1_map.lst'
			if expand_from_map: dic['refine_file1_map_lst'] = dic['PATH'] + '3_shelxe/' + dic['file'][:-len(strfolder[3:])] + '_ref1_map.lst'
			if refinement_program == 'buster':
				dic['refine_file2'] = dic['PATH'] + '1_ref/' + dic['file'] + '_ref2.pdb'
				#dic['refine_file2_map_lst'] = dic['PATH'] + '3_shelxe/' + dic['file'] + '_ref2_map.lst'
				dic['refine_file2_map_lst'] = dic['PATH'] + '3_shelxe/' + dic['file'][:-len(strfolder[3:])] + '_ref2_map.lst'
				#[:-len(strfolder[3:])]
				if edstats_path != False: dic['edstats_file2'] = dic['PATH'] + '2_edstats/' + dic['file'] + '_ref2_rss.out'
			else: dic['refine_file2'] = dic['refine_file1']

			#dic['refine_file1_lst'] = dic['PATH'] + '3_shelxe/' + dic['file'] + '_ref1_pda.lst'
			dic['refine_file1_lst'] = dic['PATH'] + '3_shelxe/' + dic['file'][:-len(strfolder[3:])] + '_ref1_pda.lst'
			if edstats_path != False: dic['edstats_file1'] = dic['PATH'] + '2_edstats/' + dic['file'] + '_ref1_rss.out'
			#if refinement_program == 'phenix.refine': dic['phenixRSCC_file1'] = dic['PATH'] + '1_ref/' + dic['file'] + '_ref1_phenixRSCC.log'
			if use_coot: dic['coot_file'] = dic['initial_pdbfile'][:-4] + '_coot.pdb'

			list_dics_all_files.append(dic)


	# Reducing complexity by only modeling either hydrophobic or low rotamers residues
	if ReduceComplexity!=False:
		if ReduceComplexity :                replacestring = 'DEKNQRST'
		#if ReduceComplexity == 'hydpho':    replacestring = 'DEKNQRST'
		#elif ReduceComplexity == 'lowrot': replacestring = 'CDEHKNQRSTY'
		for dic in list_dics_all_files:
			#print ReduceComplexity
			# print dic['seq']
			for i in replacestring: dic['seq'] = dic['seq'].replace(i, 'A')
		#     print dic['seq']
		#Removing repetitive dictionary as mode ReduceComplexity was selected
			if post_mortem and 'hydpho' in dic['file']:  removeindex = list_dics_all_files.index(dic)
		if post_mortem: list_dics_all_files=list_dics_all_files[:removeindex]+list_dics_all_files[removeindex+1:]


	####HYPOTHESES SUBMISSION TO MODELING/REFINEMENT/VALIDATION STARTS HERE!

	for dic in list_dics_all_files:
		with open(dic['seq_file'],'w') as file:
			file.write('\n'.join(dic['seq'][i:i + 70] for i in range(0, len(dic['seq']), 70)))



	###running first refinement without Side Chains to evaluate fragment without sidechains
	##refine_refmac ( pdbcl, '' , '' , ncycles , refmac_option )

	##############Scwrl4

	print('\n\nAdding sidechains with Sprout\n\n')

	#running Scwrl4
	for dic in list_dics_all_files:
		PDB_input_file=pdbcl
		PDB_output_file=dic['initial_pdbfile']
		if not os.path.isfile( PDB_output_file ):
				if  nproc[0] > -1: #NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
					while 1:
						if len(multiprocessing.active_children()) < nproc[0] :
							print(dic['initial_pdbfile'].split(output_folder)[-1] , 'being generated')
							process_sprout = multiprocessing.Process(target= LibSLIDER.run_sprout_multiprocess, args= ( PDB_input_file , dic['seq_file'], PDB_output_file , sprout_path) )
							process_sprout.start()
							time.sleep(0.1)
							break
				else:
					print("FATAL ERROR: I cannot load correctly information of CPUs.")

	#CONDITION TO WAIT ALL PROCESSES TO BE FINISHED
	while 1:
		if len(multiprocessing.active_children()) == 0 : break
		else:                                            time.sleep(0.1)

	print('\n\n\n')


	# ####OBTAINING ENERGY INTO DICTIONARIES
	# for dic in list_dics_all_files:
	# 	dic['energy']=LibSLIDER.retrieve_energies_from_Scwrl4_log_file ( dic['seq_log'] )

	# ####LIST FOR ENERGY EVALUATION
	# for DicChResNEval in ListCategoriesRun:
	# 	strfolder = LibSLIDER.convertDicChResNStr(DicChResNEval)
	# 	energy_file_name=output_folder + '/' + strfolder + '/'+'Energy_'+strfolder+'.log'
	# 	listenergies=[]

	# 	for dic in list_dics_all_files:
	# 		if dic['EvalChResn'] == DicChResNEval: listenergies.append(dic['energy'])

	# 	energymean=numpy.mean(listenergies)
	# 	energystdev=numpy.std(listenergies)

	# 	for dic in list_dics_all_files:
	# 		if dic['EvalChResn'] == DicChResNEval: dic['Zenergy']=(dic['energy']-energymean)/energystdev

	# 	#Table generation
	# 	list_dics_all_filesOrgEnergy=sorted(list_dics_all_files, key=lambda item: item['energy'])
	# 	energy_file=open(energy_file_name,'w')
	# 	if not post_mortem:                         energy_file.write('File\tEnergy\tZEnergy\tAlgnSc\t#AsRes\n')
	# 	else:                                       energy_file.write('File\tEnergy\tZEnergy\tAlgnSc\t#AsRes\t#IdRes\n')
	# 	for dic in list_dics_all_files:
	# 		if dic['EvalChResn'] == DicChResNEval:
	# 			energy_file.write(dic['file']+'\t'+'%.1f'%(dic['energy'])+'\t'+'%.1f'%(dic['Zenergy'])+'\t'+'%.2f' % (dic['align_score'])+'\t'+str(dic['assigned_res_int']) )
	# 			if post_mortem:                     energy_file.write('\t'+str(dic['#IdRes'])+'\n')
	# 			else:                               energy_file.write('\n')
	# 	energy_file.close()

	# 	print(energy_file_name)
	# 	with open(energy_file_name) as f: print(f.read())


	#adding reference Initial dictionary
	list_dics_all_files.append(DicRefInitial)


	##############Recovering 0 occupancy residues to modeled residues
	if Recover0occup==True:
		list0occupRes=LibSLIDER.listres0occup(pdb=pdbclorig)
		for dic in list_dics_all_files:
			pdbi = dic['initial_pdbfile']
			pdbo = dic['initial_pdbfile'][:-4]+'_0occ.pdb'
			if not os.path.isfile(pdbo) : LibSLIDER.GivenListRes0occScwrl4PDBRecover0occ(lres0occ=list0occupRes, pdb_input=pdbi, pdb_output=pdbo)
			dic['initial_pdbfile']=pdbo



	#############coot automatic ROTAMER modelling

	coot_number_job=0
	if use_coot:
		for dic in list_dics_all_files:
			PDB_input_file=dic['initial_pdbfile']
			PDB_output_file=dic['coot_file']
			if not os.path.isfile( PDB_output_file ):
				if  nproc[0] > -1: #NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
			#                    print "I found ", sym.REALPROCESSES, "CPUs." #NOTE: REALPROCESSES es el numero de cores de tu ordenador
					while 1:
						time.sleep(0.1)
						if len(multiprocessing.active_children()) < nproc[0]:
							print(len(multiprocessing.active_children())+1,'jobs running by SLIDER in your local computer:')
							print('modeling rotamers of' , PDB_input_file, 'with coot and saving it to',PDB_output_file)
							process_coot = multiprocessing.Process(target= LibSLIDER.coot_ROTAMER_automatic_refinement, args= ( PDB_input_file , PDB_input_file[:-4]+'.mtz' , PDB_output_file , coot_number_job , coot_path ) )
							process_coot.start()
							coot_number_job+=1
							time.sleep(0.1)
							break
				else:
					print("FATAL ERROR: I cannot load correctly information of CPUs.")
					sys.exit(1)

	#CONDITION TO WAIT ALL PROCESSES TO BE FINISHED


	while 1:
		if len(multiprocessing.active_children()) == 0 : break
		else:                                            time.sleep(0.1)



	##############Run of refinement

	print('\n\nRun of refinement\n\n')

	if not distribute_computing=='multiprocessing':
		SystemUtility.open_connection(DicGridConn,DicParameters,cm)	

	else:
		cm=False

	##for model in range(number_of_model_generation_selection) :

	input_directory = ''
	aux_dic = sorted(list_dics_all_files, key=lambda x: x['PATH'])
	counter = 0

	for dic in aux_dic:
		if use_coot:
			PDB_input_file=dic['coot_file']	
		else:
			PDB_input_file=dic['initial_pdbfile']
		PDB_output_file=dic['refine_file1']

		if not os.path.isfile( PDB_output_file ):
			if distribute_computing=='multiprocessing':
				output_directory=PDB_output_file[:(PDB_output_file.rindex('/'))]
				if  nproc[0] > -1:
					while 1:
						time.sleep(0.1)
						if len(multiprocessing.active_children()) < nproc[0]:
							print('refining' , PDB_input_file, 'model with',refinement_program,'and saving it to',PDB_output_file,'\n')
							print(len(multiprocessing.active_children()) + 1, 'jobs running by SLIDER in your local computer:')
							sh_file=PDB_input_file[:-4]+'_submit.sh'
							if refinement_program=='refmac':
								LibSLIDER.sh_refine_refmac_multiprocesses ( PDB_input_file , mtz , PDB_output_file , refmac_ins_file , refmac_path , sh_file , distribute_computing)
							elif refinement_program=='buster':
								LibSLIDER.sh_refine_buster_multiprocesses ( PDB_input_file , mtz , PDB_output_file , buster_path , sh_file , distribute_computing , buster_parameters)
							elif refinement_program=='phenix.refine':
								LibSLIDER.sh_refine_phenix_multiprocesses ( pdb_input_file=PDB_input_file , mtz_input_file=mtz , pdb_output_file=PDB_output_file , phenixrefine_path=phenixrefine_path , F=I_SLIDER , SIGF=SIGI_SLIDER , sh_file=sh_file , distribute_computing=distribute_computing , options=PhenixRefineParameters)
							process_sh = multiprocessing.Process(target= LibSLIDER.create_job_multiprocessing , args= ( sh_file, ) )
							process_sh.start()
							time.sleep(0.02)
							break
				else:
					print("FATAL ERROR: I cannot load correctly information of CPUs.")
					sys.exit(1)
			else:
				print('refining' , PDB_input_file, 'model with',refinement_program,'and saving it to',PDB_output_file,'\n')
				aux_directory = os.path.dirname(PDB_input_file)
				if input_directory != aux_directory:
					if input_directory != '':
						LibSLIDER.create_job(cm, nameJob, input_directory, mtz, counter, refmac_ins_file)
					input_directory = aux_directory
					counter = 0

				sh_file=PDB_input_file[:-4]+'_submit.sh'
				sh_formatted = str(counter)+'.sh'
				PDB_formatted = str(counter)+'.pdb'

				if refinement_program=='refmac':
					LibSLIDER.sh_refine_refmac_multiprocesses ( PDB_formatted , mtz , PDB_output_file , refmac_ins_file , refmac_path , sh_file , distribute_computing, ccp4_config_path)
				elif refinement_program=='buster':
					LibSLIDER.sh_refine_buster_multiprocesses ( PDB_formatted , mtz , PDB_output_file , buster_path , sh_file , distribute_computing , buster_parameters, ccp4_config_path , buster_config_path )
				elif refinement_program=='phenix.refine':
					LibSLIDER.sh_refine_phenix_multiprocesses ( pdb_input_file=PDB_formatted , mtz_input_file=mtz , pdb_output_file=PDB_output_file , phenixrefine_path=phenixrefine_path , phenixrefine_config_path=phenixrefine_config_path , F=I_SLIDER , SIGF=SIGI_SLIDER , sh_file=sh_file , distribute_computing=distribute_computing , options=PhenixRefineParameters)

				LibSLIDER.create_symlink(sh_file, sh_formatted)
				LibSLIDER.create_symlink(PDB_input_file, PDB_formatted)

				counter += 1

	if not distribute_computing=='multiprocessing':
		if counter > 0:
			LibSLIDER.create_job(cm, nameJob, input_directory, mtz, counter, refmac_ins_file)
		SystemUtility.close_connection(DicGridConn,DicParameters,cm)

	count_files=0
	while count_files<len(list_dics_all_files):
		count_files=0
		for dic in list_dics_all_files:
			PDB_output_file=dic['refine_file1']
			if not os.path.isfile( PDB_output_file ) and not distribute_computing=='multiprocessing':
				if use_coot:
					PDB_input_file=dic['coot_file']	
				else:
					PDB_input_file=dic['initial_pdbfile']
				PDB_src_file = os.path.join(os.path.dirname(PDB_input_file), os.path.basename(PDB_output_file))		
				mtz_ref1_file = PDB_src_file.replace('.pdb','.mtz')
				rscc_log_file = PDB_src_file.replace('.pdb','_RSCC.log')
				phenix_log_file = PDB_src_file.replace('.pdb','.log')

				if os.path.isfile(PDB_src_file) and os.path.isfile(mtz_ref1_file) and \
				(os.path.isfile(rscc_log_file) or refinement_program != 'buster') and \
				(os.path.isfile(phenix_log_file) or refinement_program != 'phenix.refine'):
					if refinement_program == 'buster':
						shutil.move(rscc_log_file, PDB_output_file.replace('.pdb','_RSCC.log'))
					elif refinement_program == 'phenix.refine':
						shutil.move(phenix_log_file, PDB_output_file.replace('.pdb','.log'))
					shutil.move(PDB_src_file, PDB_output_file)
					shutil.move(mtz_ref1_file, PDB_output_file.replace('.pdb','.mtz'))
					count_files+=1
			elif os.path.isfile( PDB_output_file ):
				count_files+=1
		if count_files<len(list_dics_all_files): 
			time.sleep(10)

	##GETTING LLG PHENIX.REFINE
	if refinement_program=='phenix.refine':
		for dic in list_dics_all_files:
			logphenixrefine=dic['refine_file1'][:-3]+'log'
			dic['refine1_LLGnorm'],dic['refine1_LLGwork'],dic['refine1_LLGfree'] = LibSLIDER.GetPhenixRefineLLG(logphenixrefine)


	##RECALCULATING RFACTORS AND RSCC
	if refinement_program=='buster':
		print('\n\nBUSTER 2nd CYCLE: Recalculating Rfactors and RSCC\n\n')
		input_directory = ''
		aux_dic = sorted(list_dics_all_files, key=lambda x: x['PATH'])
		counter = 0
		for dic in aux_dic:
			PDB_input_file=dic['refine_file1']
			PDB_output_file=dic['refine_file2']
			if not os.path.isfile( PDB_output_file ):
				if distribute_computing == 'multiprocessing':
					output_directory=PDB_output_file[:(PDB_output_file.rindex('/'))]
					if  nproc[0] > -1:
						while 1:
							time.sleep(0.1)
							if len(multiprocessing.active_children()) < nproc[0]:
								print('refining' , PDB_input_file, 'model with',refinement_program,'and saving it to',PDB_output_file,'\n')
								print(len(multiprocessing.active_children()) + 1, 'jobs running by SLIDER in your local computer:')
								sh_file=PDB_input_file[:-4]+'_submit.sh'
								LibSLIDER.sh_refine_buster_multiprocesses ( PDB_input_file , mtz , PDB_output_file , buster_path , sh_file , distribute_computing , buster_parametersRfactorRSCC)
								process_sh = multiprocessing.Process(target= LibSLIDER.create_job_multiprocessing , args= ( sh_file, ) )
								process_sh.start()
								time.sleep(0.1)
								break
				else:
					print('refining' , PDB_input_file, 'model with',refinement_program,'and saving it to',PDB_output_file,'\n')	
					aux_directory = os.path.dirname(PDB_input_file)
					if input_directory != aux_directory:
						if input_directory != '':
							LibSLIDER.create_job(cm, nameJob, input_directory, mtz, counter, refmac_ins_file)
						input_directory = aux_directory
						counter = 0
					sh_file=PDB_input_file[:-4]+'_submit.sh'
					sh_formatted = str(counter)+'.sh'
					PDB_formatted = str(counter)+'.pdb'
					LibSLIDER.sh_refine_buster_multiprocesses ( PDB_formatted , mtz , PDB_output_file , buster_path , sh_file , distribute_computing , buster_parameters, ccp4_config_path , buster_config_path )
					LibSLIDER.create_symlink(sh_file, sh_formatted)
					LibSLIDER.create_symlink(PDB_input_file, PDB_formatted)
					counter += 1

		if not distribute_computing=='multiprocessing' and counter > 0:
			LibSLIDER.create_job(cm, nameJob, input_directory, mtz, counter, refmac_ins_file)

		#CONDITION TO WAIT ALL PROCESSES TO BE FINISHED
		count_files=0
		while count_files<len(list_dics_all_files):
			count_files=0
			for dic in list_dics_all_files:
				PDB_output_file=dic['refine_file2']
				if os.path.isfile( PDB_output_file ):
					count_files+=1
			if count_files<len(list_dics_all_files): 
				time.sleep(10)

	for dic in list_dics_all_files:
		#print dic['refine_file1']
		dic['refine1_R'], dic['refine1_Rfree'] = LibSLIDER.retrieve_Rfactor_from_PDB_file(dic['refine_file1'])
		if refinement_program == 'buster':
			dic['refine1_CCmc'], dic['refine1_CCsc'] = LibSLIDER.retrieve_busterCC_from_log_file(dic['refine_file1'][:-4] + '_RSCC.log')
			dic['refine2_R'], dic['refine2_Rfree'] = LibSLIDER.obtainRfactorsBUSTERMapOnly(dic['refine_file2'])
			#print dic['refine_file2'][:-4] + '_RSCC.log'
			i=0
			dic['refine2_CCmc'], dic['refine2_CCsc'] = LibSLIDER.retrieve_busterCC_from_log_file(dic['refine_file2'][:-4] + '_RSCC.log')

			# try:
			#     dic['refine2_CCmc'], dic['refine2_CCsc'] = LibSLIDER.retrieve_busterCC_from_log_file(dic['refine_file2'][:-4] + '_RSCC.log')
			# except:
			#     print 'Running:\n'+'corr' + ' -p ' + dic['refine_file2'] + ' -m ' + dic['refine_file2'][:-3]+'mtz' + ' -F 2FOFCWT -P PH2FOFCWT -d delete' + str(i) + ' > ' + dic['refine_file2'][:-4] + '_RSCC.log'
			#     os.system( 'corr' + ' -p ' + dic['refine_file2'] + ' -m ' + dic['refine_file2'][:-3]+'mtz' + ' -F 2FOFCWT -P PH2FOFCWT -d delete' + str(i) + ' > ' + dic['refine_file2'][:-4] + '_RSCC.log')
			#     dic['refine2_CCmc'], dic['refine2_CCsc'] = LibSLIDER.retrieve_busterCC_from_log_file(
			#         dic['refine_file2'][:-4] + '_RSCC.log')



	####PHASER LLG calculation


	for dic in list_dics_all_files:
		PDB_input_file=dic['refine_file1']
		PDB_sh_file=dic['refine_file1'][:-4]+'_phaser.sh'
		PDB_sh_file_log=PDB_sh_file[:-2]+'log'
		output_directory=PDB_input_file[:(PDB_input_file.rindex('/'))]
		if not os.path.isfile( PDB_sh_file_log ):
			if  nproc[0] > -1: #NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
		#                    print "I found ", sym.REALPROCESSES, "CPUs." #NOTE: REALPROCESSES es el numero de cores de tu ordenador
				while 1:
					time.sleep(0.1)
					if len(multiprocessing.active_children()) < nproc[0]:
						process_phaser = multiprocessing.Process(target=LibSLIDER.calculate_LLG, args=(output_folder,PDB_input_file, mtz, SpaceGroup, I_SLIDER, SIGI_SLIDER, Amplitudes, HighRes, MW, NC, vrmsi,PDB_sh_file, PDB_sh_file_log , False)) #fix rmsd refinement #last variable is to set VRMS False - do not refine it
						process_phaser.start()
						time.sleep(0.1)
						break
			else:
				print("FATAL ERROR: I cannot load correctly information of CPUs.")
				sys.exit(1)

	# CONDITION TO WAIT ALL PROCESSES TO BE FINISHED
	while 1:
		if len(multiprocessing.active_children()) == 0: break
		else:                                           time.sleep(0.1)

	for dic in list_dics_all_files:
		PDB_sh_file_log = dic['refine_file1'][:-4] + '_phaser.log'
		#dic['refine1_eLLG'], dic['refine1_TFZ'] = LibSLIDER.return_LLG(phaser_log_file=PDB_sh_file_log)
		dic['refine1_LLG'] = LibSLIDER.return_LLG(phaser_log_file=PDB_sh_file_log)

	#CALCULATION OF ZLLG OF SEQ
	for DicChResNEval in ListCategoriesRun:
		listLLG=[]
		for dic in list_dics_all_files:
			#if dic['EvalChResn'] == DicChResNEval and 'seq' in dic['file']:                          listLLG.append(dic['refine1_LLG']) #exclude rdm
			if dic['EvalChResn'] == DicChResNEval and ('seq' in dic['file'] or 'rdm' in dic['file'] or 'pol' in dic['file']) or 'initial' in dic['file']: listLLG.append(dic['refine1_LLG'])  #include rdm
		meanvarLLG=numpy.mean(listLLG)
		stdevvarLLG=numpy.std(listLLG)
		for dic in list_dics_all_files:
			#if dic['EvalChResn']== DicChResNEval and 'seq' in dic['file']:                           dic['refine1_ZLLG'] = (dic['refine1_LLG'] - meanvarLLG) / stdevvarLLG    #exclude rdm
			if dic['EvalChResn'] == DicChResNEval and ('seq' in dic['file'] or 'rdm' in dic['file'] or 'pol' in dic['file'])  or 'initial' in dic['file']: dic['refine1_ZLLG'] = (dic['refine1_LLG'] - meanvarLLG) / stdevvarLLG    #include rdm

	for dic in list_dics_all_files:
		if 'refine1_ZLLG' not in dic:                                       dic['refine1_ZLLG'] = 'n/a'


	####shelxe evaluation -a0

	#LINKS!
	print('\n\nCreating links for shelxe evaluation and converting mtz map files to phs files.\n\n')
	#if post_mortem:
	countt=0
	for dic in list_dics_all_files:
		#print dic
		evalmodels = [[dic['refine_file1'],              dic['refine_file1_lst']]]
		if expand_from_map and refinement_program!='phenix.refine':  evalmodels.append([dic['refine_file1'][:-3] + 'mtz',    dic['refine_file1_map_lst']])
		if expand_from_map and refinement_program=='phenix.refine':  evalmodels.append([dic['refine_file1'][:-4]+'_FOM.mtz', dic['refine_file1_map_lst']])
		if refinement_program=='buster' and expand_from_map: evalmodels.append([dic['refine_file2'][:-3] + 'mtz', dic['refine_file2_map_lst']])
		#print 'Converting model and map of',dic['refine_file1']
		for ev in evalmodels:
			input_lstfile  = ev[0]
			output_lstfile = ev[1]
			LibSLIDER.create_symlink(hkl,output_lstfile[:-3] + 'hkl')
			if post_mortem:
				LibSLIDER.create_symlink(ent,output_lstfile[:-3] + 'ent')
			if input_lstfile.endswith('mtz'):
				inputshelxe = output_lstfile[:-3] + 'phi'
				LibSLIDER.create_symlink(shelxe_ins_path,output_lstfile[:-3] + 'ins')
				if not os.path.isfile( inputshelxe ) :
					if nproc[0] > -1:  # NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
						#                    print "I found ", sym.REALPROCESSES, "CPUs." #NOTE: REALPROCESSES es el numero de cores de tu ordenador
						while 1:
							time.sleep(0.01)
							if len(multiprocessing.active_children()) < nproc[0]:
								countt+=1
								print('Converting',input_lstfile,'to',inputshelxe)
								if refinement_program=='phenix.refine': phic='PHIFCALC'
								else:                                   phic='PHIC'
								mtz2phi_run = multiprocessing.Process(target=LibSLIDER.mtz2phi_script,
																	 args=(input_lstfile, inputshelxe, F , SIGF , 'FOM', phic , countt,False))
								mtz2phi_run.start()
								print(input_lstfile,inputshelxe)
								time.sleep(0.01)
								break
			else:
				LibSLIDER.create_symlink(input_lstfile,output_lstfile[:-3] + 'pda')

	while 1:
		if len(multiprocessing.active_children()) == 0 : break
		else:                                            time.sleep(0.1)


	#SHELXE RUN!
	solvent=shelxe_line[shelxe_line.index('-s'):shelxe_line.index('-s')+shelxe_line[shelxe_line.index('-s'):].index(' ')]
	if post_mortem:
		for dic in list_dics_all_files:
			evalmodels =                                       [dic['refine_file1_lst'][:-3]+'pda']
			if expand_from_map:                                  evalmodels.append(dic['refine_file1_map_lst'][:-3] + 'phi')
			if refinement_program=='buster' and expand_from_map: evalmodels.append(dic['refine_file2_map_lst'][:-3] + 'phi')
			for f in evalmodels:
				if not os.path.isfile( f[:-3]+'lst' ) :
					if  nproc[0] > -1: #NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
				#                    print "I found ", sym.REALPROCESSES, "CPUs." #NOTE: REALPROCESSES es el numero de cores de tu ordenador
						while 1:
							time.sleep(0.01)
							if len(multiprocessing.active_children()) < nproc[0]:
								#print 'Calculating initial CC' , PDB_input_file , '-a0 -m0'
								iCC_eval_line='-a0 -m1 -x '+solvent
								#print PDB_input_file[:-1]+'a'
								shelxe_run = multiprocessing.Process(target= LibSLIDER.shelxe_multiprocesses , args= ( f , shelxe_path , iCC_eval_line ) )
								shelxe_run.start()
								time.sleep(0.01)
								break

		while 1:
			if len(multiprocessing.active_children()) == 0 : break
			else:                                            time.sleep(0.1)

	#OBTAIN CC AND wMPE
		for dic in list_dics_all_files:
			dic                                                       ['refine1_cCCi'], dic['refine1_cwMPE'] = LibSLIDER.return_iCC_wMPE(dic['refine_file1_lst'])
			if expand_from_map:                                    dic['refine1_mCCi'], dic['refine1_mwMPE'] = LibSLIDER.return_iCC_wMPE(dic['refine_file1_map_lst'])
			if refinement_program == 'buster' and expand_from_map: dic['refine2_mCCi'], dic['refine2_mwMPE'] = LibSLIDER.return_iCC_wMPE(dic['refine_file2_map_lst'])




	########EDSTATS evaluation
	if edstats_path != False:
		for dic in list_dics_all_files:
			lend = ['1']
			if refinement_program == 'buster': lend.append('2')
			for i in lend:
				PDB_input_file=dic['refine_file'+i]
				MAP_mtz_input_file=PDB_input_file[:-3]+'mtz'
				RSS_output_file=dic['edstats_file'+i]
				if not os.path.isfile( RSS_output_file ):
					if  nproc[0] > -1: #NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
				#                    print "I found ", sym.REALPROCESSES, "CPUs." #NOTE: REALPROCESSES es el numero de cores de tu ordenador
						while 1:
							time.sleep(0.01)
							if len(multiprocessing.active_children()) < nproc[0]:
								print('EDSTATS being generated in file',RSS_output_file)
								process = multiprocessing.Process(target= LibSLIDER.RSZD_calculation , args= ( MAP_mtz_input_file, PDB_input_file , RSS_output_file , refinement_program , edstats_path) )
								# LibSLIDER.RSZD_calculation ( MAP_mtz_input_file, PDB_input_file , RSS_output_file , refinement_program )
								process.start()
								time.sleep(0.01)
								break


		while 1:
			if len(multiprocessing.active_children()) == 0: break
			else:                                           time.sleep(0.1)

	####calculation of identity % total residues

	if post_mortem:
		for dic in list_dics_all_files:
			listmatch,identicalresn,percentidentity=LibSLIDER.given_2_superposed_pdbs_return_list_res_match(ent,dic['refine_file1'],1.0)
			dic['refine1_Ident%']=percentidentity

	for DicChResNEval in ListCategoriesRun:
		list_dics_all_files.append( list_dics_all_files[-1].copy() )
		list_dics_all_files[-1]['EvalChResn']=DicChResNEval


	if edstats_path != False:
		for dic in list_dics_all_files:
			lend = ['1']
			if refinement_program == 'buster': lend.append('2')
			for i in lend:
				PDB_input_file=dic['refine_file'+i]
				MAP_mtz_input_file=PDB_input_file[:-3]+'mtz'
				file=dic['refine_file'+i][dic['refine_file'+i].rindex('/')+1:]
				RSS_output_file=dic['edstats_file'+i]
				lRSCCm , lRSCCs = LibSLIDER.GivenEdstatsOutDicChResnStats12ReturnList  (RSS_output_file, dic['EvalChResn'], 'CCSm','CCSs')
				dic['refine' + i + '_RSCCmc_mean'] = numpy.mean(lRSCCm)
				dic['refine' + i + '_RSCCmc_stdev'] =numpy.std(lRSCCm)
				dic['refine' + i + '_RSCCsc_mean'] = numpy.mean(lRSCCs)
				dic['refine' + i + '_RSCCsc_stdev'] = numpy.std(lRSCCs)
				# if refinement_program == 'phenix.refine':
				#     print dic['phenixRSCC_file1']
				#     dic['refine' + i + '_RSCC_phenix'],RSCCl=LibSLIDER.ExtractFromPhenixModelVsDataRSCCallList(dic['phenixRSCC_file1'])




	##########my calc

	if   refinement_program=='buster':        my_table=['file','HypSeq','refine2_R','refine2_Rfree','refine2_CCmc','refine2_CCsc']#,'refine2_RSCCmc_mean','refine2_RSCCsc_mean','refine2_CCmc','refine2_CCsc']
	else:                                     my_table=['file','HypSeq','refine1_R','refine1_Rfree']
	if edstats_path != False:
		if refinement_program == 'buster':
			i='2'
		else:                              
			i='1'
			my_table.append('refine'+i+'_RSCCmc_mean')
			my_table.append('refine'+i+'_RSCCsc_mean')

	if refinement_program=='phenix.refine':
		my_table.append('refine1_LLGnorm')
		my_table.append('refine1_LLGwork')
		my_table.append('refine1_LLGfree')
	#else:                                     my_table=['file','HypSeq','refine1_R','refine1_Rfree','refine1_RSCCmc_mean','refine1_RSCCsc_mean']#,'refine1_myFOM','refine1_FOM',


	if post_mortem:
		my_table.append('refine1_cwMPE')
		if expand_from_map:                                  my_table.append('refine1_mwMPE')
		if refinement_program=='buster' and expand_from_map: my_table.append('refine2_mwMPE')

	my_table.append('assigned_res_int')
	my_table.append('refine1_LLG')
	my_table.append('refine1_ZLLG')

	if post_mortem:
		# if MtzMtzCC_path != False:
		#     for i in listrefines:
		#         my_table.append('refine'+i+'_CCiA')
		#         my_table.append('refine'+i+'_CCfA')
		my_table.append('#IdRes')
		my_table.append('refine1_Ident%')

	for DicChResNEval in ListCategoriesRun:
		strfolder,_ = LibSLIDER.convertDicChResNStr(DicChResNEval)
		table1=output_folder + '/' + strfolder + '/Table_refine1_'+strfolder+'.log'
		list_dic=[]
		# If postmortem on, then hydpho and lowrot will be automatically generated for the most correct sequence
		for dic in list_dics_all_files:
			if dic['EvalChResn'] == DicChResNEval : list_dic.append(dic)
		list_dic.append(list_dics_all_files[-1])
		LibSLIDER.write_table_from_list_dict_and_keys_sorted_by (my_table,list_dic,'refine1_LLG',True,table1)


	if number_shelxe_trials>0:
		#EXPANSION OF MODELS BY ListCategoriesRun CHOSEN EVALUATIONS
		print('\nSHELXE expansion with line:',shelxe_line)
		pushexp = []
		for DicChResNEval in ListCategoriesRun:
			varpushexp = []
			for dic in list_dics_all_files:
				if dic['EvalChResn'] == DicChResNEval and dic['file'].startswith('seq'): varpushexp.append(dic)
			varpushexp=sorted(varpushexp, key=lambda item: item['refine1_LLG'], reverse=True)
			if len(varpushexp)<number_shelxe_trials:
				print('Number of chosen shelxe trials',number_shelxe_trials,'reduced to',len(varpushexp),'to adequate number of generated hypotheses')
				number_shelxe_trials=len(varpushexp)
			for i in range (number_shelxe_trials): pushexp.append(varpushexp[i])

		#add poly and rdm to be expanded -> complete 1YZF calcations
		for dic in list_dics_all_files:
			if dic not in pushexp and len(pushexp)>0 and (dic['file'].startswith('pol') or dic['file'].startswith('rdm') or dic['file'].startswith('hydpho') or dic['file'].startswith('lowrot')): pushexp.append(dic)

		#add initial  or dic['file'].startswith('initial')
		pushexp.append(list_dics_all_files[-1])

		aaa=''
		for dic in pushexp:
			aaa+=dic['file']+' '

		list_files = [[], []]

		aux_dic = sorted(pushexp, key=lambda x: x['PATH'])

		for dic in aux_dic:
			list_files[0].append(dic['refine_file1_lst'][:-3] + 'pda')
			if expand_from_map:
				list_files[1].append(dic['refine_file1_map_lst'][:-3] + 'phi')

		count_files = 0
		dic_names ={}
		for lfiles in list_files:
			input_directory = ''
			counter = 0
			aux_input_list = []
			for file in lfiles:
				count_files += 1
				if not os.path.isfile(file[:-3]+'pdb'):
					print('Model selected for expansion:',file)
					input_list = [file, file[:-3] + 'hkl']
					if file.endswith('phi'):
						input_list.append(file[:-3] + 'ins')
					if post_mortem:
						input_list.append(file[:-3] + 'ent')
						if shelxe_path.endswith('magic'):
							input_list.append(file[:-3] + 'fcf')
					if distribute_computing=='multiprocessing':
						input_directory = file[:file.rindex('/')]
						if nproc[0] > -1:
							while 1:
								time.sleep(0.01)
								if len(multiprocessing.active_children()) < nproc[0]:
									process_shelxe = multiprocessing.Process(target= LibSLIDER.create_job_shelxe, args=(input_list, shelxe_path, shelxe_line, distribute_computing, input_directory))
									process_shelxe.start()
									time.sleep(0.1)
									break
					else:
						aux_directory = os.path.dirname(file)
						if input_directory != aux_directory:
							if input_directory != '':
								LibSLIDER.create_job_shelxe(aux_input_list, shelxe_path, shelxe_line, distribute_computing, input_directory, cm , nameJob, counter)
							input_directory = aux_directory
							counter = 0
						aux_input_list = input_list
						for element in aux_input_list:
							oldext = os.path.splitext(element)[1]
							if file.endswith('phi'):
								oldext = '-map'+oldext
							LibSLIDER.create_symlink(element, str(counter)+oldext)
							if oldext == '-map.phi':
								dic_names[element] = str(counter)+'-map.pdb'
							elif oldext == '.pda':
								dic_names[element] = str(counter)+'.pdb'
		
						counter += 1
				else:
					print('Model already expanded:',file[:-3]+'pdb')

			if not distribute_computing=='multiprocessing':
				if counter > 0:
					LibSLIDER.create_job_shelxe(aux_input_list, shelxe_path, shelxe_line, distribute_computing, input_directory, cm , nameJob, counter)
				
		while 1:
			if len(multiprocessing.active_children()) == 0: 
				break
			else:
				time.sleep(5)

		if not distribute_computing=='multiprocessing':
			SystemUtility.close_connection(DicGridConn,DicParameters,cm)

		#CONDITION TO WAIT ALL PROCESSES TO BE FINISHED
		count=0
		while count<count_files:
			count=0

			if not distribute_computing=='multiprocessing':
				for key, value in list(dic_names.items()):
					pdb_file = os.path.join(os.path.dirname(key),value)
					lst_file = os.path.join(os.path.dirname(key),value[:-3]+'lst')
					#print(pdb_file)
					#print(lst_file)
					#print(key[:-3]+'pdb')
					#cprint(key[:-3]+'lst')
					if os.path.isfile(pdb_file) and os.path.isfile(lst_file):
						os.rename(pdb_file,key[:-3]+'pdb')
						os.rename(lst_file,key[:-3]+'lst')
						del dic_names[key]

			for dic in pushexp:
				if os.path.isfile( dic['refine_file1_lst'][:-3] + 'pdb' ) and os.path.isfile( dic['refine_file1_lst'][:-3] + 'lst' ):
					count+=1
				if expand_from_map and os.path.isfile(dic['refine_file1_map_lst'][:-3] +'pdb') and os.path.isfile(dic['refine_file1_map_lst'][:-3] +'lst'):
					count+=1

			if count<count_files: 
				time.sleep(10)

		for dic in pushexp:
			lfiles = [dic['refine_file1_lst'][:-3] + 'pdb']
			if expand_from_map:
				lfiles.append(dic['refine_file1_map_lst'][:-3] + 'pdb')
			for i,file in enumerate(lfiles):
				i = str(i)
				if os.path.isfile(file):
					dic['CC'+i],dic['wMPE'+i],dic['cycle'+i],dic['nres'+i],dic['nchains'+i] = LibSLIDER.ReturnShelxeCCwMPEPdbLlst ( file,file[:-3]+'lst' )
				elif os.path.isfile(file[:-3]+'lst'): 
					dic['CC'+i],dic['wMPE'+i],dic['cycle'+i],dic['nres'+i],dic['nchains'+i] = 'n/a','n/a','n/a','n/a','n/a'


		if refinement_program=='buster':
			my_table=['file','HypSeq','refine2_R','refine2_Rfree']#,'refine2_RSCCmc_mean','refine2_RSCCsc_mean','refine2_CCmc','refine2_CCsc']
		else:
			my_table=['file','HypSeq','refine1_R','refine1_Rfree']#,'refine1_RSCCmc_mean','refine1_RSCCsc_mean']#,'refine1_myFOM','refine1_FOM',
		if post_mortem:
			# my_table.append('refine1_CCiA')
			# my_table.append('refine1_CCfA')
			my_table.append('refine1_cwMPE')
			if expand_from_map:
				my_table.append('refine1_mwMPE')

		my_table.append('assigned_res_int')
		#my_table.append('energy')
		my_table.append('refine1_LLG')
		my_table.append('refine1_ZLLG')

		ic=1
		if expand_from_map:              ic+=1

		for i in range(ic):
			i=str(i)
			my_table.append('CC'+i)
			my_table.append('wMPE'+i)
			my_table.append('cycle'+i)
			my_table.append('nres'+i)
			my_table.append('nchains'+i)

		if post_mortem:
			my_table.append('#IdRes')
			#my_table.append('identity_eval')
			my_table.append('refine1_Ident%')


		for DicChResNEval in ListCategoriesRun:
			strfolder,_ = LibSLIDER.convertDicChResNStr(DicChResNEval)
			table2=output_folder + '/' + strfolder + '/Table_expansion_'+strfolder+'.log'

			listdictable = []
			for dic in pushexp:
				if dic['EvalChResn'] == DicChResNEval: listdictable.append(dic)
			#for i in listdictable[0]: print(i)
			LibSLIDER.write_table_from_list_dict_and_keys_sorted_by (my_table,listdictable,'refine1_LLG',True,table2)
			print('\n\nOutput expansion summary on',table2)

	########################LLG NEW

	#print('\n\n\n!!!HERE!!!\n\n\n')

	if LLG_testing:

		if RemoteHomologous: DicChResNRangeS=dict(DicChResNRangeSeq)
		if sliding_by_ss:    DicChResNRangeS=dict(DicChResnRangeSecStrbySecStr)

		#print DicChResNRangeS

		countFrags=0
		for ch in DicChResNRangeS: countFrags+=len(DicChResNRangeS[ch])

		if countFrags>1:
			folderLLG = output_folder + '/initial/LLG'
			LibSLIDER.mkdir(folderLLG)
			if not os.path.isdir(folderLLG): 
				os.mkdir(folderLLG)

			if not os.path.isfile(folderLLG+'/initial_phaser.log'): LibSLIDER.calculate_LLG (
				output_folder, pdbcl, mtz, SpaceGroup, I_SLIDER, SIGI_SLIDER, Amplitudes, HighRes, MW, NC,
				'1.0', folderLLG+'/initial_phaser.sh', folderLLG+'/initial_phaser.log')
			vrmsi = LibSLIDER.return_VRMS(folderLLG + '/initial_phaser.log')
			LLG0 = LibSLIDER.return_LLG (folderLLG + '/initial_phaser.log')

			with open(pdbcl) as fr:
				frl=fr.readlines()
				for ch in DicChResNRangeS:
					for resrange in DicChResNRangeS[ch]:
						idash=resrange.index('-')
						ires=resrange[:idash]
						fres=resrange[idash+1:]
						lresrange = list(range(int(ires),int(fres)+1))

						ff=folderLLG+'/initial_no'+ch+resrange+'.pdb'
						fw=open(ff,'w')

						for l in frl:
							if l.startswith('CRYST') or l.startswith('SCALE') or l.startswith('END'):
								fw.write(l)
							elif l.startswith('ATOM') and (l[21]!=ch or (l[21]==ch and int(l[22:26]) not in lresrange )):
								fw.write(l)

						fw.close()
						# print ch,ires,fres
						# print ff

						PDB_input_file=ff
						for i in range(2):
							if i == 0: PDB_sh_file_log=PDB_input_file[:-4]+'_phaser.log'
							if i == 1: PDB_sh_file_log=PDB_input_file[:-4]+'fix_phaser.log'
							PDB_sh_file=PDB_sh_file_log[:-3]+'sh'

							if i == 0: vrmsb = True
							if i == 1: vrmsb = False

							if not os.path.isfile(PDB_sh_file_log):
								if nproc[0] > -1:  # NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
									#                    print "I found ", sym.REALPROCESSES, "CPUs." #NOTE: REALPROCESSES es el numero de cores de tu ordenador
									while 1:
										time.sleep(0.1)
										if len(multiprocessing.active_children()) < nproc[0]:
											process_phaser = multiprocessing.Process(target=LibSLIDER.calculate_LLG, args=(
											output_folder, PDB_input_file, mtz, SpaceGroup, I_SLIDER, SIGI_SLIDER, Amplitudes, HighRes, MW, NC,
											vrmsi, PDB_sh_file, PDB_sh_file_log,vrmsb))
											process_phaser.start()
											time.sleep(0.1)
											break
								else:
									print("FATAL ERROR: I cannot load correctly information of CPUs.")
									sys.exit(1)

			# CONDITION TO WAIT ALL PROCESSES TO BE FINISHED
			while 1:
				if len(multiprocessing.active_children()) == 0:
					break
				else:
					time.sleep(0.1)

			print('LLG0', LLG0,'\n')

			for ch in DicChResNRangeS:
				for resrange in DicChResNRangeS[ch]:
					DicChResNRangeS[ch][resrange]={}
					DicChResNRangeS[ch][resrange]['LLG0']=LibSLIDER.return_LLG (folderLLG+'/initial_no'+ch+resrange+'_phaser.log')
					DicChResNRangeS[ch][resrange]['LLG+']=LLG0-DicChResNRangeS[ch][resrange]['LLG0']
					DicChResNRangeS[ch][resrange]['LLG0fix']=LibSLIDER.return_LLG (folderLLG+'/initial_no'+ch+resrange+'fix_phaser.log')
					DicChResNRangeS[ch][resrange]['LLG+fix']=LLG0-DicChResNRangeS[ch][resrange]['LLG0fix']
					#print ch, resrange, 'LLG0', DicChResNRangeS[ch][resrange]['LLG0'], 'fix' , DicChResNRangeS[ch][resrange]['LLG0fix']
					print(ch, resrange, 'LLG+', DicChResNRangeS[ch][resrange]['LLG+'], 'fix' , DicChResNRangeS[ch][resrange]['LLG+fix'])

	#### NEW TRIAL PHASER

		dictest={}
		for ch in DicChResNResType:
			dictest[ch]=[]
			#print DicChResNResType[ch]
			for i in DicChResNResType[ch]:
				dictest[ch].append(i)

		for DicChResNEval in ListCategoriesRun:
			strfolder,_ = LibSLIDER.convertDicChResNStr(DicChResNEval)
			LLGfolder= output_folder + '/' + strfolder + '/' + '4_LLG'
			LLGfolderfix= output_folder + '/' + strfolder + '/' + '5_LLGfix'
			if not os.path.isdir(LLGfolder): 
				os.mkdir(LLGfolder)
			if not os.path.isdir(LLGfolderfix): 
				os.mkdir(LLGfolderfix)


		for dic in list_dics_all_files:
			#print dic['EvalChResn'] , dic['file']
			if not dic['PATH'].endswith('initial'):
				PDB_input_file1 = dic['refine_file1']
				if '_' in dic['file']: filein=dic['file'][:dic['file'].index('_')]
				else:                  filein=dic['file']
				strfolder,_ = LibSLIDER.convertDicChResNStr(dic['EvalChResn'])
				LLGfolder= output_folder + '/' + strfolder + '/' + '4_LLG'
				PDB_sh_file1=LLGfolder+'/'+filein+'_phaser.sh'
				PDB_sh_file_log1=PDB_sh_file1[:-2]+'log'

				PDB_input_file2 =LLGfolder+'/'+ filein +'_no'+dic['file'][dic['file'].index('_'):]+'.pdb'
				PDB_sh_file2=PDB_input_file2[:-4]+'_phaser.sh'
				PDB_sh_file_log2=PDB_sh_file2[:-2]+'log'

				if dictest != dic['EvalChResn']:
					with open(PDB_input_file1) as fr:
						fr2 = fr.readlines()
						#print fr2
						if not os.path.isfile(PDB_input_file2):
							fw = open(PDB_input_file2, 'w')
							for l in fr2:
								if l.startswith('CRYST') or l.startswith('SCALE') or l.startswith('END'):
									fw.write(l)
								elif l.startswith('ATOM') and ( l[21] not in dic['EvalChResn'] or ( l[21] in dic['EvalChResn'] and int(l[22:26]) not in dic['EvalChResn'][l[21]] ) ):
									fw.write(l)
								#elif l.startswith('TER') and  ( l[21] not in dic['EvalChResn'] or ( l[21] in dic['EvalChResn'] and int(l[22:26]) not in dic['EvalChResn'][l[21]] ) ):
								#    fw.write(l)
								#else: print 'excluded',l[:-1]
							fw.close()
						#print 'PDB_input_file2', PDB_input_file2

		#exit()
				for i in range(4):
					if i==0:   PDB_sh_file , PDB_sh_file_log , PDB_input_file , vrmsb = PDB_sh_file1 , PDB_sh_file_log1 , PDB_input_file1 , True
					elif i==1: PDB_sh_file , PDB_sh_file_log , PDB_input_file , vrmsb = PDB_sh_file2 , PDB_sh_file_log2 , PDB_input_file2 , True
					elif i==2: PDB_sh_file , PDB_sh_file_log , PDB_input_file , vrmsb = PDB_sh_file1.replace('4_LLG','5_LLGfix') , PDB_sh_file_log1.replace('4_LLG','5_LLGfix') , PDB_input_file1 , False
					elif i==3: PDB_sh_file , PDB_sh_file_log , PDB_input_file , vrmsb = PDB_sh_file2.replace('4_LLG','5_LLGfix') , PDB_sh_file_log2.replace('4_LLG','5_LLGfix') , PDB_input_file2 , False

					if not os.path.isfile( PDB_sh_file_log ) and os.path.isfile(PDB_input_file):
						if  nproc[0] > -1: #NOTE: PROCESSES es el numero de cores que quieres lanzar, default == numero de cores-1
					#                    print "I found ", sym.REALPROCESSES, "CPUs." #NOTE: REALPROCESSES es el numero de cores de tu ordenador
							while 1:
								time.sleep(0.1)
								if len(multiprocessing.active_children()) < nproc[0]:
									process_phaser = multiprocessing.Process(target=LibSLIDER.calculate_LLG, args=(output_folder, PDB_input_file,  mtz,  SpaceGroup, I_SLIDER, SIGI_SLIDER, Amplitudes,HighRes, MW , NC , vrmsi , PDB_sh_file, PDB_sh_file_log , vrmsb ) )
									process_phaser.start()
									time.sleep(0.1)
									break
						else:
							 print("FATAL ERROR: I cannot load correctly information of CPUs.")
							 sys.exit(1)

		# CONDITION TO WAIT ALL PROCESSES TO BE FINISHED
		while 1:
			if len(multiprocessing.active_children()) == 0: 
				break
			else:                                           
				time.sleep(0.1)

		for dic in list_dics_all_files:
			if not dic['PATH'].endswith('initial'):
				filein = dic['file'][:dic['file'].index('_')]
				strfolder,_ = LibSLIDER.convertDicChResNStr(dic['EvalChResn'])
				LLGfolder = output_folder + '/' + strfolder + '/' + '4_LLG'

				PDB_sh_file_log1 = LLGfolder + '/' + filein + '_phaser.log'
				PDB_sh_file_log2 = LLGfolder + '/' + filein + '_no' + dic['file'][dic['file'].index('_'):] + '_phaser.log'
				PDB_sh_file_log3 = PDB_sh_file_log1.replace('4_LLG','5_LLGfix')
				PDB_sh_file_log4 = PDB_sh_file_log2.replace('4_LLG','5_LLGfix')

				if os.path.isfile(PDB_sh_file_log1) : dic['LLG0']    = LibSLIDER.return_LLG(phaser_log_file=PDB_sh_file_log1)
				if os.path.isfile(PDB_sh_file_log2):  dic['LLG-']    = LibSLIDER.return_LLG(phaser_log_file=PDB_sh_file_log2)
				if os.path.isfile(PDB_sh_file_log2):  dic['LLG+']    = dic['LLG0']    - dic['LLG-']

				if os.path.isfile(PDB_sh_file_log3) : dic['LLG0fix'] = LibSLIDER.return_LLG(phaser_log_file=PDB_sh_file_log3)
				if os.path.isfile(PDB_sh_file_log4):  dic['LLG-fix'] = LibSLIDER.return_LLG(phaser_log_file=PDB_sh_file_log4)
				if os.path.isfile(PDB_sh_file_log4):  dic['LLG+fix'] = dic['LLG0fix'] - dic['LLG-fix']

		#CALCULATION OF ZLLG OF SEQ
		for DicChResNEval in ListCategoriesRun:
			listLLG=[]
			listLLGplus = []
			listLLGfix=[]
			listLLGplusfix = []
			for dic in list_dics_all_files:
				if 'seq' in dic['file'] and dic['EvalChResn'] == DicChResNEval:
					listLLG.append(dic['LLG0'])
					listLLGfix.append(dic['LLG0fix'])
					if 'LLG+' in dic:    listLLGplus.append(dic['LLG+'])
					if 'LLG+fix' in dic: listLLGplusfix.append(dic['LLG+fix'])

			meanvarLLG=numpy.mean(listLLG)
			stdevvarLLG=numpy.std(listLLG)
			meanvarLLGfix=numpy.mean(listLLGfix)
			stdevvarLLGfix=numpy.std(listLLGfix)

			if len(listLLGplus)>0:
				meanvarLLGplus     = numpy.mean(listLLGplus)
				stdevvarLLGplus    = numpy.std(listLLGplus)
				meanvarLLGplusfix  = numpy.mean(listLLGplusfix)
				stdevvarLLGplusfix = numpy.std(listLLGplusfix)

			for dic in list_dics_all_files:
				if dic['EvalChResn'] == DicChResNEval and 'seq' in dic['file']:
					dic['ZLLG0']                         = (dic['LLG0']    - meanvarLLG)        / stdevvarLLG
					dic['ZLLG0fix']                      = (dic['LLG0fix'] - meanvarLLGfix)     / stdevvarLLGfix
					if 'LLG+' in dic:    dic['ZLLG+']    = (dic['LLG+']    - meanvarLLGplus)    / stdevvarLLGplus
					if 'LLG+fix' in dic: dic['ZLLG+fix'] = (dic['LLG+fix'] - meanvarLLGplusfix) / stdevvarLLGplusfix

					#print dic['file'],'ZLLG0',dic['ZLLG0'],'ZLLG0fix',dic['ZLLG0fix'],'ZLLG+',dic['ZLLG+'],'ZLLG+fix',dic['ZLLG+fix']

		for dic in list_dics_all_files:
			if 'ZLLG0' not in dic:                                       dic['ZLLG0'] , dic['ZLLG0fix'] = 'n/a' , 'n/a'
			if dictest != dic['EvalChResn'] and 'ZLLG+' not in dic:      dic['ZLLG+'] , dic['ZLLG+fix'] = 'n/a' , 'n/a'
			if 'LLG0' not in dic:                                        dic['LLG0'] , dic['LLG0fix'] , dic['LLG+'] , dic['LLG+fix'] , dic['ZLLG0'] , dic['ZLLG0fix'] , dic['ZLLG+'] , dic['ZLLG+fix'] = LLG0 , 'n/a' , 'n/a' , 'n/a' , 'n/a' , 'n/a' , 'n/a' , 'n/a'

		my_table=['file','HypSeq','LLG0','ZLLG0']
		if 'LLG+' in list_dics_all_files[0]:
			my_table.append('LLG+')
			my_table.append('ZLLG+')
		my_table.append('LLG0fix')
		my_table.append('ZLLG0fix')
		if 'LLG+fix' in list_dics_all_files[0]:
			my_table.append('LLG+fix')
			my_table.append('ZLLG+fix')
		if post_mortem:
			my_table.append('refine1_cwMPE')
			my_table.append('#IdRes')
			#my_table.append('identity_eval')
			my_table.append('refine1_Ident%')


		for DicChResNEval in ListCategoriesRun:
			strfolder,_ = LibSLIDER.convertDicChResNStr(DicChResNEval)
			table2=output_folder + '/' + strfolder + '/Table_LLG_'+strfolder+'.log'

			listdictable = []
			for dic in list_dics_all_files:
				if dic['EvalChResn'] == DicChResNEval:
					listdictable.append(dic)
			LibSLIDER.write_table_from_list_dict_and_keys_sorted_by (my_table,listdictable,'LLG0',True,table2)
			print('\n\nOutput LLG summary on',table2)


		my_table=['file','HypSeq','LLG0','ZLLG0']
		if 'LLG+' in list_dics_all_files[0]:
			my_table.append('LLG+')
			my_table.append('ZLLG+')
		my_table.append('LLG0fix')
		my_table.append('ZLLG0fix')
		if 'LLG+fix' in list_dics_all_files[0]:
			my_table.append('LLG+fix')
			my_table.append('ZLLG+fix')
		if post_mortem:
			my_table.append('refine1_cwMPE')
			my_table.append('#IdRes')
			#my_table.append('identity_eval')
			my_table.append('refine1_Ident%')


		for DicChResNEval in ListCategoriesRun:
			strfolder,_ = LibSLIDER.convertDicChResNStr(DicChResNEval)
			table2=output_folder + '/' + strfolder + '/Table_LLG_'+strfolder+'.log'

			listdictable = []
			for dic in list_dics_all_files:
				if dic['EvalChResn'] ==DicChResNEval:
					listdictable.append(dic)
			LibSLIDER.write_table_from_list_dict_and_keys_sorted_by (my_table,listdictable,'LLG0',True,table2)
			print('\n\nOutput LLG summary on',table2)

	if refinement_program == 'buster':
		my_table = ['file', 'HypSeq', 'refine2_R', 'refine2_Rfree']#, 'refine2_RSCCmc_mean', 'refine2_RSCCsc_mean', 'refine2_CCmc', 'refine2_CCsc']
	else:
		my_table = ['file', 'HypSeq', 'refine1_R', 'refine1_Rfree']#, 'refine1_RSCCmc_mean', 'refine1_RSCCsc_mean']  # ,'refine1_myFOM','refine1_FOM',

	my_table.append('refine1_LLG')
	my_table.append('refine1_ZLLG')

	if post_mortem:
		my_table.append('refine1_cwMPE')
		if expand_from_map:
			my_table.append('refine1_mwMPE')

		# my_table.append('assigned_res_int')
		# if refinement_program == 'buster': my_table.append('LLG+fix')
		# if refinement_program == 'buster': my_table.append('ZLLG+fix')

		# if MtzMtzCC_path != False:
		#     if refinement_program == 'buster': my_table.append('refine2_CCfA')
		#     else:                              my_table.append('refine1_CCfA')
		#my_table.append('#IdRes')
		my_table.append('refine1_Ident%')


	for DicChResNEval in ListCategoriesRun:
		strfolder,_ = LibSLIDER.convertDicChResNStr(DicChResNEval)
		table1 = output_folder + '/' + strfolder + '/Table_NEW_' + strfolder + '.log'
		list_dic = []
		# If postmortem on, then hydpho and lowrot will be automatically generated for the most correct sequence
		for dic in list_dics_all_files:
			if dic['EvalChResn'] == DicChResNEval and not dic['file'].startswith('initial'):
				list_dic.append(dic)
		list_dic.append(list_dics_all_files[-1])
		LibSLIDER.write_table_from_list_dict_and_keys_sorted_by(my_table, list_dic, 'refine1_LLG', True, table1)

		print('\n\nOutput NEW summary on',table1)

	LibSLIDER.write_xml_output(nameJob, output_folder, list_dics_all_files, post_mortem , refinement_program, expand_from_map, ListCategoriesRun)

	####NEW ENERGY TABLE!!!

	# my_table = ['file', 'HypSeq', 'energy','refine1_LLG','refine1_ZLLG']

	# if post_mortem:
	# 	my_table.append('refine1_cwMPE')
	# 	if expand_from_map:
	# 		my_table.append('refine1_mwMPE')

	# 	# my_table.append('assigned_res_int')
	# 	# if refinement_program == 'buster': my_table.append('LLG+fix')
	# 	# if refinement_program == 'buster': my_table.append('ZLLG+fix')

	# 	# if MtzMtzCC_path != False:
	# 	#     if refinement_program == 'buster': my_table.append('refine2_CCfA')
	# 	#     else:                              my_table.append('refine1_CCfA')
	# 	#my_table.append('#IdRes')
	# 	my_table.append('refine1_Ident%')


	# for DicChResNEval in ListCategoriesRun:
	# 	strfolder = LibSLIDER.convertDicChResNStr(DicChResNEval)
	# 	table1 = output_folder + '/' + strfolder + '/Table_energy_NEW_' + strfolder + '.log'
	# 	list_dic = []
	# 	# If postmortem on, then hydpho and lowrot will be automatically generated for the most correct sequence
	# 	for dic in list_dics_all_files:
	# 		if dic['EvalChResn'] == DicChResNEval and not dic['file'].startswith('initial'):
	# 			list_dic.append(dic)
	# 	list_dic.append(list_dics_all_files[-1])
	# 	LibSLIDER.write_table_from_list_dict_and_keys_sorted_by(my_table, list_dic, 'refine1_LLG', True, table1)

		#print('\n\nOutput energy NEW summary on',table1)

def main():

	head1 = """
				.---------------------------------------------.
				|   _____ _      _____ _____  ______ _____    |
				|  / ____| |    |_   _|  __ \|  ____|  __ \   |
				| | (___ | |      | | | |  | | |__  | |__) |  |
				|  \___ \| |      | | | |  | |  __| |  _  /   |
				|  ____) | |____ _| |_| |__| | |____| | \ \   |
				| |_____/|______|_____|_____/|______|_|  \_\  |
				#---------------------------------------------#
				   Requires Phaser >= 2.8.x and Shelxe 2019
	"""
	print(colored(head1, 'cyan'))
	print("""
	Institut de Biologia Molecular de Barcelona --- Consejo Superior de Investigaciones Científicas
			I.B.M.B.                                            C.S.I.C.
		Department of Structural Biology - “María de Maeztu” Unit of Excellence
					Crystallographic Methods Group
			http://www.sbu.csic.es/research-groups/crystallographic-methods/
		""")

	print("Email support: ", colored("bugs-borges@ibmb.csic.es", 'blue'))
	print("\n")
	usage = """usage: %prog example.bor"""
	parser = OptionParser(usage=usage)
	parser.add_option("-b", "--borconf", action="store_true", dest="borconf",
		help="Print customizable parameters for users", default=False)

	(options, args) = parser.parse_args()

	if options.borconf:
		print(colored("""#""", 'blue') + colored('NOTE', 'yellow') + colored(
			""": for a full documentation of the parameters, please read the manual at: """, 'blue') + colored(
			""" http://chango.ibmb.csic.es/manual""", 'red'))

		print(colored("""#""", 'blue') + colored('NOTE', 'yellow') + colored(
			""": For optional parameters default values are quoted.""", 'blue'))
		print(colored("""#Tutorial can be found in the website.""", 'blue'))
		print("""
[CONNECTION]:
		""")
		print(colored("""#""", 'blue') + colored('\tNOTE', 'yellow') + colored(': following is default', 'blue'),)
		print("""
distribute_computing: multiprocessing
		""")
		print(colored("""#""", 'blue') + colored('\tNOTE', 'yellow') + colored(': other modes are:', 'blue'),)
		print(colored("""
#distribute_computing: local_grid
#setup_bor_path: /path/to/setup.bor
		""", 'blue'))
		print(colored("""#""", 'blue') + colored('\tNOTE', 'yellow') + colored(
			': if the RSA private key is not found or invalid, a password is required', 'blue'),)
		print(colored("""
#distribute_computing: remote_grid
#setup_bor_path: /path/to/setup.bor
#remote_frontend_passkey: ~/.ssh/id_rsa
		""", 'blue'),)
		print("""
[GENERAL]:
		""")
		print(colored("""#""", 'blue') + colored('\tNOTE', 'yellow') + colored(': following are mandatory', 'blue'),)
		print("""
working_directory= /path/to/workdir
mtz_path: %(working_directory)s/data.mtz
hkl_path: %(working_directory)s/data.hkl
pdb_path: %(working_directory)s/data.pdb
#ent_path: %(working_directory)s/structure.ent

[SLIDER]
#name_job:
shelxe_line:
f_label:
sigf_label:
molecular_weight:
number_of_component:
#coiled_coil: 0
#For Remote Homolog Mode
align_path: /path/to/file.pir
#For Secondary Structure Mode
seq_path: /path/to/file.seq
secstr_path: /path/to/file.psipass2
#sspdb_path
#nproc
#i_label:
#sigi_label:
rfree_label:
#sliding_tolerance: 3
#size_frag_tolerance: 0
#minimum_ss_frag: 5
#psipred_confidence_level: 0
#psipred_min_frag_size: 4
#trust_loop = 0
#use_coot = 0
#models_by_chain:  100
#maximum 3000
#seq_pushed_refinement: 100
#maximum 1000
#chosen_chains: A,B
#For chains A and B NCS related (required to be identical)
#chosen_chains: A;B
#For chains A and B not NCS related (required to be identical)
#ncschains = 0
#fixed_residues_modelled: A:1-10,20-30 B:1-5,30-35
#fixed_residues_notmodelled: A:1-10,20-30 B:1-5,30-35
#RandomModels: 0
#RandomOnlyEvalSequence: 0
#number_shelxe_trials: 15
#ModelEdge: 0
#ReduceComplexity: 0
#Recover0occup: 0
expand_from_map: False
refinement_program: buster
refinement_program: refmac
#PhenixRefineParameters: strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body ramachandran_restraints=True main.number_of_macro_cycles=0 write_eff_file=false write_geo_file=false write_def_file=false optimize_xyz_weight=False optimize_adp_weight=False secondary_structure.enabled=True export_final_f_model=true simulated_annealing=false
#refmac_parameters_path#: path/path.tmp
#buster_parameters:  -noWAT -nbig 1 -RB -nthread 1 UsePdbchk="no"
		""")
		print("""
[LOCAL]
""",)
		print(colored("""#Third party software paths """, 'blue'),)
		print("""
path_local_phaser:
path_local_shelxe:
#path_local_edstats:
#path_local_sprout
#path_local_coot
""")
		print(colored("""#""", 'blue') + colored('\tNOTE', 'yellow') + colored(': If refinement program is buster:', 'blue'),)
		print("""
path_local_buster:
#path_config_buster
		""")
		print(colored("""#""", 'blue') + colored('\tNOTE', 'yellow') + colored(': If refinement program is phenix.refine:', 'blue'),)
		print("""
path_local_phenix.refine:
#path_config_phenix:
		""")
		print(colored("""#""", 'blue') + colored('\tNOTE', 'yellow') + colored(': If refinement program is refmac:', 'blue'),)
		print("""
path_local_refmac:
#path_config_ccp4
		""")

	if len(args) < 1:
		parser.print_help()
		sys.exit(0)

	input_bor = os.path.abspath(args[0])
	if not os.path.exists(input_bor):
		print('\n Sorry, the given path for the bor file either does not exist or you do not have the permissions to read it')
		sys.exit(1)
	
	path_module = os.path.dirname(__file__)

	Config = configparser.ConfigParser()

	try:
		startSLIDER(Config, input_bor)
	except SystemExit:
		pass
	except:
		print(traceback.print_exc(file=sys.stdout))

if __name__ == "__main__":
	main()
