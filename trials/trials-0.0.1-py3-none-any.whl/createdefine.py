""" to do
1. fix stylesheet hack
2. ARM - ParameterOID, Pagerefs, check for blank values
"""

import pandas as pd
import os
import shutil
import pandas
from lxml import etree
import pandas as pd
import datetime
import argparse
import logging

# set up namespaces necessary for define 2.0
ns_def="http://www.cdisc.org/ns/def/v2.0"
ns_xlink="http://www.w3.org/1999/xlink"
ns_odm="http://www.cdisc.org/ns/odm/v1.3"
ns_arm="http://www.cdisc.org/ns/arm/v1.0"
ns_xml="http://www.w3.org/XML/1998/namespace"

# create dictionary of namespace mappings
NSMAP = {"def"   : ns_def,
         "xlink" : ns_xlink,
         None    : ns_odm,
         "arm"   : ns_arm,
         "xml"	 : ns_xml}


def write_define_xml(root):

		# doing this makes pretty_print work
		for element in root.iter():
		    element.tail = None
			
		# create the xml string
		obj_xml = etree.tostring(root,
		                         pretty_print=True,
		                         xml_declaration=True,
		                         encoding='UTF-8')
		

		with open("temp_define.xml", "wb") as xml_writer:
				xml_writer.write(obj_xml)

    # Hack - replace 2nd line of file with stylesheet.  lxml strips it

		# read in temp define xml
		from_file = open("temp_define.xml") 
		line = from_file.readline()

		# update python program to point at virtual enviroment interpreter
		to_file = open("define.xml", mode="w")
		to_file.write(line + "\n" + '<?xml-stylesheet type="text/xsl" href="define2-0-0.xsl"?>\n')

		# save updated utility
		shutil.copyfileobj(from_file, to_file)

		# close file handles
		from_file.close()
		to_file.close()
		os.remove("temp_define.xml")

#### Build Description Section
def build_xml_Description(node, description):
		if not pd.isna(description):
				desc=etree.SubElement(node,"Description")
				trantxt=etree.SubElement(desc,"TranslatedText")
				trantxt.text=description
				trantxt.set("{%s}lang" % (ns_xml), "en")	

#### Build Origin Section
def build_xml_Origin(node, origin, pages, predecessor):

		orgtype=etree.SubElement(node,"{%s}Origin" % (ns_def))
		orgtype.set("Type",origin)

		if origin=='CRF' and not pd.isna(pages):
				docref=etree.SubElement(orgtype,"{%s}DocumentRef" % (ns_def))
				docref.set("leafID","LF.acrf")
				pdfref=etree.SubElement(docref, "{%s}PDFPageRef" %(ns_def))
				pdfref.set("Type","PhysicalRef")
				pdfref.set("PageRefs",str(int(pages)))
		elif origin=='Predecessor':
				build_xml_Description(orgtype, predecessor)

#### Build GlobalVariables Section
def build_xml_GlobalVariables(node):

		# Add Global Variables section
		global_vars=etree.SubElement(node,'GlobalVariables')
		study_name=etree.SubElement(global_vars,"StudyName")
		study_name.text=vstudy_name
		study_desc=etree.SubElement(global_vars,"StudyDescription")
		study_desc.text=vstudy_desc
		prot_name=etree.SubElement(global_vars,"ProtocolName")
		prot_name.text=vprotocol_name

#### Add Metadata Version and Supplmeental Doc sections
def build_xml_MetadataVersion(node):
	
		mdv=etree.SubElement(node,"MetaDataVersion")
		mdv.set("OID",mdv_oid)
		mdv.set("{%s}DefineVersion" % (ns_def),"2.0.0") 
		mdv.set("Name", "Study "+vstudy_name+" Data Definitions")
		mdv.set("{%s}StandardName" % (ns_def), vstandard_name)
		mdv.set("{%s}StandardVersion" % (ns_def), vstandard_version)
		mdv.set("Description", vstudy_desc)

		
		# Add Annotated CRF if it exists
		df_doc = pd.read_excel(xlsxname, sheet_name='Documents')
		df_doc.columns = df_doc.columns.str.lower()		
		for index, row in df_doc.head().iterrows():
				if row['id'] == 'acrf':
						acrf=etree.SubElement(mdv,"{%s}AnnotatedCRF" % (ns_def))
						docref=etree.SubElement(acrf,"{%s}DocumentRef" % (ns_def))
						docref.set("leafID","LF."+row['id'])

		# Add SupplementalDoc section
		suppdoc=etree.SubElement(mdv,"{%s}SupplementalDoc" % (ns_def))

		df_doc = pd.read_excel(xlsxname, sheet_name='Documents')
		df_doc.columns = df_doc.columns.str.lower()
		for index, row in df_doc.head().iterrows():
				if row['id'] != 'acrf':
						docref=etree.SubElement(suppdoc,"{%s}DocumentRef" % (ns_def))
						docref.set("leafID","LF."+row['id'])
		return mdv

