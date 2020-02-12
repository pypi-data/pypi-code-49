import os
import shutil
import argparse
from django.conf import settings
from django.template import Template, Context
from django.core.management.base import BaseCommand, CommandError
from django.utils.module_loading import import_string


class Command(BaseCommand):
    help = 'Generate configuration files.'

    def add_arguments(self, parser):
        parser.add_argument('template', type=str, nargs="?",
            help=("Optional. Name of the template to compile. It should be relative to "
                "the path set in CONFIGEN_TEMPLATES_DIR setting. If not "
                "provided, all the templates present in the directory set by "
                "CONFIGEN_TEMPLATES_DIR setting are compiled."
            )
        )
        parser.add_argument('--print', action='store_true', 
            help=("Print the compiled template to stdout. Useful if you want to "
                "inspect the output without creating/overwriting the output file."
            )
        )
        parser.add_argument('--printname', action='store_true', 
            help=("Print the name of the output file. Useful if you want to see "
                "what name the output file will be saved as without "
                "creating/overwriting the output file."
            )
        )
        parser.add_argument('--extra', nargs="*", 
            help=("Extra arguments that you want to pass to "
                "the config context processors."
            )
        )

    def handle(self, *args, **options):
        template = options['template']
        print_file = options['print']
        print_filename = options['printname']
        extra_args = options['extra'] or []
        verbosity = options['verbosity']

        self.initialize_settings()

        self.make_initial_checks()

        if template:
            # check if provided template exists
            if not os.path.isfile(os.path.join(self.templates_dir, template)):
                raise CommandError("No file named %s exists in %s" % (template, self.templates_dir))

            #:TODO: provide support for nested directories.
            # Until then if user provides template name via command line
            # such as path/to/template.conf, raise error
            if os.path.basename(template) != template:
                raise CommandError(
                    "Currently reading files from nested "
                    "directories is not supported."
                )

            templates = [template]
        else:
            templates = os.listdir(self.templates_dir)

        for template in templates:
            # :TODO: provide support for nested directories.
            # Until then, skip
            if os.path.isdir(os.path.join(self.templates_dir, template)):
                if verbosity > 0:
                    self.stdout.write("Skipping directory %s" % template)
                continue

            context = {} 
            context.update(self.default_context.get('*', {}))
            context.update(self.default_context.get(template, {}))
            meta = {}
            meta.update(self.default_meta.get('*', {}))
            meta.update(self.default_meta.get(template, {}))

            # run context processors
            for processor in self.config_processors:
                try:
                    func = import_string(processor)
                except ImportError as e:
                    raise CommandError("Config context processor couldn't be loaded. %s" % e)

                data = func(template, *extra_args)

                if isinstance(data, list) or isinstance(data, tuple):
                    new_context = data[0]
                    new_meta = data[1]
                else:
                    new_context = data
                    new_meta = {}

                context.update(new_context)
                meta.update(new_meta)

            template_infile = open(os.path.join(self.templates_dir, template), 'r')
            t = Template(template_infile.read())

            # if output directory doesn't exist, create it
            if not os.path.isdir(self.output_dir):
                os.mkdir(self.output_dir)

            if 'outfile' in meta:
                outfile_name = meta['outfile'].format(template_name=template)
            else:
                outfile_name = template

            if print_file:
                self.stdout.write(t.render(Context(context)))
            elif print_filename:
                self.stdout.write(outfile_name)
            else:
                template_outfile = open(os.path.join(self.output_dir, outfile_name), 'w')
                if verbosity > 0:
                    self.stdout.write("Writing to %s..." % outfile_name)
                template_outfile.write(t.render(Context(context)))
                template_outfile.close()

            template_infile.close()

    def initialize_settings(self):
        """Sets attributes on class mapping to settings variables"""

        self.templates_dir = getattr(settings, 'CONFIGEN_TEMPLATES_DIR', None)
        self.output_dir = getattr(settings, 'CONFIGEN_OUTPUT_DIR', None)
        self.config_processors = getattr(settings, 'CONFIGEN_CONFIG_PROCESSORS', [])
        self.default_context = getattr(settings, 'CONFIGEN_DEFAULT_CONTEXT', {})
        self.default_meta = getattr(settings, 'CONFIGEN_DEFAULT_META', {})


    def make_initial_checks(self):
        """Make initial checks necessary for running"""

        # Check if settings are configured
        if not self.templates_dir:
            raise CommandError("CONFIGEN_TEMPLATES_DIR setting not configured.")

        if not self.output_dir:
            raise CommandError("CONFIGEN_OUTPUT_DIR setting not configured.")

        # Check if templates directory exists
        if not os.path.isdir(self.templates_dir):
            raise CommandError(
                "Templates directory for CONFIGEN_TEMPLATES_DIR setting "
                "doesn't exist - '%s'" % self.templates_dir
            )

