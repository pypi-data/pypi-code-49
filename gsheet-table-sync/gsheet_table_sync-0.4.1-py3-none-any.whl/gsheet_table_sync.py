import json
import re
from time import sleep
from apiclient import discovery
from google.oauth2 import service_account

class GsheetTableSync:

    def __init__(self, spreadsheet_id, worksheet_id=0, credential_json=None, cache_discovery=False):
        """Initialize the client
        
        Arguments:
            spreadsheet_id {str} -- Spreadsheet ID
        
        Keyword Arguments:
            worksheet_id {int} -- Worksheet ID (default: {0})
            credential_json {obj} -- service account credential in JSON format (default: {None})
                                     the credential file needs to have the following attributes:
                                     [private_key, client_email, token_uri]
                                     If not supplied, it will attempt to use default credential
            cache_discovery {bool} -- Enable/disable cache discovery (default: {False})
                                      Disabled default to avoid file_cache import error message
        
        Raises:
            Exception: Can't establish the session to Google Sheet
        """
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]

        try:
            if credential_json:
                if isinstance(credential_json, str):
                    credential_json = json.loads(credential_json)

                credentials = service_account.Credentials.from_service_account_info(credential_json, scopes=scopes)
                service = discovery.build('sheets', 'v4', credentials=credentials, cache_discovery=cache_discovery)
            else:
                service = discovery.build('sheets', 'v4', cache_discovery=cache_discovery)
        except Exception as e:
            raise Exception("Can't establish the session to Google Sheet. Please check the credential")
        
        # Setting the write quota to 100 writes/min
        self.quota_write = 100
        self.quota_write_usage = 0

        self.spreadsheet_id = spreadsheet_id
        self.sheet = service.spreadsheets()
        self.worksheet_id = str(worksheet_id)
        self.worksheet_title = None
        self.worksheet_lookup = {}

        self.sheet_info = self.sheet.get(spreadsheetId=spreadsheet_id).execute()


        for worksheet in self.sheet_info['sheets']:
            prop = worksheet['properties']
            self.worksheet_lookup[str(prop['sheetId'])] = prop

        self.diff_sheet_data = None
        self.set_worksheet(self.worksheet_id)


    def _return(self, data, error=None):
        """Wrapper for standardizing output
        Arguments:
            data {mixed} -- Data payload

        Keyword Arguments:
            error {string} -- Error message if exists (default: {None})
        
        Returns:
            dict -- Dict which contains error/data
        """        
        if error:
            if isinstance(error, dict) or isinstance(error, list):
                error = json.dumps(error)

            return {"error": str(error), "data": None}
        else:
            return {"error": None, "data": data}
    
    def _check_quota(self):
        """Check Google Sheet API quota. Sleep for 100 secs if quota is reached
        and reset the counter. Google Sheet API quota is per 100 secs per project.
        """
        self.quota_write_usage += 1

        if self.quota_write_usage >= self.quota_write:
            sleep(100)
            self.quota_write_usage = 0


    def set_worksheet(self, worksheet_id):
        """Set active worksheet
        
        Arguments:
            worksheet_id {int} -- Active worksheet ID (0 for main/default worksheet)
        
        Raises:
            Exception: Unable to find worksheet
        """
        self.worksheet_id = worksheet_id
        if worksheet_id in self.worksheet_lookup:
            self.worksheet_title = self.worksheet_lookup[self.worksheet_id]['title']
            self.diff_sheet_data = None
        else:
            raise Exception(f"Unable to find worksheet {worksheet_id}")

    
    def remove_rows(self, row_index_A1, number_of_rows=1):
        """Remove one or more rows
        
        Arguments:
            row_index_A1 {int} -- Index of row to be deleted (1 based)
        
        Keyword Arguments:
            number_of_rows {int} -- Number of rows to be removed (default: {1})
        
        Raises:
            Exception: Row index should be 0 or greater

        Returns:
            [array] -- Reply response. Typically [{}]
        """        
        if row_index_A1 < 1:
            return self._return('', error="Row index should be 1 or greater")
        else:
            # Google Sheet for removing row is 0 based index 
            row_index = row_index_A1 - 1

        body = {
            'requests': {
                'deleteDimension': {
                    'range': {
                        'sheetId': self.worksheet_id,
                        'dimension': 'ROWS',
                        'startIndex': row_index,
                        'endIndex': row_index + number_of_rows
                    }
                }
            }
        }

        # Check the write API quota
        self._check_quota()

        response = self.sheet.batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body=body
        ).execute()

        if response['replies'] == [{}]:
            return self._return(data='')
        else:
            return self._return('', error=response['replies'])


    def update_row(self, row_number, row_data, start_from_column='A', value_input_option='USER_ENTERED'):
        """Update Google Spreadsheet's row
        
        Arguments:
            row_number {int} -- Row number on Google Sheet
            row_data {array} -- Data to replace the row
        
        Returns:
            [type] -- [description]
        """
        if not isinstance(row_data, list):
            return self._return('', error="Invalid row data")
        
        if isinstance(row_data[0], list):
            body = {'values': row_data}
        else:
            body = {'values' : [row_data]}
        
        range_name = f"{self.worksheet_title}!{start_from_column}{row_number}"

        try:
            # Check write API quota
            self._check_quota()
            
            resp = self.sheet.values().update(spreadsheetId=self.spreadsheet_id, body=body, range=range_name, valueInputOption=value_input_option).execute()
            return self._return(resp)
        except Exception as e:
            return self._return(None, str(e))


    def update_column(self, column, value):
        '''
            Update a single Google Spreadhseet's column
            Parameter:
                column            <string> Ex: A1
                value             <string>
            Return:
                {
                    error:        <None or string>
                    data:         <empty if successfull. None if there's an error>
                }
        '''
        if not isinstance(value, str):
            return {"error" : "Failed to update column. Value has to be a single value/string", "data": None}


        body = {'values' : [[value]]}
        range_name = "{}!{}".format(self.worksheet_title, column)

        try:
            # Check the write API quota
            self._check_quota()

            resp = self.sheet.values().update(
                spreadsheetId=self.spreadsheet_id,
                body=body,
                range=range_name,
                valueInputOption='USER_ENTERED').execute()
            return {"error" : None, "data": resp}
        except Exception as e:
            return {"error" : e, "data": None}


    def get_data(self, from_column, to_column, has_header=True, value_render_option=None):
        '''
            Get the current Spreadsheets
            Parameter:
                from_column       <string>       Ex: A1
                to_column         <string>       Ex: D
                has_header        <bool>         Will extract header from the top row
                value_render_option <string>     Use 'Formula' to get raw value
            Return:
                {
                    error:        <None or string>
                    data:         {
                        "row_to_be_updated" : <int>         <-- pointing to the next row to be updated
                        "header" : <list>                   <-- List of the filed name/header
                        "body" : [[row1], [row2]]           <-- Values from Google Sheet
                    }
                }
        '''
        range_name = "{}!{}:{}".format(self.worksheet_title, from_column, to_column)

        try:
            resp = self.sheet.values().get(spreadsheetId=self.spreadsheet_id, range=range_name, valueRenderOption=value_render_option).execute()

            row_offset = self._get_cell_coordinate(from_column)['row']
            row_to_be_updated = len(resp['values']) + row_offset

            if has_header:
                header = resp['values'][0]
                resp['values'].pop(0)
            else:
                header = None

            
            out = {
                # + 2..... 1 because the header is popped, 1 to point to the new empty row
                "row_to_be_updated" : row_to_be_updated,
                "header" :  header,
                "body" : resp['values'],
            }
            return {"error" : None, "data": out}
        except Exception as e:
            return {"error" : "Failed to get data from the spreadsheet", "data": None, "error_detail" : e}


    def data_to_dict(self, raw_data, header, unique_key):
        """Convert Gsheet raw data to dict 
        
        Arguments:
            raw_data {list} -- Raw data looks like [ [row1col1,row1col2,row1col3], [row2col1,row2col2,row2col3]]
            header {list} -- Header 
            unique_key {string} -- unique key
        
        Returns:
            [dict] -- [description]
        """        
        out = {}

        if not header or not isinstance(header, list):
            raise Exception("Invalid header. Please supply the list of header fields.")

        try:
            unique_key_index = header.index(unique_key)
        except (IndexError, ValueError):
            raise Exception(f"Field {unique_key} is not in the header {json.dumps(header)}")

        for row in raw_data:
            tmp = {}            
            for index, field_name in enumerate(header, start=0):
                if index >= len(row):
                    tmp[field_name] = ''
                else: 
                    tmp[field_name] = row[index]
            
            out[row[unique_key_index]] = tmp
        
        return out


    def _get_cell_coordinate(self, a1_cell):
        out = {}
        tmp = re.match(r"([A-Za-z]+)(\d+)", a1_cell)
        if tmp:
            out['column'] = tmp.group(1)
            out['row'] = int(tmp.group(2))
        else:
            raise Exception(f"Invalid call notation. Cannot parse A1 notation for: {a1_cell}")

        return out



    def _pre_diff_sheet_data(self, from_range, to_range, new_data, key):        
        # Get the existing sheet data
        res = self.get_data(from_range, to_range, has_header=True)
        if res['error']:
            raise res['error']['error_detail']
        
        # Parse sheet data
        header = res['data']['header']

        # Validate that the key exists in the header
        if key not in header:
            raise Exception(f"Cannot find {key} field in the sheet data's header")
        
        # Compare sheet header with new_data's header
        tmp = []
        for gsheet_header_name in header:
            if gsheet_header_name not in new_data[0].keys():
                tmp.append(gsheet_header_name)
        
        if len(tmp) > 0:
            missing_fields = ','.join(tmp)
            raise Exception(f"The following fields are missing from the new data: {missing_fields}")
        
        return res['data']


    def get_diff_sheet_data(self, from_range, to_range, new_data, key, capture_unchanged=False):
        """Find the diff between sheet data vs new data
        
        Arguments:
            from_range {string} -- Sheet range in A1 notation. Ex: A1 
            to_range {string} -- Sheet range in A1 notation. Ex: D (to include everything in column D)
            new_data {list} -- List of record (in list)
            key {string} -- Field name to be used as primary key
        
        Returns:
            output = {
                'update_row' : [{
                    row_number_A1: (int),
                    row_column_A1: (string),
                    values: (list),
                    old_values: (list)
                }],
                'unchanged_row': [{
                    row_number_A1: (int),
                    values: (list)
                }],
                'new_row' : [{
                    row_number_A1: (int),
                    row_column_A1: (string),
                    values: (list)
                }],
                'delete_row': [{
                    row_number_A1: (int),
                    values: (list)
                }]
            }
        """        
        output = {
            'update_row' : [],
            'unchanged_row': [],
            'new_row' : [],
            'delete_row': []
        }

        a1_offset = self._get_cell_coordinate(from_range)

        res = self._pre_diff_sheet_data(from_range, to_range, new_data, key)
        header = res['header']
        sheet_data = res['body']
        next_empty_row_A1 = res['row_to_be_updated']
        key_index = header.index(key)

        # Convert new_data to an easier format
        # { key1 : [field1_value, field2_value, ....]}
        new_data_kv = {}
        for record in new_data:
            new_data_kv[record[key]] = []
            for field_name in header:
                if field_name in record and record[field_name] is not None:
                    new_data_kv[record[key]].append(record[field_name])
                else:
                    new_data_kv[record[key]].append('')

        # +1 to take into account the header
        start_from_row = a1_offset['row'] + 1

        for row_number_A1, row in enumerate(sheet_data, start=start_from_row):
            # Pad the row with empty string 
            # to match the length of the header
            if len(row) != len(header):
                delta = len(header) - len(row)
                for _ in range(delta):
                    row.append('') 

            # If the record exists only on the gsheet
            # mark it for removal
            if row[key_index] not in new_data_kv:
                output['delete_row'].append({
                    'row_number_A1': row_number_A1,
                    'column_A1': a1_offset['column'],
                    'values': row
                })


            else:
                # Mark for matching row
                if row == new_data_kv[row[key_index]]:
                    if capture_unchanged:
                        output['unchanged_row'].append({
                            'row_number_A1': row_number_A1,
                            'column_A1': a1_offset['column'],
                            'values': row
                        })
                # If the record exists but the value doesn't match
                # mark it for update
                else:
                    output['update_row'].append({
                        'row_number_A1': row_number_A1,
                        'column_A1': a1_offset['column'],
                        'values': new_data_kv[row[key_index]],
                        'old_values': row
                    })
                    
                # remove the record
                del new_data_kv[row[key_index]]

        # What's left of new_data_kv is the list to be added
        # mark it for addition
        output['new_row'] = {
            'row_number_A1' : next_empty_row_A1,
            'column_A1': a1_offset['column'],
            'values': list(new_data_kv.values())
        }

        # Sort the row to be deleted
        # bottom row first to avoid shifting cells
        output['delete_row'] = sorted(
            output['delete_row'],
            key=lambda k: k['row_number_A1'],
            reverse=True
            )

        self.diff_sheet_data = output
        return output


    def apply_diff(self, diff, remove_obsolete_record=False):
        """Apply diff to the existing sheet data
        
        Arguments:
            diff {dict} -- See get_diff_sheet_data()
        
        Keyword Arguments:
            remove_obsolete_record {bool} -- If set to true, remove record that doesn't exist in the new data (default: {False})
        
        Returns:
            {'error': None, 'data': 'Completed'}
        """        
        # Apply changes first
        for update_info in diff['update_row']:
            resp = self.update_row(
                update_info['row_number_A1'],
                update_info['values'],
                start_from_column=update_info['column_A1']
            )

            if resp['error']:
                return resp['error']

        # Then Add new records
        if len(diff['new_row']['values']) > 0:
            resp = self.update_row(
                diff['new_row']['row_number_A1'],
                diff['new_row']['values'],
                start_from_column=diff['new_row']['column_A1']
            )

            if resp['error']:
                return resp['error']


        # Then, finally, remove records that are no longer
        # exists in the new data
        if remove_obsolete_record:
            for remove_info in diff['delete_row']:
                resp = self.remove_rows(remove_info['row_number_A1'])

                if resp['error']:
                    return resp['error']

        return self._return('Completed')
