import os
HEJrj=False
HEJrR=Exception
import logging
import localstack
from localstack.constants import LOCALSTACK_ROOT_FOLDER
from localstack.utils.common import(mkdir,run,new_tmp_file,rm_rf,chmod_r,download,unzip,get_arch,in_docker,is_alpine)
LOG=logging.getLogger(__name__)
RULE_ENGINE_INSTALL_URL='https://github.com/whummer/serverless-iot-offline'
H2_DOWNLOAD_URL='http://www.h2database.com/h2-2019-10-14.zip'
REDIS_URL_PATTERN='https://github.com/whummer/miniredis/raw/master/build/miniredis.<arch>.bin'
MINIREDIS_BINARY=os.path.join(LOCALSTACK_ROOT_FOLDER,'localstack','infra','redis','miniredis.<arch>.bin')
INFRA_DIR=os.path.join(os.path.dirname(localstack.__file__),'infra')
LOCALSTACK_DIR=os.path.dirname(localstack.__file__)
def install_libs():
 install_iot_rule_engine()
 install_postgres()
 install_redis()
def install_iot_rule_engine():
 target_dir=LOCALSTACK_DIR
 main_file=os.path.join(target_dir,'node_modules','serverless-iot-offline','query.js')
 if not os.path.exists(main_file):
  LOG.info('Installing IoT rule engine. This may take a while.')
  run('cd %s; npm install %s'%(target_dir,RULE_ENGINE_INSTALL_URL))
 return main_file
def install_postgres():
 if not in_docker():
  return
 try:
  run('which postgres',print_error=HEJrj)
  return
 except HEJrR:
  pass
 install_alpine_package('postgresql','RDS')
def install_redis():
 try:
  run('which redis-server',print_error=HEJrj)
 except HEJrR:
  install_alpine_package('redis','ElastiCache')
 return 'redis-server'
def install_alpine_package(package,api_name):
 if not is_alpine():
  return
 LOG.info('Downloading dependencies for %s API. This may take a while.'%api_name)
 run('apk add %s'%package)
def install_h2():
 target_dir=os.path.join(INFRA_DIR,'h2')
 if not os.path.exists(target_dir):
  mkdir(target_dir)
  zip_file=new_tmp_file()
  LOG.info('Downloading dependencies for RDS server. This may take a while.')
  download(H2_DOWNLOAD_URL,zip_file)
  unzip(zip_file,target_dir)
  rm_rf(zip_file)
def install_miniredis():
 arch=get_arch()
 bin_path=MINIREDIS_BINARY.replace('<arch>',arch)
 if not os.path.exists(bin_path):
  redis_folder=os.path.dirname(bin_path)
  mkdir(redis_folder)
  url=REDIS_URL_PATTERN.replace('<arch>',arch)
  LOG.debug('Downloading binary from %s'%url)
  download(url,bin_path)
  chmod_r(bin_path,0o755)
 return bin_path
# Created by pyminifier (https://github.com/liftoff/pyminifier)
