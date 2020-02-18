from flask import Blueprint, Flask
from importlib import import_module
from glob import glob
import re


def matcher(source=str, regex=str):
    match = re.search(regex, source, re.M | re.I)
    if match:
        return match.group(1)


def import_modules(app: Flask):
    scan_packages = app.property("scan_packages")
    if scan_packages:
        scan_path = scan_packages.replace('.', '/')
        url_prefix = '/%s/' % app.property("server.root") if app.property("server.root") else '/'
        regex = r'%s/(\S+).py' % scan_path
        imp = import_restful if app.property("server.restful") else import_red_print
        [imp(app, scan_packages, url_prefix, matcher(module_name, regex)) for module_name in
         glob(scan_path + '/**py')]


def import_red_print(app: Flask, scan_packages, url_prefix, module):
    if module == '__init__':
        return
    print('load module [%s.%s] success,register router mapping: %s' % (
        scan_packages, module, url_prefix + module))


def import_restful(app: Flask, scan_packages, url_prefix, module):
    if module == '__init__':
        return
    apis = import_module('%s.%s' % (scan_packages, module))
    if not apis.bp:
        return
    app.register_blueprint(apis.bp, url_prefix=url_prefix + module)
    print('load module [%s.%s] success, register restful mapping: %s' % (
        scan_packages, module, url_prefix + module))
