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


class Sample:
    """
    Generic sample class. Non-functional. Subclasses must define a command attribute.
    """

    def __init__(self, sample_name, sample_index, flow_cells, reference, cell_count, pipeline):
        """
        Args:
            sample_name (str): name provided by user to the sample
            sample_index (str): Index from well plate used for indexing of sample
            flow_cells (list of str): list of flow full paths to flow cell BCL directories
            reference (str): full path to reference to use with cellranger
            cell_count (int): approximate cell count expected
            pipeline (str): Full path to the particular installation folder to use, for example: <path>/cellranger-1.1.0

        Raises:
            ValueError if either flowcell or reference are not found on filesystem.
            ValueError if estimated cell count is zero or less.

        """

        self.sample_name = sample_name
        self.sample_index = sample_index
        self.flow_cells = flow_cells
        self.reference = reference
        self.cell_count = cell_count
        self.pipeline = pipeline
        self.supports_aggregation = True
        self.command = 'cellranger'

        self.get_executable()

        if self.cell_count <= 0:
            raise ValueError('Invalid estimated cell count (must be > 0): %s (%s, %s)' % (self.cell_count, sample_name, sample_index))

        # Validate path inputs
        # Convert reference into a refdata path
        pipeline_install = os.path.abspath(os.path.join(self.pipeline, os.pardir))
        pipeline_base = os.path.basename(self.pipeline)

        self.reference = os.path.join(pipeline_install, 'refdata-%s' % pipeline_base, self.reference)
        print(self.reference)
        if not os.path.exists(self.reference):
            raise ValueError('The specified reference could not be found: %s (%s, %s)' % (reference, sample_name, sample_index))

        for flow_cell in self.flow_cells:
            if not os.path.exists(flow_cell):
                raise ValueError('The specified flowcell could not be found: %s (%s, %s)' % (flow_cell, sample_name, sample_index))

        if len(set(self.flow_cells)) != len(self.flow_cells):
            raise ValueError('Duplicate flow cells specified for sample: %s (%s, %s)' % (','.join(self.flow_cells), sample_name, sample_index))

        self.is_demuxed = False
        self.fastq_paths = []
        self.complete = False

    def get_executable(self):
        """
        Checks set pipeline intall to confirm that expected executable is present.

        Returns:
             True if installed and False if not.

        """

        path = os.path.join(self.pipeline, self.command)

        if not os.path.exists(path):
            raise ValueError('Expected executable not found in install directory: %s' % path)

        return path

    def get_sample_id(self):
        """
        Returns a sample ID for sample.

        Returns:
             str: sample id as a combination of sample_name and index

        """
        return '%s_%s' % (self.sample_name, self.sample_index)

    def get_flow_cells(self):
        """
        Returns list of flow cells associated with the sample.

        Returns:
            list of str: list of flow cells associated with sample.

        """
        return self.flow_cells

    def get_molecule_h5_path(self):
        """
        Gets the expected molecule h5 path for pipeline output.

        Returns:
            str: the expected path to molecule h5 file.
        """
        return '%s/outs/molecule_info.h5' % self.get_sample_id()

    def get_fastqs(self):
        """
        Getter for fastqs (empty if samples not demuxed).

        Returns:
             list of str: list of absolute paths to fastqs for demuxed sample of empty list if not demuxed.

        """
        return self.fastq_paths

    def set_fastqs(self, fastq_paths):
        """
        Setter for fastqs.

        Args:
            fastq_paths: set of absolute paths for fastq files associated with sample as produced by cellranger demux.

        Raises:
            ValueError if not all fastq paths exist.

        """

        for fastq in fastq_paths:
            if not os.path.exists(fastq):
                raise ValueError('FASTQs not found. Did you quit cellwrapper before demux completed? If so, remove demux output folder and start again.')
            else:
                self.fastq_paths.append(fastq)


