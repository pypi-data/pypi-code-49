import contextlib
import munch
import copy


class Config(munch.Munch):

    @contextlib.contextmanager
    def using(self, **configs):
        save = copy.deepcopy(self)

        self.update(configs)
        yield self
        self.update(save)
