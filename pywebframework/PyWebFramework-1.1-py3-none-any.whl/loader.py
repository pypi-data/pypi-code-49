# coding: utf-8
'''
返回码说明：
0: 模块执行成功
2: 模块执行失败
3: 模块执行异常
4: 模块没找到
'''

import sys, os, json
import importlib
import traceback
from optparse import OptionParser


parser = OptionParser()
parser.add_option('-r', '--root', dest='root', help='根目录，根目录下包含所有模块目录')
parser.add_option('-m', '--module', dest='module', help='模块id')
parser.add_option('-t', '--task', dest='task', help='任务文件')

(options, args) = parser.parse_args()

module_id = options.module
task_file = options.task

if not module_id:
	parser.print_help()
	sys.exit(3)

sys.path.insert(0, '.')

root = options.root
if not root:
	root = '.'


def clean_modules():
	def find_module():
		for name in sys.modules:
			try:
				if sys.modules[name].__file__.startswith(root):
					return name
			except:
				pass
		return None

	m = find_module()
	while m:
		del sys.modules[m]
		m = find_module()


def is_module(name):
	if not os.path.exists(os.path.join(root, name, 'module.py')):
		return False
	sys.path[0] = os.path.join(root, name)
	try:
		clean_modules()
		module = importlib.import_module('module')
		if 'Module' not in dir(module):
			return False
		if 'id' not in dir(module.Module):
			return False
		return True
	except Exception as e:
		return False


def get_module_id(name):
	sys.path[0] = os.path.join(root, name)
	clean_modules()
	module = importlib.import_module('module')
	return module.Module.id


def run_module(name):
	module_root = os.path.join(root, name)
	sys.path[0] = module_root
	os.chdir(module_root)
	clean_modules()
	module = importlib.import_module('module')
	m = module.Module()
	return m.run(task_file)


for module_name in os.listdir(root):
	try:
		if not is_module(module_name):
			continue

		mids = get_module_id(module_name)
		if type(mids) == str:
			mids = [mids]
		if module_id in mids:
			if run_module(module_name):
				sys.exit(0)
			sys.exit(2)
	except Exception as e:
		traceback.print_exc()
		sys.exit(3)
else:
	if task_file.lower().endswith('.json'):
		json_str = open(task_file, 'rb').read().decode('gb2312', 'ignore')
		j = json.loads(json_str)
		j['status'] = '600C999997'
		j['message'] = '需要收取回执'

		json_str = json.dumps(j).encode('gb2312')
		open(task_file, 'wb').write(json_str)

	sys.exit(4)
