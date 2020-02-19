import numpy as np
from chainer_addons.training.extensions.learning_rate.base import ContiniousLearningRate

class CosineAnnealingLearningRate(ContiniousLearningRate):

	def __init__(self, stages=4, *args, **kwargs):
		super(CosineAnnealingLearningRate, self).__init__(*args, **kwargs)
		self.stages = stages
		self._init_epochs = self._epochs
		self._epochs = self._init_epochs * (2**stages - 1) + self._offset

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

		if epoch < self._offset:
			return self._lr

		epoch -= self._offset

		if epoch >= self.end_of_current_stage:
			self.current_stage += 1

		epoch -= self.current_stage_offset
		epochs = self.epochs_in_current_stage

		res = self._target + self.factor * (1 + np.cos(np.pi * epoch / (epochs-1)))
		return res


if __name__ == '__main__':
	from matplotlib import pyplot as plt
	from argparse import ArgumentParser

	def main(args):
		ext = CosineAnnealingLearningRate(
			attr="attr",
			lr=args.start,
			target=args.end,
			epochs=args.epochs,
			offset=args.offset,
			stages=args.stages)

		xs = np.arange(ext._epochs).astype(np.float32)
		ys = np.zeros_like(xs)

		for x in xs:
			ys[int(x)] = ext.new_lr(x)

		fig, ax = plt.subplots()

		ax.plot(xs, ys)
		if args.log_scale:
			ax.set_yscale("log")

		ax.hlines(y=args.start, xmin=0, xmax=x.max() + args.offset, linestyles="--")
		ax.hlines(y=args.end, xmin=0, xmax=x.max() + args.offset, linestyles="--")

		ax.vlines(x=args.offset + args.epochs * (2**np.arange(1, args.stages+1) - 1) - 1,
			ymin=args.end,
			ymax=args.start,
			linestyles="-.")

		ax.vlines(x=args.offset,
			ymin=args.end,
			ymax=args.start,
			linestyles="-")
		plt.show()
		plt.close()

	parser = ArgumentParser()

	parser.add_argument("--start",
		type=float, default=1e-2)

	parser.add_argument("--end",
		type=float, default=1e-5)

	parser.add_argument("--epochs",
		type=int, default=12)

	parser.add_argument("--offset",
		type=int, default=0)

	parser.add_argument("--stages",
		type=int, default=5)

	parser.add_argument("--log_scale", action="store_true")

	main(parser.parse_args())


