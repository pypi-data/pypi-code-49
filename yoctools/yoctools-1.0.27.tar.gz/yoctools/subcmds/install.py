# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class Install(Command):
    common = True
    helpSummary = "Install component into project environment"
    helpUsage = """
%prog [<component>...]
"""
    helpDescription = """
Install component into project environment
"""
    def _Options(self, p):
        self.jobs = 1
        p.add_option('-j', '--jobs',
                     dest='jobs', action='store', type='int',
                     help="projects to fetch simultaneously (default %d)" % self.jobs)

    def Execute(self, opt, args):
        if len(args) > 0:
            yoc = YoC()
            components = ComponentGroup()
            for name in args:
                depends = yoc.download_component(name)
                if depends:
                    for c in depends:
                        components.add(c)
                # yoc.update()
                # print("%s download done." % name)
            # for c in components:
            #     print(c.name)

        if opt.jobs:
            jobs = opt.jobs
        else:
            jobs = 4
            self.download(jobs, components)



    def download(self, jobs, components):
        task_pool = threadpool.ThreadPool(jobs)

        tasks = []
        np = Progress('Fetching projects', len(components))
        for component in components:
            component.np = np
            tasks.append(component)

        def thread_execture(component):
            component.np.update(msg=component.name)
            component.download()
            # git = GitRepo(component.path, component.repo_url)
            # git.pull()


        requests = threadpool.makeRequests(thread_execture, tasks)
        for req in requests:
            task_pool.putRequest(req)
        task_pool.wait()

        np.end()