#### Build ValueListDef Section
def build_xml_valueListDef(node):

		df_vl = pd.read_excel(xlsxname, sheet_name='ValueLevel')
		df_vl.columns = df_vl.columns.str.lower()
		dataset='12345678'
		variable='12345678'

		for index, row in df_vl.iterrows():

				# Add ValueListDef			
				if row['dataset'] != dataset or row['variable'] != variable:	
						dataset=row['dataset']
						variable=row['variable']
						vldef=etree.SubElement(node,"{%s}ValueListDef" % (ns_def))
						vldef.set("OID","VL."+dataset+"."+variable)

				# Add ItemRefs
				itemref=etree.SubElement(vldef,"ItemRef")
				itemref.set("ItemOID","IT."+dataset+'.'+variable+'.'+row['where clause'])
				itemref.set("OrderNumber",str(row['order']))
				itemref.set("Mandatory",row['mandatory'])

				if not pd.isna(row['method']):
						itemref.set("MethodOID",row['method'])

				# Add WhereClauseRef to Item Ref
				wcdef=etree.SubElement(itemref,"{%s}WhereClauseRef" % (ns_def))
				wcdef.set("WhereClauseOID", row['where clause'])

#### Build Where Clause Section
def build_xml_whereClauseDef(node):

		df_wc = pd.read_excel(xlsxname, sheet_name='WhereClauses')
		df_wc.columns = df_wc.columns.str.lower()
		for index, row in df_wc.iterrows():

				wcdef=etree.SubElement(node,"{%s}WhereClauseDef" % (ns_def))
				wcdef.set("OID", row['id'])
				rngchk=etree.SubElement(wcdef,"RangeCheck")
				rngchk.set("SoftHard","Soft") # when is it hard?
				rngchk.set("{%s}ItemOID" % (ns_def), "IT."+row['dataset']+"."+row['variable'])
				rngchk.set("Comparator",row['comparator'])
				chkval=etree.SubElement(rngchk, "CheckValue")
				chkval.text=row['value']

#### Build Item Group Def Section
def build_xml_itemGroupDef(node):

		df_ds = pd.read_excel(xlsxname, sheet_name='Datasets')
		df_ds.columns = df_ds.columns.str.lower()
		df_allvars = pd.read_excel(xlsxname, sheet_name='Variables')
		df_allvars.columns = df_allvars.columns.str.lower()
		for index, row in df_ds.iterrows():

				dataset=str(row['dataset'])
				keylist=str(row['key variables']).split(',')

				igdef=etree.SubElement(node,"ItemGroupDef")
				igdef.set("OID","IG."+dataset)
				igdef.set("Name",dataset)
				igdef.set("Repeating",blank_if_nan(row['repeating']))
				igdef.set("IsReferenceData",blank_if_nan(row['reference data']))
				igdef.set("SasDatasetName",dataset)
				igdef.set("Purpose",blank_if_nan(row['purpose']))
				igdef.set("{%s}Structure" % (ns_def), blank_if_nan(row['structure']))
				igdef.set("{%s}Class" % (ns_def), blank_if_nan(row['class']))
				if not pd.isna(row['comment']):				
						igdef.set("{%s}CommentOID" % (ns_def), row['comment'])
				igdef.set("{%s}ArchiveLocationID" % (ns_def), "LF."+dataset)
				build_xml_Description(igdef, row['description']);

				# Subset dataframe to have only the variables for the current dataset
				df_vars = df_allvars.loc[lambda x: x['dataset'] == dataset]

				for index, row in df_vars.iterrows():
						variable=row['variable']
						itref=etree.SubElement(igdef,"ItemRef")
						itref.set("ItemOID","IT."+dataset+"."+variable)
						itref.set("OrderNumber",str(row['order']))
						itref.set("Mandatory",str(row['mandatory']))
						if variable in keylist:
								key_seq = keylist.index(variable) + 1
								itref.set("KeySequence",str(key_seq))

						if not pd.isna(row['method']):
								itref.set("MethodOID",row['method'])
						if not pd.isna(row['role']):
								itref.set("Role",row['role'])

				# Build link to xpt dataset
				dslink=etree.SubElement(igdef,"{%s}leaf" % (ns_def))
				dslink.set("ID","LF."+dataset)
				dslink.set("{%s}href" % (ns_xlink), dataset+".xpt")
				title=etree.SubElement(dslink, "{%s}title" % (ns_def))
				title.text=dataset+".xpt"

