import os
from urllib.parse import unquote
from notebook.base.handlers import IPythonHandler
from .connection import openbis_connections


class DataSetDownloadHandler(IPythonHandler):
    """Handle the requests for /openbis/dataset/connection/permId"""

    def download_data(self, conn, permId, downloadPath=None):
        if not conn.is_session_active():
            try:
                conn.login()
            except Exception as exc:
                self.set_status(500)
                self.write({
                    "reason": 'connection to {} could not be established: {}'.format(conn.name, exc)
                })
                return

        try:
            dataset = conn.openbis.get_dataset(permId)
        except Exception as exc:
            self.set_status(404)
            self.write({
                "reason": 'No such dataSet found: {}'.format(permId)
            })
            return

        # dataset was found, download the data to the disk
        try:
            destination = dataset.download(destination=downloadPath)
        except Exception as exc:
            self.set_status(500)
            self.write({
                "reason": 'Data for DataSet {} could not be downloaded: {}'.format(permId, exc)
            })
            return

        # return success message
        path = os.path.join(downloadPath, dataset.permId)
        self.write({
            'url'       : conn.url,
            'permId'    : dataset.permId,
            'path'      : path,
            'dataStore' : dataset.dataStore,
            'location'  : dataset.physicalData.location,
            'size'      : dataset.physicalData.size,
            'files'     : dataset.file_list,
            'statusText': 'Data for DataSet {} was successfully downloaded to: {}.'.format(dataset.permId, path)
        })

    def get(self, **params):
        """Handle a request to /openbis/dataset/connection_name/permId
        download the data and return a message
        """

        try:
            conn = openbis_connections[params['connection_name']]
        except KeyError:
            self.set_status(404)
            self.write({
                "reason": 'connection {} was not found'.format(params['connection_name'])
            })
            return

        results = self.download_data(conn=conn, permId=params['permId'], downloadPath=params['downloadPath'])


class DataSetTypesHandler(IPythonHandler):
    def get(self, **params):
        """Handle a request to /openbis/datasetTypes/connection_name
        This meta-metadata is used in the dataset upload dialog (uploadDialog.js)
        to check data directly in the UI

        Returns all datasetTypes of a given connection
        - with all assigned properties
        - with some details about the property types
        - with the vocabulary, if exists

        The result will be cached, as it is a costly operation with many fetches
        """

        try:
            conn = openbis_connections[params['connection_name']]
        except KeyError:
            self.set_status(404)
            self.write({
                "reason": 'connection {} was not found'.format(params['connection_name'])
            })
            return

        if getattr(conn, 'dataset_types', False):
            self.write({
                "dataSetTypes": conn.dataset_types
            })
            return

        try:
            dataset_types = conn.openbis.get_dataset_types()

            # get all dataset types
            ds_type_dicts = []
            for dt in conn.openbis.get_dataset_types():
                dt_dict = dt.attrs.all()
                # get property assignments for every dataset-type
                # and add them in the key «propertyAssignments»
                pas = dt.get_property_assignments()
                pa_dicts = pas.df[['propertyType','mandatory','ordinal','section']].to_dict(orient='records')
                dt_dict['propertyAssignments'] = pa_dicts

                for pa_dict in pa_dicts:
                    # add a few more attributes to the property assignments
                    pt = conn.openbis.get_property_type(pa_dict['propertyType'])
                    pa_dict['code'] = pt.code
                    pa_dict['label'] = pt.label
                    pa_dict['description'] = pt.description
                    pa_dict['dataType'] = pt.dataType
                    # add vocabulary, if exists, as key «terms»
                    if pt.dataType == 'CONTROLLEDVOCABULARY':
                        terms = conn.openbis.get_terms(pt.vocabulary)
                        terms_dict = terms.df[['code','label','description','official','ordinal']].to_dict(orient='records')
                        pa_dict['terms'] = terms_dict

                ds_type_dicts.append(dt_dict)

            self.write({
                "dataSetTypes": ds_type_dicts
            })
            conn.dataset_types = ds_type_dicts
            return

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({
                "reason":'Could not fetch dataset-types: {}'.format(e)
            })
            return


