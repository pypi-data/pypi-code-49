# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("os", "re", "numpy", "pytz", "tqdm", "pandas", "requests", "lxml")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append("{0}: {1}".format(dependency, str(e)))

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies

import os
import re
import pandas as pd
import numpy as np
import requests
from lxml import etree, objectify
import urllib.parse
from time import sleep
import json
from tqdm import tqdm

def hello():
    return (u'Hello to you too')

def download_cases_locally(courts, years, language, limit):
    """
    Define operating court and year, and create the required folder structure.
    """
    if isinstance(courts, list) is False:
        raise Exception("Courts must be an array of Strings, such as ['cjeu', 'ecthr']")
    if isinstance(years, list) is False:
        raise Exception("Years must be an array of Strings, such as ['2018', '2019']")
    if isinstance(language, str) is False:
        raise Exception("Language must be a 3 letter string, such as 'eng' or 'fra'")
    if isinstance(limit, int) is False:
        raise Exception("Limit must be a positive integer.")
    if limit>3000:
        raise Exception("Limit exceeds the maximum number of cases per year.")
        
    operating_courts = courts
    operating_years = years
    operating_language = language

    for operating_court in operating_courts:
        if operating_court == 'cjeu':
            print('Currently parsing court: ', operating_court)
            if not os.path.exists(str(operating_court)):
                    os.makedirs(str(operating_court)) # create if does not exist
            else:
                for operating_year in operating_years:
                    operating_path = os.path.join(operating_court,str(operating_year))
                    if not os.path.exists(operating_path):
                        os.makedirs(operating_path) # create if does not exist
                    else:
                        operating_year_contents = os.listdir(operating_path) # make a list
                        operating_ecli_root = 'ECLI:EU:C:' + str(operating_year) + ':'
                        operating_ecli_min = 1
                        operating_ecli_max = limit

                        for current_ecli_int in tqdm(range(operating_ecli_min, operating_ecli_max)):
                            operating_ecli_url_encoded = urllib.parse.quote(operating_ecli_root) + str(current_ecli_int)
                            operating_request_url = 'http://publications.europa.eu/resource/ecli/' + operating_ecli_url_encoded
                            operating_local_xml_filename = operating_ecli_root.replace(":", "_") + str(current_ecli_int) + '.xml'
                            operating_local_rdf_filename = operating_ecli_root.replace(":", "_") + str(current_ecli_int) + '.rdf'
                            operating_local_xml_path = os.path.join(operating_path, operating_local_xml_filename)
                            operating_local_rdf_path = os.path.join(operating_path, operating_local_rdf_filename)   
                            response = requests.get(operating_request_url, headers={'AcceptLanguage': operating_language, 'Accept': 'application/xml;notice=object'})
                            if 'Content-Type' in response.headers and response.headers['Content-Type'] == 'application/xml; notice=object;charset=UTF-8':
                                with open(operating_local_xml_path, 'w', encoding='utf-8') as f:
                                    f.write(response.text)
                            else:
                                print('Skipped case: ', operating_ecli_root, current_ecli_int, '. Language ', operating_language, ' was not found in Cellar.')
        elif operating_court == 'ecthr':
            print('Currently parsing court: ', operating_court)
            if not os.path.exists(str(operating_court)):
                    os.makedirs(str(operating_court)) # create if does not exist
            else:
                for operating_year in operating_years:
                    operating_path = os.path.join(operating_court,str(operating_year))
                    if not os.path.exists(operating_path):
                        os.makedirs(operating_path) # create if does not exist
                    else:
                        print('Not yet implemented, but its on its way.')
                
        else:
            print(operating_court, ' is currently not supported. It will be skipped.')

