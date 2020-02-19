"""Handlers for experiment and ROI records

Classes that are used for accessing experiment and region of interest
records.

For modules, :class:`.experiment_generic.ExperimentGeneric` provides
methods for making new experiment records, checking whether a record
exists, and quering the experiment data. It is recommended to use
these methods for operations on experiments table.

ROI access as provided by ROI handler is used internally and is not
expected to be used by the modules. Modules, however, can request the
data or link with the ROI data through references in the database
tables to ROI table, as defined in the handler. For ROI table
description, see :class:`.roi.ROIHandler`.

"""
