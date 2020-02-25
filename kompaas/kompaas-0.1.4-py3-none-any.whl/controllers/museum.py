"""
Module that handles museums.
Museums are repositories for helm charts.
"""

import os
import subprocess
from cement import Controller, ex
from mpaas.mpaas_exceptions import TemplateFetchError


class Museum(Controller):
    """
    Child class of the Controller class.
    Handles the 'museum' sub-commands.
    """
    class Meta:
        """
        Meta class attributes.
        'museum' is a nested sub-command of the base 'mpaas' command
        """
        label = 'museum'
        aliases = ['museums']
        stacked_type = 'nested'
        stacked_on = 'base'
        usage = 'kompaas [SUB-COMMANDS]'
        help = 'Handle museums.'

    @ex(
        help='Get templates from a chart museum.',

        arguments=[
            (
                ['url'],
                {'action': 'store'}
            ),
            (
                ['--id'],
                {'action': 'store'}
            ),
            (
                ['--password'],
                {'action': 'store'}
            ),
        ],
    )
    def get(self):
        """
        Downloads new templates from target chart museum.
        Places them in the app's templates directory.
        """

        reponame = self.app.pargs.url.split('//')[-1].replace('.', '').replace('/', '')
        helmurl = self.app.pargs.url
        helmpwd = self.app.pargs.password
        helmuser = self.app.pargs.id
        downloads_path = self.app.config.get('mpaas', 'templates_dir')
        temp_path = self.app.config.get('mpaas', 'repo_file')

        # If there is no downloads directory, create it
        if os.path.isdir(downloads_path) is False:
            os.makedirs(downloads_path)

        # If credentials are provided, assume target museum is private.
        if helmpwd and helmuser:
            subprocess.run(['helm', 'repo', 'add',
                            reponame, helmurl,
                            '--password', helmpwd,
                            '--username', helmuser],
                           stdout=subprocess.DEVNULL)

        # If no credentials are provided, assume target museum is public
        else:
            subprocess.run(['helm', 'repo', 'add',
                            reponame, helmurl],
                           stdout=subprocess.DEVNULL)

        # Output all chart names in target museum to a temporary file,
        # with each line of the temp file containing the name of one chart
        subprocess.run(['/bin/sh', '-c', "helm search " + reponame +
                        """| awk -F "/" 'NR>1{ $1 = "" ; print $0 }' \\
                        | awk -F " " '{ print $1 " " $2 }' >""" + temp_path],
                       stdout=subprocess.DEVNULL)

        data = {'context': self.app.ch.get_context_all(), 'charts':[]}
        temp_file = open(temp_path, 'r')
        for line in temp_file.readlines():
            parsed_line = str(line).strip('\n').split(' ')
            data['charts'].append({'name': parsed_line[0], 'version': parsed_line[1]})

        self.app.render(data, 'list/museum_charts.jinja2')


    @ex(
        help='Get templates from a chart museum.',

        arguments=[
            (
                ['url'],
                {'action': 'store'}
            ),
            (
                ['--id'],
                {'action': 'store'}
            ),
            (
                ['--password'],
                {'action': 'store'}
            ),
            (
                ['chartname'],
                {'action': 'store'}
            ),
            (
                ['--version'],
                {'action': 'store'}
            ),
            (
                ['--downloadpath'],
                {'action': 'store'}
            ),
            (
                ['--norepoupdate'],
                {'action': 'store_true'}
            ),
        ],
    )
    def download(self):
        """
        Downloads templates from a museum
        """

        helmurl = self.app.pargs.url
        helmpwd = self.app.pargs.password
        helmuser = self.app.pargs.id
        chartname = self.app.pargs.chartname
        reponame = self.app.pargs.url.split('//')[-1].replace('.', '').replace('/', '')
        if not self.app.pargs.downloadpath:
            downloads_path = self.app.config.get('mpaas', 'templates_dir')
        else:
            downloads_path = self.app.pargs.downloadpath
        temp_path = self.app.config.get('mpaas', 'repo_file')

        # If there is no downloads directory, create it
        if os.path.isdir(downloads_path) is False:
            os.makedirs(downloads_path)

        # If credentials are provided, assume target museum is private.
        if helmpwd and helmuser:
            subprocess.run(['helm', 'repo', 'add',
                            reponame, helmurl,
                            '--password', helmpwd,
                            '--username', helmuser],
                           stdout=subprocess.DEVNULL)

        # If no credentials are provided, assume target museum is public
        else:
            subprocess.run(['helm', 'repo', 'add',
                            reponame, helmurl],
                           stdout=subprocess.DEVNULL)

        if self.app.pargs.norepoupdate:
            self.app.log.info('Repository added but not upgraded : %s' % (helmurl))
        else:
            subprocess.run(['helm', 'repo', 'update'])

        # Retrieve the chart name and chart version from the helm search command
        subprocess.run(['/bin/sh', '-c', "helm search " + reponame +
                        """| awk -F "/" 'NR>1{ $1 = "" ; print $0 }' \\
                           | awk -F " " '{ print $1 " " $2 }' >""" + temp_path],
                       stdout=subprocess.DEVNULL)

        # Using the temp file, try to download each template individually
        temp_file = open(temp_path, 'r')

        found = False
        for line in temp_file.readlines():
            if line.split(' ')[0] == chartname or chartname == 'all':
                version = line.split(' ')[1]
                found = True
                args = ['helm', 'fetch',
                        reponame + '/' + line.split(' ')[0],
                        '--untar',
                        '-d', downloads_path]

                if self.app.pargs.version:
                    version = self.app.pargs.version
                    args.extend(['--version', self.app.pargs.version])
                try:
                    subprocess.run(args)
                    self.app.log.info('Successfully added template %s %s' % (line.split(' ')[0], version))
                except:
                    raise TemplateFetchError(line)

    @ex(
        help='Add a museum repo and do nothing more',

        arguments=[
            (
                ['url'],
                {'action': 'store'}
            ),
            (
                ['--id'],
                {'action': 'store'}
            ),
            (
                ['--password'],
                {'action': 'store'}
            ),

        ],
    )
    def add(self):
        """
        Add a museum repo and do nothing more
        """

        helmurl = self.app.pargs.url
        helmpwd = self.app.pargs.password
        helmuser = self.app.pargs.id
        reponame = self.app.pargs.url.split('//')[-1].replace('.', '').replace('/', '')
        temp_path = self.app.config.get('mpaas', 'repo_file')

        # If credentials are provided, assume target museum is private.
        if helmpwd and helmuser:
            subprocess.run(['helm', 'repo', 'add',
                            reponame, helmurl,
                            '--password', helmpwd,
                            '--username', helmuser],
                           stdout=subprocess.DEVNULL)

        # If no credentials are provided, assume target museum is public
        else:
            subprocess.run(['helm', 'repo', 'add',
                            reponame, helmurl],
                           stdout=subprocess.DEVNULL)

