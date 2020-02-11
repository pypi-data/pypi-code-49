# -*- coding: utf-8 -*-
# Copyright (c) 2018  Red Hat, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Written by Chenxiong Qi <cqi@redhat.com>
#            Qixiang Wan <qwan@redhat.com>

from ursa_major.handlers.base import BaseHandler
from ursa_major import MBS_BUILD_STATES
from ursa_major.logger import log


class AddModuleHandler(BaseHandler):
    """Handler to add a module to config file and add its koji tag to inheritance data"""

    def run(self):
        self.dry_run = self.args.dry_run
        self.debug = self.args.debug

        self.tag_config_file = self.args.tag_config_file
        self.load_tag_config()

        # the koji tag we operate against
        self.tag = self.args.tag
        self.connect_mbs()
        self.connect_koji(dry_run=self.dry_run)

        module_name = self.args.module_name
        module_stream = self.args.module_stream
        module_priority = self.args.priority

        if self.args.module_requires:
            module_requires = dict(self.args.module_requires)
        else:
            module_requires = None

        if self.args.module_buildrequires:
            module_buildrequires = dict(self.args.module_buildrequires)
        else:
            module_buildrequires = None

        # find out the latest module build in MBS which matches the specified module
        match_modules = self.mbs.get_modules(
            buildrequires=module_buildrequires,
            requires=module_requires,
            name=module_name,
            stream=module_stream,
            state=MBS_BUILD_STATES['ready'],
            page=1)  # we only need the default first page items

        if match_modules:
            log.info("The latest tag for specified module in MBS is: %s",
                     match_modules[0]['koji_tag'])
        else:
            log.warning("Can't find any built module in MBS for the specified tag")

        # all MBS modules belong to this name+stream
        name_stream_modules = self.mbs.get_modules(
              name=module_name,
              stream=module_stream,
              state=MBS_BUILD_STATES['ready'])
        name_stream_tags_in_mbs = [m['koji_tag'] for m in name_stream_modules]

        inheritance_data = self.koji.get_inheritance_data(self.tag)
        inheritance_tags = [x['name'] for x in inheritance_data]

        # tags in koji inheritance that belong to this name+stream module
        name_stream_tags_in_koji = list(set(name_stream_tags_in_mbs) & set(inheritance_tags))
        # inheritance data but exclude the tags belong to this name+stream module
        non_name_stream_inheritance = [
            x for x in inheritance_data if x['name'] not in name_stream_tags_in_koji
        ]

        # priority values in inheritance that not belong to this name+stream modules
        other_inheritance_priorities = [x['priority'] for x in non_name_stream_inheritance]

        config_modules = self.tag_config.get(self.tag, {}).get('modules', [])
        # priority values in config file that not belong to this name+stream modules
        other_config_priorities = [
            m['priority'] for m in config_modules if not (
                m['name'] == module_name and m['stream'] == module_stream
            )
        ]

        if module_priority in other_config_priorities:
            raise ValueError("Priority {} is used by other modules in config".format(
                module_priority))
        if module_priority in other_inheritance_priorities:
            raise ValueError("Priority {} is used by other modules in tag {}'s "
                             "inheritance".format(module_priority, self.tag))

        self.add_module_to_config(self.tag, module_name, module_stream,
                                  priority=module_priority, requires=module_requires,
                                  buildrequires=module_buildrequires, dry_run=self.dry_run)

    def add_module_to_config(self, tag, name, stream, priority,
                             requires=None, buildrequires=None, dry_run=False):
        """
        Add the module config to tag config file

        :param tag: tag name, module config will be added under this tag
        :param name: module name
        :param stream: module stream
        :param priority: priority value in koji inheritance data
        :param requires: module requires
        :param buildrequires: module buildrequires
        :param dry_run: dry_run mode
        """
        tag_config = self.tag_config
        config = tag_config.setdefault(tag, {})
        modules = config.setdefault('modules', [])
        module_config = dict(name=name,
                             stream=stream,
                             priority=priority)
        if requires:
            module_config['requires'] = requires
        if buildrequires:
            module_config['buildrequires'] = buildrequires

        modules_with_same_name_stream = [m for m in modules if
                                         m['name'] == name and
                                         m['stream'] == stream]

        if len(modules_with_same_name_stream) > 1:
            raise RuntimeError("Unexpected error, found multiple modules in config "
                               "file with name '{}' and stream '{}'".format(
                                   name, stream))

        if len(modules_with_same_name_stream) == 0:
            log.info("Adding module config to tag %s in tag config file:\n%s",
                     tag, module_config)
            modules.append(module_config)

        if len(modules_with_same_name_stream) == 1:
            if module_config == modules_with_same_name_stream[0]:
                log.info("The specified module already exists, nothing to change")
                return
            log.info("Found one module in config with same name and stream")
            modules.remove(modules_with_same_name_stream[0])
            modules.append(module_config)

        log.info("Going to update tag config file with new module: {}".format(module_config))
        if dry_run:
            log.info("Dry run finished.")
        else:
            self.write_tag_config()