#### Build Item Def Section
def build_xml_itemDef(node):

		# Load variables tab into a pandas dataframe
		df_allvars = pd.read_excel(xlsxname, sheet_name='Variables')
		df_allvars.columns = df_allvars.columns.str.lower()
		# Load value level tab into a pandas dataframe
		df_vl = pd.read_excel(xlsxname, sheet_name='ValueLevel')
		df_vl.columns = df_vl.columns.str.lower()
		# Build ItemDefs from Variables Page
		for index, row in df_allvars.iterrows():
				dataset=row['dataset']
				variable=row['variable']
				itdef=etree.SubElement(node,"ItemDef")
				itdef.set("OID","IT."+dataset+"."+variable)
				itdef.set("Name",variable)
				itdef.set("DataType",row['data type'])
				if not pd.isna(row['length']):
						itdef.set("Length",str(int(row['length'])))
				itdef.set("SASFieldName",variable)
				if not pd.isna(row['significant digits']):
						itdef.set("SignificantDigits", str(row['significant digits']))

				build_xml_Description(itdef, row['label'])

				if not pd.isna(row['codelist']):
						cdlist=etree.SubElement(itdef,"CodeListRef")
						cdlist.set("CodeListOID","CL."+row['codelist'])

				if not pd.isna(row['format']):
						itdef.set("{%s}DisplayFormat" % (ns_def),str(row['format']))
						
				if not pd.isna(row['comment']):
						itdef.set("{%s}CommentOID" % (ns_def),row['comment'])

				# create origin (need to join up with value level page to determine if there is value levelmetadata)
				df_vl_this_var = df_vl[(df_vl['dataset'] == dataset) & (df_vl['variable'] == variable)]
				if len(df_vl_this_var)>0:
						vlref=etree.SubElement(itdef,"{%s}ValueListRef" % (ns_def))
						vlref.set("ValueListOID","VL."+row['dataset']+"."+row['variable'])

				if not pd.isna(row['origin']):
						build_xml_Origin(itdef, row['origin'], row['pages'], row['predecessor'])

		# Build ItemDefs from Value Level Page
		for index, row in df_vl.iterrows():		
				itdef=etree.SubElement(node,"ItemDef")
				itdef.set("OID", "IT."+row['dataset']+'.'+row['variable']+'.'+row['where clause'])
				itdef.set("Name", row['variable']+'.'+row['where clause'])
				itdef.set("DataType", row['data type'])
				itdef.set("Length", str(int(row['length'])))
				itdef.set("SASFieldName", str(row['variable']))

				if not pd.isna(row['significant digits']):
						itdef.set("SignificantDigits", str(row['significant digits']))

				if not pd.isna(row['codelist']):
						cdlist=etree.SubElement(itdef,"CodeListRef")
						cdlist.set("CodeListOID","CL."+row['codelist'])			

				if not pd.isna(row['format']):
						itdef.set("{%s}DisplayFormat" % (ns_def), str(row['format']))

				# create origin
				if not pd.isna(row['origin']):
						build_xml_Origin(itdef, row['origin'], row['pages'], row['predecessor'])

#### Build Code List Section
def build_xml_CodeList(node):
	
		df_cl = pd.read_excel(xlsxname, sheet_name='Codelists')
		df_cl.columns = df_cl.columns.str.lower()
		codelist='12345678'
		for index, row in df_cl.iterrows():		
			
				if row['id'] != codelist:
						codelist=row['id']						
						cdlst=etree.SubElement(node,"CodeList")					
						cdlst.set("OID", "CL."+codelist)
						cdlst.set("Name", row['name'])
						cdlst.set("DataType", row['data type'])
						
						ncicode=row['nci codelist code']
						if not pd.isna(ncicode):
								alias=etree.SubElement(cdlst,"Alias")
								alias.set("Name",row['nci codelist code'])
								alias.set("Context", "nci:ExtCodeID")
				
				if pd.isna(row['decoded value']):								
						cdlstitm=etree.SubElement(cdlst,"EnumeratedItem")
				else:
						cdlstitm=etree.SubElement(cdlst,"CodeListItem")
				cdlstitm.set("CodedValue",str(row['term']))
				cdlstitm.set("OrderNumber",str(row['order']))
				nciterm=row['nci term code']
				if not pd.isna(nciterm):
						alias=etree.SubElement(cdlstitm,"Alias")
						alias.set("Name",row['nci term code'])
						alias.set("Context", "nci:ExtCodeID")
						
				if not pd.isna(ncicode) and pd.isna(nciterm):
						cdlstitm.set("{%s}ExtendedValue" % (ns_def), "Yes")

				if not pd.isna(row['decoded value']):				
						decod=etree.SubElement(cdlstitm,"Decode")
						trantxt=etree.SubElement(decod,"TranslatedText")
						trantxt.text=row['decoded value']
						trantxt.set("{%s}lang" % (ns_xml), "en")	

				
