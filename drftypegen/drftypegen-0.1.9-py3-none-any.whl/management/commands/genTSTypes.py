import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

try:
    from drftypegen.adapters import *
    from drftypegen.compilers import TypeScriptCompiler
except:
    from drftypegen.drftypegen.adapters import *
    from drftypegen.drftypegen.compilers import TypeScriptCompiler


class Command(BaseCommand):
    def add_arguments(self, parser):
        default_filename = os.path.join(settings.STATIC_ROOT, "typegenTS.ts")
        parser.add_argument("--file", type=str, default=default_filename)

    def handle(self, *args, **options):
        filename = options["file"]
        data = TypeScriptCompiler().generate()
        if WAGTAIL_SUPPORT:
            data += "\n\n" + TypeScriptCompiler(WagtailAdapter).generate()
        with open(filename, "w") as outp:
            outp.write(data)
