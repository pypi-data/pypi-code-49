"""
Generic script to convert a CSV file to OCL-formatted JSON.
"""
import oclcsvtojsonconverter
import oclfleximporter
import pprint
import json

csv_filename = 'plm-poc-v2.csv'
verbose = False

csv_converter = oclcsvtojsonconverter.OclStandardCsvToJsonConverter(csv_filename=csv_filename, verbose=verbose)
import_list = csv_converter.process_by_definition()

# pprint.pprint(import_list[7])

if not verbose:
    for import_item in import_list:
        print(json.dumps(import_item))

#with open('plm-poc-v2-des.json') as ifile:
#    import_list = json.load(ifile)
#    print import_list

ocl_api_token = 'c3b42623c04c87e266d12ae0e297abbce7f1cbe8'  # staging datim-admin
ocl_env = 'https://api.staging.openconceptlab.org'

# bulk_import_request = oclfleximporter.OclBulkImporter.post(input_list=import_list, api_url_root=ocl_env, api_token=ocl_api_token)
# task_id = bulk_import_request.json()['task']
# import_results = oclfleximporter.OclBulkImporter.get_bulk_import_results(task_id=task_id, api_url_root=ocl_env, api_token=ocl_api_token)

importer = oclfleximporter.OclFlexImporter(
    input_list=import_list, api_url_root=ocl_env, api_token=ocl_api_token,
    test_mode=False, verbosity=2, do_update_if_exists=True)
importer.process()
