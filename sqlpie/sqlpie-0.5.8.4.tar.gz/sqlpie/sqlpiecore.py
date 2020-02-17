# run pip install -r requirements.txt
from sqlpie.compiler import Compiler
import glob
import sys
import yaml
import dag
from os import listdir
from os.path import isfile, join
class Sqlpie:

  def __init__(self, model):
    sources_config_file = open("./config/sources.yml", "r")
    self.sources_conf = yaml.load(sources_config_file, Loader=yaml.FullLoader)
    sources_config_file.close()
    self.model_sources = {}
    self.model = model
    self.staging_model = f"{model}_staging"
    self.model_path = self.get_model_path()
    models_config_file = open(f"./models/{self.model}/model_config.yml", "r")
    self.model_config = yaml.load(models_config_file, Loader=yaml.FullLoader)
    models_config_file.close()
    self.model_queries_path = glob.glob(self.model_path)
    self.payload = self.generate_payload()
    self.payload['model'] = self.model
    self.payload['staging_model'] = f"{self.model}_staging"
    self.payload['source'] = self.source
    self.payload['config'] = self.query_execution
    self.current_query = None
    self.rendered_model = {}
    self.edges = []
    self.dag = dag.DAG() 
    self.render_model()
  
  def get_model_path(self):
    return f"./models/{self.model}/queries/*"
 
  # def generate_payload(self):
  #   payload = {}
  #   for modname in modenames:
  #     payload[modname] = eval(modname)
  #   return payload

  def generate_payload(self):
    import sys
    sys.path.append('./snippets')
    path = './snippets'
    snippets = [f for f in listdir(path) if isfile(join(path, f))]
    payload = {}
    for snippet in snippets:
      prefix = snippet.split('.')[0]
      suffix = snippet.split('.')[1]
      if suffix == 'py' and prefix != '__init__':
        modname = prefix
        mod = __import__(modname)
        payload[modname] = mod
    return payload

  def source(self, source_name, table_name):
    source_table = f"{source_name}.{table_name}"
    if source_name in [self.model, self.staging_model]:
      source_schema = source_name
    else:
      source_schema = self.sources_conf[source_name]['schema']
    destination_table =f"{self.execution_metadata['destination_schema']}.{self.execution_metadata['destination_table']}"
    self.model_sources[source_table] = { 
                                          'source_name': source_name, 
                                          'schema': source_schema,
                                          'table_name': table_name,
                                          'update_method': None
                                        }
    self.dag.add_node_if_not_exists(destination_table)
    self.dag.add_node_if_not_exists(source_table)
    edge = [source_table, destination_table]
    if edge not in self.edges:
      self.edges.append(edge)
      self.dag.add_edge( source_table, destination_table)
    if source_name in self.sources_conf.keys():
      return f"{self.sources_conf[source_name]['schema']}.{table_name}"
    else:
      return source_table

  def update_current_query(self, query):
    self.current_query = query

  def query_execution(self, **kargs):
    self.execution_metadata = kargs
    if 'staging' in self.execution_metadata.keys():
      if self.execution_metadata['staging'] == True:
        self.execution_metadata['destination_schema'] = f"{self.model}_staging"
    else:
      self.execution_metadata['destination_schema'] = self.model
    return ''
  
  def parse_template_query(self, template):
    config = '\n' + template.split('}}')[0] + "}}"
    query = str('}}').join( template.split('}}')[1:])
    return {'config': config, 'query': query}

  def render_model(self):
    for path in self.model_queries_path:
      self.update_current_query(path)
      rendered_query =  self.render_query(path)
      table_name = f"{self.model}.{self.execution_metadata['destination_table']}"
      self.rendered_model[table_name] = {}
      self.rendered_model[table_name]['rendered_query'] = rendered_query
      query_template = open(path, 'r')
      self.rendered_model[table_name]['template'] = self.parse_template_query(query_template.read())
      query_template.close()
      self.rendered_model[table_name]['execution_metadata'] = self.execution_metadata
  
 

  def render_query(self, path=None):
    rendered_query = Compiler(path, self.payload).query_string[1:]
    return rendered_query

  def print_query(self, destination_table):
    print(self.rendered_model[destination_table])
    return self.rendered_model[destination_table]
  
  def get_table_metadata(self, table_name):
    if table_name in self.model_sources.keys():
      return self.model_sources[table_name]
    elif table_name in self.rendered_model.keys():
      return {
                'table_name': self.rendered_model[table_name]['execution_metadata']['destination_table'],
                'schema': self.model,
                'update_method': self.rendered_model[table_name]['execution_metadata']['update_method']
              }
    else:
      return {
              'table_name': table_name,
              'schema': table_name,
              'update_method': None
              } 

  def viz_data_prep(self):
    data_for_viz = []
    for table in self.dag.topological_sort():
      downstream = self.dag.downstream(table)
      for dep_table in downstream:
        table_metadata = self.get_table_metadata(table)
        dep_table_metadata = self.get_table_metadata(dep_table)
        data_for_viz.append({
                              'from': table, 
                              'to': dep_table,
                              'weight': 1,
                              'custom_field': {
                                                'source_schema': table_metadata['schema'], 
                                                'destination_schema': dep_table_metadata['schema']
                                              }
                            })
    return data_for_viz