class DataSetUploadHandler(IPythonHandler):
    """Handle the POST requests for /openbis/dataset/connection_name"""

    def _notebook_dir(self):
        notebook_dir = os.getcwd()
        if 'SingleUserNotebookApp' in self.config and 'notebook_dir' in self.config.SingleUserNotebookApp:
            notebook_dir = self.config.SingleUserNotebookApp.notebook_dir
        elif 'notebook_dir' in self.config.NotebookApp:
            notebook_dir = self.config.NotebookApp.notebook_dir
        return notebook_dir

    def upload_data(self, conn, data):
        if not conn.is_session_active():
            try:
                conn.login()
            except Exception as e:
                print(e)
                self.set_status(500)
                self.write({
                    "reason": 'connection to {} could not be established: {}'.format(conn.name, e)
                })
                return

        errors = []

        sample = None
        experiment = None

        if (data.get('entityIdentifier')):
            sample = None
            experiment = None
            try:
                sample = conn.openbis.get_sample(data.get('entityIdentifier'))
            except Exception as e:
                pass
            if sample is None:
                try:
                    experiment = conn.openbis.get_experiment(data.get('entityIdentifier'))
                except Exception as e:
                    experiments = conn.openbis.get_experiments(data.get('entityIdentifier'))
                    if len(experiments) == 1:
                        experiment = experiments[0]
                    else:
                        # TODO: search in all experiments with same code
                        # (but maybe different identifiers)
                        pass

            if sample is None and experiment is None:
                errors.append(
                    {
                        "entityIdentifier" : 'No such sample or experiment: {}'
                        .format(data.get('entityIdentifier')) 
                    }
                )
        else:
            errors.append(
                {"entityIdentifier": "please provide a sample or experiment identifier"}
            )

        parents = []
        if data.get('parents'):
            parents = data.get('parents')
            for parent in parents:
                try:
                    conn.openbis.get_dataset(parent)
                except Exception as e:
                    errors.append({
                        "parent": "Parent DataSet not found: {}".format(parent)
                    })

        filenames = []
        notebook_dir = self._notebook_dir()
        for filename in data.get('files'):
            filename = unquote(filename)
            full_filename_path = os.path.join(notebook_dir, filename)
            if os.path.isfile(full_filename_path):
                filenames.append(full_filename_path)
            else:
                errors.append({
                    "file": "File not found: {}".format(full_filename_path)
                })

        try:
            dataset = conn.openbis.new_dataset(
                type       = data.get('type'),
                sample     = sample,
                parents    = parents,
                experiment = experiment,
                files      = filenames,
            )
        except Exception as e:
            self.set_status(500)
            self.write({
                "reason": 'Error while creating the dataset: {}'.format(e)
            })

        # try to set the properties
        if data.get('props'):
            props = data.get('props')
            for prop, value in props.items():
                try:
                    setattr(dataset.props, prop.lower(), value)
                except Exception as e:
                    errors.append({
                        "prop."+prop : str(e)
                    })

        # check if any mandatory property is missing
        for prop_name, prop in dataset.props._property_names.items():
            if prop['mandatory']:
                if getattr(dataset.props, prop_name) is None or getattr(dataset.props, prop_name) == "":
                    errors.append({
                        "prop."+prop_name : "is mandatory"
                    })

        # write errors back if already occured
        if errors:
            self.set_status(500)
            self.write({"errors": errors})
            return

        try:
            dataset.save()
        except Exception as e:
            errors.append({
                "save": 'Error while saving the dataset: {}'.format(e)
            })

        # write errors back if they occured
        if errors:
            self.set_status(500)
            self.write({"errors": errors})
        else:
            # ...or return a success message
            self.write({
                'status': 200,
                'statusText': 'Jupyter Notebook was successfully uploaded to: {} with permId: {}'.format(conn.name, dataset.permId)
            })
        print('Jupyter Notebook was successfully uploaded to: {} with permId: {}'.format(conn.name, dataset.permId))

    def post(self, **params):
        """Handle a request to /openbis/dataset/connection_name/permId
        download the data and return a message
        """

        try:
            conn = openbis_connections[params['connection_name']]
        except KeyError:
            self.write({
                "reason": 'connection {} was not found'.format(params['connection_name'])
            })
            return

        data = self.get_json_body()
        self.upload_data(conn=conn,data=data)
