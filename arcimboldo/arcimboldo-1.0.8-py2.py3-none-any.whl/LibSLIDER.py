#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import range
from future.utils import iteritems

amino_acid_list=           ['A',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'K',  'L',  'M',  'N',  'P',  'Q',  'R',  'S',  'T',  'V',  'W',  'Y',  'M'  ]
amino_acid_list_3L=        ['ALA','CYS','ASP','GLU','PHE','GLY','HIS','ILE','LYS','LEU','MET','ASN','PRO','GLN','ARG','SER','THR','VAL','TRP','TYR','MSE']
amino_acid_list_numb_atoms=[   5,    6,    8  ,  9  , 11  ,  4  , 10  ,  8  ,  9  ,  8  ,  8  ,  8  ,  7  ,  9  , 11  ,  6  ,  7  ,  7 ,  14 ,  12 , 8   ]

import os
import stat
import numpy
import Bio.PDB
import subprocess
import configparser
import xml.etree.ElementTree as ET
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as MatList
from collections import defaultdict
import re
from six import string_types
import Grid
import sys
import errno
import re
import threading
import arci_output

def extract_protein_chainID_res_number (pdb_input) :
	file=open(pdb_input,'r')
	file_list=file.readlines()
	file.close()
	DicChResNResType={}
	listChResNCA=[]
	chain_ID=[]
	res=[]
	number=0
	res_check = 'FirstOccurrence'
	chain_check=0
	res_string=''
	for line in file_list:
		if line.startswith('ATOM') or (line.startswith('HETATM') and line[17:20]=='MSE'):
			#line2=line.split()
			if line[12:15]==' CA' and [line[21],int(line[22:26])] not in listChResNCA: listChResNCA.append([line[21],int(line[22:26])]) #Constructing a list of lists [ [chain1,resnumb1] , [chain2,resnumb2] ]
			if res_check=='FirstOccurrence':
				res_check=int(line[22:26])
				chain_check=line[21]
				chain_ID.append(chain_check)
				residue=amino_acid_list[ amino_acid_list_3L.index(line[17:20]) ]
				DicChResNResType[chain_check]={res_check:residue}
				res_string=res_string+residue
			else:
				if not res_check==int(line[22:26]):
					if chain_check==line[21]:
						if int(line[22:26])==res_check+1:
							res_check=res_check+1
							residue=amino_acid_list[ amino_acid_list_3L.index(line[17:20]) ]
							DicChResNResType[chain_check][res_check]=residue
							res_string=res_string+residue
						else:
							res_check=int(line[22:26])
							residue=amino_acid_list[ amino_acid_list_3L.index(line[17:20]) ]
							DicChResNResType[chain_check][res_check] = residue
							res_string=res_string+'/'+residue
					else:
						res.append(res_string)
						res_string=''
						chain_check=line[21]
						chain_ID.append(chain_check)
						residue=amino_acid_list[ amino_acid_list_3L.index(line[17:20]) ]
						res_string=residue
						res_check=int(line[22:26])
						if chain_check not in DicChResNResType: DicChResNResType[chain_check] = {res_check: residue}
						else:                                   DicChResNResType[chain_check][res_check]  = residue
	res.append(res_string)
	count=0
	for chain in res:      count=count+len(chain.replace('/',''))
##    print 'verifying fn'
##    print 'chain_ID',chain_ID
##    print 'res',res
##    print 'count',count
	return chain_ID , res , count , DicChResNResType , listChResNCA

def create_job(cm, nameJob, input_directory, mtz, counter, refmac_ins_file):
	job = Grid.gridJob(nameJob)
	job.setExecutable(os.path.join(input_directory, "$(Process).sh"))
	job.setInitialDir(input_directory)
	job.addInputFile(".sh", True)
	job.addInputFile(".pdb", True)
	job.addInputFile(mtz, False)
	if os.path.isfile(refmac_ins_file):
		job.addInputFile(refmac_ins_file, False)
	cm.setRank("kflops")
	cm.submitJobs(job, counter)

