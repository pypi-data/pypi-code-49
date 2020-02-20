import numpy

from collections import namedtuple

from beat.backend.python.database import View


class FooView(View):
    def setup(
        self,
        root_folder,
        outputs,
        parameters,
        force_start_index=None,
        force_end_index=None,
    ):
        """Initializes the database"""

        return True

    def index(self, root_folder, parameters):
        """Creates the data for the database indexation"""

        Entry = namedtuple("Entry", ["out"])

        return [Entry(42)]

    def get(self, output, index):
        """Returns the data for the output based on the index content"""

        obj = self.objs[index]

        if output == "out":
            return {"value": numpy.int32(obj.out)}
