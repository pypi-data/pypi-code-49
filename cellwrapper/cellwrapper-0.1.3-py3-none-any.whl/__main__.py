#!/bin/env python
import os
import subprocess
import argparse
import time
import logging
import sys
import socket
import re
import collections
import xml.etree.ElementTree as ET
import warnings
from . import cellwrapper

POLL_TIME = 5
SGE_RECOMMENDED_LIMIT = 30
CELLWRAPPER_LOG_PREFIX = '[CELLWRAPPER]: '

# Set up a basic logger
LOGGER = logging.getLogger('something')
myFormatter = logging.Formatter('%(asctime)s: %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(myFormatter)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.DEBUG)
myFormatter._fmt = "[CELLWRAPPER]: " + myFormatter._fmt



def run_cellwrapper(args=None):
    parser = argparse.ArgumentParser('A wrapper around the cellranger product from 10X genomics that automates all processing of multiple samples from flowcell to matrix. See https://github.com/cole-trapnell-lab/cellwrapper.')
    parser.add_argument('sample_sheet', help='File with sample fields as defined in the README.md file.')
    parser.add_argument('--samplelimit', '-s', default=1, type=int, help='Maximum cellranger pipestances to allow to run concurrently.')
    parser.add_argument('--cellranger_log', '-l', default='cellranger.log', help='Log for cellranger output from cellwrapper calls.')
    parser.add_argument('--installation', '-i', default='/home/sfurla/software/cellranger', help='Path to parent directory containing cellranger-<version> and reference data folders. Default is general lab install.')
    parser.add_argument('--aggregate', '-a', help='ID / output directory to output aggregated dataset from all samples in sample sheet. Only valid for samplesheets with samples all run with same version of cellranger and with cellranger 1.2.1+')
    parser.add_argument('--archived', action='store_true', help='Only supported on NextSeq. Flag if runs in the samplesheet are archived where no BCL directory is present. Uses a hacky method to get flow cell ID from original BCL directory name. No guarantees about this working and obviously demux directory must already be present.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Run more verbosely, (will echo shell commands)')
    parser.add_argument('--jobmode', '-jm', default='local', type=str, help='To run in cluster mode, either place an abbreviated code for a jobmanager template (e.g. "pbspro" or "sge") or the full path to a cluster template file, defaults to "local" mode')
    args = parser.parse_args()
    print(vars(args))

    if args.jobmode=='local' and args.samplelimit > 1:
        warnings.warn("You have selected a sample limit of more than 1 but are running in local mode; samplelimit will be set to 1; change jobmode if you want to run in cluster mode", RuntimeWarning)
    if args.jobmode!='local' and args.samplelimit == 1:
        warnings.warn("You have selected a sample limit of 1 but are running in cluster mode; this will likely not run as quickly as it could in cluster mode", RuntimeWarning)

    #quit()
    # Check python version > 2.7
    if sys.version_info <= (2, 7):
        raise RuntimeError('Python 2.7 or greater is required to run cellwrapper. Python 3.X also supported.')
    ##removed##
    # # Check for SGE_CLUSTER_NAME
    # env = os.environ.copy()
    # if not 'SGE_CLUSTER_NAME' in env:
    #     raise EnvironmentError('cellranger expects the SGE_CLUSTER_NAME environment variable to be set for SGE mode. Set this to a reasonable value such as your default queue. For example, Shendure lab folks might run: export SGE_CLUSTER_NAME="ravana.q". Set and restart cellwrapper.')

    # Validate arguments
    args.sample_sheet = os.path.abspath(args.sample_sheet)
    if not os.path.exists(args.sample_sheet):
        raise ValueError('Specified samplesheet cannot be found: %s' % args.sample_sheet)

    if not os.path.exists(args.installation):
        raise ValueError('Specified cellranger installation not found: %s' % args.installation)

    if args.samplelimit > SGE_RECOMMENDED_LIMIT:
        raise ValueError('%s concurrent cellranger pipestances is a bad idea. Try %s or less.' % (args.samplelimit, SGE_RECOMMENDED_LIMIT))

    # Initialize cellranger with sample and run info
    LOGGER.info("Logging to %s... examine this file if samples fail." % args.cellranger_log)

    cellranger = cellwrapper.CellRanger(args.sample_sheet, sample_limit=args.samplelimit, cellranger_log=open(args.cellranger_log, 'w'), install=args.installation, verbose=args.verbose)

    for sample_id in cellranger.get_sample_ids():
        LOGGER.info('Demuxing sample flowcell(s): %s ...' % sample_id)

        cellranger.demux(sample_id, archived=args.archived, verbose=args.verbose, jobmode=args.jobmode)
        LOGGER.info('Demuxing complete...')

    LOGGER.info('All demux runs complete. Begin data processing...')

    # Process samples
    for sample_id in cellranger.get_sample_ids():
        LOGGER.info(cellranger.get_pipeline_status_string(sample_id))
        while cellranger.at_sample_limit():
            time.sleep(POLL_TIME)

        LOGGER.info('Adding sample pipestance to queue: %s ...' % sample_id)

        cellranger.run(sample_id=sample_id, verbose=args.verbose, jobmode=args.jobmode)

    # Wait for all jobs to finish
    LOGGER.info(cellranger.get_pipeline_status_string())
    samples_remaining = cellranger.running_sample_count()

    while samples_remaining > 0:
        updated_sample_count = cellranger.running_sample_count()
        # Only log messages if sample count changes
        if updated_sample_count != samples_remaining:
            LOGGER.info(cellranger.get_pipeline_status_string())
            samples_remaining = updated_sample_count

        time.sleep(POLL_TIME)

    # Print summary
    sample_summary = cellranger.get_sample_summary()
    LOGGER.info('All samples processed:')
    LOGGER.info(sample_summary)

    # Optionally aggregate samples into a single dataset
    if args.aggregate:
        if cellranger.failed_sample_count() == 0:
            LOGGER.info('Aggregating samples into a single dataset with aggr pipeline...')

            try:
                cellranger.aggregate(aggregate_id=args.aggregate, verbose=args.verbose, jobmode=args.jobmode)
                # cellranger.aggregate(args.aggregate, jobmode='sge')

                LOGGER.info('Aggregation complete.')
            except ValueError as e:
                LOGGER.info('Aggregation failed.')
                LOGGER.info('Done! Exit.')

                LOGGER.info('Error from aggregation:')
                raise e
        else:
            LOGGER.info('WARNING: skipping aggregation because some samples failed')

    LOGGER.info('Done! Exit.')


if __name__ == "__main__":
    run_cellwrapper()

"""
[parsed_runsheet[i-1] for i in list(parse_range_list("1:4,11,12"))]

"""