def create_job_multiprocessing(sh_file):
	p = subprocess.Popen(['nohup','/bin/bash',sh_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()

def create_job_shelxe(list_files_input , executable , argums , distribute_computing, input_directory = '' , cm = '', nameJob = '', counter = 0, log_name = ''):
	if distribute_computing == 'multiprocessing':
		file_name=list_files_input[0][list_files_input[0].rindex('/')+1:]
		argums=file_name+' '+argums
		argums=argums.split()
		p = subprocess.Popen([executable]+argums, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=input_directory )
		out, err = p.communicate()
	else:
		if os.path.splitext(list_files_input[0])[1] == '.pda':
			argums='$(Process).pda '+argums
		else:
			argums='$(Process)-map.phi '+argums
		argums=argums.split()

		job = Grid.gridJob(nameJob)
		job.setExecutable(executable)
		for file in list_files_input:
			if os.path.splitext(list_files_input[0])[1] == '.phi':
				job.addInputFile('$(Process)-map'+os.path.splitext(file)[1],False)
			else:
				job.addInputFile('$(Process)'+os.path.splitext(file)[1],False)
		job.setInitialDir(input_directory)
		print(argums)
		job.setArguments(argums)
		out=log_name+'.out'
		err=log_name+'.err'
		job.addOutputFile(out, False)
		job.addOutputFile(err, False)
		cm.setRank("kflops")
		cm.submitJobs(job, counter)

def create_symlink(src, dst):
	try:
		os.symlink(src, os.path.join(os.path.dirname(src), dst))
	except OSError as e:
		if e.errno == errno.EEXIST:
			os.remove(os.path.join(os.path.dirname(src), dst))
			os.symlink(src, os.path.join(os.path.dirname(src), dst))


def create_xml_tree(root, dict_result):
	if type(dict_result) == dict:
		for k, v in iteritems(dict_result):
			create_xml_tree(ET.SubElement(root, re.sub('\W+','',k)), v)
		return root
	else:
		root.text = str(dict_result)

def write_xml_output(name, output_folder, dict_result, post_mortem, refinement_program, expand_from_map, ListCategoriesRun):
	xml_file = os.path.join(output_folder, name+'.xml')
	if os.path.exists(xml_file):
		os.remove(xml_file)
	
	tree_root = ET.Element('slider')

	tree_vars = ET.SubElement(tree_root, 'vars')
	ET.SubElement(tree_vars, 'post_mortem').text = str(post_mortem)
	ET.SubElement(tree_vars, 'refinement_program').text = str(refinement_program)
	ET.SubElement(tree_vars, 'expand_from_map').text = str(expand_from_map)

	tree_data= ET.SubElement(tree_root, 'data')
	for dic in dict_result:
		create_xml_tree(ET.SubElement(tree_data, dic['file']), dic)

	tree_results = ET.SubElement(tree_root, 'results')

	cc1_max = 0
	cc1_file = ''
	cc0_max = 0
	cc0_file = ''
	cc0_list = [e for e in dict_result if 'CC0' in e]
	cc0_list = sorted(cc0_list, key=lambda x: (x['CC0'], x['refine1_LLG']), reverse=True)
	if cc0_list:
		cc0_max = cc0_list[0]['CC0']
		cc0_file = cc0_list[0]['refine_file1_lst']

	if expand_from_map:
		cc1_list = [e for e in dict_result if 'CC1' in e]
		cc1_list = sorted(cc1_list, key=lambda x: (x['CC1'], x['refine1_LLG']), reverse=True)
		if cc1_list:
			cc1_max = cc0_list[0]['CC1']
			cc1_file = cc0_list[0]['refine_file1_map_lst']
	
	if cc0_max >= cc1_max:
		ET.SubElement(tree_vars, 'max_cc').text = str(cc0_max)
		ET.SubElement(tree_vars, 'max_file').text = str(cc0_file[:-3] + 'pdb')
	else:
		ET.SubElement(tree_vars, 'max_cc').text = str(cc1_max)
		ET.SubElement(tree_vars, 'max_file').text = str(cc1_file[:-3] + 'pdb')
		ET.SubElement(tree_vars, 'max_file_map').text = str(cc1_file[:-3] + 'phs')

	for DicChResNEval in ListCategoriesRun:
		_,title = convertDicChResNStr(DicChResNEval)
		tree_dic = ET.SubElement(tree_results, list(DicChResNEval)[0])
		ET.SubElement(tree_dic, 'title').text = title
		aux_dict = [element for element in dict_result if element['EvalChResn'] == DicChResNEval]
		

		values_y = [e['align_score'] for e in aux_dict if 'align_score' in e and 'seq' in e['file']]
		min_value = min(values_y)-min(values_y)*0.10


		if post_mortem:
			values_wmpe0 = [e['wMPE0'] for e in aux_dict if 'CC0' in e and 'wMPE0' in e]
			values_wmpe1 = [e['wMPE1'] for e in aux_dict if 'CC0' in e and 'wMPE1' in e]
			values_cwmpe = [e['refine1_cwMPE'] for e in aux_dict]

			if values_wmpe0:
				ET.SubElement(tree_dic, 'min_wMPE0').text = str(min(values_wmpe0))
				ET.SubElement(tree_dic, 'max_wMPE0').text = str(max(values_wmpe0))
			if values_wmpe1:
				ET.SubElement(tree_dic, 'min_wMPE1').text = str(min(values_wmpe1))
				ET.SubElement(tree_dic, 'max_wMPE1').text = str(max(values_wmpe1))
			if values_cwmpe:
				ET.SubElement(tree_dic, 'min_refine1_cwMPE').text = str(min(values_cwmpe))
				ET.SubElement(tree_dic, 'max_refine1_cwMPE').text = str(max(values_cwmpe))

		for types in ['initial', 'rdm', 'seq', 'polyS']:
			tree_types = ET.SubElement(tree_dic, types)

			types_dict = [e for e in aux_dict if types in e['file']]

			refine1_llg = [e['refine1_LLG'] for e in types_dict]

			ET.SubElement(tree_types, "max_refine1_llg").text = str(max(refine1_llg))

			if post_mortem:
				refine1_cwmpe = [e['refine1_cwMPE'] for e in types_dict]
				refine1_y = [e['refine1_Ident%'] for e in types_dict]
				ET.SubElement(tree_types, "refine1_cwmpe").text = ','.join(map(str, refine1_cwmpe))
			else:

				refine1_y = [e['align_score'] if 'align_score' in e and e['align_score'] != 0 else min_value for e in types_dict]

			ET.SubElement(tree_types, "refine1_llg").text = ','.join(map(str, refine1_llg))
			ET.SubElement(tree_types, "refine1_y").text = ','.join(map(str, refine1_y))

			refine1_cc0 = [e['CC0'] for e in types_dict if 'CC0' in e]
			refine1_cc1 = []

			refine1_llg_cc0 = [e['refine1_LLG'] for e in types_dict if 'CC0' in e and 'refine1_LLG' in e]
			if post_mortem:
				wmpe0 = [e['wMPE0'] for e in types_dict if 'CC0' in e and 'wMPEO' in e]
				ET.SubElement(tree_types, "wmpe0").text = ','.join(map(str, wmpe0))

			ET.SubElement(tree_types, "refine1_llg_cc0").text = ','.join(map(str, refine1_llg_cc0))
			ET.SubElement(tree_types, "refine1_cc0").text = ','.join(map(str, refine1_cc0))

			if expand_from_map:
				refine1_cc1 = [e['CC1'] for e in types_dict if 'CC1' in e]
				refine1_llg_cc1 = [e['refine1_LLG'] for e in types_dict if 'CC1' in e and 'refine1_LLG' in e]
				if post_mortem:
					wmpe1 = [e['wMPE1'] for e in types_dict if 'CC1' in e and 'wMPE1' in e]
					ET.SubElement(tree_types, "wmpe1").text = ','.join(map(str, wmpe1))

				ET.SubElement(tree_types, "refine1_cc1").text = ','.join(map(str, refine1_cc1))
				ET.SubElement(tree_types, "refine1_llg_cc1").text = ','.join(map(str, refine1_llg_cc1))

			ET.SubElement(tree_types, "max_expansions").text = str(max(max(refine1_cc1 or [0]), max(refine1_cc0 or [0])))

	ET.ElementTree(tree_root).write(xml_file)

	lock = threading.RLock()
	lock = threading.Condition(lock)
	arci_output.generateHTML(lock, output_folder, name)


def mtzfix (file_input,file_output,type_refinement_program):
	if not os.path.isfile( file_output ):
		if 'sigmaa' in type_refinement_program or 'sigmaa' in file_input:
			mtzfix_job = subprocess.Popen([ 'mtzfix','FLABEL F SIGF FC PHIC FC_ALL PHIC_ALL 2FOFCWT PH2FOFCWT FOFCWT PHFOFCWT FOM'.split(),'HKLIN',file_input,'HKLOUT',file_output], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			#mtzfix_job = subprocess.Popen([ 'mtzfix','FLABEL F SIGF FC PHIC FC_ALL PHIC_ALL 2FOFCWT PH2FOFCWT FOFCWT PHFOFCWT FOM'.split(),'HKLIN',file_input,'HKLOUT',file_output], stdin=fft_job_instr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		else:
			#mtzfix_job = subprocess.Popen([ 'mtzfix','HKLIN',file_input,'HKLOUT',file_output], stdin=fft_job_instr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			mtzfix_job = subprocess.Popen([ 'mtzfix','HKLIN',file_input,'HKLOUT',file_output], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = mtzfix_job.communicate()
		#print out[-110:]
		if not os.path.isfile( file_output ):
			print("mtzfix did not generate mtzfixfile, previous file",file_input," being used.")
			os.system("cp "+file_input+" "+file_output)
		else:
			print("mtzfix performed correctly in file:",file_input)

def RSZD_calculation (file_mtz, file_pdb , file_out , type_refinement_program , edstats_path ): #script generated ?, upgraded for evaluating coot output mtz in May, 4th 2016
	#type_refinement_program = refmac buster sigmaa (coot)
	file_mtz_fix=file_mtz[:-4]+'_mtzfix.mtz'
	file_map_fo=file_mtz[:-4]+'_fo.map'
	file_map_df=file_mtz[:-4]+'_df.map'
##    print 'mtz to be fixed:',file_mtz_fix
##    print 'map fo:',file_map_fo
##    print 'map fc:',file_map_df
	mtzfix (file_mtz,file_mtz_fix,type_refinement_program)
	#correct mtz through mtzfix line: mtzfix  [FLABEL <string>]  HKLIN in.mtz  HKLOUT out.mtz   [FLABEL <string>]=not necessary
	#generate maps through fft
	#if 'BUSTER' in file_mtz or 'buster' in type_refinement_program or 'sigmaa' in type_refinement_program or 'sigmaa' in file_pdb or 'phenix.refine' in type_refinement_program:
	if type_refinement_program in ['buster','phenix.refine','sigmaa']:
		fft_script ( file_mtz_fix , file_map_fo , '2FOFCWT' , 'PH2FOFCWT' )
		fft_script ( file_mtz_fix , file_map_df , 'FOFCWT' , 'PHFOFCWT' )
	elif type_refinement_program in ['refmac']:
		fft_script ( file_mtz_fix , file_map_fo , 'FWT' , 'PHWT' )
		fft_script ( file_mtz_fix , file_map_df , 'DELFWT' , 'PHDELWT'  )
	# elif 'phenix' in file_mtz or 'phenix' in type_refinement_program:
	#     print 'phenix.refine is under development, it may be advisable to use phenix.model_vs_data'
	#     exit()
	#     fft_script ( file_mtz_fix , file_map_fo , 'FWT' , 'PHWT' )
	#     fft_script ( file_mtz_fix , file_map_df , 'DELFWT' , 'PHDELWT'  )
	else:
		print('Unable to find if mtz file '+file_mtz+' was coming from BUSTER or REFMAC or sigmaa (coot>get-eds-pdb-and-mtz), thus unable to generate edstats .out file')
	#extract resolution from mtz with mtzdmp
	low_res,high_res=extract_resolution_from_mtz(file_mtz)
	#generate out through edstats
	os.system('echo resl=' + low_res + ',resh=' + high_res + ' | '+edstats_path+'  MAPIN1 ' + file_map_fo + ' MAPIN2 ' + file_map_df + '  XYZIN ' + file_pdb + ' OUT ' + file_out + ' > ' + file_out[:-3] +'log')
	os.system('rm '+file_map_fo+' '+file_map_df+' '+file_mtz_fix)

def extract_resolution_from_mtz ( file_input_mtz ):
	os.system('mtzdmp ' + file_input_mtz + ' | grep " *  Resolution Range :" -A2 | grep A > '+file_input_mtz[:-4]+'_res.log')
	b=open(file_input_mtz[:-4]+'_res.log', 'r')
	c=b.read().split()
	b.close()
	low_res=c[3]
	high_res=c[5]
	os.system('rm '+file_input_mtz[:-4]+'_res.log')
	return low_res,high_res

def fft_script ( file_input_mtz , file_output_map , F , PHI ):
	#writting fft_job_description_file
	fft_job_description=open(file_output_map+'_fft_job.txt','w')
	fft_job_description.write('XYZLIM ASU\n')
	fft_job_description.write('GRID SAMPLE 4.5\n')
	fft_job_description.write('LABIN -\n')
	fft_job_description.write('     F1='+F+' PHI='+PHI)
	fft_job_description.write('\nEND')
	fft_job_description.close()
	fft_job_instr=open(file_output_map+'_fft_job.txt', 'r')
	fft_job = subprocess.Popen([ 'fft','HKLIN',file_input_mtz,'MAPOUT',file_output_map], stdin=fft_job_instr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = fft_job.communicate()
	fft_job_instr.close()
	os.system('rm '+file_output_map+'_fft_job.txt')

def add_Bfactors_occup_to_pdb ( pdb_input_file , pdb_output_file , Bf_number_in_string_6characters , occ_number_in_string_3characters=False ): #example Bf_number_in_string_5characters=" 20.00" or "  4.00" and occ_number_in_string_3characters_'1.00' or '0.00'
	if len(Bf_number_in_string_6characters)<6: Bf_number_in_string_6characters=' '*(6-len(Bf_number_in_string_6characters))+Bf_number_in_string_6characters
	with open(pdb_input_file) as f: f2=f.readlines()
	with open(pdb_output_file,'w') as f:
		for line in f2:
			if line.startswith('ATOM'):
				if occ_number_in_string_3characters == False: occ = line[56:60]
				else:                                         occ = occ_number_in_string_3characters
				f.write( line[:56] + occ + Bf_number_in_string_6characters + line[66:] )
			else:f.write(line)
			
def sh_refine_refmac_multiprocesses ( pdb_input_file , mtz_input_file , pdb_output_file , refmac_tmp_file , refmac_path , sh_file , distribute_computing, ccp4_config_path = '' ):
	file_sh=open(sh_file,'w')
##    if distribute_computing=='multiprocessing':
##        file_sh.write('#!/bin/sh'+ '\n')
	if distribute_computing=='local_grid':
		file_sh.write('#!/bin/bash'+ '\n')
		#file_sh.write('source /xtal/xtalsetup'+ '\n')
		#file_sh.write('hostname > '+sh_file.split('/')[-1]+ '_host \n')
		#file_sh.write('source /xtal/ccp4/ccp4/include/ccp4.setup\n') # obsolute after May 10, 2019
		file_sh.write('source '+ccp4_config_path+'\n')  # updated on May  10, 2019

	xyzin=pdb_input_file
	xyzout=pdb_output_file
	hklin=mtz_input_file
	hklout=xyzout[:-4]+'.mtz'
	cifout=xyzout[:-4]+'.cif'
	refmac_output_log = xyzout[:-4]+'.log'
	if distribute_computing=='local_grid':
		xyzin =xyzin.split('/')[-1]
		xyzout=xyzout.split('/')[-1]
		hklin =hklin.split('/')[-1]
		hklout=hklout.split('/')[-1]
		cifout=cifout.split('/')[-1]
		refmac_output_log = refmac_output_log.split('/')[-1]
		refmac_tmp_file=refmac_tmp_file.split('/')[-1]
	#p = subprocess.Popen([refmac_path,'XYZIN',xyzin,'XYZOUT',xyzout,'HKLIN',hklin,'HKLOUT',hklout,'LIBOUT',cifout], stdin=refmacTMP, stdout=refmac_output_log, stderr=subprocess.PIPE)
	#os.system( '/xtal/ccp4/ccp4-6.4.0/bin/refmac5 XYZIN "0_Scwrl4/seq' + str(b) + '.pdb" XYZOUT "1_refmac/seq' + str(b) + '_refmac1.pdb" HKLIN "' + mtz_file + '" HKLOUT "1_refmac/seq' + str(b) + '_refmac1.mtz" LIBOUT "1_refmac/seq' + str(b) + '_refmac1.cif" < 1_refmac/refmacTMP.tmp > 1_refmac/seq' + str(b) + '_refmac1.log ')
	file_sh.write(refmac_path+' XYZIN '+xyzin+' XYZOUT '+xyzout+' HKLIN '+hklin+' HKLOUT '+hklout+' LIBOUT '+cifout+" < "+refmac_tmp_file+" > "+refmac_output_log+' \n\n')
	file_sh.close()

def return_impartial_res (pdb):
	# amino_acid_list=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
	# amino_acid_list_3L=['ALA','CYS','ASP','GLU','PHE','GLY','HIS','ILE','LYS','LEU','MET','ASN','PRO','GLN','ARG','SER','THR','VAL','TRP','TYR']
	# amino_acid_list_numb_atoms=[5,6,  8  ,  9  , 11  ,  4  , 10  ,  8  ,  9  ,  8  ,  8  ,  8  ,  7  ,  9  , 11  , 6   ,  7  ,  7  ,  14 ,  12 ]
	f1=open(pdb)
	fi=f1.readlines()
	f1.close()
	resnumb=''
	restype=''
	c=0 # counter of number of atoms per residue
	chain=''
	dic_ch_resn={}
	for l in fi:
		if l.startswith('ATOM') and (l[16]==' ' or l[16]=='A') and not l[12]=='H' and not l[13]=='H': # read each line of ATOM without considering hydrogen atoms
			resnumb_new=int(l[22:26])
			if resnumb_new==resnumb:
				c+=1
			else:
				if l[21]!=chain and not c==0:  c-=1
				if not c==0:
					if not amino_acid_list_numb_atoms[amino_acid_list_3L.index(restype)]==c:
						try:     dic_ch_resn[chain][resnumb]=amino_acid_list[amino_acid_list_3L.index(restype)].upper()
						except:  dic_ch_resn[chain]={resnumb:amino_acid_list[amino_acid_list_3L.index(restype)].upper()}
				c=1
			resnumb=int(l[22:26])
			restype=l[17:20]
			chain=l[21]
	c-=1
	if not amino_acid_list_numb_atoms[amino_acid_list_3L.index(restype)]==c:
		try:     dic_ch_resn[chain][resnumb]=amino_acid_list[amino_acid_list_3L.index(restype)].upper()
		except:  dic_ch_resn[chain]={resnumb:amino_acid_list[amino_acid_list_3L.index(restype)].upper()}
	return dic_ch_resn

def retrieve_Rfactor_from_PDB_file ( PDB_file ): #copied from SLIDER_POINTMUTATION.py September 13rd 2015
	R_factor, Rfree = '',''
	PDB_Rfactor_file=open ( PDB_file , 'r' )
	PDB_Rfactors_list=PDB_Rfactor_file.readlines()
	PDB_Rfactor_file.close()
	skipp=False
	for PDB_file_Rfac in range( len(PDB_Rfactors_list) ):
		if PDB_Rfactors_list[PDB_file_Rfac].startswith('REMARK') and len( PDB_Rfactors_list[PDB_file_Rfac].split() )>=5 and not skipp:
			if PDB_Rfactors_list[PDB_file_Rfac].split()[2]=='R' and PDB_Rfactors_list[PDB_file_Rfac].split()[5]=='SET)' :
				R_factor=float( PDB_Rfactors_list[PDB_file_Rfac].split()[7] )
			elif PDB_Rfactors_list[PDB_file_Rfac].split()[2]=='FREE' and PDB_Rfactors_list[PDB_file_Rfac].split()[5]==':' :
				Rfree=float ( PDB_Rfactors_list[PDB_file_Rfac].split()[6] )
			elif PDB_Rfactors_list[PDB_file_Rfac].startswith('REMARK best refinement for ') and 'R/Rfree' in PDB_Rfactors_list[PDB_file_Rfac]:
				R_factor=float(PDB_Rfactors_list[PDB_file_Rfac][-14:-8])
				Rfree  =float(PDB_Rfactors_list[PDB_file_Rfac][-7:-1])
				skipp=True

	if R_factor=='' and Rfree=='':
		print('Failure obtaining R/Rfree of PDB',PDB_file,'EXITING.')
		quit()
	else: return R_factor,Rfree

def sh_refine_buster_multiprocesses ( pdb_input , mtz_input , pdb_output , buster_path , sh_file , distribute_computing , buster_options='-noWAT -nbig 10 -RB -nthread 1  UsePdbchk="no"', ccp4_config_path = '' , buster_config_path = ''):
	file_sh=open(sh_file,'w')
	if distribute_computing=='multiprocessing':
		file_sh.write('#!/bin/bash'+ '\n')
	if distribute_computing=='local_grid':
		file_sh.write('#!/bin/bash'+ '\n')
		file_sh.write('source '+ccp4_config_path+'\n')
		file_sh.write('source '+buster_config_path+'\n')
		
	#xyzin=pdb_input
	folder=pdb_output[:-4]
	if distribute_computing=='local_grid':
		#xyzin =xyzin.split('/')[-1]
		folder=folder.split('/')[-1]
		mtz_input=mtz_input.split('/')[-1]
##    os.system('mkdir '+folder)
	if buster_options==False:
	#buster_options=' -noWAT -nbig 10 -RB -nthread 1 "StopOnGellySanityCheckError=no"'
		buster_options=' -noWAT -nbig 10 -RB -nthread 1 UsePdbchk="no" '
	#-w 50 AdjustXrayWeightAutomatically="no" -autoncs
	#check if file has arrived
	#file_sh.write('if (! -f "'+xyzin+'" ) then\n        echo "Files did not arrive yet, waiting 15 seconds."\n        sleep 15\n        endif\n')
	file_sh.write(buster_path+' -p '+pdb_input+' -m '+mtz_input+' -d '+folder+' '+buster_options)
	file_sh.write(' > '+folder+'.log\n')

	#p = subprocess.Popen([buster_path,'-p',xyzin,'-m',mtz_input,'-d',folder]+buster_options.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#out, err = p.communicate()
	#file=open(folder+'.log','w')
	#file.write(out)
	#file.close()
	#rename_compress_remove_BUSTER_jobs ( folder_output , dictionary_buster['folder'] , file_name )
	folder_input_BUSTER=folder
	filename_output_without_extension=pdb_output[:-4]
	if distribute_computing=='local_grid':
		filename_output_without_extension=filename_output_without_extension.split('/')[-1]

	#added for new version
	# file:///xtal/buster/BUSTER_snapshot_20170920/docs/autobuster/manual/autoBUSTER7.html#corr
	#general run line: % corr -p refine.pdb -m refine.mtz -F 2FOFCWT -P PH2FOFCWT
	file_sh.write(buster_path[:buster_path.rindex('/')]+'/corr'+' -p '+folder+'/refine.pdb -m '+folder+'/refine.mtz -F 2FOFCWT -P PH2FOFCWT -d '+folder+'_RSCC  > '+folder+'_RSCC.log\n')

	#recent BUSTER refine does not output html file
	#file_sh.write( 'cp ' + folder_input_BUSTER + '/analyse.html ' + filename_output_without_extension + '.html' + '\n')
	file_sh.write( 'cp ' + folder_input_BUSTER + '/refine.pdb ' + filename_output_without_extension + '.pdb' + '\n')
	file_sh.write( 'cp ' + folder_input_BUSTER + '/refine.mtz ' + filename_output_without_extension + '.mtz' + '\n')

	file_sh.write( 'tar -zcf ' + filename_output_without_extension  + '.tar.gz ' + folder_input_BUSTER + ' '+folder_input_BUSTER+'_RSCC \n')
	file_sh.write( 'rm -r ' + folder_input_BUSTER + ' '+folder_input_BUSTER+'_RSCC  \n\n')
	#rename_chosen_outputname_compress_remove_BUSTER_jobs ( folder , pdb_output[:-4] )
	file_sh.close()
	os.system('chmod 755 '+sh_file)
	os.system('chmod -R 755 '+pdb_output[:pdb_output.rindex('/')])
##    f=open(sh_file)
##    f2=f.read()
##    print f2
##    f.close()

def retrieve_busterCC_from_log_file ( log_file ): # old, I dont know why but this line '       Total' wasnt outputting in the run in: /localdata/rafael/SLIDER_phasing/1YZF/5-Article/control-seqs/control-1YZF_stats/1_ref/c0_true_ref1_RSCC.log
	#print log_file
	LOG_file_BUSTER_CCs  = open ( log_file , 'r' )
	LOG_file_BUSTER_CCs_list = LOG_file_BUSTER_CCs.readlines()
	LOG_file_BUSTER_CCs.close()
	CCmc = 0
	CCsc = 0
	i=0
	while CCmc == 0 and i<=len(LOG_file_BUSTER_CCs_list):
		if LOG_file_BUSTER_CCs_list[i].startswith('   CC: main-chain = '):
			l=LOG_file_BUSTER_CCs_list[i].split()
			CCmc = float ( l[-4] )
			CCsc = float(l[-1])
	# while CCmc == 0 or i<=len(LOG_file_BUSTER_CCs_list):
	#     if LOG_file_BUSTER_CCs_list[i].startswith('       Total'):
	#         l=LOG_file_BUSTER_CCs_list[i].split()
	#         CCmc = float ( l[6] )
	#         CCsc = float(l[-1])
		else: i+=1
	if CCmc == 0:
		print('Condition not found in',log_file)
		print('Failure in function RJB_lib.retrieve_busterCC_from_log_file')
		exit()
	return CCmc , CCsc

def read_secstr_pred_psipred (input_file):
	file_read=open(input_file,"r")
	file_list=file_read.readlines()
	file_read.close()
##    confidence=file_list[2].split()[1]
##    sectr=file_list[3].split()[1]
##    sequence=file_list[4].split()[1]
	#considering that 
	for line_index in range(len(file_list)):
		line=file_list[line_index]
		if file_list[line_index].startswith('Conf:'):
			try:
				confidence+=file_list[line_index].split()[1]
				sec_str_pred+=file_list[line_index+1].split()[1]
				sequence+=file_list[line_index+2].split()[1]
			except:
				confidence=file_list[line_index].split()[1]
				sec_str_pred=file_list[line_index+1].split()[1]
				sequence=file_list[line_index+2].split()[1]
	list_secstr_pred=[]
	aa_verify=sec_str_pred[0]
	string_var=''
	for letter in sec_str_pred:
		if aa_verify==letter:
			string_var+=letter
		else:
			list_secstr_pred.append(string_var)
			string_var=letter
			aa_verify=letter 
	if len(string_var)==1:
		list_secstr_pred.append(string_var)
	#return sequence,sec_str_pred,confidence,list_secstr_pred
	dic_secstr_pred_psipred={}
	dic_secstr_pred_psipred['sequence']=sequence
	dic_secstr_pred_psipred['sec_str_pred']=sec_str_pred
	dic_secstr_pred_psipred['confidence']=confidence
	dic_secstr_pred_psipred['list_secstr_pred']=list_secstr_pred
	return dic_secstr_pred_psipred
			
def from_secstr_pred_psipred_generate_trusted_fragments (dic_secstr_pred_psipred,confidence_level,min_size_frag, trust_loop ): #confidence_level_from_1 to 9, should be an integer adding 4Jun16: ['initial_res'] / ['final_res'] #changing in Jul18,2016 to include loops
	min_size_frag=int(min_size_frag)
	confidence_level=int(confidence_level)
	list_dic_ss_frag=[]
	#dic_ss_frag will have same keys as: dic_secstr_pred_psipred keys: ['sequence'] ['sec_str_pred'] ['confidence']
	count_previous=0
	ss_previous=dic_secstr_pred_psipred['sec_str_pred'][0]
	seq=''
	conf=''
	ss=''
	for int_index in range(len(dic_secstr_pred_psipred['sequence'])):
		#print 'index',int_index,'seq',dic_secstr_pred_psipred['sequence'][int_index],'conf',dic_secstr_pred_psipred['confidence'][int_index],'ss',dic_secstr_pred_psipred['sec_str_pred'][int_index]
		#condition to extend fragment of same SS of previous residue but it won't take last residue into consideration
		if (dic_secstr_pred_psipred['sec_str_pred'][int_index]=='H' or dic_secstr_pred_psipred['sec_str_pred'][int_index]=='E' or (trust_loop==True and dic_secstr_pred_psipred['sec_str_pred'][int_index]=='C')) and int(dic_secstr_pred_psipred['confidence'][int_index]) >= confidence_level and ( (dic_secstr_pred_psipred['sec_str_pred'][int_index]==ss_previous and len(seq)>0) or len(seq)==0 ) and int_index!=len(dic_secstr_pred_psipred['sequence'])-1:
			#print 'COND1'
			#dic_secstr_pred_psipred['confidence'][int_index], 'ss', dic_secstr_pred_psipred['sec_str_pred'][int_index]
			seq+=dic_secstr_pred_psipred['sequence'][int_index]
			conf+=dic_secstr_pred_psipred['confidence'][int_index]
			ss+=dic_secstr_pred_psipred['sec_str_pred'][int_index]
		else:
			#when last res is the same ss as previous and should be also counted
			if int_index==len(dic_secstr_pred_psipred['sequence'])-1 and dic_secstr_pred_psipred['sec_str_pred'][int_index]==ss_previous:
				#print 'COND2','index',int_index,'seq',dic_secstr_pred_psipred['sequence'][int_index],'conf',dic_secstr_pred_psipred['confidence'][int_index],'ss',dic_secstr_pred_psipred['sec_str_pred'][int_index]
				seq+=dic_secstr_pred_psipred['sequence'][int_index]
				conf+=dic_secstr_pred_psipred['confidence'][int_index]
				ss+=dic_secstr_pred_psipred['sec_str_pred'][int_index]
			#when other res is found that below 
			if len(seq)>=min_size_frag:
				#print 'COND3'
				dic_ss_frag={}
				dic_ss_frag['sequence']=seq
				dic_ss_frag['sec_str_pred']=ss
				dic_ss_frag['confidence']=conf
				dic_ss_frag['initial_res']=int_index+1-len(seq)
				dic_ss_frag['final_res']=int_index
				list_dic_ss_frag.append(dic_ss_frag)
			seq=dic_secstr_pred_psipred['sequence'][int_index]
			conf=dic_secstr_pred_psipred['confidence'][int_index]
			ss=dic_secstr_pred_psipred['sec_str_pred'][int_index]
		ss_previous=dic_secstr_pred_psipred['sec_str_pred'][int_index]
	#print list_dic_ss_frag
	return list_dic_ss_frag

def return_chain_list (pdb_input): #['A', 'B', 'W']
	p = Bio.PDB.PDBParser(PERMISSIVE=1)
	struct = p.get_structure(pdb_input[:-4], pdb_input)
	list_chains=[]
	for chain in struct[0].get_list():
		list_chains.append(chain.get_id())
	return list_chains
#
# def return_list_resnumb_list (pdb_input): #[[1,2,3],[1,2]] 1st list: res of 1st chain, 2nd list: res of 2nd chain
#     p = Bio.PDB.PDBParser(PERMISSIVE=1)
#     struct = p.get_structure(pdb_input[:-4], pdb_input)
#     list_chains=return_chain_list (pdb_input)
#     list_res_numb=[]
#     for chain in list_chains:
#         list_var=[]
#         for res in struct[0][chain].get_list():
#             if res.get_id()[0]==' ':
#                 list_var.append(res.get_id()[1])
#         list_res_numb.append(list_var)
#     return list_res_numb
#
#

def total_numb_res (pdb_input): #it also counts water as residues return integer
	p = Bio.PDB.PDBParser(PERMISSIVE=1)
	struct = p.get_structure(pdb_input[:-4], pdb_input)
	residues = struct[0].get_residues()
	rescount=0
	for r in residues:
		rescount+=1
	return rescount

def return_tuple_chain_resnumb_restype (pdb_input):#[[('A', 1, 'S'), ('A', 2, 'A')],[('B', 1, 'S')]]
	p = Bio.PDB.PDBParser(PERMISSIVE=1)
	struct = p.get_structure(pdb_input[:-4], pdb_input)
	#list_chains=return_chain_list (pdb_input)
	list_chains=[]
	for chain in struct[0].get_list():
		 list_chains.append(chain.get_id())
	list_tuples=[]
	for chain in list_chains:
		list_var=[]
		for res in struct[0][chain].get_list():
			if res.get_id()[0]==' ':
				if res.get_resname() in amino_acid_list_3L:
					seq=amino_acid_list[amino_acid_list_3L.index(res.get_resname())]
					resnumb=res.get_id()[1]
					tuple=(chain,resnumb,seq)
					list_var.append(tuple)
				else:
					print('Compound',res.get_resname() , 'numbered',res.get_id()[1] , 'chained',chain, 'was rejected by RJB_lib.return_tuple_chain_resnumb_restype!')
		list_tuples.append(list_var)
	return list_tuples

def return_restype_list (pdb_input,printe=False): #['SAVQFEVSIIKIAGKSGVEEYGSLGCYCGSGGASRPLLASDACCAVHDCCFGLVSSCDPGAGVYTYAKLLGVATCGLGNPCAVQICECDKVAATCFRKNAAVFDIKRQFKPAKICAEAQPC', '']
	if isinstance(pdb_input, string_types):
		p = Bio.PDB.PDBParser(PERMISSIVE=1)
		struct = p.get_structure(pdb_input[:-4], pdb_input)
	else:
		struct=pdb_input
	list_chains=return_chain_list (pdb_input)
	list_restype=[]
	for chain in list_chains:
		string_var=''
		for res in struct[0][chain].get_list():
			if res.get_id()[0]==' ':
				try:
					seq=amino_acid_list[amino_acid_list_3L.index(res.get_resname())]
					string_var+=seq
				except:
					if printe:
						print('Restype',res.get_resname(),'not a residue, therefore it was not considered.')
		list_restype.append(string_var)
	return list_restype
#
# def return_list_of_number_residues_by_chain (pdb_input):
#     l=return_restype_list (pdb_input)
#     ll=[len(i) for i in l]
#     return ll
#

def return_chainlist_seqlist_numbres (pdb_input): #(['A', 'W'], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121], []], 196)
	p = Bio.PDB.PDBParser(PERMISSIVE=1)
	struct = p.get_structure(pdb_input[:-4], pdb_input)

	list_chains=return_chain_list (pdb_input)

	list_res_numb=[]
	for chain in list_chains:
		list_var=[]
		for res in struct[0][chain].get_list():
			if res.get_id()[0]==' ':
				list_var.append(res.get_id()[1])
		list_res_numb.append(list_var)

	rescount=total_numb_res (pdb_input)

	return list_chains , list_res_numb , rescount

def remove_partial_res_from_PDB_BioPython ( pdb_input, pdb_output ):
	p = Bio.PDB.PDBParser(PERMISSIVE=1)
	struct = p.get_structure(pdb_input[:-4], pdb_input)
	residues = struct[0].get_residues()
	verify=False
	while verify==False:
		for res in residues:
			if len(res)>=4:
				verify=True
	if verify:
		class FullResSelect(Bio.PDB.Select):
			def accept_residue(self, residue):
				if len(residue)>=4:
					return True
				else:
					return False
		io = Bio.PDB.PDBIO()
		io.set_structure(struct)
		io.save( pdb_output , FullResSelect() )
		print('Script RJB_lib.remove_partial_res_from_PDB_BioPython corrected pdb',pdb_input,'and named to',pdb_output)
		add_previous_ATOM_lines_to_pdb ( pdb_input, pdb_output , pdb_output )
		print('Script RJB_lib.add_previous_ATOM_lines_to_pdb added header into same name file.')
	else:
		print('\n\nPDB without partial residues.\n\n')
	return verify

def add_previous_ATOM_lines_to_pdb (pdb_input_header, pdb_input_atoms , pdb_output):
	input_header=open(pdb_input_header,'r')
	header=input_header.read()
	input_header.close()
	input_atoms=open(pdb_input_atoms,'r')
	atoms=input_atoms.read()
	input_atoms.close()
	output=open(pdb_output,'w')
	output.write(header[:header.index('\nATOM')]+'\n')
	output.write(atoms)
	output.close()

def given_2_superposed_pdbs_return_list_res_match ( pdb_match , pdb_fit , dist=1.0):#method='one') : #method may be all (get all atoms)
	#Script written 10Jun2016 for SLIDER_phasing to calculate correspondence of res of two structures to be calculated post_morten analysis
	#method=X if distance is above 1.0A between trace and reference, an 'X' is given
	#method=write write correspondent residues
	ProteinPDB = Bio.PDB.PDBParser()
	trace = ProteinPDB.get_structure ( pdb_match[:-4] , pdb_match )
	ent = ProteinPDB.get_structure ( pdb_fit[:-4] , pdb_fit )

	#list_CA_trace=[]
	list_CA_trace_related_ent_BioPDB = []
	for atom in trace.get_atoms():
		if atom.get_name()=='CA':
			a_tr = atom
			r_tr = a_tr.get_parent()
			r_tr_type = amino_acid_list[amino_acid_list_3L.index(r_tr.get_resname())]
			c_tr = r_tr.get_parent()
			#list_CA_trace.append(atom)
			list_CA_trace_related_ent_BioPDB.append([(c_tr.get_id(), r_tr.get_id()[1], r_tr_type, a_tr)])

	list_CA_ent=[]
	for atom in ent.get_atoms():
		if atom.get_name()=='CA':
			list_CA_ent.append(atom)
	ns=Bio.PDB.NeighborSearch(list_CA_ent)
	#
	# listforcomb=[]
	# for match in list_CA_trace_related_ent_BioPDB:
	#     listvar=[]
	#     coord = CAtrace.get_coord()
	#     pair = ns.search(coord, i, "A")
	#     for CAent in pair:
	#         listvar.append(CAent)
	#     listforcomb.append(listvar)

	table_remove=[]
	for i in numpy.arange(0.5,dist+0.1,0.25):
		# print i
		#count = 0
		#for CA in list_CA_trace:
		for listpair in list_CA_trace_related_ent_BioPDB:
			if len(listpair)==1:
				# print 'listpair1',listpair
				CAtrace=listpair[0][-1]
				coord= CAtrace.get_coord()
				pair = ns.search(coord, i, "A")
				# print 'pair',pair,len(pair)
				if len(pair)>0:
					listvar=[]
					for CAent in pair:
						if CAent not in table_remove: listvar.append( (CAent,CAtrace-CAent) )

					if len(listvar)>0:
						# print 'listpair2',listvar
						listvar.sort(key=(lambda item: item[-1]), reverse=False)
						# print 'listpair2',listvar
						a_ent= listvar[0][0]
						r_ent=a_ent.get_parent()
						r_ent_type=amino_acid_list[amino_acid_list_3L.index(r_ent.get_resname())]
						c_ent=r_ent.get_parent()
						distvar=listvar[0][1]

						table_remove.append(a_ent)
						listpair.append((c_ent.get_id(),r_ent.get_id()[1],r_ent_type, a_ent))
						listpair.append(distvar)

	identicalresiduesn = 0
	for i in list_CA_trace_related_ent_BioPDB:
		#print i
		if len(i) == 3 and i[0][2] == i[1][2]: identicalresiduesn += 1
	percentidentity = 100 * float(identicalresiduesn) / len(list_CA_trace_related_ent_BioPDB)

	return list_CA_trace_related_ent_BioPDB , identicalresiduesn , percentidentity
	#output is like list_CA_trace_related_ent_BioPDB[0]=[('A', 2, 'N', <Atom CA>)]       #here no match was found
				   #list_CA_trace_related_ent_BioPDB[1]=[('A', 3, 'T', <Atom CA>), ('A', 3, 'K', <Atom CA>), 1.2654423]


	# print 'Algorithm made to obtain minimum independent distance:'
	#
	# listdist = []
	# for i in list_CA_trace_related_ent_BioPDB:
	#     print i
	#     if len(i) > 1:
	#         listdist.append(i[-1])
	#
	# rmsd = calculateRMSDfromdistances(listdist)
	# rmsd = '%.1f' % (rmsd)
	# print rmsd,'\n\n\n'
	#
	# return list_CA_trace_related_ent_BioPDB , rmsd
	#
	# listbyfrag=[]
	# chprev   = list_CA_trace_related_ent_BioPDB[0][0][0]
	# resnprev = list_CA_trace_related_ent_BioPDB[0][0][1]-1
	# listvar=[]
	# for match in list_CA_trace_related_ent_BioPDB:
	#     ch  =match[0][0]
	#     resn=match[0][1]
	#     if ch==chprev and resn-1==resnprev:
	#         listvar.append(match)
	#     else:
	#         listbyfrag.append(listvar)
	#         listvar=[]
	#     chprev=ch
	#     resnprev=resn
	# listbyfrag.append(listvar)
	#
	# listbyfrag.sort(key=(lambda item: len(item)), reverse=True)
	#
	# list_CA_trace_related_ent_BioPDB2=[]
	#
	# for frag in listbyfrag:
	#     lresnmatch= [x[1] for x in frag]
	#     minm=numpy.min(lresnmatch)
	#     maxm = numpy.max(lresnmatch)
	#     listvar=[]
	#     for i in range(minm-5,maxm+5):
	#         countt=i
	#         count2=0
	#         for aa in frag:
	#             resn=aa[1][1]
	#             if countt==resn: count2+=1
	#         listvar.append(count2)
	#     best=minm-5+listvar.index( max(listvar) )
	#     for i, aa in enumerate(frag):
	#         tupletrace=aa[0]
	#         atomCAentnew = ent[0]['A'][100]['CA']
	#         list_CA_trace_related_ent_BioPDB2
	#
	#
	# return list_CA_trace_related_ent_BioPDB

def GivenListMatchCA2PDBsReturnCorrespondentResString (list_CA_trace_related_ent):
	seq=''
	for item in list_CA_trace_related_ent:
		try:            seq+=item[1][2]
		except:         seq+='X'
	return seq #seq='XXKIVLF'

def GivenListListMatchCA2PDBsReturnDicSequenceByChain(list_CA_trace_related_ent):
# def given_list_pair_res_return_dic_sequence_by_chain (list_CA_trace_related_ent): # OBSOLETE
	dic_seq={}
	for item in list_CA_trace_related_ent:
		try:            dic_seq[item[0][0]]
		except:         dic_seq[item[0][0]]=''
		try:            dic_seq[item[0][0]]+=item[1][2]
		except:         dic_seq[item[0][0]]+='X'
	return dic_seq #dic_seq['A']='XXKIVLF'

def GivenListListMatchCA2PDBsReturnDicChResNResT(list_CA_trace_related_ent):
	DicResNResT={}
	for item in list_CA_trace_related_ent:
		ch  =item[0][0]
		resn=item[0][1]
		if len(item)>1: restrue=item[1][2]
		else:           restrue='X'
		if ch not in DicResNResT: DicResNResT[ch]={resn:restrue}
		else:                     DicResNResT[ch][resn]=restrue
	return DicResNResT

def GivenDicChResNResTReturnDicChResNRangeSeq(DicChResNResT,DicChResNResSS=False):
	DicChResNRangeSeq={}
	for ch,DicResNResT in DicChResNResT.items():
		DicChResNRangeSeq[ch]={}
		prevRN = sorted(DicResNResT)[0]
		resni  = str(prevRN) + '-'
		seq    = DicResNResT[prevRN]
		if DicChResNResSS!=False: prevSS=DicChResNResSS[ch][prevRN]

		for resn in sorted(DicResNResT.keys())[1:]:
			if prevRN == resn-1 and (DicChResNResSS==False or DicChResNResSS[ch][resn]==prevSS): #condition to increase segment
				seq   += DicResNResT[resn]
			else:                #condition to save previous segment and start new one
				DicChResNRangeSeq[ch][resni+str(prevRN)]=seq
				resni=str(resn)+'-'
				seq=DicResNResT[resn]
			prevRN = resn
			if DicChResNResSS!=False: prevSS = DicChResNResSS[ch][resn]
		# condition to save last and forgotten segment
		DicChResNRangeSeq[ch][resni + str(prevRN)] = seq
	# for ch in TrueSeqDicResNRangeSeq:
	#     print ch
	#     for resn in sorted(TrueSeqDicResNRangeSeq[ch]):
	#         print resn, TrueSeqDicResNRangeSeq[ch][resn]
	return DicChResNRangeSeq

def GivenPDBlistChResNCAReturnlistChResNRangeCA (listChResNCA): #input = [['A',1],['A',2],['A',3],['A',10],['A',11],['A',12],['A',13]]
	listChResNRangeCA=[]                                        #output= [['A','1-3'],            ['A','10-13']                      ]
	prevresn=listChResNCA[0][-1]
	prevch = listChResNCA[0][0]
	listvar=[prevch,[prevresn]]
	for ch,resn in listChResNCA[1:]:
		if ch==prevch and resn-1==prevresn: listvar[-1].append(resn)
		else:
			listChResNRangeCA.append([listvar[0],str(listvar[-1][0])+'-'+str(listvar[-1][-1])])
			listvar = [ch, [resn]]
		prevresn=resn
		prevch  =ch
	listChResNRangeCA.append([listvar[0], str(listvar[-1][0]) + '-' + str(listvar[-1][-1])])
	return listChResNRangeCA

def sh_refine_phenix_multiprocesses ( pdb_input_file , mtz_input_file , pdb_output_file , phenixrefine_path , F, SIGF, sh_file , distribute_computing , options=False, phenixrefine_config_path = ''):
	file_sh=open(sh_file,'w')
##    if distribute_computing=='multiprocessing':
##        file_sh.write('#!/bin/sh'+ '\n')
	if distribute_computing=='local_grid':
		file_sh.write('#!/bin/bash'+ '\n')
		file_sh.write('export PATH=/usr/local/bin:/usr/bin:/bin:$PATH\n')  # suggested by MAX
		#file_sh.write('source /xtal/xtalsetup'+ '\n')
		#file_sh.write('hostname > '+sh_file.split('/')[-1]+ '_host \n')
		file_sh.write('source '+phenixrefine_config_path+'\n')
	xyzin=pdb_input_file
	outf=pdb_output_file[:-4].split('/')[-1]
	hklin=mtz_input_file
	#hklout=xyzout[:-4]+'.mtz'
	#phenix_output_log = xyzout[:-4]+'.log'
	if distribute_computing=='local_grid':
		xyzin =xyzin.split('/')[-1]
		pdb_output_file = pdb_output_file.split('/')[-1]
		hklin =hklin.split('/')[-1]
		#hklout=hklout.split('/')[-1]
		#phenix_output_log = phenix_output_log.split('/')[-1]

	#if not options: options = 'strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body main.number_of_macro_cycles=5 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=False optimize_adp_weight=False nproc=1 export_final_f_model=true'

	# fewer restrictions   5LCY#
	if not options:                          options = 'strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body                              main.number_of_macro_cycles=5 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=False optimize_adp_weight=False                                   nproc=1 export_final_f_model=true '
	#with NCS             5LCY/2#
	#if not options:                          options = 'strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body                              main.number_of_macro_cycles=5 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=False optimize_adp_weight=False                                   nproc=1 export_final_f_model=true ncs_search.enabled=True '

	#various restrictions 1YZF#if not options: options= 'strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body ramachandran_restraints=True main.number_of_macro_cycles=5 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=False optimize_adp_weight=False  secondary_structure.enabled=True nproc=1 export_final_f_model=true'
	#1YZF#                     if not options: options= 'strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body ramachandran_restraints=True main.number_of_macro_cycles=5 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=False optimize_adp_weight=False  secondary_structure.enabled=True nproc=1 export_final_f_model=true simulated_annealing=true'
	#if not options: options = 'strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body ramachandran_restraints=True main.number_of_macro_cycles=5 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=False optimize_adp_weight=False  secondary_structure.enabled=True nproc=1 export_final_f_model=true simulated_annealing=true'

	file_sh.write(phenixrefine_path+' '+xyzin+' '+hklin+' refinement.input.xray_data.labels="'+F+','+SIGF+'" prefix='+outf+' '+options+'\n')
	file_sh.write('mv ' + outf + '_001.mtz '+pdb_output_file[:-4]+'.mtz\n')
	file_sh.write('mv '+outf+'_001_f_model.mtz '+pdb_output_file[:-4]+'_FOM.mtz\n')
	file_sh.write('mv ' + outf + '_001.log ' + pdb_output_file[:-4] + '.log\n')
	file_sh.write('mv ' + outf + '_001.pdb ' + pdb_output_file+'\n')
	file_sh.close()

# def phenix_refine_multiprocessing (pdb_input,mtz_input,output,F,SF,options=False): #type is a string
#     type could be < None , strategy=rigid_body , 'optimize_xyz_weight=true optimize_adp_weight=true' , 'strategy=tls tls.find_automatically=True' , ncs_search.enabled=True >
#    file_name=dictionary_buster['file'].split('.pd')[0]
#    folder_output=dictionary_buster['folder']+'/BUSTER_temp_'+file_name
#    xyzin=dictionary_buster['folder']+'/'+dictionary_buster['file']
#    os.system( 'mkdir ' + folder_output )
#    buster_options='-noWAT -nbig 10 -RB -nthread 1'
#     #-w 50 AdjustXrayWeightAutomatically="no" -autoncs
	#'phenix.refine '+pdb_file+' '+mtz_file+' refinement.input.xray_data.labels="'+F+','+SIGF+'" refinement.output.prefix='+output_file+' strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body ramachandran_restraints=True main.number_of_macro_cycles=20 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=True optimize_adp_weight=True  secondary_structure.enabled=True nproc=1'
	#phenix.refine n1-polyA.pdb 1YZF.mtz      refinement.input.xray_data.labels="FOBS,SIGFOBS"  refinement.output.prefix=example          strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body ramachandran_restraints=True main.number_of_macro_cycles=20 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=True optimize_adp_weight=True  secondary_structure.enabled=True nproc=1
	# if not options: options='strategy=individual_sites+individual_adp+individual_sites_real_space+rigid_body ramachandran_restraints=True main.number_of_macro_cycles=20 write_eff_file=false write_geo_file=false  write_def_file=false optimize_xyz_weight=True optimize_adp_weight=True  secondary_structure.enabled=True nproc=1'
	# '=+' export_final_f_model=true output.write_eff_file=False output.write_geo_file=False output.write_def_file=False refinement.main.number_of_macro_cycles=10'
	# p = subprocess.Popen(['phenix.refine',pdb_input,mtz_input,'refinement.input.xray_data.labels="'+F+','+SIGF,'prefix='+output]+options.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# out, err = p.communicate()
	#export_final_f_model=true
#    file=open(folder_output+'/'+file_name+'.log','w')
#    file.write(out)
#    file.close()
	
	#phenix.refine mtz_input pdb_input prefix=output_name
	#< None , strategy=rigid_body , 'optimize_xyz_weight=true optimize_adp_weight=true' , 'strategy=tls tls.find_automatically=True' , ncs_search.enabled=True >
	#export_final_f_model=true output.write_eff_file=False output.write_geo_file=False output.write_def_file=False

def GetPhenixRefineLLG (log):
	with open(log) as f:
		fl=f.read()
		#
		indnormllg=fl.rindex('normalized target function (ml) (work):')+len('normalized target function (ml) (work):')
		strnormllg=fl[indnormllg:indnormllg+28]
		normllg=float(strnormllg)
		#
		indllgwork=fl.rindex('target function (ml) not normalized (work):')+len('target function (ml) not normalized (work):')
		strllgwork=fl[indllgwork:indllgwork+28]
		llgwork=float(strllgwork)
		#
		indllgfree=fl.rindex('target function (ml) not normalized (free):')+len('target function (ml) not normalized (free):')
		strllgfree=fl[indllgfree:indllgfree+28]
		llgfree=float(strllgfree)
	return normllg , llgwork , llgfree

def generate_matrix_SLIDER_alignment (includeX=False):
	matrix_align={}
	for ind1,aa1 in enumerate(amino_acid_list):
		for ind2,aa2 in enumerate(amino_acid_list):
			if aa1==aa2:
				matrix_align[(aa1.lower(),aa2)]=4
				matrix_align[(aa1,aa2)]=6
			else:
				matrix_align[(aa1.lower(),aa2)]=-1
				matrix_align[(aa1,aa2)]=-4
	matrix_align[('a','A')]=0
	if includeX:
		for aa1 in amino_acid_list:
			for k in ['X']:#,'-']:
				matrix_align[(aa1, k)] = 0
				matrix_align[(k, aa1)] = 0
	#from Bio.SubsMat import MatrixInfo
	#matrix_align=MatrixInfo.ident
	return matrix_align

def AlignTwoSequences (seq1,seq2,matrix_align=False,printt=False):#,MatrixAlign=matlist.blosum62): # this was written in Feb27 2018 and it has proven really bad to find remoto homologous sequence pairing
																   # clustalomega was effective in 1YZF sequence pairing and was replaced by it, its file should be given by user
	#options available on:
	#matrix_align =  MatrixAlign
	#matrix_align = MatList.blosum62
	#matrix_align = MatList.blosum30
	#matrix_align = MatList.gonnet
	#matrix_align = MatList.ident
	if matrix_align==False: matrix_align = generate_matrix_SLIDER_alignment(includeX=True)
	#print 'Aligning and scoring:'
	#print seq1,seq2
	# _align(sequenceA, sequenceB, match_fn, gap_A_fn, gap_B_fn, penalize_extend_when_opening, penalize_end_gaps, align_globally, gap_char, force_generic, score_only, one_alignment_only)
	# pairwise_tuple=pairwise2.align.localdd (sequence, tuple_elem[0] ,matrix_align,-15,-5) #(1st seq,2nd seq,penalization for opening gap,penalization extending gap)
	# pairwise_tuple=pairwise2.align.localdd (sequence, seq ,matrix_align,-50,-25,-15,-5) #(1st seq,2nd seq,penalization for opening gap,penalization extending gap)
	#pairwise_tuple = pairwise2.align.localds(seq1, seq2, matrix_align, -10, -1)  # (1st seq,2nd seq,penalization for opening gap,penalization extending gap)
	pairwise_tuple = pairwise2.align.localds(seq1, seq2, matrix_align, -2, -1)  # (1st seq,2nd seq,penalization for opening gap,penalization extending gap)
	align_score = float(pairwise_tuple[0][2])
	if printt:
		for a in pairwise_tuple:
			print(pairwise2.format_alignment(*a))
	# exit()
	return pairwise_tuple[0] , align_score

def write_refmac_TMP_default_file ( refmacTMP_filename , ncycles , additional_line , mtz_f=False , mtz_sf=False , mtz_free=False ): # if you would like to add additional options not written by default, give a string here, otherwise just use empty string ''
	refmacTMP=open(refmacTMP_filename,'w')
	refmacTMP.write( 'make check NONE\nmake -\n    hydrogen ALL -\n    hout NO -\n    peptide NO -\n    cispeptide YES -\n    ssbridge YES -\n    symmetry YES -\n    sugar YES -\n    connectivity NO -\n    link NO\nrefi -\n    type REST -\n    resi MLKF -\n    meth CGMAT -\n    bref ISOT\n')
	refmacTMP.write( additional_line )
	refmacTMP.write( '\nncyc ' + ncycles + '\nscal -\n    type SIMP -\n    LSSC -\n    ANISO -\n    EXPE\nsolvent YES\nweight -\n    AUTO\nmonitor MEDIUM -\n    torsion 10.0 -\n    distance 10.0 -\n    angle 10.0 -\n    plane 10.0 -\n    chiral 10.0 -\n    bfactor 10.0 -\n    bsphere 10.0 -\n    rbond 10.0 -\n    ncsr 10.0\n')
	refmacTMP.write( 'labin  FP=')
	if mtz_f==False:
		refmacTMP.write( 'F')
	else:
		refmacTMP.write( mtz_f )
	refmacTMP.write(' SIGFP=')
	if mtz_sf==False:
		refmacTMP.write( 'SIGF')
	else:
		refmacTMP.write( mtz_sf )
	refmacTMP.write(' FREE=')
	if mtz_free==False:
		refmacTMP.write( 'FreeR_flag')
	else:
		refmacTMP.write(mtz_free)
	refmacTMP.write('\n')
	#refmacTMP.write('labout  FC=FC FWT=FWT PHIC=PHIC PHWT=PHWT DELFWT=DELFWT PHDELWT=PHDELWT FOM=FOM\nPNAME unknown\nDNAME unknown101\nRSIZE 80\nEXTERNAL WEIGHT SCALE 10.0\nEXTERNAL USE MAIN\nEXTERNAL DMAX 4.2\nEND' )
	refmacTMP.write( 'labout  FC=FC FWT=FWT PHIC=PHIC PHWT=PHWT DELFWT=DELFWT PHDELWT=PHDELWT FOM=FOM\n')
	#refmacTMP.write( 'PNAME unknown\nDNAME unknown101\nRSIZE 80\nEXTERNAL WEIGHT SCALE 10.0\nEXTERNAL USE MAIN\nEXTERNAL DMAX 4.2\nEND')
	refmacTMP.write('RIDG DIST SIGM 0.02\nEND')
	refmacTMP.close()

def run_sprout_multiprocess (pdb_input, seq_input, pdb_output , sprout_path ) :
	folder = os.path.dirname(seq_input)
	sprout_pdb = os.path.join(folder, 'input_sprout.pdb')
	sprout_result = seq_input.replace('.seq', 'seq1.pdb')
	create_symlink(pdb_input, sprout_pdb)

	p = subprocess.Popen ( [sprout_path,'input_sprout.pdb',os.path.basename(seq_input)],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
	out, err = p.communicate()
	file=open(seq_input+'.log','w')
	file.write(out.decode())
	file.close()
	if not os.path.isfile( sprout_result ):
		print('ERROR in Sprout generation.\nFile',pdb_output,'not generated.')
		exit()
	else:
		os.rename(sprout_result, pdb_output)
	add_Bfactors_occup_to_pdb(pdb_input_file=pdb_output, pdb_output_file=pdb_output,Bf_number_in_string_6characters=' 20.00', occ_number_in_string_3characters='1.00')

#def retrieve_energies_from_Scwrl4_log_file ( Scwrl4_log_file ) : #extracted from SLIDER script
#	energy_file=open(Scwrl4_log_file,'r')
#	energy_list=energy_file.readlines()
#	energy_file.close()
#	for energ in energy_list:
#		if energ.startswith('Total minimal energy of the graph'):
#energ.startswith('Energy of this cluster') or
#			return float( energ[energ.index('=')+2:energ.index('\n')] )

def obtainRfactorsBUSTERMapOnly (pdbfile):
	Rfactor=[]
	Rfree = []
	with open(pdbfile, 'r') as f:
		f2=f.readlines()
		f.close()
		skipp=False
		for l in f2:
			if l.startswith('REMARK best refinement for ') and 'R/Rfree' in l and not skipp:
				# print 'Rfactor',l[-14:-8]
				# print 'Rfree  ',l[-7:-1]
				# print l,f2.index(l)
				Rfactor.append(float(l[-14:-8]))
				Rfree.append(float(l[-7:-1]))
				skipp=True
	if len(Rfactor)==1 and len(Rfree)==1: return Rfactor[0],Rfree[0]
	else:
		print('More than one line meeting criteria in file',pdbfile,'function RJB_lib.obtainRfactorsBUSTERMapOnly')
		print(Rfactor,Rfree)
		exit()

def write_table_from_list_dict_and_keys_sorted_by (list_item,dic_all,key_sorted,reverse_state,output_filename): #not tested, generated 4/4/16 to write superimposition tables monomer B with monB
	output_file=open(output_filename,'w')
	for item in list_item:
		if item.startswith('refine'):
			item=item[8:]
		output_file.write(item[:7]+'\t')
	output_file.write('\n')
	dic_all.sort(key=(lambda item: item[key_sorted]), reverse=reverse_state)
	for lista in dic_all:
		for chosen_key in list_item:
			try:    var=lista[chosen_key]
			except:
				print ('Writting table:',output_filename)
				print ('chosen_key',chosen_key,'absent in')
				for i in lista: print (i,lista[i])
				exit()

			if type(var) is float or type(var) is numpy.float64:
				var='%.3f'%(var)
				if len(str(var))>7: var='%.2f'%(float(var))
				if 'Ident%' in chosen_key or 'wMPE' in chosen_key or 'ZLLG' in chosen_key: var='%.1f'%(float(var))
				if chosen_key.endswith('LLG') and not chosen_key.endswith('ZLLG'):         var='%.0f'%(float(var))
			elif type(var) is int:
				var=str(var)
			output_file.write(var+'\t')
		output_file.write('\n')
	output_file.close()

def shelxe_multiprocesses ( input , shelxe_path , shelxe_options ):
	if shelxe_path=='' or shelxe_path==False:
		shelxe_path=which_program ("shelxe")
	print('Shelxe expanding',input,'with options',shelxe_options)
	folder=input[:input.rindex('/')]
	input=input[input.rindex('/')+1:]
	p = subprocess.Popen([shelxe_path,input]+shelxe_options.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd=folder)
	out, err = p.communicate()
	
def checkFile(path):
	if not os.path.isfile( path ):
		print('Path given in borfile is not a file:',path,'\nPlease, correct it.')
		sys.exit(1)

def return_iCC_wMPE ( lst_file ):
	f=open(lst_file)
	f2=f.read()
	f.close()
	try:
		i=f2.index('wMPE')+len('wMPE')
		wMPE=float(f2[i:i+5])
	except:
		wMPE=''
	if 'Overall CC between native Eobs and Ecalc (from fragment) =' in f2:
		i=f2.index('Overall CC between native Eobs and Ecalc (from fragment) =')+len('Overall CC between native Eobs and Ecalc (from fragment) =')
		iCC=float(f2[i:i+6])
	else:
		iCC=False
	return iCC,wMPE

def phaser_Ani_tNCS_correction (input_mtz,F,SigF,Amplitudes,sh_file,log_file,output_folder): #Amplitudes should be True or False
	print('Running phaser to perform ANISOTROPY and tNCS CORRECTION')
	f=open(sh_file,'w')
	f.write('#!/bin/sh\n')
	f.write('phaser << EOF - phaser\n')
	f.write('MODE NCS\n')
	f.write('MR_NCS\n')
	f.write('HKLIN "'+input_mtz+'"\n')
	if Amplitudes: f.write('LABIN F='+F+' SIGF='+SigF+'\n')
	else:          f.write('LABIN I='+F+' SIGI='+SigF+'\n')
	f.write('TITLE Anisotropy and TNCS Correction\n')
	f.write('TNCS EPSFAC WRITE anis.tncs\n')
	f.write('NORM EPSFAC WRITE anis.norm\n')
	f.write('ROOT anis\n')
	f.write('END\n')
	f.write('EOF-phaser\n')
	f.close()
	os.chmod(sh_file, stat.S_IRWXU| stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)
	with open(log_file, "w+") as log:
		p = subprocess.Popen([sh_file], stdout=log, stderr=subprocess.PIPE,
	                             cwd=output_folder)
		out, err = p.communicate()

def calculate_LLG (output_folder,input_pdb,input_mtz,SG,F,SigF,Amplitudes,HighRes,Mw,nASU,eRMSD,sh_file,log_file,VRMS=True):
	if VRMS: VRMS='ON'
	else:    VRMS='OFF'
	print('Running phaser to calculate LLG of model:',input_pdb)
	f=open(sh_file,'w')
	f.write('#!/bin/sh\n')
	f.write('phaser << EOF - phaser\n')
	f.write('MODE MR_RNP\n')
	f.write('HKLIN "'+input_mtz+'"\n')
	f.write('HKLOUT OFF\n')
	if Amplitudes: f.write('LABIN F='+F+' SIGF='+SigF+'\n')
	else:          f.write('LABIN I='+F+' SIGI='+SigF+'\n')
	f.write('TITLE Calculate LLG\n')
	f.write('JOBS 1\n')
	f.write('SGALTERNATIVE SELECT NONE\n')
	f.write('COMPOSITION PROTEIN MW '+Mw+' NUMBER '+nASU+'\n')
	#f.write('MACMR PROTOCOL OFF\n')
	f.write('MACMR ROT OFF TRA OFF BFAC OFF VRMS '+VRMS+' CELL OFF LAST OFF NCYCLE 1000\n')#NCYCLE <NCYC> MINIMIZER [BFGS|NEWTON|DESCENT]\n')
	f.write('MACANO PROTOCOL OFF\n')
	f.write('MACTNCS PROTOCOL OFF\n')
	f.write('TNCS EPSFAC READ anis.tncs\n')
	f.write('NORM EPSFAC READ anis.norm\n')
	f.write('RESOLUTION 99 '+str(HighRes)+'\n')
	f.write('SOLPARAMETERS BULK USE OFF\n')
	f.write('XYZOUT OFF\n')
	f.write('TOPFILES 34\n')
	#f.write('ENSEMBLE ensarci0 PDBFILE '+input_pdb+' RMS 0.1\n')
	f.write('ENSEMBLE ensarci0 PDBFILE ' + input_pdb + ' RMS '+eRMSD+'\n')#'#0.1\n')
	f.write('ENSEMBLE ensarci0 DISABLE CHECK ON\n')
	f.write('SOLU SET\n')
	f.write('SOLU SPAC '+SG+'\n')
	f.write('SOLU 6DIM ENSE ensarci0 EULER 	0.0 0.0 0.0	FRAC 0.0 0.0 0.0	BFAC 0.0\n')
	f.write('ROOT "0"\n')
	f.write('END\n')
	f.write('EOF-phaser\n')
	f.close()
	#os.system('chmod 755 '+sh_file)
	#os.system('tcsh '+sh_file+' > ' + log_file)
	os.chmod(sh_file, stat.S_IRWXU| stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)
	with open(log_file, "w+") as log:
		p = subprocess.Popen([sh_file], stdout=log, stderr=subprocess.PIPE,
	                             cwd=output_folder)
		out, err = p.communicate()

def return_LLG(phaser_log_file):
	f2=open(phaser_log_file)
	f=f2.readlines()
	f2.close()
	for i,l in enumerate(f):
		#if l.startswith('   Refined TF/TFZ equivalent ='):
		if l.startswith('$$ loggraph $$'):
			LLG=float( f[i+1].split()[1] )
			#TFZ= float( l[l.rindex('/')+1:l.rindex('(')] )
			#return eLLG,TFZ
			return LLG
	#print 'Failure in function RJB_lib.return_LLG , it did not found eLLG and TFZ, exiting.'
	print('Function RJB_lib.return_LLG failed to find LLG in file: '+phaser_log_file+' . Exiting.')
	exit()

def return_VRMS(phaser_log_file):
	f2=open(phaser_log_file)
	f=f2.read()
	f2.close()
	i=len('   SOLU ENSEMBLE ensarci0 VRMS DELTA -0.9944 #RMSD  1.00 #VRMS  ')
	ivrms=f.index('   SOLU ENSEMBLE ensarci0 VRMS DELTA')
	vrms=f[ ivrms+i:ivrms+i+4]
	return f[ ivrms+i:ivrms+i+4]
	# print 'Function RJB_lib.return_LLG failed to find LLG in file: '+phaser_log_file+' . Exiting.'
	# exit()

def get_PhenixMapMtzMtzCC (log):
	f=open(log)
	f2=f.readlines()
	#f2.reverse()
	f.close()
	for i in range(len(f2)-1,-1,-1):
		l=f2[i]
		if l.startswith('Starting correlation:'):
			cci=float(l.split()[2])
			ccf=float(l.split()[-1])
			return cci,ccf
	print('Failure obtaining mapCC from file:',log)

def listres0occup(pdb):
	f2=open(pdb)
	f=f2.readlines()
	lres0occ=[]
	for l in f:
		if l.startswith ('ATOM') and l[56:60]=='0.00' and l[13:15]=='CA':
			ch=l[21]
			restype=amino_acid_list [ amino_acid_list_3L.index(l[17:20])]
			resnumb=int(l[22:26])
			tup=(ch, resnumb)
			lres0occ.append(tup)
			#lres0occ.append ( (ch,resnumb,restype) )

	return lres0occ

def GivenListRes0occScwrl4PDBRecover0occ (lres0occ,pdb_input,pdb_output):
	with open(pdb_input) as f: f2=f.readlines()
	with open(pdb_output,'w') as f:
		for l in f2:
			if not l.startswith('ATOM'): f.write(l)
			else:
				ch=l[21]
				resn=int(l[22:26])
				if not (ch,resn) in lres0occ: f.write(l)
				else:                         f.write(l[:56]+'0.00'+l[60:])

def convertALEPHfrags2listSSpdb (pdbinicial,pdbborgesmatrix):
	residuespdbinicial=return_tuple_chain_resnumb_restype(pdbinicial)
	listSSpdb=[]
	for i1 in residuespdbinicial:
		for i2 in i1:
			tupleres=i2
			sstype='coil'
			ch=i2[0]
			resn=i2[1]
			for i3 in pdbborgesmatrix:
				reslist = i3['reslist']
				if i3['sstype']=='coil': continue
				sstypev=i3['sstype']
				for res in reslist:
					chv=res[2]
					resnv=res[3][1]
					if chv==ch and resn==resnv: sstype=sstypev
			listSSpdb.append(tupleres+tuple([sstype]))
	return listSSpdb

#example listSSpdb: [('A', 7, 'A', 'coil'), ('A', 8, 'A', 'ah'), ('A', 9, 'A', 'ah'), ('A', 10, 'A', 'ah'),('F', 32, 'A', 'ah'), ('F', 33, 'A', 'ah'), ('F', 34, 'A', 'ah')]

def readPIRalignment (alignfile):
	dic={}
	from Bio.SeqIO import PirIO
	with open (alignfile) as f:
		for record in PirIO.PirIterator(f):
			#print record.seq
			dic[record.id]=record.seq
	return dic


#written in 11May2018 to convert dic['A']=[1,2,3,4] to folder string seq_A1-4 for SLIDER1.9.py
def convertDicChResNStr ( DicChResNStr ):
	strr = 'seq'
	strr2=''
	#for k, v in sorted (DicChResNStr.items()):
	lch=[]
	lresrange=[]

	for k, resrange in DicChResNStr.items():
		if resrange not in lresrange:
			lch.append([k])
			lresrange.append(resrange)
		else:
			lch[lresrange.index(resrange)].append(k)
	for i,v in enumerate(lresrange):
		strr2+='Chain(s) '+', '.join(lch[i])+': Residues: '
		for n in v:
			if not n - 1 in v:
				strr2 += str(n)
			if not n + 1 in v:
				strr2 += '-' + str(n) + ', '
		strr2 = strr2[:-2]
		strr2 += '\n'
	strr2=strr2[:-1]

	for k, v in DicChResNStr.items():
		strr += '_' + k
		for n in v:
			if not n - 1 in v:
				strr += str(n)
			if not n + 1 in v:
				strr += '-' + str(n) + '_'
		strr = strr[:-1]

	return strr,strr2

def GivenEdstatsOutDicChResnStats12ReturnList (RSS_output_file,DicChResn,Stat1,Stat2): #Stat usually CCSm or CCSs or CCSa m,s,a=main,side,all atoms
	f2=open(RSS_output_file)
	f=f2.readlines()
	llabels=f[0].split()
	iCh=llabels.index('CI')
	iResn=llabels.index('RN')
	if Stat1 in llabels: iStat1 = llabels.index(Stat1)
	else: print(Stat1,'not found in',RSS_output_file,'"n/a" value being atributed.')
	if Stat2 in llabels: iStat2 = llabels.index(Stat2)
	else: print(Stat2,'not found in',RSS_output_file,'"n/a" value being atributed.')
	lvar1 = []
	lvar2 = []
	for l in f[1:]:
		l=l.split()
		if l[iCh] in DicChResn and int(l[iResn]) in DicChResn[l[iCh]]:
			if Stat1 in llabels and l[iStat1]!='n/a':  lvar1.append(float( l[iStat1] ))
			if Stat2 in llabels and l[iStat2] != 'n/a':lvar2.append(float( l[iStat2] ))
	if lvar1 == []: lvar1 = 0
	if lvar2 == []: lvar2 = 0
	return lvar1,lvar2

def BestAlignment2StringsReturnIndex (st1,st2):
	if '~' in st1:
		print('~ in string 1, failure, correct code')
		exit()
	st11='~'*(len(st2)-1)+st1+'~'*(len(st2)-1)
	bestscore=0
	bestindex=0
	for i in range( len(st11)-len(st2)+1 ):
		scorevar = 0
		v1=st11[i:]
		for ii in range(len(st2)):
			if st2[ii]==v1[ii]: scorevar+=1
		# print st2
		# print v1
		# print scorevar
		# print '\n'
		if scorevar>bestscore:
			bestscore=scorevar
			bestindex=i
	bestindex-=len(st2)-1
	# print bestscore
	# print ' '*(-1*bestindex)+st1
	# print ' '*bestindex+st2
	# print bestindex
	return bestindex

def GivenTwoSequencesIdenticalRes(st1,st2):
	if len (st1)!=len(st2):
		print(st1,st2,"with different lengths (",len (st1),len(st2),")")
		exit()
	id=0
	for i in range(len(st1)):
		if st1[i]==st2[i]: id+=1
	return id

def CheckHeaderPDB (inputpdb):
	checknumb=0
	with open(inputpdb) as f:
		f2 = f.readlines()
		for l in f2:
			if l.startswith('SCALE') or l.startswith('CRYST1'): checknumb+=1
	if checknumb!=4:
		print('REQUIRED INFORMATION IN PDB HEADER NOT FOUND (CRYST1/SCALE CARDS). CORRECT THE FILE:',inputpdb)
		exit()

def ReturnShelxeCCwMPEPdbLlst ( pdb_file,lst_file ):
	with open(lst_file) as ff:
		f2=ff.readlines()
		f3=ff.read()
		if '** Unable to trace map - giving up **' in f3:
			return 'n/a','n/a','n/a','n/a','n/a' #CC,wMPE,cycle,nres,nchains
		else:
			with open(pdb_file) as f:
				l1stline = f.readlines()[0].split()
				CC = float(l1stline[6][:-1])
				cycle = int(l1stline[3])
				nres = int(l1stline[7])
				nchains = int(l1stline[10])
				# print CC,cycle,nres,nchains
			count = 0
			for l in f2:
				if l.startswith(' CC for partial structure against native data ='):
					count+=1
					if count==cycle:
						try:
							wMPE = float ( f2 [f2.index(l) + 3 ] .split()[-3] )
						except:
							wMPE = 'n/a'
						break
	return CC,wMPE,cycle,nres,nchains

def GivenSeqListChResNCASeqReturnStringRef(seqSeqPushRef , listChResNCA , Sequence ) :

	DicChResNRangeSeqVar={}

	DicChResNSeqVar=seqSeqPushRef[1]
	seqvarall=seqSeqPushRef[0]
	chvar=''
	resnvar=''
	for Ch in DicChResNSeqVar:
		#print Ch
		DicChResNRangeSeqVar[Ch]={}
		for ResN in DicChResNSeqVar[Ch]:
			#print ResN
			if (Ch==chvar and ResN-1!=resnvar) or Ch!=chvar:
				if chvar!='': DicChResNRangeSeqVar[Ch][str(ResIvar)+'-'+str(resnvar)]=seqvar
					#print 'placing dic',str(ResIvar)+'-'+str(resnvar),seqvar
				seqvar=''
				ResIvar=ResN
			#print seqvar
			seqvar += seqvarall[listChResNCA.index([Ch, ResN])]
			chvar = Ch
			resnvar = ResN
	DicChResNRangeSeqVar[Ch][str(ResIvar) + '-' + str(resnvar)] = seqvar

	strvar=''
	for Ch in DicChResNRangeSeqVar:
		for ResNRange , seqvar in DicChResNRangeSeqVar[Ch].items():
			bestindexalignment=BestAlignment2StringsReturnIndex( Sequence , seqvar )
			if strvar!='': strvar += '&'
			strvar += str(bestindexalignment) + '-' + str(bestindexalignment + len(seqvar) - 1)
			#strvar+=Ch+'_'+ResNRange+'_seq'+str(bestindexalignment)+'-'+str(bestindexalignment+len(seqvar)-1)
	return strvar

def mtz2phi_script ( file_input_mtz , file_output_phi , mtz_f=False , mtz_sigf=False , mtz_fom=False, mtz_strf=False , count=0, printt=False): #change file to variable

	if printt: print('Converting',file_input_mtz,'into',file_output_phi)

	mtz2phi_job_descr = open('mtz2phi_job_instr' + str(count) + '.txt', 'w')

	if mtz_f!=False and mtz_sigf!=False and mtz_fom!=False and mtz_strf!=False:
		mtz2phi_job_descr.write('LABIN FP='+mtz_f)
		mtz2phi_job_descr.write(' DUM1='+mtz_fom)
		mtz2phi_job_descr.write(' DUM2='+mtz_strf)
		mtz2phi_job_descr.write(' SIGFP='+mtz_sigf+' \n')

	else:
		labels_list=extract_labels_mtz_to_list ( file_input_mtz )
		types_list=extract_types_mtz_to_list ( file_input_mtz )

		mtz2phi_job_descr.write('LABIN FP=')
		if mtz_f==False:
			if 'FP' in labels_list :
				mtz2phi_job_descr.write('FP')
			elif 'F' in labels_list :
				mtz2phi_job_descr.write('F')
			elif 'FOBS' in labels_list :
				mtz2phi_job_descr.write('FOBS')
			elif 'F-obs' in labels_list:
				mtz2phi_job_descr.write('F-obs')
			elif 'F-obs-filtered' in labels_list:
				mtz2phi_job_descr.write('F-obs-filtered')
			else:
				print('mtz2phi_script was unable to find F/FP/FOBS/F-obs/F-obs-filtered from mtz file:'+file_input_mtz)
				quit()
		else:
			mtz2phi_job_descr.write(mtz_f)

		mtz2phi_job_descr.write(' DUM1=')
		if mtz_fom==False:
			try:
				FOM=labels_list[types_list.index('W')]
				mtz2phi_job_descr.write(FOM)
			except:
				mtz2phi_job_descr.write('FOM')
		else: mtz2phi_job_descr.write(mtz_fom)

		mtz2phi_job_descr.write(' DUM2=')
		if mtz_fom==False:
			if 'PHIC' in labels_list :
				mtz2phi_job_descr.write('PHIC SIGFP=')
			elif 'PHIFCALC' in labels_list :
				mtz2phi_job_descr.write('PHIFCALC SIGFP=')
			elif 'PHIF-model' in labels_list :
				mtz2phi_job_descr.write('PHIF-model SIGFP=')
			else:
				print('mtz2phi_script was unable to find PHIC/PHIFCALC from mtz file:' + file_input_mtz)
				quit()
		else: mtz2phi_job_descr.write(mtz_strf)
		if mtz_sigf==False:
			if 'SIGFP' in labels_list :
				mtz2phi_job_descr.write('SIGFP \n')
			elif 'SIGF' in labels_list :
				mtz2phi_job_descr.write('SIGF \n')
			elif 'SIGFOBS' in labels_list :
				mtz2phi_job_descr.write('SIGFOBS \n')
			elif 'SIGF-obs' in labels_list:
				mtz2phi_job_descr.write('SIGF-obs \n')
			elif 'SIGF-obs-filtered' in labels_list:
				mtz2phi_job_descr.write('SIGF-obs-filtered \n')
			else:
				print('mtz2phi_script was unable to find SIGFP/SIGF/SIGFOBS/SIGF-obs/SIGF-obs-filtered from mtz file:'+file_input_mtz)
				quit()
		else:
			mtz2phi_job_descr.write(mtz_sigf+' \n')

	mtz2phi_job_descr.write("OUTPUT USER '(3I4,F9.2,F6.3,F7.1,F8.2)' \n")
	mtz2phi_job_descr.write('END')
	mtz2phi_job_descr.close()
	mtz2phi_job_instr=open('mtz2phi_job_instr'+str(count)+'.txt','r')
	# print 'mtz2various','HKLIN',file_input_mtz,'HKLOUT',file_output_phi
	# exit()
	mtz2phi_job = subprocess.Popen([ 'mtz2various','HKLIN',file_input_mtz,'HKLOUT',file_output_phi], stdin=mtz2phi_job_instr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = mtz2phi_job.communicate()
	#print out
	mtz2phi_job_instr.close()
	if not os.path.isfile(file_output_phi):
		print('\n\n\n\n\n\nFAILURE IN FUNCTION RJB_LIB.mtz2phi_script CONVERTING',file_input_mtz,'TO',file_output_phi)
		print('Command used:')
		print('mtz2various', 'HKLIN', file_input_mtz, 'HKLOUT', file_output_phi, mtz2phi_job_instr)
		print('Instruction file:,mtz2phi_job_instr'+str(count)+'.txt')
		print('out:')
		print(out.decode())
		print('err')
		print(err.decode())
		mtz2phi_job_instr.close()
		quit()
	else:
		mtz2phi_job_instr.close()
		os.system('rm mtz2phi_job_instr'+str(count)+'.txt')
