from notebook.base.handlers import IPythonHandler
import os


class Requirements(IPythonHandler):
    """Handle the requests for /requirements"""

    def _notebook_dir(self):
        notebook_dir = os.getcwd()
        if 'SingleUserNotebookApp' in self.config and 'notebook_dir' in self.config.SingleUserNotebookApp:
            notebook_dir = self.config.SingleUserNotebookApp.notebook_dir
        elif 'notebook_dir' in self.config.NotebookApp:
            notebook_dir = self.config.NotebookApp.notebook_dir
        return notebook_dir

    def post(self, **params):
        data = self.get_json_body()
        #print(data)

        notebook_dir = self._notebook_dir()
        if 'notebook_path' in data:
            notebook_dir = os.path.dirname(os.path.join(notebook_dir, data['notebook_path']))
        #print("*********notebook_dir: {}".format(notebook_dir))

        if 'requirements_list' in data and 'requirements_filename' in data:
            req_filename = os.path.join(notebook_dir, data['requirements_filename'])
            #print("*********req_filename: {}".format(req_filename))
            with open(req_filename, 'w') as fh:
                fh.write(data['requirements_list'])

        if 'runtime' in data and 'runtime_filename' in data:
            runtime_filename = os.path.join(notebook_dir, data['runtime_filename'])
            #print("**********runtime_filename: {}".format(runtime_filename))
            with open(runtime_filename, 'w') as fh:
                fh.write(data['runtime'])