def get_standard_fields_from_cjeu_xml(file_path):

    """
    Parse the xml file to get standard fields necessary for building a dataframe
    """
    with open(file_path) as fobj:
        xml = fobj.read().encode("utf-8")

    root = objectify.fromstring(xml)

    return_value = "COULD NOT PARSE XML"
    this_ecli = "ECLI ERROR"
    this_full_date = "FULL DATE ERROR"
    this_year = "YEAR ERROR"
    this_month = "MONTH ERROR"
    this_day = "DAY ERROR"
    this_celex = "CELEX ERROR"
    this_cellar = "CELLAR ERROR"
    this_document_type = "DOCUMENT TYPE ERROR"
    this_language = "LANGUAGE ERROR"
    this_document_title = "DOCUMENT TITLE ERROR"
    
    for appt in root.getchildren():
        for elem in appt.getchildren():
            if elem.tag == "ECLI": # parse the ECLI number
                for sub_elem in elem.getchildren():
                    if sub_elem.tag == "VALUE":
                        this_ecli = sub_elem.text
            elif elem.tag == "DATE_DOCUMENT":  # parse the DATE, YEAR, MONTH and DAY
                for sub_elem in elem.getchildren():
                    if sub_elem.tag == "VALUE":
                        this_full_date = sub_elem.text
                    elif sub_elem.tag == "YEAR":
                        this_year = sub_elem.text
                    elif sub_elem.tag == "MONTH":
                        this_month = sub_elem.text
                    elif sub_elem.tag == "DAY":
                        this_day = sub_elem.text
            elif elem.tag == "ID_CELEX": # parse the CELEX ID
                for sub_elem in elem.getchildren():
                    if sub_elem.tag == "VALUE":
                        this_celex = sub_elem.text
            elif elem.tag == "WORK_HAS_RESOURCE-TYPE": # parse the DOCUMENT TYPE
                for sub_elem in elem.getchildren():
                    if sub_elem.tag == "PREFLABEL":
                        this_document_type = sub_elem.text
            elif elem.tag == "WORK_PART_OF_WORK": # parse the LANGUAGE AND TITLE
                for sub_elem in elem.getchildren():
                    if sub_elem.tag == "EMBEDDED_NOTICE":
                        for sub_sub_elem in sub_elem.getchildren():
                            if sub_sub_elem.tag == "EXPRESSION":
                                for sub_sub_sub_elem in sub_sub_elem.getchildren():
                                    if sub_sub_sub_elem.tag == "EXPRESSION_USES_LANGUAGE":
                                        for sub_sub_sub_sub_elem in sub_sub_sub_elem.getchildren():
                                            if sub_sub_sub_sub_elem.tag == "IDENTIFIER":
                                                this_language = sub_sub_sub_sub_elem.text
                                    elif sub_sub_sub_elem.tag == "EXPRESSION_TITLE":
                                        for sub_sub_sub_sub_elem in sub_sub_sub_elem.getchildren():
                                            if sub_sub_sub_sub_elem.tag == "VALUE":
                                                this_document_title = sub_sub_sub_sub_elem.text
            elif elem.tag == "URI": # parse the CELLAR ID
                for sub_elem in elem.getchildren():
                    if sub_elem.tag == "VALUE":
                        this_cellar = sub_elem.text
            else: 
                pass
    return {
        "ecli": this_ecli, 
        "celex": this_celex, 
        "cellar": this_cellar, 
        "document_type": this_document_type, 
        "full_date": this_full_date, 
        "year": this_year, 
        "month": this_month, 
        "day": this_day, 
        "language": this_language, 
        "document_title": this_document_title
    }

def get_file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size
    
def build_local_cjeu_dataframe(year, limit):
    if isinstance(year, int) is False:
        raise Exception("Year must be an integer, such as 2019")
    if isinstance(limit, int) is False:
        raise Exception("Limit must be a positive integer.")
    if limit>3000:
        raise Exception("Limit exceeds the maximum number of cases per year.")
        
    operating_court = 'cjeu'
    operating_year = year
    operating_limit = limit
    
    operating_path = os.path.join(operating_court,str(operating_year))
    
    print('Currently parsing court: ', operating_court, ' using path: ', operating_path)
    
    operating_file_list = []

    for root, dirs, files in os.walk(operating_path):
        for file in files:
            if file.endswith('.xml'):
                try:
                    file_path = os.path.join(operating_path,str(file))
                    file_size = get_file_size(file_path)
                    if file_size > 5:
                        print(file_path, ',', file_size)
                        operating_file_list.append(file)
                except:
                    pass
#     print('Working with: ', operating_file_list)
    
    operating_df = pd.DataFrame()
    operating_range = 0
    
    for single_xml_file in tqdm(operating_file_list[:int(operating_limit)]):
        operating_file_path = os.path.join(operating_path,str(single_xml_file))
        operating_df = operating_df.append(get_standard_fields_from_cjeu_xml(operating_file_path), ignore_index=True)
        
    return operating_df
