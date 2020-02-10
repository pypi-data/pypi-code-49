#!/usr/bin/env

'''
Django front end dependency manager template tags.
'''

from django import template
from django.utils.safestring import mark_safe

from fe_manager.utils import fe_modules_load, TopologicalSorter


register = template.Library()


@register.simple_tag(takes_context=True)
def fe_manager_add_module(context, module):
    # If it does not exist, create a context variable to store required modules...
    if not '_fe_manager_modules' in context:
        context['_fe_manager_modules'] = []
    # Append the required module to the list
    context['_fe_manager_modules'].append(module)
    return ''


@register.simple_tag(takes_context=True)
def fe_manager_output_js(context):
    # Load the stored module dependencies
    if not '_fe_manager_modules' in context:
        modules = []
    else:
        modules = context['_fe_manager_modules']
    # Load installed modules
    installed_modules = fe_modules_load()
    # Output javascript loading HTML
    return mark_safe(_get_ordered_js(installed_modules, _topologically_sort(installed_modules, modules)))


@register.simple_tag(takes_context=True)
def fe_manager_output_css(context):
    # Load the stored module dependencies
    if not '_fe_manager_modules' in context:
        modules = []
    else:
        modules = context['_fe_manager_modules']
    # Load installed modules
    installed_modules = fe_modules_load()
    # Output javascript loading HTML
    return mark_safe(_get_ordered_css(installed_modules, _topologically_sort(installed_modules, modules)))


def _topologically_sort(installed_modules, modules):
    tree = {}
    for module_name in modules:
        try:
            module = installed_modules[module_name]
        except KeyError:
            raise FeManagerModuleNotFound(
                f'Cannot module \'{module_name}\' in require configuration files!')
        try:
            deps = module['dependencies']
        except KeyError:
            deps = {}
        tree[module_name] = deps
    sorter = TopologicalSorter(tree)
    ordered_modules = list(sorter.static_order())
    for module_name in ordered_modules:
        if not module_name in installed_modules.keys():
            raise FeManagerModuleNotFound(
                f'Cannot resolve dependency module \'{module_name}\' in require configuration files!')
    return ordered_modules


def _get_ordered_files(installed_modules, modules, prop):
    files = []
    for module_name in modules:
        try:
            files.extend(installed_modules[module_name][prop])
        except KeyError:
            pass
    return files


def _get_ordered_css(installed_modules, modules):
    html = ''
    for file in _get_ordered_files(installed_modules, modules, 'css'):
        html += f"<link rel=\"stylesheet\" type=\"text/css\" href=\"{file}\">\n"
    return html


def _get_ordered_js(installed_modules, modules):
    html = ''
    for file in _get_ordered_files(installed_modules, modules, 'js'):
        html += f"<script src=\"{file}\"></script>\n"
    return html


class FeManagerModuleNotFound(Exception):
    pass