def build_xml_MethodDef(node):

		df_md = pd.read_excel(xlsxname, sheet_name='Methods')
		df_md.columns = df_md.columns.str.lower()		
		for index, row in df_md.iterrows():		
				mthdef=etree.SubElement(node,"MethodDef")
				mthdef.set("OID",row['id'])
				mthdef.set("Name",row['name'])
				mthdef.set("Type",row['type'])
				
				if not pd.isna(row['description']):				
						build_xml_Description(mthdef, row['description'])					
			  
def build_xml_CommentDef(node):
	
		df_cm = pd.read_excel(xlsxname, sheet_name='Comments')
		df_cm.columns = df_cm.columns.str.lower()
		
		for index, row in df_cm.iterrows():
				cmtdef=etree.SubElement(node,"{%s}CommentDef" % (ns_def))
				cmtdef.set("OID",row['id'])

				if not pd.isna(row['description']):
						build_xml_Description(cmtdef, row['description'])

def build_xml_external_docs(node):

		df_xdoc = pd.read_excel(xlsxname, sheet_name='Documents')
		df_xdoc.columns = df_xdoc.columns.str.lower()

		for index, row in df_xdoc.iterrows():
				leaf=etree.SubElement(node,"{%s}leaf" % (ns_def))
				leaf.set("ID","LF."+row['id'])
				leaf.set("{%s}href" % (ns_xlink), row['href'])
				title=etree.SubElement(leaf, "{%s}title" % (ns_def))
				title.text=row['title']

def build_xml_arm(node):

		df_adisplays = pd.read_excel(xlsxname, sheet_name='Analysis Displays')
		df_adisplays.columns = df_adisplays.columns.str.lower()

		if len(df_adisplays.index)==0:
				exit()

		df_aresults = pd.read_excel(xlsxname, sheet_name='Analysis Results', index=['Display'])
		df_aresults.columns = df_aresults.columns.str.lower()
		
		df_acriteria = pd.read_excel(xlsxname, sheet_name='Analysis Criteria', index=['Display'])
		df_acriteria.columns = df_acriteria.columns.str.lower()

		ards=etree.SubElement(node,"{%s}AnalysisResultDisplays" % (ns_arm))

		for index, row in df_adisplays.iterrows():

				rd=etree.SubElement(ards,"{%s}ResultDisplay" % (ns_arm))
				display=row['id']
				rd.set("OID","RD."+display)
				rd.set("Name",display)
				build_xml_Description(rd, row['title'])

				docref=etree.SubElement(rd,"{%s}DocumentRef" % (ns_def))
				docref.set("leafID","LF."+row['document'])
				pdfref=etree.SubElement(docref, "{%s}PDFPageRef" %(ns_def))
				pdfref.set("Type","PhysicalRef")
				pdfref.set("PageRefs",str(row['pages']))

				# Join up with Analysis results for this display
				df_ar_this_display = df_aresults[(df_aresults['display'] == display)]
				
				for index, ar_row in df_ar_this_display.iterrows():
						ar=etree.SubElement(rd,"{%s}AnalysisResult" % (ns_arm))
						ar.set("OID","AR."+ar_row['ID'])
						#ar.set("ParameterOID','') # ??? where to get this info?
						ar.set("AnalysisReason",ar_row['reason'])
						ar.set("AnalysisPurpose",ar_row['purpose'])
						build_xml_Description(ar, ar_row['description'])

						# Join up with Analysis results for this display
						df_ac_this_display = df_acriteria[(df_acriteria['display'] == display)]
						if len(df_ac_this_display.index)!=0:
								ads=etree.SubElement(ar,"{%s}AnalysisDatasets" % (ns_arm))
								ads.set("{%s}CommentOID" %(ns_def),"COM."+ar_row['join comment'])
								for index, ac_row in df_ac_this_display.iterrows():
										ad=etree.SubElement(ads,"{%s}AnalysisDataset" % (ns_arm))
										ad.set("ItemGroupOID","IG."+ac_row['dataset'])
										wcref=etree.SubElement(ad,"{%s}WhereClauseRef" % (ns_def))
										wcref.set("WhereClauseOID", "WC."+ac_row['where clause'])
										if not pd.isna(ac_row['variables']):
												av=etree.SubElement(ad,"{%s}AnalysisVariable" % (ns_arm))
												av.set("ItemOID","IT."+ac_row['dataset']+'.'+ac_row['variables'])

						doc=etree.SubElement(ar, "{%s}Documentation" % (ns_arm))
						if not pd.isna(ar_row['documentation']):
								build_xml_Description(doc, ar_row['documentation'])
						if not pd.isna(ar_row['Documentation refs']):
								docref=etree.SubElement(doc,"{%s}DocumentRef" % (ns_def))
								docref.set("leafID","LF."+ar_row['documentation refs'])
								pdfref=etree.SubElement(docref, "{%s}PDFPageRef" %(ns_def))
								pdfref.set("Type","PhysicalRef")
								#pdfref.set("PageRefs",str(row['pages']))
						if not pd.isna(ar_row['programming code']):
								pc=etree.SubElement(ar,"{%s}ProgrammingCode" % (ns_arm))
								pc.set('Context',ar_row['programming context'])
								pgcode=etree.SubElement(pc,"{%s}Code" % (ns_arm))
								pgcode.text=ar_row['programming code']
								docref=etree.SubElement(pc,"{%s}DocumentRef" % (ns_def))
								docref.set("leafID","LF."+ar_row['programming document'])
 
