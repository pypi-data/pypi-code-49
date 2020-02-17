#!/usr/bin/env python

"""
Conduct recurrence quantification analysis.

Input data representation: Row store
Recurrence matrix materialisation: No
Recurrence matrix representation: NA
Similarity value representation: NA
Intermediate results recycling: NA
"""

from pyrqa.utils import SettableSettings
from pyrqa.runtimes import FlavourRuntimesMultipleOperators

from pyrqa.operators.detect_vertical_lines.radius.row_no_materialisation import detect_vertical_lines
from pyrqa.operators.detect_diagonal_lines.radius.row_no_materialisation import detect_diagonal_lines

__author__ = "Tobias Rawald"
__copyright__ = "Copyright 2015, 2018, 2019, 2020 The PyRQA project"
__credits__ = ["Tobias Rawald",
               "Mike Sips"]
__license__ = "Apache-2.0"
__maintainer__ = "Tobias Rawald"
__email__ = "pyrqa@gmx.net"
__status__ = "Development"


class RowNoMaterialisation(SettableSettings):
    """
    See module description regarding computational properties.

    :ivar opencl: OpenCL environment.
    :ivar device: OpenCL device.
    :ivar data_type: Data type to represent the similarity values.
    :ivar optimisations_enabled: Are the default OpenCL compiler optimisations enabled?
    :ivar loop_unroll: Loop unrolling factor.
    :ivar program: OpenCL program.
    :ivar program_created: Has the OpenCL program already been created?
    :ivar kernels: OpenCL kernels.
    :ivar kernels_created: Have the OpenCL kernels already been created?
    """

    def __init__(self,
                 settings,
                 opencl,
                 device,
                 **kwargs):
        """
        :param settings: Settings.
        :param opencl: OpenCL environment.
        :param device: OpenCL device.
        :param kwargs: Keyword arguments.
        """

        SettableSettings.__init__(self,
                                  settings)

        self.opencl = opencl
        self.device = device

        self.optimisations_enabled = kwargs['optimisations_enabled'] if 'optimisations_enabled' in list(kwargs.keys()) else False
        self.loop_unroll = kwargs['loop_unroll'] if 'loop_unroll' in list(kwargs.keys()) else 1

        self.program = None
        self.program_created = False

        self.kernels = {}
        self.kernels_created = False

        self.detect_vertical_lines_kernel_name = self.settings.detect_vertical_lines_kernel_name
        self.detect_diagonal_lines_kernel_name = self.settings.detect_diagonal_lines_kernel_name

        self.__initialize()

    def __initialize(self):
        """
        Initialization of the variant.
        """
        if not self.program_created:
            self.program = self.opencl.create_program(self.device,
                                                      (detect_vertical_lines,
                                                       detect_diagonal_lines),
                                                      self.settings.kernels_sub_dir,
                                                      self.settings.dtype,
                                                      optimisations_enabled=self.optimisations_enabled,
                                                      loop_unroll=self.loop_unroll)

            self.program_created = True

        if not self.kernels_created:
            self.kernels = self.opencl.create_kernels(self.program,
                                                      (self.detect_vertical_lines_kernel_name,
                                                       self.detect_diagonal_lines_kernel_name))

            self.kernels_created = True

    def process_sub_matrix(self,
                           sub_matrix):
        """
        Processing of a single sub matrix.

        :param sub_matrix: Sub matrix.
        :return: Runtimes for processing the sub matrix.
        """
        # Create variant runtimes
        variant_runtimes = FlavourRuntimesMultipleOperators()

        # Detect vertical lines
        vectors_x_buffer, \
            vectors_y_buffer, \
            detect_vertical_lines_runtimes = detect_vertical_lines(self.settings,
                                                                   sub_matrix,
                                                                   self.device,
                                                                   self.opencl.contexts[self.device],
                                                                   self.opencl.command_queues[self.device],
                                                                   (self.kernels[self.detect_vertical_lines_kernel_name],),
                                                                   return_vectors_buffers=True)

        variant_runtimes.detect_vertical_lines_runtimes = detect_vertical_lines_runtimes

        # Detect diagonal lines
        detect_diagonal_lines_runtimes = detect_diagonal_lines(self.settings,
                                                               sub_matrix,
                                                               self.device,
                                                               self.opencl.contexts[self.device],
                                                               self.opencl.command_queues[self.device],
                                                               (self.kernels[self.detect_diagonal_lines_kernel_name],),
                                                               vectors_x_buffer=vectors_x_buffer,
                                                               vectors_y_buffer=vectors_y_buffer)

        variant_runtimes.detect_diagonal_lines_runtimes = detect_diagonal_lines_runtimes

        return variant_runtimes
