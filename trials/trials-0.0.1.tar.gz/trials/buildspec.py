
import pandas as pd
from pandas.io.sas.sas_xport import XportReader
from pandas.io.sas.sas7bdat import SAS7BDATReader
import xlsxwriter
import os
import glob
import argparse
import logging
def format_worksheet(worksheet, header_dict):

		for col_header in header_dict:
				col_ltr = col_header[0]
				worksheet.write(col_ltr+'1', col_header[1], header_format)
				worksheet.set_column(col_ltr+':'+col_ltr, col_header[2])
				
def build_sas7bdat_spec(ds_workbook, var_workbook, directory):

		# find all SAS files in a direcotry
		sas_files = glob.glob(directory+'*.sas7bdat')
		sas_files.sort()

		dataset_count = 1
		variable_count = 0
		row_count = 1
		for sas_file in sas_files:
				dataset_count += 1
				dataset = sas_file.split('/')[-1].replace('.sas7bdat','').upper()
				ds_workbook.write('A'+str(dataset_count), dataset)
				variable_count = 0		
				reader = SAS7BDATReader(sas_file)
				for index in range(len(reader.column_names)):
						row_count += 1
						variable_count += 1
						col_num=str(row_count)

						# Order
						var_workbook.write('A'+col_num, variable_count)
						# Dataset
						var_workbook.write('B'+col_num, dataset)
						# Variable Name
						var_name = reader.columns[index].name
						var_workbook.write('C'+col_num, var_name)
						# Variable Label
						var_workbook.write('D'+col_num, reader.columns[index].label)
						# Variable Type
						if reader.columns[index].ctype==b's':
								var_type='text'
						else:
								var_type='integer'
						if var_name.endswith('DTC'):
								var_type='datetime'
						var_workbook.write('E'+col_num, var_type)
						# Variable Length
						var_workbook.write('F'+col_num, reader.columns[index].length)

		workbook.close()

def build_xpt_spec(ds_workbook, var_workbook, directory):

		# find all SAS files in a direcotry
		sas_files = glob.glob(directory+'*.xpt')
		sas_files.sort()

		dataset_count = 1
		variable_count = 0
		row_count = 1
		for sas_file in sas_files:
				dataset_count += 1
				dataset = sas_file.split('/')[-1].replace('.xpt','').upper()
				ds_workbook.write('A'+str(dataset_count), dataset)
				variable_count = 0		
				reader = XportReader(sas_file)
				for field in reader.fields:
						row_count += 1
						variable_count += 1
						col_num=str(row_count)

						# Order
						var_workbook.write('A'+col_num, variable_count)
						# Dataset
						var_workbook.write('B'+col_num, dataset)
						# Variable Name
						var_name = field.get('name').decode()
						var_workbook.write('C'+col_num, var_name)
						# Variable Label
						var_workbook.write('D'+col_num, field.get('label').decode())
						# Variable Type
						if field.get('ntype')=='char':
								var_type='text'
						else:
								var_type='integer'
						if var_name.endswith('DTC'):
								var_type='datetime'
						var_workbook.write('E'+col_num, var_type)
						# Variable Length
						var_workbook.write('F'+col_num, field.get('field_length'))

		workbook.close()

