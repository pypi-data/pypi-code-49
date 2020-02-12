import sys
import os
import argparse

from sequana.pipelines_common import *
from sequana.snaketools import Module
from sequana import logger
logger.level = "INFO"

col = Colors()

NAME = "variant_calling"
m = Module(NAME)
m.is_executable()


class Options(argparse.ArgumentParser):
    def __init__(self, prog="variant_calling"):
        usage = col.purple(
            """This script prepares the sequana pipeline variant_calling layout to
            include the Snakemake pipeline and its configuration file ready to
            use.

            In practice, it copies the config file and the pipeline into a
            directory (variant_calling) together with an executable script

            For a local run, use :

                sequana_pipelines_variant_calling --input-directory PATH_TO_DATA --run-mode local

            For a run on a SLURM cluster:

                sequana_pipelines_variant_calling --input-directory PATH_TO_DATA --run-mode slurm

        """
        )
        super(Options, self).__init__(usage=usage, prog=prog, description="",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        # add a new group of options to the parser
        so = SlurmOptions()
        so.add_options(self)

        # add a snakemake group of options to the parser
        so = SnakemakeOptions(working_directory=NAME)
        so.add_options(self)

        # add a data group of options to the parser
        so = InputOptions()
        so.add_options(self)

        so = GeneralOptions()
        so.add_options(self)

        pipeline_group = self.add_argument_group("pipeline")
        pipeline_group.add_argument(
            "--reference",
            dest="reference",
            required=True,
            help="The input reference to mapped reads onto"
        )
        pipeline_group.add_argument(
            "--annotation",
            dest="annotation",
            default=None,
            help="The annotation for snpeff"
        )
        pipeline_group.add_argument("--threads", dest="threads", default=4, type=int)


def main(args=None):
    if args is None:
        args = sys.argv

    if "--version" in sys.argv:
        print_version(NAME)
        sys.exit(0)

    options = Options(NAME).parse_args(args[1:])

    manager = PipelineManager(options, NAME)

    # create the beginning of the command and the working directory
    manager.setup()

    # fill the config file with input parameters
    cfg = manager.config.config
    cfg.input_directory = os.path.abspath(options.input_directory)
    cfg.input_pattern = options.input_pattern
    cfg.input_readtag = options.input_readtag
    if options.annotation:
        cfg.snpeff.do = True
        cfg.snpeff.reference_file = os.path.abspath(options.annotation)

    cfg.bwa_mem_ref.reference = os.path.abspath(options.reference)

    # finalise the command and save it; copy the snakemake. update the config
    # file and save it.
    manager.teardown()


if __name__ == "__main__":
    main()
