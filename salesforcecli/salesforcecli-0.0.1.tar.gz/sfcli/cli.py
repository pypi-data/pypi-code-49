from cmd import Cmd
from functools import lru_cache
from typing import List
from simple_salesforce import Salesforce
from tabulate import tabulate
import pprint
from sfcli.util import bulk_change, bulk_delete, write_results, start_session, strtime, print_error
import sys


class Cli(Cmd):

    def __init__(self):
        super(Cli, self).__init__()
        self.env = 'default'
        self.vs = 44.0
        self.threads = 4
        self.session, self.domain = start_session(self.vs, self.env)
        self._set_base_url()

    def _set_base_url(self):
        self.base_url = f'https://{self.session.sf_instance}/services/data/v{self.vs}'

    def _update_env(self):
        self._revoke_session()
        self.session, self.domain = start_session(self.vs, self.env)
        self._set_base_url()
        print('environment updated')

    def help_setthreads(self):
        print('set the number of threads to use in threaded processes like create and update')

    def do_setthreads(self, args):
        self.threads = args

    def help_getenv(self):
        print('show the current environment')

    def do_getenv(self, args):
        print(self.env)

    def help_setenv(self):
        print('End the current session and log into a new Salesforce Environment\n'
              'based on the environment suffix you input (this suffix will be\n'
              'appended to the default environment variable names to retrieve\n'
              'the desired variables from the .env file')

    def do_setenv(self, env_suffix: str = None):
        self.env = env_suffix if env_suffix else 'default'
        self._update_env()

    def help_setversion(self):
        print('Input the version of the API being used. E.g. input 42.0')

    def do_setversion(self, args):
        self.vs = args
        self._update_env()

    def _query(self, query: str) -> dict:
        results = self.session.query_all(query)
        if results:
            records = results['records']
            for r in records:
                del r['attributes']
            return records

    def help_select(self):
        print('type in a SOQL query as you normally would. Results will be printed in the console')

    @print_error
    def do_select(self, args):
        query = f'select {args}'
        records = self._query(query)
        if records:
            print(tabulate(records, headers='keys'))            

    @print_error
    def do_SELECT(self, args):
        self.do_select(args)

    def help_download(self):
        print('type in a SOQL query after the "download" keyword. Results will be saved in a .csv')

    @print_error
    def do_download(self, args: str):
        records = self._query(args)
        if records:
            write_results(f'query_{strtime()}', records)

    def _get_object_names(self) -> List[list]:
        url = f'{self.base_url}/sobjects'
        results = self.session._call_salesforce('GET', url)
        if results:
            objects = results.json()['sobjects']
            names = [[o['name']] for o in objects]
            return names
        else:
            return None

    def help_objects(self):
        print('returns a list of all the objects in the org.\n'
              'Optional string parameter to filter the objects by.')

    def do_objects(self, args: str):
        names = self._get_object_names()
        names = [n for n in names if args.lower() in n[0].lower()] if args else names
        if names:
            print(tabulate(names, headers=['name']))
        else:
            print('no results')

    @lru_cache(maxsize=32)
    def _get_object_fields(self, object_name: str) -> dict:
        url = f'{self.base_url}/sobjects/{object_name}/describe/'
        results = self.session._call_salesforce('GET', url).json()['fields']
        return [[r['name']] for r in results]

    def help_fields(self):
        print('Input the name of the object to return the fields for e.g. order\n'
               'Optional string parameter to filter the fields by e.g. name.')

    def do_fields(self, args: str):
        arg_lst = args.split()
        object_name = arg_lst[0]
        results = self._get_object_fields(object_name)
        if len(arg_lst) > 1:
            filter = arg_lst[1]
            results = [r for r in results if filter.lower() in r[0].lower()]
        print(tabulate(results, headers=['field_name']))

    def help_update(self):
        print('input the name of the object to update and the name of the file including the path.\n'
              'This file should contain columns for the fields you want set on create of these records.\n'
              'One of the columns must have the id header and contain the id of the record to be updated.\n'
              'Note the columns headers in the file must match the API names of the fields in Salesforce\n'
              'Optional parameter to specify the number of threads to use (default is 4)')

    @print_error
    def do_update(self, args: str):
        bulk_change(args, 'PATCH', self.session, self.base_url, self.threads)

    def help_create(self):
        print('input the name of the object to update and the name of the file including the path.\n'
              'This file should contain columns for the fields you want set on create of these records.\n'
              'Note the columns headers in the file must match the API names of the fields in Salesforce\n'
              'Optional parameter to specify the number of threads to use (default is 4)')

    @print_error
    def do_create(self, args: str):
        bulk_change(args, 'POST', self.session, self.base_url, self.threads)

    def help_delete(self):
        print('input the name of the object to update and the name of the file including the path.\n'
              'The file should contain one column titled id with the ids of all the records to delete.\n'
              'These records do not need to be of the same type.\n'
              'Optional parameter to specify the number of threads to use (default is 4)')

    @print_error
    def do_delete(self, args: str):
        bulk_delete(args, self.session, self.base_url, self.threads)

    def _revoke_session(self):
        token = self.session.session_id
        payload = {'token': token}
        domain = self.domain if self.domain else 'login'
        url = f'https://{domain}.salesforce.com/services/oauth2/revoke'
        self.session._call_salesforce('GET', url, params=payload)

    def help_end(self):
        print('Revokes the access token and exits the shell')

    def do_end(self, args: str = None):
        self._revoke_session()
        sys.exit()


if __name__ == '__main__':
    Cli().cmdloop()