def blank_if_nan(value):
		if pd.isna(value):
				return ''
		else:
				return value

#### Main body of program

def createdefine(specdoc, arm):
	try:
		if specdoc == None:
				logging.warning('Metadata Spec file, not specified')
				exit(1)		
		if not (os.path.isfile(specdoc)):
				logging.warning('Metadata Spec file, ' + specdoc + ' does not exist')
				exit(1)

		global xlsxname
		xlsxname=specdoc
			
		# read spec in pandas dataframe			
		df_study = pd.read_excel(xlsxname, sheet_name='Study', index_col="Attribute")
		
		# set useful variables from study page of spec
		global vstudy_name, vstudy_desc, vprotocol_name, mdv_oid, vstandard_name, vstandard_version
		vstudy_name=blank_if_nan(df_study.loc["StudyName"].iloc[0])
		vstandard_name=blank_if_nan(df_study.loc["StandardName"].iloc[0])
		vstudy_desc=blank_if_nan(df_study.loc["StudyDescription"].iloc[0])
		vprotocol_name=blank_if_nan(df_study.loc["ProtocolName"].iloc[0])
		vstandard_version=blank_if_nan(df_study.loc["StandardVersion"].iloc[0])
		vstudy_oid=vstudy_name+"."+vstandard_name+'.'+vstandard_version
		mdv_oid="MDV."+vstudy_oid+'.'+vstandard_version

		# create ODM element
		odm=etree.Element('ODM', nsmap = NSMAP)

		# add ODM attributes
		odm.set("ODMVersion","1.3.2")
		odm.set("FileType","Snapshot")
		odm.set("CreationDateTime",datetime.datetime.now().replace(microsecond=0).isoformat())
		odm.set("SourceSystem","lxml_define")
		odm.set("SourceSystemVersion","1.0")
		
		# Add Study Tag
		study=etree.SubElement(odm,'Study')
		study.set("OID",vstudy_oid)
		
		      	
		#### Calls to major functions to build xml
		build_xml_GlobalVariables(study)
		mdv=build_xml_MetadataVersion(study)
		build_xml_valueListDef(mdv)
		build_xml_whereClauseDef(mdv)
		build_xml_itemGroupDef(mdv)
		build_xml_itemDef(mdv)
		build_xml_CodeList(mdv)
		build_xml_MethodDef(mdv)
		build_xml_CommentDef(mdv)
		build_xml_external_docs(mdv)
		if arm:
				build_xml_arm(mdv)	
		write_define_xml(odm)
	except:
		logging.error('Errors creating define.xml, XML was NOT created.')

if __name__ == '__main__':
	# Parse command line arguments
	parser = argparse.ArgumentParser(description='Python define.xml 2.0 generator')
	parser.add_argument('xlsx_name',nargs='?', help='Name and Location of Define Metadata Spec to Use to Create Define.XML', default=None)
	parser.add_argument('-a','--arm', nargs=1, help='Specify if creation of ARM is wanted (Y)', default=None)
	
	args = parser.parse_args()

	createdefine(args.xlsx_name,args.arm)