def buildspec(directory, xlsx_name, use_xpt):
		try:
			global header_format, workbook
			if (directory):
					if not os.path.exists(directory):
							logging.warning('XPT/SAS7BDAT Location ' + directory + ' does not exist')
							exit(1)
			else:
					# assume current directory
					directory='./'

			if not directory.endswith('/'):
					directory=directory+'/'

			if (xlsx_name):
					""" Check if file name ends with .xlsx,
					if not add it"""
					dstname=xlsx_name
					if not dstname.endswith('.xlsx'):
						dstname = dstname + '.xlsx'

			else:
					dstname='Python_Generated_Define_Spec.xlsx'

			# Create an new Excel file.
			workbook = xlsxwriter.Workbook(dstname)

			# default cell format to size 8 
			workbook.formats[0].set_font_size(10)# Add a header format.

			header_format = workbook.add_format({
				'bold': False,
				'text_wrap': True,
				'valign': 'top',
				'fg_color': 'orange',
				'border': 1})

			cols='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

			# Add study worksheet to workbook
			study = workbook.add_worksheet('Study')
			stdy_header={('A','Attribute',15), ('B','Value',80)}
			format_worksheet(study, stdy_header)
			study.write('A2','StudyName')
			study.write('A3','StudyDescription')
			study.write('A4','ProtocolName')
			study.write('A5','StandardName')
			study.write('A6','StandardVersion')
			study.write('A7','Language')
			study.write('A8','SDTMCTVersion')
			study.write('A9','ADaMCTVersion')

			# Add datasets worksheet to workbook
			datasets = workbook.add_worksheet('Datasets')
			ds_header={('A','Dataset',8), ('B','Description',40), ('C','Class',10) , ('D','Structure',10), 
				('E','Purpose',10), ('F','Key Variables',50), ('G','Repeating',10), ('H','Reference Data',10), ('I','Comment',10)}
			format_worksheet(datasets, ds_header)

			# Add variables worksheet to workbook
			variables = workbook.add_worksheet('Variables')
			var_header={('A','Order',6), ('B','Dataset',8), ('C','Variable',20), ('D','Label',40), ('E','Data Type',10), 
				('F','Length',10), ('G','Significant Digits',10), ('H','Format',10),('I','Mandatory',10), ('J','Codelist',10), 
				('K','Origin',10),('L','Pages',10), ('M','Method',10), ('N','Predecessor',15), ('O','Role',10), ('P','Comment',10)}
			format_worksheet(variables, var_header)

			# Add Value Level worksheet to workbook
			vlm = workbook.add_worksheet('ValueLevel')
			vlm_header={('A','Order',6), ('B','Dataset',8), ('C','Variable',20), ('D','Where Clause',40), ('E','Description',40),
				('F','Data Type',10) , ('G','Length',10), ('H','Significant Digits',10), ('I','Format',10), ('J','Mandatory',10),
				('K','Codelist',10), ('L','Origin',10), ('M','Pages',10), ('N','Method',10), ('O','Predecessor',15), ('P','Comment',10)}
			format_worksheet(vlm, vlm_header)

			# Add Where Clauses worksheet to workbook
			where_clauses = workbook.add_worksheet('WhereClauses')
			where_clauses_header={('A','ID',6), ('B','Dataset',8), ('C','Variable',20), ('D','Comparator',40), ('E','Value',10)}
			format_worksheet(where_clauses, where_clauses_header)

			# Add Codelists worksheet to workbook
			codelist = workbook.add_worksheet('Codelists')
			codelist_header={('A','ID',6), ('B','Name',8), ('C','NCI Codelist Code',20), ('D','Data Type',40), ('E','Order',10),
				('F','Term',20) , ('G','NCI Term Code',10), ('H','Decoded Value',40)}
			format_worksheet(codelist, codelist_header)

			# Add Dictionaries worksheet to workbook
			dictionaries = workbook.add_worksheet('Dictionaries')
			dictionaries_header={('A','ID',6), ('B','Name',8), ('C','Data Type',40), ('D','Dictionary',40), ('E','Version',10)}
			format_worksheet(dictionaries, dictionaries_header)

			# Add Methods worksheet to workbook
			methods = workbook.add_worksheet('Methods')
			methods_header={('A','ID',6), ('B','Name',8), ('C','Type',40), ('D','Description',60), ('E','Expression',10),
				('F','Code',10) , ('G','Document',10), ('H','Pages',10)}
			format_worksheet(methods, methods_header)

			# Add Comments worksheet to workbook
			comments = workbook.add_worksheet('Comments')
			comments_header={('A','ID',6), ('B','Description',15), ('C','Document',40), ('D','Pages',40)}
			format_worksheet(comments, comments_header)

			# Add Documents worksheet to workbook
			documents = workbook.add_worksheet('Documents')
			documents_header={('A','ID',6), ('B','Title',8), ('C','Href',40)}
			format_worksheet(documents, documents_header)

			# Add Analysis Displays to workbook
			analysis_displays = workbook.add_worksheet('Analysis Displays')
			analysis_displays_header={('A','ID',6), ('B','Title',8), ('C','Document',40), ('D','Pages',20)}
			format_worksheet(analysis_displays, analysis_displays_header)

			# Add Analysis Results to workbook
			analysis_results = workbook.add_worksheet('Analysis Results')
			analysis_results_header={('A','Display',15), ('B','ID',8), ('C','Description',40), ('D','Reason',20), ('E','Purpose',8), ('F','Documentation',20),
				('G','Documentation Refs',20), ('H','Programming Context',20), ('I','Programming Code',20), ('J','Programming Document',25)}
			format_worksheet(analysis_results, analysis_results_header)

			# Add Analysis Criteria to workbook
			analysis_criteria = workbook.add_worksheet('Analysis Criteria')
			analysis_criteria_header={('A','Display',15), ('B','Result',15), ('C','Dataset',10), ('D','Variables',20), ('E','Where Clause',20)}
			format_worksheet(analysis_criteria, analysis_criteria_header)

			if (use_xpt):
					build_xpt_spec(datasets, variables, directory)
			else:
					build_sas7bdat_spec(datasets, variables, directory)
		except:
			logging.error('Errors creating spec: ' + xlsx_name + ' was NOT created.')

if __name__ == '__main__':
	# Parse command line arguments
	parser = argparse.ArgumentParser(description='Python define.xml 2.0 metadata xlsx spec generator')
	parser.add_argument('xlsx_name', nargs='?', help='Name and Location of Define Metadata Spec to Be Created', default=None)
	parser.add_argument('-d','--directory',nargs=1,help='Location of XPT or SAS7BDAT Files',type=str)
	parser.add_argument('-x','--xpt', nargs=1, help='Specify if using XPT files in directory (Y/N)', default=False)

	args = parser.parse_args()
	
	if args.directory != None:
		input1 = args.directory[0]
		buildspec(input1, args.xlsx_name, args.xpt[0])
	else:
		buildspec(None,args.xlsx_name, args.xpt[0])
