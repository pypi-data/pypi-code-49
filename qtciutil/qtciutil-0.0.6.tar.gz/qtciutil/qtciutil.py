# encoding: utf-8

import platform
import os
import sys
import subprocess
import re
import multiprocessing
import glob

class QtCiUtilError(Exception):
  """
  Custom Exception for Qt Ci Util.
  """
  pass

def common_cmd(env_name, cmd_name):
  """
  Get command path based on environment variable name and command name.
  """
  r = cmd_name
  if env_name in os.environ:
    r = os.path.abspath(os.path.join(os.environ[env_name], cmd_name))
  if platform.system() == 'Windows':
    r = r + '.exe'
  return r

def qt_cmd(cmd_name):
  """
  Get command path in qt bin directory.
  """
  return common_cmd('QT_BIN', cmd_name)

def qtcreator_cmd(cmd_name):
  """
  Get command path in qt creator bin directory.
  """
  return common_cmd('QTCREATOR_BIN', cmd_name)

def qt_version():
  """
  Get qt version.

  :return
    Example: "5.6.3"
  """
  pinfo = subprocess.run([qt_cmd('qmake'), '-query', 'QT_VERSION'], 
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  if pinfo.returncode != 0:
    raise QtCiUtilError("qmake -query QT_VERSION faield.")
  return pinfo.stdout.decode('utf-8', 'ignore').rstrip()

def platform_system():
  """
  For example: windows/linux
  """
  return platform.system().lower()

def qmake_spec():
  """
  Get QMAKE_SPEC

  :return
    Example: win32-msvc2015, linux-g++, win32-g++
  """
  pinfo = subprocess.run([qt_cmd('qmake'), '-query', 'QMAKE_SPEC'], 
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  if pinfo.returncode != 0:
    raise QtCiUtilError("qmake -query QMAKE_SPEC faield.")
  return pinfo.stdout.decode('utf-8', 'ignore').rstrip()

def _vs_env_dict(env_name):
  """
  Get MSVC related environment variables
  
  :param env_name
    common tools environ name.
    MSVC2013: VS130COMNTOOLS
    MSVC2015: VS140COMNTOOLS
    MSVC2017: VS150COMNTOOLS
    MSVC2019: VS160COMNTOOLS

  :return
    All environment infomation about MSVC Tools.
  """
  # @todo
  # Support MSVC 64bit
  vsvar32 = '{vscomntools}vsvars32.bat'.format(vscomntools=os.environ[env_name])
  cmd = [vsvar32, '&&', 'set']
  popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = popen.communicate()
  if popen.wait() != 0:
    print(stderr.decode("mbcs"))
    return dict()
  output = stdout.decode("mbcs").split("\r\n")
  return dict((e[0].upper(), e[1]) for e in [p.rstrip().split("=", 1) for p in output] if len(e) == 2)

def update_msvc_env(qmake_spec):
  """
  Update MSVC's environment variables according to QMAKE_SPEC.

  :param qmake_spec
    String from exec 'qmake -query QMAKE_SPEC'
  """
  m = re.search(r'msvc(\d+)', qmake_spec)
  if not m:
    raise QtCiUtilError('No msvc in QMAKE_SPEC.')
  msvc_version = m.group(1)
  env_name = ''
  if msvc_version == '2013':
    env_name = 'VS130COMNTOOLS'
  elif msvc_version == '2015':
    env_name = 'VS140COMNTOOLS'
  elif msvc_version == '2017':
    env_name = 'VS150COMNTOOLS'
  elif msvc_version == '2019':
    env_name = 'VS160COMNTOOLS'
  else:
    raise QtCiUtilError('Unsupported msvc version.')
  os.environ.update(_vs_env_dict(env_name))

def build(pro_file, build_dir, debug_or_release):
  """
  Build Qt Project

  :param pro_file
    file path of xxx.pro
  
  :param build_dir
    build directory path

  :debug_or_release
    "debug" or "release"
  """
  # create build directory if necessary
  if not os.path.isdir(build_dir):
    os.makedirs(build_dir)
  
  # qmake
  qmake_spec_str = qmake_spec()
  qmake_args = [qt_cmd('qmake'), pro_file, '-r', '-spec', qmake_spec_str]
  if debug_or_release == 'debug':
    qmake_args.append('CONFIG+=debug')
    qmake_args.append('CONFIG+=qml_debug')
  os.chdir(build_dir)
  if 'msvc' in qmake_spec_str:
    update_msvc_env(qmake_spec_str)
  print('qmake_args: ', qmake_args)
  pinfo = subprocess.run(qmake_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  if pinfo.returncode != 0:
    raise QtCiUtilError('qmake failed. %s' % pinfo.stdout.decode('utf-8', 'ignore'))

  # build
  platform_system_str = platform_system()
  make = 'make'
  if platform_system_str == 'windows':
    if 'msvc' in qmake_spec_str:
      make = qtcreator_cmd('jom')
    else:
      make = qtcreator_cmd('mingw32-make')
  build_args = [make, '-j%d' % multiprocessing.cpu_count()]
  print("build_args: ", build_args)
  pinfo = subprocess.run(build_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  if pinfo.returncode != 0:
    raise QtCiUtilError('make failed. %s' % pinfo.stdout.decode('utf-8', 'ignore'))

def unit_test(pro_file, build_dir, dist_dir):
  """
  Unit Test.

  :param pro_file
    file path of test.pro
  
  :param build_dir
    build directory path

  :param dist_dir
    dest directory path
  """
  build(pro_file, build_dir, 'release')
  if not os.path.isdir(dist_dir):
    raise QtCiUtilError("no dist directory found.")
  wildcard_path = os.path.normpath(os.path.join(dist_dir, "**/tst_*.exe"))
  os.environ["PATH"] = os.environ['QT_BIN'] + os.pathsep + os.environ["PATH"]
  for filename in glob.glob(wildcard_path, recursive=True):
    if os.path.isfile(filename):
      pinfo = subprocess.run([filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      if pinfo.returncode != 0:
        raise QtCiUtilError('run test failed.')
      m = re.search(r'Totals:\s(\d+)\spassed,\s(\d+)\sfailed,\s(\d+)\sskipped,\s(\d+)\sblacklisted', pinfo.stdout.decode('utf-8', 'ignore'))
      if m:
        print(m.group(0))
        failed = int(m.group(2))
        if failed > 0:
          raise QtCiUtilError("test({exe}) failed.".format(exe=filename))
  print("unit test done.")