class CellRangerSample(Sample):
    """
    Class to keep track of properties of a cellranger sample.
    """

    def __init__(self, **kwargs):
        Sample.__init__(self, **kwargs)
        self.command = 'cellranger'

    def get_run_command(self):
        """
        Returns the sub-command used to run the main thread of cellranger execution.
        """
        return 'count'


class CellRanger:
    """
    Class to store a set of CellRanger samples and manage execution of cellranger functions.
    """

    def __init__(self, sample_sheet, sample_limit, cellranger_log, install, verbose):
        """
        Args:
            sample_sheet (str): Name of sample sheet file used to define cellranger samples. See README.
            samplelimit (int): Max number of cellranger pipestances to run at once.
            cellranger_log (str): name of a log file to use for cellranger output.
            install (str): name of parent folder that contains all installs of cellranger and refdata tools

        Note:
            Preprocesses sample_sheet file to remove windows newlines from Excel as users may want to use Excel to generate.

        """

        self.samples = collections.OrderedDict()
        self.running_samples = collections.OrderedDict()
        self.completed_samples = collections.OrderedDict()
        self.failed_samples = collections.OrderedDict()

        self.sample_limit = sample_limit
        self.cellranger_log = cellranger_log
        self.install = install
        self.verbose = verbose


        # Validate arguments
        if not os.path.exists(sample_sheet):
            raise ValueError('Specified samplesheet cannot be found: %s' % sample_sheet)

        # Keep track of all indices and names ever seen across flow cells
        sample_names = set()
        flow_cell_index_combos = set()

        # Preprocess samplesheet to remove newlines
        CellRanger._convert_windows_newlines(sample_sheet)

        for sample in CellRanger._parse_sample_sheet(open(sample_sheet)):
            SampleConstructor = CellRanger.sample_factory(sample['pipeline'])

            cellranger_sample = SampleConstructor(
                sample_name=sample['sample_name'].replace('.', '_'),  # periods break cellranger
                sample_index=sample['sample_index'],
                flow_cells=sample['flow_cells'],
                reference=sample['reference'],
                cell_count=sample['cell_count'],
                pipeline=os.path.join(self.install, sample['pipeline']),
            )

            # Track name and sample-index collisions within flow-cells
            if cellranger_sample.sample_name in sample_names:
                raise ValueError('Duplicated sample name found in sample sheet: %s' % cellranger_sample.sample_name)

            for flow_cell in cellranger_sample.flow_cells:
                if (flow_cell, cellranger_sample.sample_index) in flow_cell_index_combos:
                    raise ValueError('Duplicated sample-index/flowcell combination found in sample sheet: %s, %s' % (flow_cell, cellranger_sample.sample_index))

            sample_names.add(cellranger_sample.sample_name)
            for flow_cell in cellranger_sample.flow_cells:
                flow_cell_index_combos.add((flow_cell, cellranger_sample.sample_index))

            # Store sample objects in index
            self.samples[cellranger_sample.get_sample_id()] = cellranger_sample

    def get_mkfastq_samplesheet(self, flowcell):
        # Note must use BCL2FASTQ samplesheet here otherwise the demux doesn't correctly
        # handle non-10X indices as 10X samples (important for our CFG stuff, etc.)
        DEMUX_SAMPLESHEET = """
[Header],,,,,,,,
IEMFileVersion,4,,,,,,,
Investigator Name,rjr,,,,,,,
Experiment Name,hiseq_test,,,,,,,
Date,8/15/16,,,,,,,
Workflow,GenerateFASTQ,,,,,,,
Application,HiSeq FASTQ Only,,,,,,,
Assay,TruSeq HT,,,,,,,
Description,hiseq sample sheet,,,,,,,
Chemistry,Default,,,,,,,
,,,,,,,,
[Reads],,,,,,,,
26,,,,,,,,
98,,,,,,,,
,,,,,,,,
[Settings],,,,,,,,
,,,,,,,,
[Data],,,,,,,,
Sample_ID,Sample_Name,Sample_Plate,Sample_Well,I7_Index_ID,index,Sample_Project,Description
%s
"""
        samples_with_flowcell = [self.samples[sample] for sample in self.samples if flowcell in self.samples[sample].get_flow_cells()]

        lines = []
        for sample in samples_with_flowcell:
            sample_name = sample.sample_name
            index = sample.sample_index
            sample_plate = ''
            sample_well = ''
            project = ''
            description = ''

            lines.append(','.join([sample_name, sample_name, sample_plate, sample_well, index, index, project, description]))

        return DEMUX_SAMPLESHEET % '\n'.join(lines)

    def demux(self, sample_id, verbose, archived=False, **kwargs):
        """
        Runs cellranger demux on flowcell(s) associated with a particular sample.

        Args:
            sample_id (str): ID for sample to demux.
            archived (bool): Only supported on NextSeq. Flag for runs that are archived where no BCL directory is present. Uses a hacky method to get flow cell ID from original BCL directory name. No guarantees about this working and obviously demux directory must already be present.
            **kwargs: additional arguments to the cellranger demux utility. Not validated except for conflict with
                --run parameter.

        Examples:
            myCellRanger.demux(flow_cell, jobmode='sge')

        Raises:
            ValueError if any flowcell did not demux properly or if invalid kwargs.

        Note:
             cellranger demux generates directories in the current working directory.

        """

        self._validate_sample_id(sample_id)
        reserved_arguments = set('run')
        additional_arguments = CellRanger._get_user_options_kwargs_string(reserved_arguments, **kwargs)

        unprocessed_flow_cells = self.get_unprocessed_flowcells(sample_id, archived)

        for flow_cell in unprocessed_flow_cells:
            # Write out a samplesheet for mkfastq for each flowcell
            mkfastq_text = self.get_mkfastq_samplesheet(flow_cell)
            flow_cell_shortname = CellRanger._get_flow_cell_shortname(flow_cell, archived)
            mkfastq_file = '.%s.cellwrapper.sample_sheet.txt' % flow_cell_shortname

            with open(mkfastq_file, 'w') as output_file:
                output_file.write(mkfastq_text)

            # Run demux with mkfastq pipeline
            command = '%s mkfastq --id %s --run=%s --samplesheet=%s %s' % (self.samples[sample_id].get_executable(), flow_cell_shortname, flow_cell, mkfastq_file, additional_arguments)
            if verbose:
                print(command)
            subprocess.check_call(command, stdout=self.cellranger_log, stderr=self.cellranger_log, shell=True)

        # Verify that demux was successful
        final_unprocessed_flowcells = self.get_unprocessed_flowcells(sample_id, archived)
        self.set_demuxed(sample_id, len(final_unprocessed_flowcells) == 0, archived)

        if not self.samples[sample_id].is_demuxed:
            raise ValueError('Flowcell(s) did not demux as expected: %s' % ','.join(final_unprocessed_flowcells))

    def run(self, sample_id, verbose, **kwargs):
        """
        Runs cellranger run on a particular sample.

        Args:
            sample_id (str): ID for sample to run cellranger on.
            **kwargs: additional arguments to the cellranger run utility. Not validated except for conflict with
                id, transcriptome, fastqs, indices arguments.

        Returns:
            True if sample could be scheduled or False otherwise.

        Note:
            cellranger run generates directories and files in the current working directory.

        """
        self._validate_sample_id(sample_id)

        # Don't go over the limit
        self.update_sample_status()

        if self.at_sample_limit():
            return False

        if sample_id in self.running_samples:
            raise ValueError('Sample is already running in a pipestance: %s' % sample_id)
        elif sample_id in self.failed_samples:
            raise ValueError('Sample has already run and failed: %s' % sample_id)
        elif sample_id in self.completed_samples:
            raise ValueError('Sample has already run and completed: %s' % sample_id)

        # Run command and add to completed samples
        self._add_pipestance(sample_id=sample_id, verbose=verbose, **kwargs)

    def aggregate(self, aggregate_id, verbose, **kwargs):
        """
        Runs cellranger aggr on the set of completed samples.

        Args:
            **kwargs: additional arguments to the cellranger run utility. Not validated except for conflict with
                id, transcriptome, fastqs, indices arguments.

        Note:
            cellranger aggr generates directories and files in the current working directory.

        """
        # Ensure that all samples can be aggregated (all on a version of cellranger that supports aggr)
        aggregation_supported = True

        # TODO should also really check that all have same version
        for sample_name, sample in self.samples.items():
            if not sample.supports_aggregation:
                aggregation_supported = False

        if not aggregation_supported:
            raise ValueError('Automatic aggregation not supported for one or more samples in sample sheet... please check cellranger versions')

        # Make the sample sheet required for aggr
        aggregation_csv = '%s.aggregation.csv' % aggregate_id
        sample_ids = []
        molecule_h5s = []

        for sample_id, sample in self.samples.items():
            molecule_h5 = sample.get_molecule_h5_path()

            if not os.path.exists(molecule_h5):
                raise ValueError('Expected molecule_h5 file not found: %s' % molecule_h5)
            else:
                molecule_h5s.append(molecule_h5)
                sample_ids.append(sample_id)

        with open(aggregation_csv, 'w') as csv_out:
            csv_out.write(','.join(['library_id', 'molecule_h5']) + '\n')

            for sample, h5 in zip(sample_ids, molecule_h5s):
                csv_out.write(','.join([sample, h5]) + '\n')

        # Run command
        additional_arguments = self._get_user_options_kwargs_string(set(), **kwargs)
        if verbose:
            print('%s aggr --id=%s --csv=%s %s' % (self.samples[sample_ids[0]].get_executable(), aggregate_id, aggregation_csv, additional_arguments))
        subprocess.check_call('%s aggr --id=%s --csv=%s %s' % (self.samples[sample_ids[0]].get_executable(), aggregate_id, aggregation_csv, additional_arguments), shell=True, stderr=self.cellranger_log, stdout=self.cellranger_log)

    def _add_pipestance(self, sample_id, verbose, **kwargs):
        """
        Helper function to add a pipestance to the current queue.

        Args:
            sample_id: sample name
            **kwargs: additional arguments as specfied for run()

        Note:
            Adds to working queue.

        """
        # Validate inputs
        self._validate_sample_id(sample_id)
        self.update_sample_status()

        if self.at_sample_limit():
            raise ValueError('Already at sample limit, cannot add pipestance: %s' % sample_id)

        additional_arguments = self._get_user_options_kwargs_string(set(), **kwargs)
        fastq_list = ','.join(self.samples[sample_id].get_fastqs())
        sample_name = self.samples[sample_id].sample_name
        expect_cells = self.samples[sample_id].cell_count
        transcriptome = self.samples[sample_id].reference
        if verbose:
            print('%s %s --id %s --fastqs %s --sample %s --transcriptome %s --expect-cells=%s %s' % (self.samples[sample_id].get_executable(), self.samples[sample_id].get_run_command(), sample_id, fastq_list, sample_name, transcriptome, expect_cells, additional_arguments))
        pid = subprocess.Popen('%s %s --id %s --fastqs %s --sample %s --transcriptome %s --expect-cells=%s %s' % (self.samples[sample_id].get_executable(), self.samples[sample_id].get_run_command(), sample_id, fastq_list, sample_name, transcriptome, expect_cells, additional_arguments), shell=True, stderr=self.cellranger_log, stdout=self.cellranger_log)
        self.running_samples[sample_id] = pid

    def get_pipeline_status_string(self, sample_id=None):
        """
        Helper function to get the current status of the pipeline for active samples.

        Return:
             str: formatted string with status of pipeline.

        """
        self.update_sample_status()
        prefix = ''

        if self.at_sample_limit() and sample_id:
            prefix = 'At sample limit (%s). Holding %s.' % (self.sample_limit, sample_id)
        elif self.processed_sample_count() == len(self.samples):
            prefix = 'All samples in flight.'

        suffix = '[%s queued; %s completed; %s failed]' % (self.running_sample_count(),
                                                           self.completed_sample_count(),
                                                           self.failed_sample_count(),
                                                           )

        return '%s %s' % (prefix, suffix)

    def processed_sample_count(self):
        """
        Helper to get the total number of samples processed thus far.

        Returns:
             int: total processed samples thus far.

        """
        return self.running_sample_count() + self.completed_sample_count() + self.failed_sample_count()

    def at_sample_limit(self):
        """
        Determine if already at limit for running pipestances.

        Returns:
            True if at set sample limit and False otherwise.

        """
        self.update_sample_status()
        return len(self.running_samples) >= self.sample_limit

    def running_sample_count(self):
        """
        Getter for running samples count.

        Returns:
            int: number of samples in progress.

        """
        self.update_sample_status()
        return len(self.running_samples)

    def failed_sample_count(self):
        """
        Getter for failed samples count.

        Returns:
            int: number of samples that have failed.

        """
        self.update_sample_status()
        return len(self.failed_samples)

    def completed_sample_count(self):
        """
        Getter for completed samples count.

        Returns:
            int: number of samples that have completed.

        """
        self.update_sample_status()
        return len(self.completed_samples)

    def update_sample_status(self):
        """
        Update running sample list based on which pipestances have completed.

        Notes:
             Modifies list of samples in progress, failed, and completed samples

        """
        samples_to_delete = []

        # Move samples to completed or failed lists and mark for deletion
        for sample_id, sample in self.running_samples.items():
            status = sample.poll()

            if status:
                samples_to_delete.append(sample_id)
                self.failed_samples[sample_id] = status
            elif status is not None:
                samples_to_delete.append(sample_id)
                self.completed_samples[sample_id] = status

        # Delete any completed samples
        for sample_id in samples_to_delete:
            del self.running_samples[sample_id]

    def get_sample_ids(self):
        """
        Get a list of sample IDs associated with cellranger object. Can be passed to access

        Returns:
            list of str: list of sample_ids for use with other methods.

        """

        return [sample_id for sample_id in self.samples]

    def set_demuxed(self, sample_id, demuxed, archived=False):
        """
        Sets demuxed status of a sample.

        Args:
            sample_id (str): sample_id for sample
            demuxed (bool): value of demuxed status for flowcells
            archived (bool): Only supported on NextSeq. Flag for runs that are archived where no BCL directory is present. Uses a hacky method to get flow cell ID from original BCL directory name. No guarantees about this working and obviously demux directory must already be present.
        """

        self.samples[sample_id].is_demuxed = demuxed

        if demuxed:
            self.samples[sample_id].set_fastqs([CellRanger._get_fastq_path_from_flow_cell(flow_cell, archived) for flow_cell in self.samples[sample_id].flow_cells])

            for flow_cell_path, fastq_path in zip(self.samples[sample_id].get_flow_cells(), self.samples[sample_id].get_fastqs()):
                if not os.path.exists(fastq_path):
                    raise ValueError('Flowcells for sample are not demuxed: %s' % flow_cell_path)

    def get_unprocessed_flowcells(self, sample_id, archived=False):
        """
        Get a list of flowcells for a given sample that have yet to be demuxed.

        Args:
            sample_id (str): sample_id to query demuxing status for
            archived (bool): Only supported on NextSeq. Flag for runs that are archived where no BCL directory is present. Uses a hacky method to get flow cell ID from original BCL directory name. No guarantees about this working and obviously demux directory must already be present.
        Returns:
            list of str: list of flow cell paths that require demuxing

        """

        self._validate_sample_id(sample_id)

        sample = self.samples[sample_id]

        flow_cells = []

        for flow_cell in sample.get_flow_cells():
            demux_directory = CellRanger._get_flow_cell_shortname(flow_cell, archived)

            if not os.path.exists(demux_directory):
                if archived:
                    raise ValueError('Archived run specified, but original demux directory, %s, not found. Archived run only guaranteed to behave correctly for NextSeq and this functionality is a bit hacky.' % demux_directory)
                flow_cells.append(flow_cell)

        return flow_cells

    def _validate_sample_id(self, sample_id):
        """
        Helper function to raise error if sample_id specified is invald.

        Args:
            sample_id (str): sample_id for a sample

        Raises
            ValueError if sample_id is not present in object.

        """

        if sample_id not in self.samples:
            raise ValueError('Sample ID not found: %s' % sample_id)

    @staticmethod
    def _get_fastq_path_from_flow_cell(flow_cell_path, archived=False):
        """
        Helper function to get fastq path produced by cellranger from flow_cell path.

        Args:
            flow_cell_path (str): full path to flowcell
            archived (bool): Only supported on NextSeq. Flag for runs that are archived where no BCL directory is present. Uses a hacky method to get flow cell ID from original BCL directory name. No guarantees about this working and obviously demux directory must already be present.

        Returns:
            flow_cell_path (str): absolute path to fastq path produced by cellranger for the specified flowcell

        """
        return os.path.abspath(os.path.join(CellRanger._get_flow_cell_shortname(flow_cell_path, archived), 'outs', 'fastq_path'))

    @staticmethod
    def _get_user_options_kwargs_string(reserved_arguments, **kwargs):
        """
        Convert **kwargs provided by user to a string usable by cellranger as arguments.

        Args:
            **kwargs (dict): **kawargs argument provided to cellranger
            reserved_arguments (set or list of str): set of arguments prohibited for user use

        Returns:
            str: string formatted appropriately for use as cellranger options. Returns empty string if none.

        Raises:
            ValueError if user requested argument conflicts with one of the specified reserved arguments.

        """

        arguments = []
        reserved_arguments = set(reserved_arguments)

        for key, value in kwargs.items():
            normalized_key = key.strip('-').replace('_', '-')  # bowtie2 uses hypens not underscores

            # Validate user inputs to make sure no blatant conflicts
            if normalized_key in reserved_arguments:
                raise ValueError('Specified cellranger option conflicts with reserved argument: %s. \
                                 Reserved arguments are: %s' % (normalized_key, ','.join(reserved_arguments)))

            # Correctly prefix arguments by cellranger conventions
            if len(key) > 1:
                prefix = '--'
            else:
                prefix = '-'

            cellranger_argument = '%s%s' % (prefix, normalized_key)
            option_value = kwargs.get(key) if kwargs.get(key) is not None else ''

            if kwargs.get(key):
                arguments.append('%s=%s' % (cellranger_argument, option_value))
            else:
                arguments.append('%s' % (cellranger_argument))

        return ' '.join(arguments)

    @staticmethod
    def _get_flow_cell_shortname(flow_cell_path, archived=False):
        """
        Helper function to get the path that cellranger produces locally from a flow cell demux run. This now uses run info from the BCL directory.

        Args:
            flow_cell_path (str): full path to flowcell.
            archived (bool): Only supported on NextSeq. Flag for runs that are archived where no BCL directory is present. Uses a hacky method to get flow cell ID from original BCL directory name. No guarantees about this working and obviously demux directory must already be present.

        Returns:
            str: local directory name cellranger demux would output

        Examples:
            /net/shendure/vol9/seq/NEXTSEQ/160708_NS500488_0197_AHN3FKBGXX
            =>
            HN3FKBGXX

        """
        if not archived:
            bcl_run_info = os.path.join(flow_cell_path, 'RunInfo.xml')
            if not os.path.exists(bcl_run_info):
                raise ValueError('BCL RunInfo not found for specified flowcell: %s' % bcl_run_info)

            flowcells = list(ET.parse(bcl_run_info).getroot().iter('Flowcell'))
            if len(flowcells) > 1:
                raise ValueError('BCL RunInfo contains %s flowcell declarations. Expected 1.' % len(flowcells))

            return flowcells[0].text.split('-')[-1]

        else:
            # Note this only works for NextSeq
            return flow_cell_path.split('_')[-1][1:]

    @staticmethod
    def _convert_windows_newlines(file_name):
        """
        Helper function for converting windows newlines in a file as a preprocessing step in case users make samplesheet
        in excel.

        Args:
            file_name (str): name of file to convert to unix newlines.

        """
        # Read in the file in entirety first
        with open(file_name) as input:
            file_text = input.read()

        # Replace newlines produced by excel
        file_text = file_text.replace('\r', '\n')

        # Write the new output back to the file
        with open(file_name, 'w') as output:
            output.write(file_text)

    @staticmethod
    def _parse_sample_sheet(sample_sheet):
        """
        Helper function for parsing sample sheets provided by user.

        Args:
            sample_sheet (file): file object to sample sheet.

        Yields:
            Each line of the sample sheet as a dict by column name.
            Columns: sample_name, sample_index, flow_cells, reference

        """
        columns = ['sample_name', 'sample_index', 'flow_cells', 'reference', 'cell_count', 'pipeline']
        for line in sample_sheet:
            entries = [entry.strip() for entry in line.strip().split('\t')]

            if len(entries) != len(columns):
                raise ValueError('Sample sheet does not match expected columns. Expects: %s' % ','.join(columns))

            entry_dict = dict(zip(columns, entries))
            entry_dict['flow_cells'] = [entry.strip() for entry in entry_dict['flow_cells'].split(',')]
            entry_dict['cell_count'] = int(entry_dict['cell_count'])
            yield entry_dict

    def get_sample_summary(self):
        """
        Helper function to summarize pipeline run results.

        Returns:
            str: string with text summarizing status of samples that were run

        """

        self.update_sample_status()

        samples_processed = len(self.failed_samples) + len(self.completed_samples) + len(self.running_samples)

        if not len(self.samples) == samples_processed:
            raise ValueError('Not all samples have been processed: %s/%s' % (len(self.samples), self.samples_processed))

        if len(self.running_samples) > 0:
            raise ValueError('There are still samples in the queue: %s' % len(self.running_samples))

        completed_samples = '\n'.join(self.completed_samples.keys())
        failed_samples = '\n'.join(self.failed_samples.keys())

        if len(failed_samples) > 0:
            return 'Summary:\nsamples completed: %s\n\nsamples failed: %s' % (completed_samples, failed_samples)
        else:
            return 'Summary:\nsamples completed: %s\n\nNo samples failed!' % completed_samples

    @staticmethod
    def sample_factory(pipeline):
        """
        Return appropriate constructor for specified sample.

        Args:
            pipeline (str): short name of pipeline such as cellranger-1.1.0

        Return:
             Sample contructor for specified pipeline.

        Raises:
            ValueError if pipeline not supported.

        """
        # Variables for version numbers
        x = None
        y = None
        z = None

        pipeline_match = re.search('cellranger-([0-9]).([0-9]).([0-9])', pipeline)
        if pipeline_match:
            x = int(pipeline_match.group(1))
            y = int(pipeline_match.group(2))
            z = int(pipeline_match.group(3))

        if pipeline_match and x == 1:
            raise ValueError('Cellranger 1.X versions are no longer supported: %s, please use an older commit of cellwrapper.' % pipeline)
        elif pipeline_match and x in [2,3]:
            return CellRangerSample
        else:
            raise ValueError('Specified pipeline is not supported: %s' % pipeline)


if __name__ == '__main__':
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

    cellranger = CellRanger(args.sample_sheet, sample_limit=args.samplelimit, cellranger_log=open(args.cellranger_log, 'w'), install=args.installation, verbose=args.verbose)

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