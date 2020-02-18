import chainermn
import logging
from chainermn import scatter_dataset as scatter

from .base import DefaultFinetuner

class _mpi_mixin(object):
	"""
		This mixin is used to remove "comm" argument from
		argument lists, so that object class gets an empty list
	"""

	def __init__(self, comm, *args, **kwargs):
		super(_mpi_mixin, self).__init__(*args, **kwargs)

class MPIFinetuner(DefaultFinetuner, _mpi_mixin):

	@property
	def mpi(self):
		return self.comm is not None

	@property
	def mpi_main_process(self):
		return not (self.comm is not None and self.comm.rank != 0)

	def gpu_config(self, opts, comm=None, *args, **kwargs):
		super(MPIFinetuner, self).gpu_config(opts, *args, **kwargs)

		self.comm = comm
		if self.mpi:
			if len(opts.gpu) > 1:
				self.device = opts.gpu[self.comm.rank]
			else:
				self.device += self.comm.intra_rank
			ranks = f"{self.comm.rank}|{self.comm.intra_rank}|{self.comm.inter_rank}"
			logging.info(f"Node with ranks {ranks} assigned to GPU #{self.device}")
		else:
			logging.warn("Using MPIFinetuner without setting a communicator!")

	def scatter_datasets(self):
		if self.mpi:
			self.train_data = scatter(self.train_data, self.comm)
			self.val_data = scatter(self.val_data, self.comm)
		else:
			logging.warn("Data scattering was not Possible!")


	def init_datasets(self, *args, **kwargs):

		if self.mpi_main_process:
			super(MPIFinetuner, self).init_datasets(*args, **kwargs)
		else:
			self.train_data, self.val_data = None, None

		self.scatter_datasets()

	def init_optimizer(self, opts):
		super(MPIFinetuner, self).init_optimizer(opts)

		if self.mpi:
			self.opt = chainermn.create_multi_node_optimizer(self.opt, self.comm)

	def init_evaluator(self):
		super(MPIFinetuner, self).init_evaluator()

		if self.mpi:
			self.evaluator = chainermn.create_multi_node_evaluator(
				self.evaluator, self.comm)

	def run(self, trainer_cls, opts, *args, **kwargs):
		kwargs["no_observe"] = not self.mpi_main_process
		opts.no_snapshot = not self.mpi_main_process
		super(MPIFinetuner, self).run(trainer_cls, opts, *args, **kwargs)
