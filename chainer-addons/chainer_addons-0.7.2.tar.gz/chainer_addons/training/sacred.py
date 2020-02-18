from chainer_addons.training.extensions import SacredReport

class SacredTrainerMixin(object):
	def __init__(self, opts, sacred_params, sacred_trigger=(1, "epoch"), *args, **kwargs):
		super(SacredTrainerMixin, self).__init__(opts=opts, *args, **kwargs)
		self.sacred_reporter = SacredReport(opts,
			sacred_params=sacred_params,
			trigger=sacred_trigger)
		self.extend(self.sacred_reporter)

		def _run(*args, **kwargs):
			res = super(SacredTrainerMixin, self).run(*args, **kwargs)

			# import pdb; pdb.set_trace()
			return res

		if getattr(self, "_only_eval", False):
			self.run = _run
		else:
			self.sacred_reporter.ex.main(_run)
			self.run = self.sacred_reporter.ex

