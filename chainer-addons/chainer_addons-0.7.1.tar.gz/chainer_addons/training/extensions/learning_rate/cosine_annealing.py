import numpy as np
from chainer_addons.training.extensions.learning_rate.base import ContiniousLearningRate

class CosineAnnealingLearningRate(ContiniousLearningRate):

	def __init__(self, stages=4, *args, **kwargs):
		super(CosineAnnealingLearningRate, self).__init__(*args, **kwargs)
		self.stages = stages
		self._init_epochs = self._epochs
		self._epochs = self._init_epochs * (2**stages - 1)

		self.current_stage = 0

	@property
	def epochs_in_current_stage(self):
		return self._init_epochs * 2**self.current_stage

	@property
	def end_of_current_stage(self):
		return self._init_epochs * (2**(self.current_stage + 1) - 1)

	@property
	def current_stage_offset(self):
		return self._init_epochs * (2**self.current_stage - 1)

	@property
	def factor(self):
		return 0.5 * (self._lr - self._target)

	def new_lr(self, epoch):

		if epoch >= self.end_of_current_stage:
			self.current_stage += 1

		epoch -= self.current_stage_offset
		epochs = self.epochs_in_current_stage - self._offset

		res = self._target + self.factor * (1 + np.cos(np.pi * epoch / epochs))

		return res


if __name__ == '__main__':

	from matplotlib import pyplot as plt
	ext = CosineAnnealingLearningRate(
		attr="attr",
		lr=1e-2,
		target=1e-5,
		epochs=12,
		offset=0,
		stages=5)

	xs = np.arange(ext._epochs).astype(np.float32)
	ys = np.zeros_like(xs)

	for x in xs:
		ys[int(x)] = ext.new_lr(x)

	plt.plot(xs, ys)
	plt.show()
